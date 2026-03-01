# Black-Scholes Model Implementation


### Overview

A mathematical and computational implementation of the Black–Scholes model for European option pricing, including derivation sketches, closed-form solutions, simulation of underlying paths, and numerical delta hedging verification. This project bridges continuous-time financial theory and practical discrete-time implementation.


### Project aims

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


### Implementation

- Option classes, with methods for pricing and Greeks.
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
