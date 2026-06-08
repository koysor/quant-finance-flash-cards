# Passport Option

**Topic:** Derivatives
**Tags:** passport option, path-dependent, optimal control, hjb equation, trading strategy, exotic option
**Created:** 2026-06-08
**Author:** Claude Sonnet 4.6

---

## Definition

A **passport option** gives the holder the right to receive the positive profit-and-loss of a managed trading account at expiry, where the holder may choose any bounded trading strategy $q_t \in [-q_{\max}, q_{\max}]$ adaptively during the option's life. The option writer funds losses; the holder pockets any gains — making it a call on the value of an optimally-run trading account.

## Key Formula

Let $X_t$ be the mark-to-market account value at time $t$ under strategy $q_t$:

$$dX_t = q_t \, dS_t = q_t \, S_t (\mu \, dt + \sigma \, dW_t)$$

The payoff at expiry is $\max(X_T, 0)$. The passport option value $V(t, x, S)$ satisfies the Hamilton–Jacobi–Bellman (HJB) PDE:

$$\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + rS\frac{\partial V}{\partial S} - rV + \max_{q \in [-q_{\max}, q_{\max}]} \left[ q \sigma^2 S^2 \frac{\partial^2 V}{\partial x \partial S} + \frac{1}{2}q^2 \sigma^2 S^2 \frac{\partial^2 V}{\partial x^2} \right] = 0$$

The optimal strategy is: go **maximum long** ($q = +q_{\max}$) when $\partial V/\partial x > 0$ (gains improve option value), and **maximum short** ($q = -q_{\max}$) when $\partial V/\partial x < 0$.

## Example

Consider a 1-year passport option, $\sigma = 20\%$, $q_{\max} = 1$ share, $S_0 = 100$, $r = 5\%$. The optimal policy switches between fully long and fully short as the account value evolves. If the account reaches $X_T = +\$25$, the payoff is \$25; if $X_T = -\$8$, the holder receives \$0 (losses are borne by the option writer). The premium is approximately twice that of an at-the-money European call on the same underlying.

## Remember

Passport options sit at the intersection of derivatives pricing and optimal control theory: the pricing PDE is solved numerically (typically via finite difference methods on a 2-D grid of account value and stock price). They are used in **performance-linked compensation structures** where a portfolio manager is guaranteed not to lose the firm's capital but retains full upside from their trading decisions — aligning incentives without exposing the firm to downside risk.
