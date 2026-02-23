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





class DeltaHedgeSimulation:
    # produces S,V,Delta,cash,pnl

    def __init__(self) -> None:
        pass # store option, gbm

    def run(self):
        # runs the sim and populated the data. returns None (stateful) #this is the actual delta hedging (seeds the info)
        pass

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
