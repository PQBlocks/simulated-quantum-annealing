"""Example 02: Evaluating quantum transverse-field annealing with varying Trotter replicas."""

import numpy as np
from pqblocks_anneal_sqa import SimulatedQuantumAnnealingSampler


def main():
    # 4-spin frustrated Ising model
    h = [-1.0, 1.0, 2.0, -2.0]
    J = [
        [0.0, 1.0, -1.0, 2.0],
        [0.0, 0.0, 1.0, -1.0],
        [0.0, 0.0, 0.0, -2.0],
        [0.0, 0.0, 0.0, 0.0],
    ]

    print("--- SQA Multi-Replica Transverse-Field Annealing ---")
    sampler = SimulatedQuantumAnnealingSampler()
    trotter_dims = [4, 8, 16]

    for p in trotter_dims:
        samples, energies = sampler.sample_ising(
            h=h,
            J=J,
            P=p,
            num_sweeps=200,
            beta=4.0,
        )
        print(f"Trotter replicas (P={p:2d}): Best Energy = {energies[0]:.6f}, Config = {samples[0].tolist()}")

    print("\nTrotter replica evaluation completed successfully.")


if __name__ == "__main__":
    main()
