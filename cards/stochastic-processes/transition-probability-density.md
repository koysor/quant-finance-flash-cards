# Transition Probability Density Function

**Topic:** Stochastic Processes
**Tags:** transition density, probability density, Fokker-Planck, Kolmogorov, normalisation, option pricing
**Created:** 2026-02-28
**Author:** Claude Opus 4.6

---

## Definition

The **transition probability density function** $p(y, t;\, y', t')$ gives the probability density that a stochastic process currently at state $y$ at time $t$ will be found at state $y'$ at a later time $t' > t$. The semicolon separates the present (conditioning) variables from the future variables: everything before the semicolon is "where you are now", everything after is "where you might end up".

The density must satisfy the **normalisation condition**:

$$\int_{-\infty}^{\infty} p(y, t;\, y', t') \, dy' = 1$$

This simply states that the process must be *somewhere* at the future time $t'$.

## Key Formula

For the SDE $dX = a(X)\,dt + b(X)\,dW$, the transition density $p(y,t;\,y',t')$ satisfies two complementary PDEs:

**Forward (Fokker-Planck) equation** — differentiate with respect to the future variables $(y', t')$:

$$\frac{\partial p}{\partial t'} = -\frac{\partial}{\partial y'}\bigl[a(y')\,p\bigr] + \frac{1}{2}\frac{\partial^2}{\partial y'^2}\bigl[b(y')^2\,p\bigr]$$

**Backward (Kolmogorov) equation** — differentiate with respect to the present variables $(y, t)$:

$$-\frac{\partial p}{\partial t} = a(y)\frac{\partial p}{\partial y} + \frac{1}{2}b(y)^2\frac{\partial^2 p}{\partial y^2}$$

The same function $p$ satisfies both equations — the forward equation evolves the density in the future direction, while the backward equation evolves it in the present direction.

## Example

For **Brownian motion** ($a = 0$, $b = 1$) starting at $y$ at time $t$, the transition density to $y'$ at time $t'$ is:

$$p(y, t;\, y', t') = \frac{1}{\sqrt{2\pi(t'-t)}} \exp\!\left(-\frac{(y'-y)^2}{2(t'-t)}\right)$$

Verify normalisation: this is a Gaussian in $y'$ with mean $y$ and variance $t' - t$, so $\int p\,dy' = 1$ by the standard Gaussian integral.

For **geometric Brownian motion** under the risk-neutral measure ($dS = rS\,dt + \sigma S\,dW$), the transition density in $\log S$ is Gaussian with mean $\log S_0 + (r - \tfrac{1}{2}\sigma^2)(T - t)$ and variance $\sigma^2(T - t)$.

## Remember

In derivatives pricing, the transition probability density **is** the risk-neutral probability of the underlying asset reaching a given price $S'$ at expiry. The fair value of any European payoff $f(S_T)$ is computed by integrating the payoff against this density:

$$V = e^{-r(T-t)} \int_0^{\infty} f(S')\,p(S, t;\, S', T)\,dS'$$

The Black-Scholes formula is simply the closed-form result of this integral when $f$ is a call or put payoff and $p$ is the lognormal transition density of GBM. Understanding the transition density lets you price any payoff — exotic or vanilla — by numerical integration, and it connects the PDE approach (backward Kolmogorov) to the expectation approach (forward Fokker-Planck) in a single object.
