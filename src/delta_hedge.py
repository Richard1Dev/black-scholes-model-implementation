this_filename = '''src/delta_hedge.py'''
declare_import = False
import numpy as np



class MarketState:
    
    def __init__(self, runs, steps, maturity):
        self.runs = runs
        self.steps = steps
        length = steps + 1
        shape = (runs, length)

        self.time = np.linspace(0, maturity, length)

        self.cash = np.zeros(shape)
        self.underlying = np.zeros(shape)
        self.option = np.zeros(shape)
        self.true_delta = np.zeros(shape)
        self.approx_delta = np.zeros(shape)
        self.gamma = np.zeros(shape)

        self.pnl = np.zeros(runs)



class DeltaHedgingEngine:

    def __init__(self, option, model, steps_threshold=1000):
        self.option = option
        self.model = model
        self.s_threshold = steps_threshold

    def run(self, rate, sigma, runs, mesh, random_seed=None):
        if random_seed is not None:
            np.random.seed(random_seed)

        maturity = self.option.T
        temp = int(round(maturity * (1/mesh)))
        mesh_multiplier = int(self.s_threshold // temp) + 1
        steps = mesh_multiplier * temp
        length = steps + 1
        dt = maturity / steps

        data = MarketState(runs, steps, maturity)
        data.underlying = self.model.simulate(maturity, runs, dt, random_seed)
        data.option = self.option.price(data.underlying, data.time, rate, sigma)
        data.true_delta = self.option.delta(data.underlying, data.time, rate, sigma)
        data.gamma = self.option.gamma(data.underlying, data.time, rate, sigma)

        old_delta = data.true_delta[:, 0]
        data.approx_delta[:, 0] = old_delta
        data.cash[:, 0] = -data.option[:, 0] + data.true_delta[:, 0]*data.underlying[:, 0]

        for j in range(1, length):

            data.cash[:, j] = np.exp(rate*dt)*data.cash[:, j-1]

            if j % mesh_multiplier:
                data.approx_delta[:, j] = old_delta
            else:
                data.approx_delta[:, j] = data.true_delta[:, j]
                data.cash[:, j] += (data.true_delta[:, j] - old_delta)*data.underlying[:, j]
                old_delta = data.true_delta[:, j]
        
        data.cash[:, -1] = np.exp(rate*dt)*data.cash[:, -2]
        data.pnl[:] = data.option[:, -1] - old_delta*data.underlying[:, -1] + data.cash[:, -1]

        return data



if __name__ == '__main__':
    print(f"Running {this_filename}...")
else:
    if declare_import:
        print(f"Importing {this_filename}...")
