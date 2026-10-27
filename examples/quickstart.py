from pqblocks_anneal_sqa import SimulatedQuantumAnnealingSampler

h = [-1.0, 1.0, 2.0, -2.0]
J = [[0.0, 1.0, -1.0, 2.0],
     [0.0, 0.0, 1.0, -1.0],
     [0.0, 0.0, 0.0, -2.0],
     [0.0, 0.0, 0.0, 0.0]]

sampler = SimulatedQuantumAnnealingSampler()
samples, energies = sampler.sample_ising(h, J)
print(f'Best Spin State: {samples[0].tolist()}')
print(f'Best Energy: {energies[0]:.6f}')
