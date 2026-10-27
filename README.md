# pqblocks-anneal-sqa

> Simulated Quantum Annealing (Path-Integral Monte Carlo via Suzuki-Trotter decomposition) heuristic solver for Ising and QUBO optimization problems.

[![CI](https://github.com/PQBlocks/simulated-quantum-annealing/actions/workflows/ci.yml/badge.svg)](https://github.com/PQBlocks/simulated-quantum-annealing/actions/workflows/ci.yml)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)

---

> [!NOTE]
> **Domain Classification**: Quantum-inspired classical optimisation: not cryptography, no security claim.

---

## Overview

`pqblocks-anneal-sqa` is a classical quantum-inspired optimization solver implementing Simulated Quantum Annealing (SQA).

By mapping a quantum transverse-field Ising Hamiltonian into an equivalent classical $(d+1)$-dimensional system via Suzuki-Trotter decomposition (Path-Integral Monte Carlo), the solver simulates quantum tunneling effects through narrow potential energy barriers. The inner Trotter loop is accelerated with Numba JIT compilation, delivering high-throughput sampling on CPU architectures.

### Key Highlights

- **Suzuki-Trotter Mapping**: Replaces quantum transverse terms with $P$ classical replicas coupled along an imaginary-time Trotter dimension.
- **Quantum Tunneling Emulation**: Enables transitions across tall, narrow barriers where thermal simulated annealing often gets trapped in local minima.
- **Numba JIT Kernel**: Optimized inner Monte Carlo sweeps for high throughput.
- **Standard Interface**: Exposes a clean `sample_ising` interface and `SQABenchmarkWrapper` conforming to the `dimod` benchmark harness interface.

---

## Installation

```bash
pip install pqblocks-anneal-sqa
```

### Dependencies

Requires Python 3.11+, `numpy`, `scipy`, `dimod`, and `numba`.

---

## Quickstart

```python
from pqblocks_anneal_sqa import SimulatedQuantumAnnealingSampler

# 1. Define 4-spin Ising problem
h = [-1.0, 1.0, 2.0, -2.0]
J = [
    [0.0, 1.0, -1.0, 2.0],
    [0.0, 0.0, 1.0, -1.0],
    [0.0, 0.0, 0.0, -2.0],
    [0.0, 0.0, 0.0, 0.0],
]

# 2. Initialize SQA solver
sampler = SimulatedQuantumAnnealingSampler()

# 3. Sample Ising ground state
samples, energies = sampler.sample_ising(h, J, num_sweeps=1000, beta=5.0, P=32)

print("Best Spin State:", samples[0].tolist())
print(f"Best Energy: {energies[0]:.6f}")
```

---

## Multi-Replica Trotter Dimensions

Control the Trotter dimension $P$ (the number of classical replicas in imaginary time):

```python
# Evaluate with P=16 Trotter replicas
samples, energies = sampler.sample_ising(h, J, P=16, num_sweeps=500)
```

---

## Fair Benchmarking Disclaimer

When comparing SQA against classical simulated annealing (like D-Wave Neal) and constraint solvers (CP-SAT):
- **Work Normalization**: SQA computes updates across $P$ Trotter replicas simultaneously (e.g. $P=32$), doing $P \times$ more spin updates per sweep than single-replica simulated annealing.
- **Latency vs Barrier Crossing**: Single-replica SA exhibits lower per-read latency, while SQA is designed to traverse barriers via simulated quantum tunneling.

---

## Verification & Testing

Tested across Python 3.11, 3.12, 3.13, and 3.14.

```bash
pytest
```

---

## License

Licensed under the Apache License, Version 2.0. See [LICENSE](LICENSE) and [NOTICE](NOTICE).
