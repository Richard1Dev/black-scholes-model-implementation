# Black-Scholes Model Implementation

### Overview: Pricing and Discrete Delta Hedging Simulation

Option pricing plays a crucial role in modern financial markets, providing a framework for evaluating financial derivatives such as stock options, interest rate options, and commodities. The Black-Scholes model, developed in 1973 by Fischer Black, Myron Scholes, and Robert C. Merton, revolutionised the pricing of European-style options by providing an analytical solution to the problem of option valuation under certain assumptions. This model is widely regarded as one of the foundational theories in financial mathematics. This model is implemented in this project.

###### Project aims:

- Document the key Black-Scholes assumptions.
- Provide a loose derivation of famous results such as the Black-Scholes Equation, Black-Scholes Formula, and closed-form solutions of vanilla options.
- Implement vanilla option pricing and sensitivities (Greeks) in Python.
- Provide key visualisation such as sample underlying paths and the option pricing function.
- Carry out delta hedging in order to numerically verify the Black-Scholes Equation.

---

# Theory

### Assumptions

The Black–Scholes model relies on the following key assumptions:

- **Efficient Markets:** Markets have no arbitrage opportunities.
- **Risk-Free Rate:** The risk-free interest rate is constant and known.
- **Frictionless Markets:** Assets are perfectly liquid, with no bid-ask spread, and can always be traded without additional transaction costs. Short selling is also included.
- **Underlying Asset Dynamics:** The asset price follows a geometric Brownian motion with constant drift and volatility.
    - **Log-Normal Prices:** Asset prices are log-normally distributed.
    - **Constant Drift:** Emphasising again that the drift is constant and known.
    - **Constant Volatility:** Emphasising again that the volatility is constant and known.
- **Continuous Trading:** The asset can be traded continuously in any quantity.
- **European Options:** Options can only be exercised at expiration.
- **No Dividends:** The asset does not pay dividends during the option's life.

### Notation

- $S_t$ is the price of the asset at time $t$.
- $\mu$ is the drift.
- $\sigma$ is the volatility.
- $W_t$ is a standard Brownian motion or Wiener process.

### Black-Scholes Equation

The underlying price

$$
S_T = S_t \exp \Big( (\mu - \frac{1}{2} \sigma^2)(T-t) + \sigma (W_T - W_t) \Big)
$$

### Black-Scholes Formula


### Vanilla Options


### Greeks





