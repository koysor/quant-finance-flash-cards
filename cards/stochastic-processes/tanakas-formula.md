# Tanaka's Formula

**Topic:** Stochastic Processes
**Tags:** tanaka formula, local time, ito calculus, non-smooth, absolute value, barrier options
**Created:** 2026-06-20
**Author:** Claude Sonnet 4.6

---

## Definition

**Tanaka's formula** extends Itô's lemma to the function $f(x) = \lvert x \rvert$, which is not twice differentiable at $x = 0$. It shows that the absolute value of a Brownian motion is a semimartingale, and introduces **local time** $L_t^0(W)$ — the measure of time the process spends at level zero — as the correction term that replaces the missing second derivative.

## Key Formula

For a standard Brownian motion $W_t$:

$$\lvert W_t \rvert = \int_0^t \operatorname{sgn}(W_s)\,dW_s + L_t^0(W)$$

where $\operatorname{sgn}(x) = \mathbf{1}_{x > 0} - \mathbf{1}_{x \le 0}$ and $L_t^0(W)$ is the **local time at zero**, defined as the limit:

$$L_t^0(W) = \lim_{\varepsilon \to 0} \frac{1}{2\varepsilon} \int_0^t \mathbf{1}_{\{\lvert W_s \rvert < \varepsilon\}}\,ds$$

More generally, for any level $a \in \mathbb{R}$ and the function $f(x) = \lvert x - a \rvert$:

$$\lvert W_t - a \rvert = \lvert W_0 - a \rvert + \int_0^t \operatorname{sgn}(W_s - a)\,dW_s + L_t^a(W)$$

## Example

Consider $W_t$ with $W_0 = 0$. At time $t = 1$, simulate 100,000 paths. The first term $\int_0^1 \operatorname{sgn}(W_s)\,dW_s$ is a stochastic integral with mean zero and variance $\int_0^1 1\,ds = 1$, so it behaves like a standard normal. The local time $L_1^0$ accumulates positively whenever $W$ is near zero. Numerically, $E[\lvert W_1 \rvert] = \sqrt{2/\pi} \approx 0.798$, which equals $E[L_1^0]$ since the stochastic integral term has zero expectation, confirming $E[L_1^0] = \sqrt{2/\pi}$.

## Remember

Tanaka's formula is the theoretical foundation for pricing **barrier options** and other path-dependent contracts that depend on how often an asset crosses a particular level. The local time $L_t^a$ at level $a$ measures the density of crossings of that level up to time $t$ — in a barrier option context, this quantifies how close the asset price $S_t$ has been to the barrier. The formula also underpins the **reflection principle** for Brownian motion and appears in the proof that the running maximum $\max_{s \le t} W_s$ has the same distribution as $\lvert W_t \rvert$, a result used directly in closed-form barrier option pricing formulae.
