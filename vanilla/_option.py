this_filename = '''vanilla/_option.py'''
from abc import ABC, abstractmethod
import numpy as np

class EuropeanOption(ABC):
    def __init__(self, strike, maturity):
        self.K = strike
        self.T = maturity

    def _tau(self, time):
        return self.T - time

    def _d1(self, spot, time, rate, sigma):
        tau = self._tau(time)
        return (np.log(spot/self.K) + (rate + 0.5*sigma**2) * tau) / (sigma * np.sqrt(tau))

    def _d2(self, d1, time, sigma):
        tau = self._tau(time)
        return d1 - sigma*np.sqrt(tau)
    
    def intrinsic_value(self, spot, time, rate):
        return self.payoff(spot) * np.exp(-rate*self._tau(time))

    def implied_volatility(self, spot, time, rate, sigma):
        raise NotImplementedError

    @abstractmethod
    def payoff(self, spot):
        raise NotImplementedError

    @abstractmethod
    def price(self, spot, time, rate, sigma):
        raise NotImplementedError

    @abstractmethod
    def delta(self, spot, time, rate, sigma):
        raise NotImplementedError

    @abstractmethod
    def gamma(self, spot, time, rate, sigma):
        raise NotImplementedError

    @abstractmethod
    def vega(self, spot, time, rate, sigma):
        raise NotImplementedError

    @abstractmethod
    def theta(self, spot, time, rate, sigma):
        raise NotImplementedError


if __name__ == '__main__':
    print(f'Running {this_filename}...')
else:
    print(f'Importing {this_filename}...')
