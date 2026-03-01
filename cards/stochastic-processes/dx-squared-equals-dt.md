# The Rule dX Squared Equals dt

**Topic:** Stochastic Processes
**Tags:** stochastic calculus, quadratic variation, Itô's lemma, dW squared
**Author:** Claude Opus 4.6

---

## Definition

The rule $dW^2 = dt$ (equivalently $dX^2 = dt$) is the single most important identity in stochastic calculus. It states that the square of a Brownian increment is **deterministic** — equal to the time step exactly. This is a direct consequence of quadratic variation and is the reason Taylor expansions of stochastic processes retain their second-order terms.

Combined with two companion rules, it forms the complete **multiplication table** for stochastic calculus:

$$dW^2 = dt, \qquad dt \cdot dW = 0, \qquad (dt)^2 = 0$$

## Key Formula

**The rule:**

$$dW^2 = dt$$

**Why it holds:** the sum of squared Brownian increments converges to elapsed time:

$$\sum_{j=1}^{n} (\Delta W_j)^2 \xrightarrow{n \to \infty} t$$

**Contrast with ordinary calculus:**

$$dx^2 = 0 \quad \text{(smooth functions)} \qquad \text{vs} \qquad dW^2 = dt \quad \text{(Brownian motion)}$$

**Application in Itô's lemma** — for $F(W_t)$, the Taylor expansion is:

$$dF = F'(W_t)\,dW + \frac{1}{2}F''(W_t)\,dW^2 + \cdots = F'(W_t)\,dW + \frac{1}{2}F''(W_t)\,dt$$

The second-order term survives because $dW^2 = dt$, not zero.

## Example

Apply the rule to $F(W_t) = W_t^2$:

$$dF = 2W_t \, dW + \frac{1}{2}(2)\,dW^2 = 2W_t \, dW + dt$$

In ordinary calculus, $d(x^2) = 2x\,dx$. In stochastic calculus, there is an extra $+dt$ — a deterministic drift created purely by the curvature of $W_t^2$ interacting with the non-zero quadratic variation.

Integrating: $W_t^2 = 2\int_0^t W_s \, dW_s + t$, which rearranges to the well-known identity $\int_0^t W_s\,dW_s = \tfrac{1}{2}(W_t^2 - t)$.

## Remember

- This rule is the **bridge between Taylor series and Itô's lemma**. Whenever you see $dW^2$ in an expansion, replace it with $dt$ and discard all higher-order terms.
- The rule explains **volatility drag**: applying Itô's lemma to $\ln S$ under GBM produces the $-\tfrac{1}{2}\sigma^2$ correction that separates the arithmetic mean return $\mu$ from the geometric mean return $\mu - \tfrac{1}{2}\sigma^2$.
- In ordinary calculus, smoothness means $dx^2 \to 0$; in stochastic calculus, path roughness means $dW^2 \to dt$. This single distinction is what necessitates an entirely different calculus for random processes.
