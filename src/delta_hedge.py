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



_ = '''
def delta_hedge(underlying, call, rate):
    assert underlying.maturity == call.T
    paths = underlying.paths
    n_steps = underlying.n_steps
    dt = underlying.step_size

    spot = paths[:, 0]
    sigma = underlying.sigma
    
    delta = call.delta(spot, 0, rate, sigma)
    cost = call.price(spot, 0, rate, sigma) - delta*spot
    for j in range(1, n_steps):
        t = j*dt
        spot = paths[:, j]
        cost *= np.exp(rate*dt)
        new_delta = call.delta(spot, t, rate, sigma)
        cost -= (new_delta - delta)*spot
        delta = new_delta
    cost *= np.exp(rate*dt)
    spot = paths[:, n_steps]
    portfolio = call.payoff(spot) - delta*spot
    pnl = portfolio - cost
    return pnl

    # note: bs is risk neutral (Q-measure), but the stock is allowed to be mu (P-measure)
    #initial conditions:
    #       portfolio = 0
    #    get a loan to buy option and short shares
    #       cash_0 = -option +delta_shares
    #       inventory = +option -delta_shares
    #at t = t_j = j*dt
    #       cash = cash_j
    #       invy = +option_j -delta_j*shares_j
    #at t = t_{j+1}
    #       cash = cash_j * e**(r*dt)
    #       invy = +option_{j+1} -delta_j*shares_{j+1}
    #    we need to rebalance!
    #       cash = cash_j * e**(r*dt) +(delta_{j+1} - delta_j)*shares_{j+1}
    #       invy = +option_{j+1} -delta_{j+1}*shares_{j+1}
    #at t = T
    #       cash = cash_T
    #       invy = +option_T -delta_{hat{T}}*shares_T
    #    close the position! i.e liquidate invy
    #       liquidate invy cash gain = max(S-K,0) -delta_{hat{T}}*shares_T
    #       cash = cash_T + max(S-K,0) -delta_{hat{T}}*shares_T
    # since we took a loan at the start and the value of our invy should grow at the same rate, the liquidation at the end ought to cancel out
    # expect final cash to be 0

    #portfolio = cash_0 + (V-DS) where cash_0 = -(V-DS)

    
    #plot singluar path method
    #mean/var method
    #plot pnl histogram method
'''



if __name__ == '__main__':
    print(f"Running {this_filename}...")
else:
    if declare_import:
        print(f"Importing {this_filename}...")
