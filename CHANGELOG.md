# Changelog

All notable changes to `pqblocks-anneal-sqa` are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2026-10-26

### Added
- Simulated Quantum Annealing (Path-Integral Monte Carlo) heuristic solver.
- Suzuki-Trotter Hamiltonian mapping with configurable Trotter replicas $P$.
- Dynamic transverse magnetic field annealing from $\Gamma_0$ to $\Gamma_f$.
- High-performance Numba JIT-compiled inner Monte Carlo sweep kernel.
- Standard benchmark wrapper (`SQABenchmarkWrapper`) conforming to `dimod.BinaryQuadraticModel`.
- Comprehensive test suite with 18 tests passing across Python 3.11, 3.12, 3.13, and 3.14.
- Quickstart and multi-replica evaluation examples.
