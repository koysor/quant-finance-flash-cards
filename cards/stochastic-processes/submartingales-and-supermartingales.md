# Submartingales and Supermartingales

**Topic:** Stochastic Processes
**Tags:** submartingale, supermartingale, drift, martingale, inequality, american options
**Created:** 2026-03-07
**Author:** Claude Opus 4.6

---

## Definition

A **submartingale** is a process whose conditional expected future value is at least as large as its current value — it has non-negative drift (an upward tendency on average). A **supermartingale** is the opposite: its conditional expected future value is at most its current value — it has non-positive drift (a downward tendency on average). A martingale is the special case that is simultaneously both.

## Key Formula

| Process | Condition | Drift |
|---|---|---|
| Submartingale | $E[M_t \mid \mathcal{F}_s] \geq M_s$ | Non-negative ($\geq 0$) |
| Martingale | $E[M_t \mid \mathcal{F}_s] = M_s$ | Zero ($= 0$) |
| Supermartingale | $E[M_t \mid \mathcal{F}_s] \leq M_s$ | Non-positive ($\leq 0$) |

For an SDE $dY = f(t)\,dt + g(t)\,dW_t$:

- $f(t) > 0$ for all $t$ $\Rightarrow$ $Y$ is a submartingale
- $f(t) = 0$ for all $t$ $\Rightarrow$ $Y$ is a martingale
- $f(t) < 0$ for all $t$ $\Rightarrow$ $Y$ is a supermartingale

## Example

Consider three processes where $W_t$ is standard Brownian motion:

**Submartingale:** $Y_t = W_t + 2t$. Since $dY = 2\,dt + dW$, the drift is $+2 > 0$:

$$E[Y_t \mid \mathcal{F}_s] = W_s + 2s + 2(t - s) = Y_s + 2(t - s) \geq Y_s$$

**Martingale:** $W_t$ itself. Drift is zero: $E[W_t \mid \mathcal{F}_s] = W_s$.

**Supermartingale:** $Z_t = W_t - 3t$. Drift is $-3 < 0$:

$$E[Z_t \mid \mathcal{F}_s] = Z_s - 3(t - s) \leq Z_s$$

## Remember

Supermartingales are central to American option pricing. The discounted price of an American option under $\mathbb{Q}$ is a supermartingale — it can only decrease in expected value because the holder's right to exercise early is being consumed over time. The **Snell envelope** (the smallest supermartingale dominating the discounted payoff) gives the American option price at every time step, and the **optimal exercise boundary** is the set of points where the supermartingale touches the payoff. Submartingales arise in wealth processes of strategies with positive expected return under $\mathbb{P}$ — a profitable trading strategy generates a submartingale wealth process, which is why the optional stopping theorem places restrictions on when you can "cash out" without losing the drift advantage.
