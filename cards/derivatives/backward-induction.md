# Backward Induction

**Topic:** Derivatives
**Tags:** binomial tree, option pricing, dynamic programming, delta, CQF

---

## Definition

**Backward induction** is the algorithm used to price options on a binomial tree. Starting from the known payoffs at expiry (the terminal nodes), we work backwards through the tree one time-step at a time, computing the option value at each node as the discounted risk-neutral expectation of the two successor nodes. At every interior node we also compute the hedge ratio (delta) from the difference in option values divided by the difference in stock prices.

For American-style options, backward induction includes an additional comparison at each node: the continuation value is checked against the immediate exercise value, and the larger of the two is kept.

## Key Formula

At each interior node, the **one-step pricing formula** gives the option value:

$$V_{i,j} = e^{-r\Delta t}\bigl[q\,V_{i+1,j+1} + (1-q)\,V_{i+1,j}\bigr]$$

where $q$ is the risk-neutral probability of an up move:

$$q = \frac{e^{r\Delta t} - d}{u - d}$$

and $u$, $d$ are the up and down multipliers (e.g. $u = e^{\sigma\sqrt{\Delta t}}$, $d = 1/u$).

The **delta** (hedge ratio) at each node is:

$$\Delta_{i,j} = \frac{V_{i+1,j+1} - V_{i+1,j}}{S_{i+1,j+1} - S_{i+1,j}}$$

For an American option, replace $V_{i,j}$ with:

$$V_{i,j} = \max\!\bigl(\text{exercise value},\; e^{-r\Delta t}[q\,V_{i+1,j+1} + (1-q)\,V_{i+1,j}]\bigr)$$

## Example

Price a European call: $S_0 = 100$, $K = 100$, $r = 5\%$, $u = 1.10$, $d = 0.90$, $\Delta t = 1$ year, 2 steps.

**Step 1 — Build the stock tree:**

| Node | Price |
|------|-------|
| $S_{uu}$ | $100 \times 1.10^2 = 121$ |
| $S_{ud}$ | $100 \times 1.10 \times 0.90 = 99$ |
| $S_{dd}$ | $100 \times 0.90^2 = 81$ |

**Step 2 — Terminal payoffs** ($\max(S - K, 0)$):

$$V_{uu} = 21, \quad V_{ud} = 0, \quad V_{dd} = 0$$

**Step 3 — Risk-neutral probability:**

$$q = \frac{e^{0.05} - 0.90}{1.10 - 0.90} = \frac{1.0513 - 0.90}{0.20} = 0.756$$

**Step 4 — Work backward to step 1:**

$$V_u = e^{-0.05}(0.756 \times 21 + 0.244 \times 0) = 0.9512 \times 15.88 = 15.11$$

$$V_d = e^{-0.05}(0.756 \times 0 + 0.244 \times 0) = 0$$

**Step 5 — Work backward to step 0:**

$$V_0 = e^{-0.05}(0.756 \times 15.11 + 0.244 \times 0) = 0.9512 \times 11.42 = \textbf{£10.87}$$

**Delta at the root:**

$$\Delta_0 = \frac{15.11 - 0}{110 - 90} = 0.756$$

## Remember

Backward induction is the workhorse algorithm behind the Cox-Ross-Rubinstein binomial model. It prices any payoff — European, American, exotic — on a recombining tree by reducing the problem to a sequence of one-period no-arbitrage arguments. As the number of steps increases, the binomial price converges to the Black-Scholes price for European options. On trading desks, the same backward-pass logic extends to trinomial trees and finite-difference grids for pricing instruments where no closed-form solution exists.
