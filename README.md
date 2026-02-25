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

- $r$ is the risk free interest rate.
- $S_t$ is the price of the asset at time $t$.
- $\mu$ is the drift.
- $\sigma$ is the volatility.
- $W_t$ is a standard Brownian motion or Wiener process.
- $V = V(S,t)$ is the pricing function for an option.

### Black-Scholes Equation

Setting the underlying price

$$
S_T = S_t \exp \Big( (\mu - \frac{1}{2} \sigma^2)(T-t) + \sigma (W_T - W_t) \Big)
$$

to one side, we seek to derive the famous partial differential equation. Consider a portfolio

$$
\Pi = V - \Delta \mathrm{d} S
\qquad\qquad
\mathrm{d} \Pi = \mathrm{d} V - \Delta \mathrm{d} S
$$

and apply It\^o's lemma. Then

$$
\mathrm{d}\Pi = \left(\frac{\partial V}{\partial t} + \frac{1}{2} \sigma^2 S^2 \frac{\partial^{2}V}{\partial S^{2}} \right) \mathrm{d}t + \left( \frac{\partial V}{\partial S} - \Delta \right) \mathrm{d} S
$$

since $\langle S \rangle_t = \sigma^2 S^2 t$. To eliminate stochasticity, we set

$$
\Delta = \frac{\partial V}{\partial S}
$$

using the assumption that we may trade assets continuously. In doing so, we have eliminated risk.

$$
\left( \frac{\partial V}{\partial S} - \Delta \right) \mathrm{d} S
$$

vanishes to leave

$$
\mathrm{d}\Pi = \left(\frac{\partial V}{\partial t} + \frac{1}{2} \sigma^2 S^2 \frac{\partial^{2}V}{\partial S^{2}} \right) \mathrm{d}t
$$

as a risk-free portfolio. But by no-arbitrage, we must have that

$$
\mathrm{d} \Pi = r \Pi \mathrm{d} t
$$

which, after plugging in $\mathrm{d} \Pi$ on the left and $\Pi$ on the right, yields

$$
\frac{\partial V}{\partial t} + \frac{1}{2} \sigma^{2} S^{2} \frac{\partial^{2}V}{\partial S^{2}} + rS \frac{\partial V}{\partial S} - rV = 0 \qquad\quad V(T,S) = \Phi(S)
$$

which is otherwise known as the Black-Scholes Equation.


### Black-Scholes Formula


### Vanilla Options


### Greeks







