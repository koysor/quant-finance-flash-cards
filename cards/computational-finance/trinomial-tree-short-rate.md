# Trinomial Tree for Short-Rate Models

**Topic:** Computational Finance
**Tags:** trinomial tree, Ho-Lee, Hull-White, lattice, numerical methods, yield curve, short rate, calibration, backward induction
**Created:** 2026-06-14
**Author:** Claude Sonnet 4.6

---

## Definition

A **trinomial tree** is a recombining lattice in which the spot rate $r$ can move up, stay flat, or move down by $\Delta r = \sigma\sqrt{3\Delta t}$ at each time step. The branching probabilities are tuned column by column so the tree **exactly reprices every observed zero-coupon bond** — the discrete-time analogue of calibrating the continuous drift function $\eta(t)$ in Ho-Lee or Hull-White.

## Key Formula

At each node the three probabilities must match the first two moments of the rate process. With $\Delta r = \sigma\sqrt{3\Delta t}$:

$$p_u = \tfrac{1}{6} + \tfrac{u_j\,\Delta t}{2\Delta r}, \qquad p_m = \tfrac{2}{3}, \qquad p_d = \tfrac{1}{6} - \tfrac{u_j\,\Delta t}{2\Delta r}$$

where $u_j$ is the column-specific drift offset. The **calibration step** at column $j$ solves for $u_j$ such that backward induction from all nodes at time $j$ reprices the market zero-coupon bond $Z_M(0;\,j\Delta t)$ exactly. Repeating this for $j = 1, 2, \ldots$ builds the fully calibrated tree by **forward induction** through the maturity pillars.

## Example

Ho-Lee with $c = 0.01$ (1% annual vol), monthly steps ($\Delta t = 1/12$):

$$\Delta r = 0.01\sqrt{3/12} = 0.00289 \approx 29\text{ bps}$$

At $j=1$, one drift offset $u_1$ is solved from one bond price $Z_M(0;\,1\text{m})$. At $j=2$, a new offset $u_2$ is solved from $Z_M(0;\,2\text{m})$ using the already-calibrated $j=1$ nodes. Each step uses only one free parameter and one market price.

## Remember

The trinomial tree turns calibration into a **column-by-column forward sweep**: one drift unknown, one market bond price, one equation per step. This is the standard numerical implementation of Ho-Lee and Hull-White in practice — fast enough to use for pricing callable bonds and Bermudan swaptions where a closed-form solution does not exist.
