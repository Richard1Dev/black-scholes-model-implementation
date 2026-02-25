# Black-Scholes Model Implementation

A mathematical and computational implementation of the Black–Scholes model for European option pricing, including derivation sketches, closed-form solutions, Greeks computation, simulation of underlying paths, and numerical delta hedging verification. This project bridges continuous-time financial theory and practical discrete-time implementation.


### Overview

The **Black–Scholes model (1973)** provides an analytical framework for pricing European-style options under no-arbitrage assumptions. Developed by Fischer Black, Myron Scholes, and Robert C. Merton, it remains foundational in quantitative finance.


### Project aims:

- Document the key Black-Scholes assumptions.
- Sketch derivations of famous results:
    - the Black-Scholes Equation,
    - Feynman-Kac Formula,
    - Black-Scholes Formula,
    - and closed-form solutions of vanilla options.
- Implement vanilla option pricing and sensitivities (Greeks) in Python.
- Provide key visualisation such as sample underlying paths and the option pricing function.
- Conduct discrete delta hedging experiments.
- Analyse portfolio error under discrete trading.

The aim is to connect theory, computation, and financial interpretation in a unified framework.


### Project Structure

```
root/
│
├── figures/
│   └── ...
│
├── notebooks/
│   └── results.ipynb
│
├── src
│   ├── delta_hedge.py
│   ├── option.py
│   └── underlying.py
│
├── .gitattributes
├── .gitignore
└── README.md
```


### Implementation

- Methods for pricing and Greeks within option classes.
- Addition operator overriding to instantiate linear combinations of options. E.g. butterfly spread.
- Geometric Brownian Motion simulation.
- Discrete delta hedging engine.
- PnL replication error analysis.
- Visualisations:
    - Sample price paths
    - Payoff functions
    - Option price surfaces
    - Hedging error convergence


### Numerical Experiments

The project investigates:

- Convergence of discrete delta hedging to continuous hedging
- Impact of:
    - Not hedging at all (control)
    - Rebalancing frequency
    - Drift
- Distribution of hedging PnL

As trading frequency increases, hedging error converges in probability toward zero, numerically validating the Black–Scholes Equation.


### Skills Demonstrated

- Stochastic calculus (Ito processes)
- Risk-neutral valuation
- PDE methods (parabolic equations)
- Measure change techniques
- Numerical simulation (Monte Carlo)
- Quantitative risk decomposition
- Python scientific computing (NumPy, SciPy, Matplotlib)


### Conclusion and Project Outcomes



---

### Future Extensions

- Dividend-paying assets
- Implied volatility solver
- Local volatility models
- Stochastic volatility (e.g., Heston)
- Transaction costs in hedging
- American option pricing (finite difference methods)



---

# Theory

Derivations are found in the appendix.


### Assumptions

The Black–Scholes model relies on the following key assumptions:

- **Efficient Markets:** Markets have no arbitrage opportunities.
- **Risk-Free Rate:** The risk-free interest rate is constant and known.
- **Frictionless Markets:** Assets are perfectly liquid, with no bid-ask spread, and can always be traded without additional transaction costs. Short selling is also included.
- **Underlying Asset Dynamics:** The asset price follows a geometric Brownian motion with constant drift and volatility.
    - **Log-Normal Prices:** Asset prices are log-normally distributed.
    - **Constant Drift:** Emphasising again that the drift is constant and known.
    - **Constant Volatility:** Emphasising again that the volatility is constant and known.
- **Continuous Trading:** The asset can be traded infinitely often, and in any quantity.
- **European Options:** Options can only be exercised at expiration.
- **No Dividends:** The asset does not pay dividends during the option's life.


### Notation

- $r$ is the risk free interest rate.
- $S_t$ is the price of the asset at time $t$.
- $\mu$ is the drift.
- $\sigma$ is the volatility.
- $V = V(S,t)$ is the pricing function for an option with a payoff $\Phi = \Phi(S)$.
- $T$ is the maturity (years).
- $K$ is the strike price.
- $N(\cdot)$ is the cdf of the standard Gaussian distribution $\mathcal{N}(0,1)$.


### Hedging Analysis



---

# Appendix


### Black-Scholes Equation

Let $W_t$ denote a standard Brownian motion or Wiener process. Setting the underlying price

$$
S_T = S_t \exp \Big( (\mu - \frac{1}{2} \sigma^2)(T-t) + \sigma (W_T - W_t) \Big)
$$

to one side, we seek to derive the famous partial differential equation. Consider a portfolio

$$
\Pi = V - \Delta \mathrm{d}S
\qquad\qquad
\mathrm{d}\Pi = \mathrm{d}V - \Delta \mathrm{d}S
$$

and apply Ito's lemma. Then

$$
\mathrm{d}\Pi = \left(\frac{\partial V}{\partial t} + \frac{1}{2} \sigma^2 S^2 \frac{\partial^{2}V}{\partial S^{2}} \right) \mathrm{d}t + \left( \frac{\partial V}{\partial S} - \Delta \right) \mathrm{d} S
$$

since $\langle S \rangle_t = \sigma^2 S^2 t$. To eliminate stochasticity, we set

$$
\Delta = \frac{\partial V}{\partial S}
$$

using the assumption that we may trade assets continuously. In doing so, we have eliminated risk. The $\mathrm{d} S$ term vanishes to leave

$$
\mathrm{d}\Pi = \left(\frac{\partial V}{\partial t} + \frac{1}{2} \sigma^2 S^2 \frac{\partial^{2}V}{\partial S^{2}} \right) \mathrm{d}t
$$

as a risk-free portfolio. But by no-arbitrage, we must have that

$$
\mathrm{d} \Pi = r \Pi \mathrm{d} t
$$

which, after plugging in $\mathrm{d} \Pi$ on the left and $\Pi$ on the right, yields

$$
\frac{\partial V}{\partial t} + \frac{1}{2} \sigma^{2} S^{2} \frac{\partial^{2}V}{\partial S^{2}} + rS \frac{\partial V}{\partial S} - rV = 0
\qquad\quad
V(S,T) = \Phi(S)
$$

which is otherwise known as the Black-Scholes Equation.


### Feynman-Kac Formula and Black-Scholes Formula

To obtain the solution to the parabolic second order partial differential equation, we may use one of two methods:

- Heat Equation,
- Feynman-Kac.

We will state the substitutions necessary to sketch the heat equation route and discuss Feynman-Kac.

To get to the heat equation, apply the following substitutions:

1. $\tau = T-t$,
2. $x = \ln (S)$,
3. $V = e^{ax + b\tau} u$ with $a = \frac{1}{2} - \frac{r}{\sigma^2}$ and $b = -\frac{1}{2} \left( \frac{r^2}{\sigma^2} + r + \frac{\sigma^2}{4} \right)$,

and you arrive at

$$
\frac{\partial u}{\partial \tau} = \frac{1}{2} \sigma^{2} \frac{\partial^2 u}{\partial x^2}
\qquad\qquad
u(x,0) = e^{-ax}\Phi(e^x)
$$

otherwise known as the heat equation. The solution is

$$
I_1 = \frac{S^a e^{b\tau}}{\sqrt{2\pi \sigma^2 \tau}} \int_{-\infty}^{\infty} \exp\left(\frac{-(\ln (S)-w)^2}{2\sigma^2 \tau} - aw\right) \Phi(e^w) \mathrm{d}w
$$

by convoluting the transformed payoff function with the Guassian heat kernal.

In the Feynman-Kac route, consider a change of measure $\mathbb{Q}$ such that

$$
\frac{\mathrm{d} S_t}{S_t} = r \mathrm{d}t + \sigma \mathrm{d}W_t^\mathbb{Q}
$$

and the discounted option price $U = e^{-rt} V$. Then by the product rule

$$
\mathrm{d}U = e^{-rt} (-rV\mathrm{d}t + \mathrm{d}V)
$$

and ito's lemma (again... along with using the $\mathbb{Q}$ model for $S$)

$$
\mathrm{d}V = \left( \frac{\partial V}{\partial t} + \frac{1}{2} \sigma^{2} S^{2} \frac{\partial^{2}V}{\partial S^{2}} + rS \frac{\partial V}{\partial S} \right) \mathrm{d}t + \sigma S \frac{\partial V}{\partial S} \mathrm{d}W^\mathbb{Q}
$$

we find that

$$
\mathrm{d}U = e^{-rt} \sigma S \frac{\partial V}{\partial S} \mathrm{d}W^\mathbb{Q}
$$

is a $\mathbb{Q}$-martingale. Taking the conditional expectation yields

$$
V(S,t) = \mathbb{E}^\mathbb{Q} [e^{-r\tau}\Phi(S_T)|S_t = S]
$$

otherwise known as the Feynman-Kac formula. Taking

$$
\ln (S_T) \sim \mathcal{N} \Big( \ln(S) + (r - \frac{1}{2}\sigma^2)\tau, \sigma^2 \tau \Big) \Big| S_t=S,\ \tau=T-t
$$

yields

$$
I_2 = e^{-r\tau} \int_0^\infty \Phi(y) \frac{1}{\sqrt{2\pi \sigma^2 \tau}} \exp \left( -\frac{\left(\ln y - \ln S - (r-\tfrac12\sigma^2)\tau\right)^2} {2\sigma^2 \tau} \right) \frac{\mathrm{d}y}{y}
$$

or alternatively,

$$
S_T = S_t \exp \Big((r - \frac{1}{2}\sigma^2)\tau + \sigma \sqrt{\tau} Z\Big)
\quad\quad
\tau=T-t
\quad\quad
Z \sim \mathcal{N}(0,1)
$$

yields

$$
I_3 = e^{-r\tau} \int_{-\infty}^{\infty} \Phi \left( S \exp\Big((r-\frac12\sigma^2)\tau + \sigma\sqrt{\tau} z\Big) \right) \frac{1}{\sqrt{2\pi}} e^{-z^2/2} \mathrm{d} z
$$

where it can be shown that $I_1 = I_2 = I_3$.


### Vanilla Options

Consider $I_3$ for a call option $C(S,t)$ with payoff $\Phi(S) = max(S-K,0)$. Write

$$
N(x) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^x e^{-u^2/2} du
\qquad
N'(x) = \frac{1}{\sqrt{2\pi}} e^{-x^2/2}
$$

and define

$$
d_1 = \frac{\ln(S/K) + (r + \frac{1}{2}\sigma^2)\tau}{\sigma \sqrt{\tau}}
\qquad\quad
d_2 = d_1 - \sigma \sqrt{\tau}
\qquad\quad
\tau = T-t
$$

to see

$$
C(S,t) = e^{-r\tau} \left[S e^{(r-\frac12\sigma^2)\tau} \int_{-d_2}^{\infty} e^{\sigma\sqrt{\tau}z}N'(z) dz - K \int_{-d_2}^{\infty} N'(z) dz \right]
$$

after noting $[-d_2,\infty)$ is the non-vanishing part of the integrand and distributing the intergral over the minus sign. Applying the identity

$$
\int_\alpha^\infty e^{\beta z}N'(z) dz = e^{\beta^2/2} N(-\alpha+\beta)
$$

with $\alpha=-d_2$ and $\beta=\sigma\sqrt{\tau}$ yields the standard result for the call option

$$
C(S,t) = S N(d_1)-K e^{-r\tau} N(d_2)
$$

with the put option

$$
P(S,t) = K e^{-r\tau} N(-d_2) - S N(-d_1)
$$

following from put-call parity: $P = C - S + K e^{-r\tau}$.


### Greeks

The quantities

$$
\Delta = \frac{\partial V}{\partial S} \qquad \Gamma = \frac{\partial^2 V}{\partial S^2} \qquad \mathcal{V} = \frac{\partial V}{\partial \sigma} \qquad \Theta = \frac{\partial V}{\partial t}
$$

are known as "the Greeks" and are the primary option sensitivities. These quantities measure the local sensitivity of the option value $V(S,t)$ to changes in the underlying price $S$, volatility $\sigma$, and time $t$. Beyond their computational definitions, they characterise the structure of risk in the Black-Scholes framework. Together, they decompose option risk into directional (delta), curvature (gamma), volatility (vega), and temporal (theta) components, forming the basis of practical risk management and hedging strategies. The Greeks therefore characterise both the local behaviour of the pricing function and the stability of the replication strategy. They provide the link between the continuous-time theory and the discrete-time approximations. Deriving the Greeks are left as an exercise for brevity.

---


