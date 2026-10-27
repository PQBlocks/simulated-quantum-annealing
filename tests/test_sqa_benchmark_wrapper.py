"""
Test for the SQA benchmark wrapper.
"""

import numpy as np
import unittest
from pqblocks_anneal_sqa.sqa_benchmark_wrapper import SQABenchmarkWrapper

class TestSQABenchmarkWrapper(unittest.TestCase):
    
    def setUp(self):
        """Set up test fixtures."""
        # Create a small problem instance for testing
        self.N = 4
        self.h = np.array([-1.0, 1.0, 2.0, -2.0])
        self.J = np.array([
            [0, 1, -1, 2],
            [1, 0, 1, -1],
            [-1, 1, 0, -2],
            [2, -1, -2, 0]
        ])
        
    def test_wrapper_initialization(self):
        """Test that the wrapper initializes correctly."""
        wrapper = SQABenchmarkWrapper(num_sweeps=1000, beta=5.0, P=32)
        
        self.assertEqual(wrapper.name(), "SQA")
        self.assertEqual(wrapper.short_name(), "sqa")
        self.assertEqual(wrapper.description(), "Simulated Quantum Annealing solver")
        self.assertEqual(wrapper.parameters(), {"num_sweeps": 1000, "beta": 5.0, "P": 32})
        
    def test_wrapper_call(self):
        """Test that the wrapper can be called to solve a problem."""
        wrapper = SQABenchmarkWrapper(num_sweeps=100, beta=2.0, P=4)
        
        # Call the wrapper
        samples, energies = wrapper(self.h, self.J)
        
        # Check the shapes of the results
        self.assertEqual(samples.shape[1], self.N)
        self.assertEqual(energies.shape[0], samples.shape[0])
        
        # Check that all spins are either -1 or 1
        self.assertTrue(np.all((samples == -1) | (samples == 1)))
        
    def test_wrapper_with_custom_parameters(self):
        """Test that the wrapper can be called with custom parameters."""
        wrapper = SQABenchmarkWrapper()
        
        # Call the wrapper with custom parameters
        samples, energies = wrapper(self.h, self.J, num_sweeps=50, beta=1.0, P=2)
        
        # Check the shapes of the results
        self.assertEqual(samples.shape[1], self.N)
        self.assertEqual(energies.shape[0], samples.shape[0])
        
        # Check that all spins are either -1 or 1
        self.assertTrue(np.all((samples == -1) | (samples == 1)))

if __name__ == '__main__':
    unittest.main()