this_filename = '''src/underlying.py'''
declare_import = False
import numpy as np


class GeometricBrownianMotion:
    def __init__(self, spot, drift, sigma, maturity, runs, mesh, mesh_ratio=1, random_seed=None):
        self.spot = spot
        self.drift = drift
        self.sigma = sigma
        self.maturity = maturity
        self.mesh = mesh
        self.fine_mesh = mesh / mesh_ratio
        self.length = int(self.maturity / self.fine_mesh)
        self.runs = runs
        if random_seed is not None:
            np.random.seed(random_seed)
        noise = np.random.normal(size=(runs, self.length))
        increments = (
            (self.drift - 0.5*self.sigma**2) * self.fine_mesh
            + self.sigma * np.sqrt(self.fine_mesh) * noise
        )
        log_paths = np.cumsum(increments, axis=1)
        log_paths = np.hstack([np.zeros((runs, 1)), log_paths])
        self.paths = self.spot * np.exp(log_paths)


if __name__ == '__main__':
    print(f'Running {this_filename}...')
else:
    if declare_import:
        print(f'Importing {this_filename}...')
