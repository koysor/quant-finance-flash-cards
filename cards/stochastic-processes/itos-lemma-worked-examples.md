# Itô's Lemma Worked Examples

**Topic:** Stochastic Processes
**Tags:** Itô's lemma, stochastic calculus, worked examples, Brownian motion
**Author:** Claude Opus 4.6

---

## Definition

Applying **Itô's lemma** to a function $f(W_t)$ of Brownian motion follows a mechanical recipe: compute $f'$ and $f''$, plug into the formula, and replace $dW^2$ with $dt$. The key departure from ordinary calculus is that the second derivative always produces an extra deterministic drift term.

**The recipe** for $f(W_t)$ (no explicit time dependence):

$$df = f'(W_t)\,dW_t + \frac{1}{2}f''(W_t)\,dt$$

## Key Formula

**Power functions:** $f(W_t) = W_t^n$

$$dW_t^n = nW_t^{n-1}\,dW_t + \frac{1}{2}n(n-1)W_t^{n-2}\,dt$$

**Exponential:** $f(W_t) = e^{W_t}$

$$de^{W_t} = e^{W_t}\,dW_t + \frac{1}{2}e^{W_t}\,dt \qquad \Longleftrightarrow \qquad \frac{de^{W_t}}{e^{W_t}} = dW_t + \frac{1}{2}\,dt$$

**Logarithm:** $f(W_t) = \ln W_t$ (for $W_t > 0$)

$$d\ln W_t = \frac{1}{W_t}\,dW_t - \frac{1}{2W_t^2}\,dt$$

**General exponential:** $f(W_t) = a^{W_t}$ (constant $a > 0$)

$$\frac{da^{W_t}}{a^{W_t}} = (\ln a)\,dW_t + \frac{1}{2}(\ln a)^2\,dt$$

## Example

Apply Itô's lemma to $f(W_t) = \sin W_t + \cos W_t$:

$$f' = \cos W_t - \sin W_t, \qquad f'' = -\sin W_t - \cos W_t = -f$$

$$df = (\cos W_t - \sin W_t)\,dW_t - \frac{1}{2}(\sin W_t + \cos W_t)\,dt$$

The Itô correction $-\frac{1}{2}f\,dt$ acts as a **damping drift** — the curvature of sinusoidal functions causes the process to drift downward on average, even though the underlying Brownian motion has no drift.

## Remember

- The exponential example is the origin of the **$-\frac{1}{2}\sigma^2$ correction** that appears throughout finance. When $f = e^{W_t}$, the Itô correction adds $+\frac{1}{2}\,dt$ drift; applying this to GBM's $\ln S$ gives the compensating $-\frac{1}{2}\sigma^2$ in the log return.
- Every worked example follows the same three steps: differentiate twice, substitute into the formula, simplify. There is no guesswork — Itô's lemma is purely mechanical.
- The sign and magnitude of the Itô correction depend on $f''$ — convex functions ($f'' > 0$) gain upward drift, concave functions ($f'' < 0$) gain downward drift. This is **Jensen's inequality in continuous time**.
