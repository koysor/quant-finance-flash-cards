# Arrow-Debreu State Prices

**Topic:** Derivatives
**Tags:** arrow-debreu, state prices, no-arbitrage, complete markets, contingent claims, risk-neutral pricing
**Created:** 2026-06-21
**Author:** Claude Sonnet 4.6

---

## Definition

An Arrow-Debreu state price $Q_{t,j}$ is the time-0 price of a security that pays £1 if and only if node $(t, j)$ of the interest rate tree is reached, and £0 in every other state. Because every payoff can be decomposed into a sum of such unit payoffs, $Q_{t,j}$ are the fundamental building blocks of no-arbitrage pricing in a complete discrete market.

## Key Formula

State prices are propagated forward recursively from the root:

$$Q_{t+1,\,j+1} = p\,e^{-r_{t,j}\,\Delta t}\,Q_{t,j}, \qquad Q_{t+1,\,j} = (1-p)\,e^{-r_{t,j}\,\Delta t}\,Q_{t,j}$$

(for a recombining binomial tree the two contributions to the middle node are summed). Any security with terminal payoff $\Pi_j$ at time $T$ is then priced as:

$$V_0 = \sum_{j} Q_{T,j}\,\Pi_j$$

The zero-coupon bond price follows immediately as the special case $\Pi_j = 1$:

$$P(0,T) = \sum_{j} Q_{T,j}$$

## Example

Two-step tree: $r_0 = 5\%$, $r_u = 6.2\%$, $r_d = 5.8\%$, $p = \tfrac{1}{2}$, $\Delta t = 1$ year.

**Step 1** — state prices at $t = 1$:

$$Q_{1,u} = \tfrac{1}{2}\,e^{-0.05} = 0.4756, \qquad Q_{1,d} = \tfrac{1}{2}\,e^{-0.05} = 0.4756$$

**Step 2** — state prices at $t = 2$ (three nodes; the middle receives contributions from both $t{=}1$ nodes):

$$Q_{2,uu} = \tfrac{1}{2}\,e^{-0.062}\times 0.4756 = 0.2234$$

$$Q_{2,ud} = \tfrac{1}{2}\,e^{-0.062}\times 0.4756 + \tfrac{1}{2}\,e^{-0.058}\times 0.4756 = 0.2234 + 0.2243 = 0.4477$$

$$Q_{2,dd} = \tfrac{1}{2}\,e^{-0.058}\times 0.4756 = 0.2243$$

**Check:** $Q_{2,uu} + Q_{2,ud} + Q_{2,dd} = 0.2234 + 0.4477 + 0.2243 = 0.8954 \approx P(0,2) \checkmark$

A floorlet paying $\max(5.8\% - r_{2,j},\,0)\times 100$ is then priced as $0.4477 \times 0 + 0.2243 \times 0 + 0 = 0$ for the up/mid nodes and $0.2243 \times (5.8\%-5.8\%)\times 100 = 0$ at the down node — or substitute any rate payoff directly into the sum.

## Remember

Two facts tie Arrow-Debreu prices to practice. First, $\sum_j Q_{T,j} = P(0,T)$: calibrating an interest rate tree to zero-coupon bond prices is *exactly* the requirement that the state prices sum to the correct discount factors — the two tasks are mathematically identical. Second, once state prices are computed in a single forward sweep, *every* fixed income derivative (cap, floor, swaption, callable bond) reduces to the same weighted sum $\sum_j Q_{T,j}\,\Pi_j$, eliminating repeated backward inductions and making sensitivity analysis (bumping one rate) computationally trivial.
