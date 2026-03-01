# American Option Pricing

**Topic:** Derivatives
**Tags:** American options, options pricing, early exercise, binomial tree, exercise boundary

---

## Definition

An **American option** can be exercised at any time up to and including expiry. This early-exercise right means the option is worth at least as much as its European counterpart, but it also destroys the possibility of a simple closed-form price. Pricing requires solving an optimal stopping problem: at every instant, the holder must decide whether to exercise now or wait.

## Key Formula

At each point in time, the American option price $V$ satisfies:

$$V(S, t) = \max\!\bigl(\text{intrinsic value},\; e^{-r\,\delta t}\,\mathbb{E}^{\mathbb{Q}}[V(S_{t+\delta t}, t+\delta t)]\bigr)$$

For an American put, the intrinsic value is $\max(K - S, \, 0)$. The option is exercised early whenever the stock price falls below the **critical exercise boundary** $S^*(t)$:

$$\text{Exercise when } S_t \leq S^*(t) \quad \text{(American put)}$$

For an American call on a non-dividend-paying stock, early exercise is never optimal, so $C_{\text{American}} = C_{\text{European}}$.

## Example

Price an American put using a one-step binomial tree. $S_0 = 40$, $K = 42$, $u = 1.2$, $d = 0.8$, $r = 5\%$, $T = 1$ year.

Risk-neutral probability: $q = \frac{e^{0.05} - 0.8}{1.2 - 0.8} = \frac{1.051 - 0.8}{0.4} = 0.628$

Payoffs at expiry: up → $\max(42 - 48, 0) = 0$; down → $\max(42 - 32, 0) = 10$

European value: $e^{-0.05}(0.628 \times 0 + 0.372 \times 10) = 0.951 \times 3.72 = £3.54$

But the intrinsic value today is $\max(42 - 40, 0) = £2.00 < £3.54$, so early exercise is not optimal at this node. American put price = **£3.54**.

## Remember

American options dominate equity markets — most single-stock options are American-style. The early-exercise premium is largest for deep in-the-money puts (where locking in cash now beats waiting) and for calls on dividend-paying stocks (where exercising just before the ex-dividend date captures the payout). Because no closed-form solution exists, practitioners price American options using binomial trees, finite-difference methods, or the Longstaff-Schwartz Monte Carlo algorithm.
