# Recombining Tree

**Topic:** Derivatives
**Tags:** recombining tree, binomial tree, lattice, CRR, option pricing, computational complexity
**Created:** 2026-04-19
**Author:** Claude Sonnet 4.6

---

## Definition

A **recombining tree** (or recombining lattice) is a discrete-time model for an asset price in which an up move followed by a down move returns to the same price node as a down move followed by an up move. This path-independence means an $N$-step tree has $N+1$ terminal nodes rather than $2^N$, reducing computational complexity from exponential to quadratic.

## Key Formula

**Recombining condition:** $u \cdot d = 1$

In the Cox-Ross-Rubinstein (CRR) parameterisation this is satisfied by:

$$u = e^{\sigma\sqrt{\Delta t}}, \qquad d = e^{-\sigma\sqrt{\Delta t}} = \frac{1}{u}$$

Node value after $j$ up-moves and $k$ down-moves in $n = j+k$ steps:

$$S_{j,k} = S_0\, u^j d^k = S_0\, u^{j-k}$$

which depends only on the net number of up-moves $j - k$, not on the order they occurred.

## Example

A 3-step non-recombining tree has $2^3 = 8$ terminal nodes. The CRR tree with $ud = 1$ has only $3+1 = 4$: $S_0 u^3$, $S_0 u$, $S_0 d$, $S_0 d^3$. For $N = 500$ steps used in practice, this reduces $2^{500} \approx 10^{150}$ nodes to just 501.

## Remember

The recombining property is what makes lattice methods computationally feasible for option pricing: American options, barrier options, and other path-independent derivatives are priced by backward induction through the tree's $\mathcal{O}(N^2)$ nodes. Non-recombining trees are sometimes used for path-dependent options (e.g. Asian options) but their exponential node count forces truncation, making Monte Carlo simulation the preferred alternative for those products.
