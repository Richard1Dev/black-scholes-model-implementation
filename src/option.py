this_filename = '''src/options.py'''
declare_import = False
from abc import ABC, abstractmethod
import numpy as np
from scipy.stats import norm


class Position:
    def __init__(self, components=None):
        self.components = components or []

    def add(self, instrument, weight=1.0):
        self.components.append((instrument, weight))
        return self

    def __add__(self, other):
        if isinstance(other, Position):
            return Position(self.components + other.components)
        return Position(self.components + [(other, 1.0)])

    def __sub__(self, other):
        if isinstance(other, Position):
            neg = [(inst, -w) for inst, w in other.components]
            return Position(self.components + neg)
        return Position(self.components + [(other, -1.0)])

    def __mul__(self, scalar):
        return Position([(inst, scalar*w) for inst, w in self.components])

    __rmul__ = __mul__

    def payoff(self, spot):
        return sum(w * inst.payoff(spot) for inst, w in self.components)

    def price(self, spot, time, rate, sigma):
        return sum(w * inst.price(spot, time, rate, sigma) for inst, w in self.components)

    def delta(self, spot, time, rate, sigma):
        return sum(w * inst.delta(spot, time, rate, sigma) for inst, w in self.components)

    def gamma(self, spot, time, rate, sigma):
        return sum(w * inst.gamma(spot, time, rate, sigma) for inst, w in self.components)

    def vega(self, spot, time, rate, sigma):
        return sum(w * inst.vega(spot, time, rate, sigma) for inst, w in self.components)

    def theta(self, spot, time, rate, sigma):
        return sum(w * inst.theta(spot, time, rate, sigma) for inst, w in self.components)


class EuropeanOption(ABC):
    def __init__(self, strike, maturity):
        self.K = strike
        self.T = maturity

    def _tau(self, time):
        return np.maximum(self.T - time, 1e-12)

    def _d1(self, spot, time, rate, sigma):
        tau = self._tau(time)
        return (np.log(spot/self.K) + (rate + 0.5*sigma**2) * tau) / (sigma * np.sqrt(tau))

    def _d2(self, d1, time, sigma):
        tau = self._tau(time)
        return d1 - sigma*np.sqrt(tau)
    
    def discounted_payoff(self, spot, time, rate):
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
    
    def __mul__(self, scalar):
        return Position([(self, scalar)])

    __rmul__ = __mul__

    def __add__(self, other):
        return Position([(self, 1.0)]) + other

    def __sub__(self, other):
        return Position([(self, 1.0)]) - other


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


class PutOption(EuropeanOption):
    
    def payoff(self, spot):
        return np.maximum(self.K - spot, 0.0)

    def price(self, spot, time, rate, sigma):
        tau = self._tau(time)
        d1 = self._d1(spot, time, rate, sigma)
        d2 = self._d2(d1, time, sigma)
        return self.K*np.exp(-rate*tau)*norm.cdf(-d2) - spot*norm.cdf(-d1)

    def delta(self, spot, time, rate, sigma):
        return -norm.cdf(-self._d1(spot, time, rate, sigma))

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
        return -(((spot*norm.pdf(d1)*sigma) / (2*np.sqrt(tau))) - (rate*self.K*np.exp(-rate*tau)*norm.cdf(-d2)))


if __name__ == '__main__':
    print(f'Running {this_filename}...')
else:
    if declare_import:
        print(f'Importing {this_filename}...')
