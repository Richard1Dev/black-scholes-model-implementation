this_filename = '''src/underlying.py'''
declare_import = False
import numpy as np



class GeometricBrownianMotion:
    def __init__(self, spot, drift, sigma):
        self.spot = spot
        self.drift = drift
        self.sigma = sigma
    def simulate(self, terminal, runs, mesh, random_seed=None):
        if random_seed is not None:
            np.random.seed(random_seed)
        length = int(terminal / mesh)
        noise = np.random.normal(size=(runs, length))
        increments = (
            (self.drift - 0.5*self.sigma**2) * mesh
            + self.sigma * np.sqrt(mesh) * noise
        )
        log_paths = np.cumsum(increments, axis=1)
        log_paths = np.hstack([np.zeros((runs, 1)), log_paths])
        return self.spot * np.exp(log_paths)



if __name__ == '__main__':
    print(f"Running {this_filename}...")
else:
    if declare_import:
        print(f"Importing {this_filename}...")
