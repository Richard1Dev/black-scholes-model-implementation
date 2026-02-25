# Black-Scholes Model Implementation


### Overview: Pricing and Discrete Delta Hedging Simulation

Option pricing plays a crucial role in modern financial markets, providing a framework for evaluating financial derivatives such as stock options, interest rate options, and commodities. The Black-Scholes model, developed in 1973 by Fischer Black, Myron Scholes, and Robert C. Merton, revolutionised the pricing of European-style options by providing an analytical solution to the problem of option valuation under certain assumptions. This model is widely regarded as one of the foundational theories in financial mathematics. This model is implemented in this project.


### Project aims:

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
- $V = V(S,t)$ is the pricing function for an option with a payoff $\Phi = \Phi(S)$.


### Black-Scholes Equation

Setting the underlying price

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
\frac{\partial V}{\partial t} + \frac{1}{2} \sigma^{2} S^{2} \frac{\partial^{2}V}{\partial S^{2}} + rS \frac{\partial V}{\partial S} - rV = 0 \qquad\quad V(T,S) = \Phi(S)
$$

which is otherwise known as the Black-Scholes Equation.


### Black-Scholes Formula

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
\frac{\partial u}{\partial \tau} = \frac{1}{2} \sigma^{2} \frac{\partial^2 u}{\partial x^2} \qquad\qquad u(x,0) = e^{-ax}\Phi(e^x)
$$

otherwise known as the heat equation. The solution is

$$
I_1 = \frac{\exp(a\ln (S)+b\tau)}{\sqrt{2\pi \sigma^2 \tau}} \int_{-\infty}^{\infty} \exp\left(\frac{-(\ln (S)-w)^2}{2\sigma^2 \tau} - aw\right) \Phi(e^w) \,\mathrm{d}w
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

and ito's lemma (again)

$$
\mathrm{d}V
= \frac{\partial V}{\partial t} \mathrm{d}t + \frac{\partial V}{\partial S} \mathrm{d}S + \frac{1}{2} \frac{\partial^{2}V}{\partial S^{2}} \mathrm{d} \langle S \rangle \\
= \frac{\partial V}{\partial t} \mathrm{d}t + \frac{\partial V}{\partial S} \left( r S_t\mathrm{d}t + \sigma S_t \mathrm{d}W_t^\mathbb{Q} \right) + \frac{1}{2} \sigma^2 S^2 \frac{\partial^{2}V}{\partial S^{2}} \mathrm{d} t \\
= \left( \frac{\partial V}{\partial t} + \frac{1}{2} \sigma^{2} S^{2} \frac{\partial^{2}V}{\partial S^{2}} + rS \frac{\partial V}{\partial S} \right) \mathrm{d}t + \sigma S \frac{\partial V}{\partial S} \mathrm{d}W^\mathbb{Q} \\
= rV\mathrm{d}t + \sigma S \frac{\partial V}{\partial S} \mathrm{d}W^\mathbb{Q}
$$

we find that

$$
\mathrm{d}U = e^{-rt} \sigma S \frac{\partial V}{\partial S} \, \mathrm{d}W^\mathbb{Q}
$$

is a $\mathbb{Q}$-martingale. Taking the conditional expectation yields

$$
V(S,t) = \mathbb{E}^\mathbb{Q} [e^{-r\tau}\Phi(S_T)|S_t = S]
$$

otherwise known as the Feynman-Kac formula. Taking

$$
\ln (S_T) \sim \mathcal{N} \Big( \ln(S) + (r - \frac{1}{2}\sigma^2)\tau, \sigma^2 \tau \Big) \Big| S_t=S,\ \tau=T-t,
$$

yields

$$
I_2 = e^{-r\tau} \int_0^\infty \Phi(y) \frac{1}{\sqrt{2\pi \sigma^2 \tau}} \exp\!\left( -\frac{\left(\ln y - \ln S - (r-\tfrac12\sigma^2)\tau\right)^2} {2\sigma^2 \tau} \right) \, \frac{\mathrm{d}y}{y}
$$

or we could have said

$$
S_T = S_t \exp ((r - \frac{1}{2}\sigma^2)\tau + \sigma \sqrt{\tau} Z) \quad\quad \tau=T-t \quad\quad Z \sim \mathcal{N}(0,1)
$$

yielding

$$
I_3 = e^{-r\tau} \int_{-\infty}^{\infty} \Phi\!\left( S \exp\Big((r-\frac12\sigma^2)\tau + \sigma\sqrt{\tau} z\Big) \right) \frac{1}{\sqrt{2\pi}} e^{-z^2/2} \,\mathrm{d} z
$$

where in any case, we have $I_1 = I_2 = I_3$.




### Vanilla Options




### Greeks







