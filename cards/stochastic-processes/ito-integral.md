# Itô Integral

**Topic:** Stochastic Processes
**Tags:** stochastic integral, martingale, brownian motion, zero expectation, hedging
**Created:** 2026-03-07
**Author:** Claude Opus 4.6

---

## Definition

The **Itô integral** $\int_0^t g(s, X_s)\,dX_s$ is the stochastic integral of an adapted process with respect to Brownian motion. A fundamental property is that every Itô integral is a **martingale** with zero expectation, provided the integrand satisfies standard integrability conditions.

## Key Formula

$$I(t) = \int_0^t g(s, X_s)\,dX_s$$

Since $I(0) = 0$ and $I(t)$ is a martingale:

$$E\!\left[\int_0^t g(s, X_s)\,dX_s\right] = 0$$

When computing expectations via Itô's lemma, the $dX$ terms vanish and only the $dt$ terms survive:

$$E[f(X_T)] = f(X_0) + E\!\left[\int_0^T (\text{drift terms})\,ds\right]$$

## Example

Compute $E[X_T^2]$ where $X_t$ is standard Brownian motion. By Itô's lemma:

$$d(X_t^2) = dt + 2X_t\,dX_t$$

Integrate and take expectations. The Itô integral $\int_0^T 2X_t\,dX_t$ has zero expectation:

$$E[X_T^2] = \int_0^T dt + 0 = T$$

This confirms $\text{Var}(X_T) = T$.

## Remember

The zero-expectation property of Itô integrals is the workhorse result for computing expected values in derivative pricing. When you apply Itô's lemma to an option price $V(S, t)$ and take expectations, all the $dW$ terms vanish — leaving only the deterministic $dt$ terms. This is precisely how the Black–Scholes PDE is derived: the hedged portfolio's return must equal the risk-free rate because the stochastic component (the Itô integral) contributes zero expected value, and any remaining drift would create an arbitrage opportunity.
