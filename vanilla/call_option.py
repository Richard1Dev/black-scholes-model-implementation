this_filename = '''vanilla/call_option.py'''
import numpy as np
from scipy.stats import norm
from _option import EuropeanOption

class CallOption(EuropeanOption):
    
    def payoff(self, spot):
        return np.maximum(spot - self.K, 0.0)

    def price(self, spot, time, rate, sigma):
        tau = self._tau(time)
        d1 = self._d1(spot, time, rate, sigma)
        d2 = self._d2(d1, time, sigma)
        return spot*norm.cdf(d1) - self.K*np.exp(-rate*tau)*norm.cdf(d2)

    def delta(self, spot, time, rate, sigma):
        return norm.cdf(self._d1(spot, time, rate, sigma))

    def gamma(self, spot, time, rate, sigma):
        tau = self._tau(time)
        return norm.pdf(self._d1(spot, time, rate, sigma)) / (spot*sigma*np.sqrt(tau))

    def vega(self, spot, time, rate, sigma):
        tau = self._tau(time)
        return spot*norm.pdf(self._d1(spot, time, rate, sigma))*np.sqrt(tau)

    def theta(self, spot, time, rate, sigma):
        tau = self._tau(time)
        d1 = self._d1(spot, time, rate, sigma)
        d2 = self._d2(d1, time, sigma)
        return -(((spot*norm.pdf(d1)*sigma) / (2*np.sqrt(tau))) + (rate*self.K*np.exp(-rate*tau)*norm.cdf(d2)))

if __name__ == '__main__':
    print(f'Running {this_filename}...')
else:
    print(f'Importing {this_filename}...')
