# Weak Path Dependence

**Topic:** Derivatives
**Tags:** weak path dependence, asian option, state augmentation, pde, running average, exotic options
**Created:** 2026-06-13
**Author:** Claude Sonnet 4.6

---

## Definition

An option is **weakly path-dependent** if its payoff depends on the history of the underlying price, but that history can be summarised by a small number of additional state variables that evolve continuously alongside $S_t$. Because the history compresses into finitely many extra dimensions, the pricing PDE can be augmented rather than replaced — a 2D or 3D finite-difference grid suffices, with no need for full-path Monte Carlo simulation.

## Key Formula

For a discretely-sampled Asian call with $n$ fixing dates and running sum $I_t = \sum_{t_i \leq t} S_{t_i}$, the augmented PDE between consecutive fixings is:

$$\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + rS\frac{\partial V}{\partial S} - rV = 0, \qquad \frac{\partial I}{\partial t} = 0$$

At each fixing date $t_k$, the running sum jumps: $I \mapsto I + S_{t_k}$. The terminal condition on the $(S,\, I)$ grid is:

$$V(S,\, I,\, T) = \max\!\left(\frac{I}{n} - K,\; 0\right)$$

## Example

An Asian call with $n = 3$ monthly fixings, $K = 100$, and first two fixings at $S_{t_1} = 105$ and $S_{t_2} = 97$ gives running sum $I = 202$. The remaining pricing problem is a 2D PDE in $(S,\, I,\, t)$: once $S_{t_3}$ is realised, payoff $= \max\!\left((202 + S_{t_3})/3 - 100,\, 0\right)$. If $S_{t_3} = 100$, payoff $= \max(100.67 - 100, 0) = 0.67$; the 2D grid prices this at inception without simulating any paths.

## Remember

Weak path dependence is the reason Asian options can be priced accurately on a finite-difference grid, giving Greek sensitivities (delta, gamma, vega) at every $(S, I)$ node simultaneously — a major advantage over Monte Carlo, which delivers Greeks only by bumping the model and re-running thousands of paths. In risk management, this speed advantage is decisive: a bank that writes hundreds of Asian options on the same underlying needs to compute deltas across all of them in real time, and a 2D PDE grid does this in milliseconds rather than seconds. The cost is that each extra state variable multiplies the grid size by a factor, so options with two or more path-dependent accumulators become computationally heavy and switch to Monte Carlo.
