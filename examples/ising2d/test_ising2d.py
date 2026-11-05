"""Small correctness checks; not a proof of scientific validity."""
import itertools
import math
import unittest

import numpy as np

from ising2d import Ising2D, TC_EXACT, aggregate, run_replica


class IsingTests(unittest.TestCase):
    def test_all_up_energy(self):
        m = Ising2D(8, np.random.default_rng(17), ordered=True)
        e, mag = m.measure()
        self.assertEqual(e, -2.0)
        self.assertEqual(mag, 1.0)
        self.assertEqual(m.flip_energy(0, 0), 8)

    def test_delta_e_matches_full_energy(self):
        model = Ising2D(8, np.random.default_rng(7))
        for i, j in itertools.product((0, 1, 5), (0, 2, 6)):
            before = model.measure()[0] * model.N
            prediction = model.flip_energy(i, j)
            model.spins[i, j] *= -1
            after = model.measure()[0] * model.N
            self.assertAlmostEqual(after - before, prediction)
            model.spins[i, j] *= -1

    def test_zero_temperature_nonincreasing_energy(self):
        model = Ising2D(12, np.random.default_rng(44))
        before = model.measure()[0]
        for _ in range(30):
            model.sweep(0)
            after = model.measure()[0]
            self.assertLessEqual(after, before + 1e-12)
            before = after

    def test_repeatability_and_bounds(self):
        a, _ = run_replica(8, 2.3, burnin=20, samples=30, thin=2, seed=33, replica=0)
        b, _ = run_replica(8, 2.3, burnin=20, samples=30, thin=2, seed=33, replica=0)
        self.assertEqual(a, b)
        self.assertLessEqual(abs(a['m_signed']), 1)
        self.assertTrue(0 <= a['acceptance'] <= 1)
        self.assertTrue(math.isfinite(a['binder']))

    def test_replica_summary(self):
        a, _ = run_replica(8, 2.3, burnin=10, samples=10, thin=1, seed=5, replica=0)
        b, _ = run_replica(8, 2.3, burnin=10, samples=10, thin=1, seed=5, replica=1)
        summary = aggregate([a, b])
        self.assertEqual(summary[0]['replicas'], 2)
        self.assertTrue(math.isfinite(summary[0]['energy_se']))

    def test_small_lattice_exact_enumeration(self):
        # Independently enumerate all 2^16 states on the 4x4 periodic lattice.
        # Compare MC finite-run estimates with exact finite-system expectations.
        bit_patterns = ((np.arange(1 << 16)[:, None] >> np.arange(16)) & 1).astype(np.int8)
        spins = (2 * bit_patterns - 1).reshape(-1, 4, 4)
        energy_total = -np.sum(spins * (np.roll(spins, -1, axis=1) +
                                        np.roll(spins, -1, axis=2)), axis=(1, 2))
        temp = 2.2
        boltzmann = np.exp(-energy_total / temp)
        weights = boltzmann / boltzmann.sum()
        exact_energy = float(np.sum(weights * energy_total) / 16)
        exact_mabs = float(np.sum(weights * np.abs(spins.sum(axis=(1, 2)))) / 16)
        measured, _ = run_replica(4, temp, burnin=300, samples=2500, thin=2,
                                  seed=101, replica=0)
        self.assertAlmostEqual(measured['energy'], exact_energy, delta=0.065)
        self.assertAlmostEqual(measured['m_abs'], exact_mabs, delta=0.065)

    def test_exact_reference(self):
        self.assertAlmostEqual(TC_EXACT, 2.269185314213022, places=11)

    def test_cold_and_hot_ordering_smoke(self):
        cold, _ = run_replica(16, 1.5, burnin=90, samples=80, thin=2,
                              seed=99, replica=0, ordered=True)
        hot, _ = run_replica(16, 4.0, burnin=90, samples=80, thin=2,
                             seed=99, replica=0, ordered=True)
        self.assertGreater(cold['m_abs'], hot['m_abs'] + 0.25)


if __name__ == '__main__':
    unittest.main()
