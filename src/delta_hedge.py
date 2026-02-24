this_filename = '''src/delta_hedge.py'''
declare_import = False
import numpy as np

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
    #       invy = +option_T -delta_{\hat{T}}*shares_T
    #    close the position! i.e liquidate invy
    #       liquidate invy cash gain = max(S-K,0) -delta_{\hat{T}}*shares_T
    #       cash = cash_T + max(S-K,0) -delta_{\hat{T}}*shares_T
    # since we took a loan at the start and the value of our invy should grow at the same rate, the liquidation at the end ought to cancel out
    # expect final cash to be 0

    #portfolio = cash_0 + (V-DS) where cash_0 = -(V-DS)



class MarketState:
    #hold S paths, V paths, D paths for plotting
    # be vectorised so it hold pnl mean/var/histogram

    def __init__(self, runs, steps, maturity):
        self.runs = runs
        self.steps = steps
        self.time = np.linspace(0, maturity, steps+1) # 1*steps
        shape = (runs, steps+1)
        self.spot = np.zeros(shape)
        self.option = np.zeros(shape)
        self.true_delta = np.zeros(shape)
        self.approx_delta = np.zeros(shape)
        self.cash = np.zeros(shape) #????
        self.portfolio = np.zeros(shape) #????V-D*S
        self.pnl = np.zeros(shape) # 1*runs



    time = np.linspace(0, underlying.maturity, n_steps_plus_one)

    delta = call.delta(paths[:, 0], 0, rate, sigma)
    option_value = call.price(paths[:, 0], 0, rate, sigma)

    stock_position = delta
    cash_account = option_value - stock_position * paths[:, 0]

    pnl_series = np.zeros((n_paths, n_steps_plus_one))

# len = terminal / mesh
# N = T/dt
# want N1 N2... N1 = T/dt (hedge mesh) and N2 = k*N1 (simulation mesh)
# shape <----> length
# [0.000, 0.001, 0.002]
# 
class DeltaHedgingEngine:
    # produces S,V,Delta,cash,pnl

    def __init__(self, option, model):
        self.option = option
        self.model = model
        self.state = None

    def run(self, rate, sigma, runs, mesh, mesh_multiplier=100, random_seed=None):
        # runs the sim and populated the data. returns None (stateful) #this is the actual delta hedging (seeds the info)
        maturity = self.option.T
        if random_seed is not None:
            np.random.seed(random_seed)
        temp = int(round(maturity / mesh))
        hedge_mesh = maturity / temp
        length = mesh_multiplier * temp
        sim_mesh = maturity / length
        data = MarketState(runs, length, maturity)
        data.spot = self.model.simulate(maturity, runs, sim_mesh, random_seed)
        time = 0
        spot = data.spot[:, time]
        data.option[:, 0] = self.option.price(spot, time, rate, sigma)
        data.true_delta[:, 0] = self.option.delta(spot, time, rate, sigma)
        self.pnl[:, 0] = 0
        pass

    
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

    def path(self, i=0):
        return {
            #'S': self.gbm.S[i],
            #'V': self.V[i],
            #'delta': self.delta[i]
        }
    
    #plot singluar path method
    #mean/var method
    #plot pnl histogram method



if __name__ == '__main__':
    print(f'Running {this_filename}...')
else:
    if declare_import:
        print(f'Importing {this_filename}...')
