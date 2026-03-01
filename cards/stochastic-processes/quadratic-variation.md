# Quadratic Variation

**Topic:** Stochastic Processes
**Tags:** quadratic variation, Brownian motion, stochastic calculus, path roughness
**Author:** Claude Opus 4.6

---

## Definition

The **quadratic variation** of a process $X$ over the interval $[0, t]$ is the limit of the sum of squared increments as the partition becomes infinitely fine:

$$[X]_t = \lim_{n \to \infty} \sum_{j=1}^{n} \bigl(X(t_j) - X(t_{j-1})\bigr)^2$$

For a smooth (deterministic) function, the quadratic variation is zero — the squared increments vanish faster than they accumulate. For Brownian motion, the quadratic variation is **non-zero and deterministic**: $[W]_t = t$. This is what makes stochastic calculus fundamentally different from ordinary calculus.

## Key Formula

**Brownian motion quadratic variation:**

$$[W]_t = \sum_{j=1}^{n} (W_{t_j} - W_{t_{j-1}})^2 \xrightarrow{n \to \infty} t$$

The convergence is in **mean square**: the expected squared error vanishes:

$$E\!\left[\left(\sum_{j=1}^{n} (\Delta W_j)^2 - t\right)^{\!2}\right] = O\!\left(\frac{1}{n}\right) \to 0$$

**Discrete random walk:** each step is $\pm 1$, so $(S_j - S_{j-1})^2 = 1$ always. After $i$ steps:

$$\text{QV}_i = \sum_{j=1}^{i} 1 = i$$

The quadratic variation is deterministic even though the path is random.

## Example

Consider a coin-toss random walk with 100 steps. The path is random — it could end anywhere from $-100$ to $+100$. Yet the sum of squared increments is:

$$\text{QV}_{100} = \sum_{j=1}^{100} (\pm 1)^2 = \textbf{100}$$

with certainty. Every path, no matter how it twists and turns, has exactly the same quadratic variation. When this walk is rescaled to Brownian motion over $[0, 1]$, the quadratic variation becomes $[W]_1 = 1$.

## Remember

- Quadratic variation is the **fingerprint of randomness**. Smooth functions have zero quadratic variation; Brownian motion has quadratic variation equal to elapsed time.
- The result $[W]_t = t$ is what forces the second-order term in the Taylor expansion to survive, leading directly to the **Itô correction** $\tfrac{1}{2}\sigma^2 f''(X)\,dt$ in Itô's lemma.
- In finance, non-zero quadratic variation means that **hedging is never perfect over discrete intervals** — the accumulated squared rebalancing errors scale with time, not with the square of time.
