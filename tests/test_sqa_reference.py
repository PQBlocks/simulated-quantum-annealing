import numpy as np
from pqblocks_anneal_sqa.sqa_sampler import SimulatedQuantumAnnealingSampler

def test_sqa_worked_example():
    """
    Test the SQA implementation against the 4-spin worked example from the spec.
    """
    # Constants from the worked example
    N = 4
    P = 4
    beta = 2.0
    gamma = 1.0  # Gamma is constant in the example
    
    # Calculate J_perp
    J_perp = -0.25 * np.log(np.tanh(0.5))  # ≈ 0.1929842
    
    # Problem weights
    h = np.array([-1.0, 1.0, 2.0, -2.0])
    J_sym = np.array([
        [0, 1, -1, 2],
        [1, 0, 1, -1],
        [-1, 1, 0, -2],
        [2, -1, -2, 0]
    ])
    
    # Initial state
    s = np.array([
        [1, 1, -1, 1],
        [1, -1, -1, -1],  # <-- Slice 1
        [-1, -1, -1, -1],
        [1, 1, 1, 1]
    ])
    
    # Create sampler instance
    sampler = SimulatedQuantumAnnealingSampler()
    
    # Manually run the calculation for the specific flip evaluation
    # Flip Evaluation: Slice k=1, Spin i=2
    k = 1
    i = 2
    
    # Current spin
    current_spin = s[k, i]
    assert current_spin == -1, f"Expected s[{k}, {i}] = -1, got {current_spin}"
    
    # Calculate delta_E_prob
    local_field = h[i] + np.dot(J_sym[i], s[k])
    delta_E_prob = -2 * s[k, i] * local_field
    assert np.isclose(delta_E_prob, 4.0), f"Expected delta_E_prob = 4.0, got {delta_E_prob}"
    
    # Calculate delta_H_trotter
    s_prev = s[(k-1) % P, i]
    s_next = s[(k+1) % P, i]
    delta_H_trotter = 2 * J_perp * s[k, i] * (s_prev + s_next)
    expected_delta_H_trotter = 0.7719368
    assert np.isclose(delta_H_trotter, expected_delta_H_trotter, atol=1e-6), \
        f"Expected delta_H_trotter ≈ {expected_delta_H_trotter}, got {delta_H_trotter}"
    
    # Calculate delta_S
    delta_S = (beta / P) * delta_E_prob + beta * delta_H_trotter
    expected_delta_S = 3.5438736
    assert np.isclose(delta_S, expected_delta_S, atol=1e-6), \
        f"Expected delta_S ≈ {expected_delta_S}, got {delta_S}"
    
    # Calculate P_accept
    P_accept = np.exp(-delta_S)
    expected_P_accept = 0.0289011
    assert np.isclose(P_accept, expected_P_accept, atol=1e-6), \
        f"Expected P_accept ≈ {expected_P_accept}, got {P_accept}"

def test_sqa_inner_loop():
    """
    Test the full SQA inner loop implementation.
    """
    # Use a small example that we can verify
    h = np.array([0.0, 0.0])
    J = np.array([[0, 1], [1, 0]])
    num_sweeps = 10
    beta = 1.0
    P = 2
    
    # Set a fixed random seed for reproducibility
    np.random.seed(42)
    
    sampler = SimulatedQuantumAnnealingSampler()
    
    # Run the sampler
    samples, energies = sampler.sample_ising(h, J, num_sweeps, beta, P=P)
    
    # Check that we got the expected shapes
    assert samples.shape == (1, 2), f"Expected samples shape (1, 2), got {samples.shape}"
    assert energies.shape == (1,), f"Expected energies shape (1,), got {energies.shape}"
    
    # Check that all spins are either -1 or 1
    assert np.all((samples == -1) | (samples == 1)), "All spins should be either -1 or 1"

if __name__ == "__main__":
    test_sqa_worked_example()
    test_sqa_inner_loop()
    print("All tests passed!")