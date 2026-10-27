# Autonomous Agent Integration Guide

> Operational instructions and best practices for AI and autonomous software agents integrating `pqblocks-anneal-sqa`.

---

## 1. Package Purpose

`pqblocks-anneal-sqa` provides a Simulated Quantum Annealing (Path-Integral Monte Carlo) heuristic solver for Ising spin-glass and QUBO optimization problems.

---

## 2. Key APIs

```python
from pqblocks_anneal_sqa import SimulatedQuantumAnnealingSampler, SQABenchmarkWrapper

# Direct solver invocation
sampler = SimulatedQuantumAnnealingSampler()
samples, energies = sampler.sample_ising(
    h=h_vector,         # list or np.ndarray: (N,) linear bias terms
    J=J_matrix,         # list or np.ndarray: (N, N) coupling terms
    beta=5.0,           # float: inverse temperature (default: 5.0)
    gamma_0=2.0,        # float: initial transverse field (default: 2.0)
    gamma_f=0.01,       # float: final transverse field (default: 0.01)
    P=32,               # int: Trotter dimension / replicas (default: 32)
    num_sweeps=1000     # int: Monte Carlo sweeps (default: 1000)
)
```

---

## 3. Best Practices for Agents

1. **Trotter Dimension Tuning**: Default $P=32$ provides solid quantum emulation. For fast exploratory searches, $P=8$ or $P=16$ reduces runtime linearly with negligible quality loss on small models ($N \le 20$).
2. **Deterministic Execution**: Always pass fixed seeds if testing probabilistic convergence distributions.
3. **Ising Variable Conventions**: Variables are spins $s_i \in \{-1, +1\}$. For binary $x_i \in \{0, 1\}$, use `pqblocks-qubo` to perform lossless conversion prior to sampling.
