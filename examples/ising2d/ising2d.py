"""A deliberately small, inspectable 2D Ising Metropolis laboratory.

Periodic square lattice, zero field, J=k_B=1, even L only. Each sweep visits
both checkerboard sublattices; it is *not* random-site sequential Metropolis.
Results are descriptive finite-size Monte Carlo estimates, not a precise Tc fit.
"""
from __future__ import annotations

import argparse
import csv
import json
import math
import platform
from pathlib import Path

import numpy as np

TC_EXACT = 2.0 / math.log(1.0 + math.sqrt(2.0))


class Ising2D:
    def __init__(self, size: int, rng: np.random.Generator, *, ordered: bool = False):
        if size < 4 or size % 2:
            raise ValueError("Checkerboard periodic updates require an even L >= 4")
        self.L = size
        self.N = size * size
        self.rng = rng
        self.spins = (np.ones((size, size), dtype=np.int8) if ordered else
                      (2 * rng.integers(0, 2, size=(size, size), dtype=np.int8) - 1))
        coords = np.indices((size, size))
        self.sublattice = [((coords[0] + coords[1]) % 2) == p for p in (0, 1)]

    def neighbor_sum(self) -> np.ndarray:
        s = self.spins
        return (np.roll(s, 1, 0) + np.roll(s, -1, 0) +
                np.roll(s, 1, 1) + np.roll(s, -1, 1))

    def flip_energy(self, i: int, j: int) -> int:
        return int(2 * self.spins[i, j] * self.neighbor_sum()[i, j])

    def sweep(self, temperature: float) -> float:
        if temperature < 0:
            raise ValueError("Temperature must be non-negative")
        accepted = 0
        for mask in self.sublattice:
            dE = 2 * self.spins * self.neighbor_sum()
            if temperature == 0:
                accept = dE <= 0
            else:
                # No exponential overflow for energetically favorable flips.
                probability = np.exp(-np.maximum(dE, 0) / temperature)
                accept = (dE <= 0) | (self.rng.random((self.L, self.L)) < probability)
            flips = mask & accept
            self.spins[flips] *= -1
            accepted += int(flips.sum())
        return accepted / self.N

    def measure(self) -> tuple[float, float]:
        s = self.spins
        # Each nearest-neighbor bond is counted exactly once (right and down).
        energy_per_spin = -float(np.sum(s * (np.roll(s, 1, 0) + np.roll(s, 1, 1)))) / self.N
        signed_magnetization = float(s.mean())
        return energy_per_spin, signed_magnetization


def run_replica(size: int, temperature: float, *, burnin: int, samples: int,
                thin: int, seed: int, replica: int, ordered: bool = False,
                return_spins: bool = False) -> tuple[dict, np.ndarray | None]:
    if temperature <= 0 or burnin < 0 or samples < 2 or thin < 1:
        raise ValueError("Use T>0, burnin>=0, samples>=2, thin>=1")
    # Parameter-derived seed: changing traversal order does not change results.
    seed_components = [seed, size, int(round(temperature * 1_000_000)), replica]
    rng = np.random.default_rng(np.random.SeedSequence(seed_components))
    model = Ising2D(size, rng, ordered=ordered)
    for _ in range(burnin):
        model.sweep(temperature)
    energies, mags, accepts = [], [], []
    for _ in range(samples):
        for _ in range(thin):
            accepts.append(model.sweep(temperature))
        e, m = model.measure()
        energies.append(e)
        mags.append(m)
    e = np.asarray(energies)
    m = np.asarray(mags)
    m2 = float(np.mean(m * m))
    m4 = float(np.mean(m**4))
    # 'chi_abs' is a *modified finite-size proxy*, not the exact zero-field
    # susceptibility; both versions are exported to avoid ambiguity.
    out = dict(L=size, T=temperature, replica=replica, seed=seed,
               energy=float(e.mean()), m_signed=float(m.mean()),
               m_abs=float(np.abs(m).mean()),
               chi_connected=float((size * size / temperature) * (m2 - float(m.mean())**2)),
               chi_abs=float((size * size / temperature) * (m2 - float(np.abs(m).mean())**2)),
               heat_capacity=float((size * size / temperature**2) * (float(np.mean(e**2)) - float(e.mean())**2)),
               binder=(float(1 - m4 / (3 * m2**2)) if m2 > 0 else float('nan')),
               acceptance=float(np.mean(accepts)), burnin=burnin, samples=samples, thin=thin,
               ordered_initial=ordered)
    return out, model.spins.copy() if return_spins else None


def mean_and_se(values: list[float]) -> tuple[float, float]:
    a = np.array(values, dtype=float)
    return float(a.mean()), float(a.std(ddof=1) / math.sqrt(len(a))) if len(a) > 1 else float('nan')


def aggregate(records: list[dict]) -> list[dict]:
    result = []
    for size, temperature in sorted(set((r['L'], r['T']) for r in records)):
        members = [r for r in records if r['L'] == size and r['T'] == temperature]
        row = {'L': size, 'T': temperature, 'replicas': len(members)}
        for name in ('energy', 'm_abs', 'chi_connected', 'chi_abs', 'heat_capacity', 'binder', 'acceptance'):
            row[name], row[f'{name}_se'] = mean_and_se([r[name] for r in members])
        result.append(row)
    return result


def write_csv(path: Path, records: list[dict]) -> None:
    if not records:
        return
    with path.open('w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=list(records[0]))
        writer.writeheader()
        writer.writerows(records)


def render_plots(summary: list[dict], snapshots: dict[float, np.ndarray], out: Path) -> None:
    import matplotlib.pyplot as plt
    sizes = sorted({r['L'] for r in summary})
    for metric, ylabel, name in [
        ('m_abs', r'$\langle |m|\rangle$', 'magnetization.png'),
        ('energy', r'$\langle E\rangle/N$', 'energy.png'),
        ('chi_abs', r'$\chi_{|m|}=N(\langle m^2\rangle-\langle|m|\rangle^2)/T$', 'chi_abs_proxy.png'),
        ('binder', r'$U_4=1-\langle m^4\rangle/(3\langle m^2\rangle^2)$', 'binder.png'),
    ]:
        fig, ax = plt.subplots(figsize=(6.5, 4))
        for size in sizes:
            rows = sorted([r for r in summary if r['L'] == size], key=lambda x: x['T'])
            ax.errorbar([r['T'] for r in rows], [r[metric] for r in rows],
                        yerr=[r[f'{metric}_se'] for r in rows], fmt='o-', capsize=2, label=f'L={size}')
        ax.axvline(TC_EXACT, color='gray', linestyle='--', linewidth=1, label='Tc exato (L→∞)')
        ax.set(xlabel=r'$k_B T/J$', ylabel=ylabel,
               title=f'Ising 2D — {metric} (finite size; exploratory)')
        ax.legend(fontsize=8)
        fig.tight_layout()
        fig.savefig(out / name, dpi=160)
        plt.close(fig)
    if snapshots:
        for temp, spins in snapshots.items():
            fig, ax = plt.subplots(figsize=(4.5, 4.5))
            ax.imshow(spins, cmap='gray', vmin=-1, vmax=1, interpolation='nearest')
            ax.set(title=f'Ising L={spins.shape[0]}, T={temp:g} — one replica')
            ax.axis('off')
            fig.tight_layout()
            fig.savefig(out / f'snapshot_T{temp:g}.png', dpi=160)
            plt.close(fig)


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--profile', choices=['quick', 'study'], default='quick')
    parser.add_argument('--sizes', nargs='+', type=int)
    parser.add_argument('--temps', nargs='+', type=float)
    parser.add_argument('--burnin', type=int)
    parser.add_argument('--samples', type=int)
    parser.add_argument('--thin', type=int)
    parser.add_argument('--replicas', type=int)
    parser.add_argument('--seed', type=int, default=20261104)
    parser.add_argument('--out', type=Path, default=Path('ising_results'))
    parser.add_argument('--no-plots', action='store_true')
    args = parser.parse_args(argv)
    defaults = ({'sizes': [8, 16, 24], 'temps': [1.8, 2.1, 2.25, 2.4, 2.7, 3.0],
                 'burnin': 250, 'samples': 100, 'thin': 3, 'replicas': 3} if args.profile == 'quick'
                else {'sizes': [16, 24, 32, 48], 'temps': [2.0, 2.1, 2.2, 2.26, 2.3, 2.4, 2.5, 2.6],
                      'burnin': 1200, 'samples': 500, 'thin': 5, 'replicas': 6})
    cfg = {k: getattr(args, k) if getattr(args, k) is not None else v for k, v in defaults.items()}
    if any(L < 4 or L % 2 for L in cfg['sizes']):
        parser.error('all sizes must be even and >= 4 (checkerboard periodic updates)')
    if (any(t <= 0 for t in cfg['temps']) or
            len(set(round(t, 6) for t in cfg['temps'])) != len(cfg['temps'])):
        parser.error('temperatures must be positive and distinct to six decimals')
    if cfg['replicas'] < 2 or cfg['samples'] < 2 or cfg['thin'] < 1 or cfg['burnin'] < 0:
        parser.error('need replicas>=2, samples>=2, thin>=1, burnin>=0')
    if args.seed < 0:
        parser.error('seed must be non-negative')
    args.out.mkdir(parents=True, exist_ok=True)
    observations, snaps = [], {}
    sizes = sorted(set(cfg['sizes']))
    temps = sorted(cfg['temps'])
    chosen_temps = sorted(set([temps[0], min(temps, key=lambda v: abs(v - TC_EXACT)), temps[-1]]))
    for L in sizes:
        for temp in temps:
            for rep in range(cfg['replicas']):
                capture = (L == max(sizes) and rep == 0 and temp in chosen_temps)
                values, final_spin = run_replica(L, temp, burnin=cfg['burnin'],
                    samples=cfg['samples'], thin=cfg['thin'], seed=args.seed,
                    replica=rep, return_spins=capture)
                observations.append(values)
                if capture:
                    snaps[temp] = final_spin
    summary = aggregate(observations)
    write_csv(args.out / 'replicas.csv', observations)
    write_csv(args.out / 'summary.csv', summary)
    metadata = {
        'status': 'EXECUTED_MONTE_CARLO_EXPLORATORY_ONLY', 'model': '2D zero-field ferromagnetic Ising',
        'Hamiltonian': 'H=-J sum_nearest_neighbor s_i s_j, J=1, periodic square lattice',
        'update': 'Metropolis, deterministic alternating checkerboard sublattice sweeps, even L',
        'measurement': 'one observation every thin full sweeps after burnin',
        'chi_connected': 'N/T * (<m^2>-<m>^2), signed m',
        'chi_abs': 'N/T * (<m^2>-<|m|>^2), modified finite-size proxy',
        'uncertainty': 'SE across independent RNG replicas; does not diagnose equilibration or integrated autocorrelation',
        'Tc_exact_infinite_square': TC_EXACT,
        'profile': args.profile, 'settings': cfg, 'base_seed': args.seed,
        'independent_rng_keys': ['base_seed', 'L', 'int(round(T*1e6))', 'replica'],
        'python_version': platform.python_version(), 'numpy_version': np.__version__,
        'matplotlib_plots': not args.no_plots,
        'disclaimer': 'No precise Tc inference, exponent inference or independent scientific validation claimed',
    }
    (args.out / 'metadata.json').write_text(json.dumps(metadata, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    if not args.no_plots:
        render_plots(summary, snaps, args.out)
    print(f"Wrote {len(observations)} replica rows, {len(summary)} conditions -> {args.out}")
    print(f"Exact Onsager reference k_B Tc/J = {TC_EXACT:.6f}; this run does not estimate Tc precisely")


if __name__ == '__main__':
    main()
