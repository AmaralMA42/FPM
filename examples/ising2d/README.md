# 2D Ising — from a question to an experiment

**Goal:** illustrate how a researcher can move from curiosity about magnetic order to model choices, observables, controls, and an executable small experiment. The FPM Companion guides the decisions; the code is optional.

A beginner can start with *“I want to see how spins lose order as temperature rises.”* The Companion may suggest a 2D ferromagnetic Ising model, spin snapshots and magnetization. An experienced researcher can jump directly to finite-size effects, equilibration, autocorrelation and Binder ratios. See [illustrative conversations](EXAMPLE_CONVERSATIONS.md); these are not real user test transcripts.

For spins `s_i = ±1` on a periodic square lattice, no field, `J=k_B=1`:

`H = -J Σ_{<i,j>} s_i s_j`.

The **infinite-lattice** critical temperature is `T_c = 2 / ln(1+√2) ≈ 2.269185`. Finite systems do not have a sharp nonanalytic transition. The quick simulation is an **exploratory educational illustration, not a precision estimate of T_c**.

### Optional execution

Run from `examples/ising2d` with Python, NumPy and Matplotlib:

```bash
python -m pip install -r requirements.txt
python -m unittest discover -p 'test_*.py' -v
python ising2d.py --profile quick --out ising_results
```

The implementation uses **alternating checkerboard Metropolis** updates on even-sized periodic lattices. The quick profile uses `L=8,16,24`, six temperatures and three independent replicates per condition. It writes CSV outputs, metadata, plots and spin snapshots. A longer `study` preset is available but is **not** required to try the Companion.

[Sample outputs](sample/README.md) are retained from an earlier local execution, with source metadata. Without a Python environment the assistant can still help reason about the scientific design, but it cannot claim to have executed anything.

`m_abs` is mean absolute magnetization per spin; `energy` is energy per spin; `chi_connected` uses signed magnetization, whereas `chi_abs` is a **modified finite-size proxy**, not the strict susceptibility. `binder` requires careful sampling before interpreting crossings. Finite-size effects, equilibration and autocorrelation are important limits.

Eight basic unit tests include energy and flip checks, deterministic seeds and a scoped comparison with exact 4×4 enumeration. They are not independent verification of all physical inferences or a precision critical-temperature result.

The [Quarantine Games on Networks repository](https://github.com/AmaralMA42/quarantine_games_network) is a distinct, longer research example; its scientific data are not included here.
