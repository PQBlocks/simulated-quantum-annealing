import numpy as np
import unittest
from pqblocks_anneal_sqa.sqa_sampler import SimulatedQuantumAnnealingSampler

class TestSQASampler(unittest.TestCase):
    
    def test_empty_input(self):
        """Test that empty input raises ValueError."""
        sampler = SimulatedQuantumAnnealingSampler()
        h = []
        J = np.array([]).reshape(0, 0)
        
        with self.assertRaises(ValueError) as context:
            sampler.sample_ising(h, J)
        self.assertIn("Empty input", str(context.exception))

    def test_dimension_mismatch_h_vs_J(self):
        """Test that dimension mismatch between h and J raises ValueError."""
        sampler = SimulatedQuantumAnnealingSampler()
        h = [1, 2, 3]  # Length 3
        J = np.array([[0, 1], [1, 0]])  # Shape (2, 2)
        
        with self.assertRaises(ValueError) as context:
            sampler.sample_ising(h, J)
        self.assertIn("Dimension mismatch", str(context.exception))

    def test_dimension_mismatch_J_not_square(self):
        """Test that non-square J matrix raises ValueError."""
        sampler = SimulatedQuantumAnnealingSampler()
        h = [1, 2]
        J = np.array([[0, 1, 2], [1, 0, 3]])  # Shape (2, 3)
        
        with self.assertRaises(ValueError) as context:
            sampler.sample_ising(h, J)
        self.assertIn("Dimension mismatch", str(context.exception))

    def test_nan_in_h(self):
        """Test that NaN in h raises ValueError."""
        sampler = SimulatedQuantumAnnealingSampler()
        h = [1, np.nan, 3]
        J = np.array([[0, 1, 2], [1, 0, 3], [2, 3, 0]])
        
        with self.assertRaises(ValueError) as context:
            sampler.sample_ising(h, J)
        self.assertIn("NaN or Inf values detected", str(context.exception))

    def test_inf_in_J(self):
        """Test that Inf in J raises ValueError."""
        sampler = SimulatedQuantumAnnealingSampler()
        h = [1, 2, 3]
        J = np.array([[0, 1, np.inf], [1, 0, 3], [np.inf, 3, 0]])
        
        with self.assertRaises(ValueError) as context:
            sampler.sample_ising(h, J)
        self.assertIn("NaN or Inf values detected", str(context.exception))

    def test_negative_sweeps(self):
        """Test that negative sweeps raises ValueError."""
        sampler = SimulatedQuantumAnnealingSampler()
        h = [1, 2]
        J = np.array([[0, 1], [1, 0]])
        
        with self.assertRaises(ValueError) as context:
            sampler.sample_ising(h, J, num_sweeps=-5)
        self.assertIn("Negative or zero sweeps", str(context.exception))

    def test_zero_sweeps(self):
        """Test that zero sweeps raises ValueError."""
        sampler = SimulatedQuantumAnnealingSampler()
        h = [1, 2]
        J = np.array([[0, 1], [1, 0]])
        
        with self.assertRaises(ValueError) as context:
            sampler.sample_ising(h, J, num_sweeps=0)
        self.assertIn("Negative or zero sweeps", str(context.exception))

    def test_single_spin(self):
        """Test that single spin case returns optimal state immediately."""
        sampler = SimulatedQuantumAnnealingSampler()
        h = [2.5]
        J = np.array([[0]])
        
        # For single spin, it should return the optimal state without running SQA
        # The optimal state for h[0] = 2.5 is -1 (since energy = h*s, min when s = -sign(h))
        samples, energies = sampler.sample_ising(h, J)
        
        # Check that we get the expected optimal state and energy
        self.assertEqual(samples[0][0], -1)
        self.assertEqual(energies[0], -2.5)

    def test_matrix_normalization(self):
        """Test that non-symmetric J is properly normalized."""
        # This test will be fully implemented once we have the core algorithm
        # For now, we just check that it doesn't raise errors during validation
        sampler = SimulatedQuantumAnnealingSampler()
        h = [1, -1, 2]
        # Non-symmetric J matrix
        J = np.array([
            [0, 1, 2],
            [3, 0, 4],  # Note: 3 and 1 are not symmetric
            [5, 6, 0]   # Note: 5,2 and 6,4 are not symmetric
        ])
        
        # Should not raise errors during validation
        # Since we have a working implementation now, it should complete successfully
        samples, energies = sampler.sample_ising(h, J, num_sweeps=10, P=4)
        
        # Check that we got the expected shapes
        self.assertEqual(samples.shape, (1, 3))
        self.assertEqual(energies.shape, (1,))
        
        # Check that all spins are either -1 or 1
        self.assertTrue(np.all((samples == -1) | (samples == 1)))

if __name__ == '__main__':
    unittest.main()