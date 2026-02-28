# Itô's Lemma

**Topic:** Stochastic Processes
**Level:** A Level Mathematics
**Tags:** Itô's lemma, stochastic calculus, SDE, chain rule, Black-Scholes
**Created:** 2026-02-28
**Author:** Unknown

---

## Definition

**Itô's lemma** is the stochastic calculus analogue of the chain rule. Given a stochastic process $X_t$ and a twice-differentiable function $f(t, X_t)$, it tells us how $f$ evolves over time. The key departure from ordinary calculus is an extra second-order term that arises because $(dW_t)^2 = dt$.

## Key Formula

Suppose $X_t$ satisfies the SDE:

$$dX_t = \mu(t, X_t) \, dt + \sigma(t, X_t) \, dW_t$$

Then for $f(t, X_t)$ twice continuously differentiable:

$$df = \frac{\partial f}{\partial t} \, dt + \frac{\partial f}{\partial x} \, dX_t + \frac{1}{2} \frac{\partial^2 f}{\partial x^2} \, (dX_t)^2$$

Substituting $(dX_t)^2 = \sigma^2 \, dt$ (using $(dW_t)^2 = dt$, $dt \cdot dW_t = 0$, $(dt)^2 = 0$):

$$df = \left(\frac{\partial f}{\partial t} + \mu \frac{\partial f}{\partial x} + \frac{1}{2}\sigma^2 \frac{\partial^2 f}{\partial x^2}\right)dt + \sigma \frac{\partial f}{\partial x} \, dW_t$$

The extra $\frac{1}{2}\sigma^2 \frac{\partial^2 f}{\partial x^2}$ term is the **Itô correction** — it has no counterpart in ordinary calculus.

## Example

Derive the GBM solution: let $X_t = S_t$ with $dS_t = \mu S_t \, dt + \sigma S_t \, dW_t$, and set $f = \ln S_t$.

$$\frac{\partial f}{\partial t} = 0, \quad \frac{\partial f}{\partial S} = \frac{1}{S}, \quad \frac{\partial^2 f}{\partial S^2} = -\frac{1}{S^2}$$

$$d(\ln S_t) = \left(\mu - \frac{1}{2}\sigma^2\right)dt + \sigma \, dW_t$$

Integrating from $0$ to $T$:

$$\ln S_T = \ln S_0 + \left(\mu - \frac{\sigma^2}{2}\right)T + \sigma W_T$$

which gives the closed-form GBM solution $S_T = S_0 \exp\!\left(\left(\mu - \tfrac{\sigma^2}{2}\right)T + \sigma W_T\right)$.

## Remember

- The Itô correction is what produces the $-\tfrac{\sigma^2}{2}$ **volatility drag** term in GBM — higher volatility lowers the expected log return even when the drift $\mu$ is fixed.
- Itô's lemma is used directly to derive the **Black-Scholes PDE**: apply it to the option price $V(t, S_t)$, then construct a risk-free portfolio to eliminate the $dW_t$ term.
- In quantitative finance, every time you see a function of a stochastic process, Itô's lemma is the tool that lets you differentiate it.
