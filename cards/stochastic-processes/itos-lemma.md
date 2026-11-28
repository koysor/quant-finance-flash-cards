# Itô's Lemma

**Topic:** Stochastic Processes
**Tags:** Itô's lemma, stochastic calculus, SDE, chain rule, Black-Scholes
**Created:** 2026-03-01 00:41:23
**Author:** Unknown

---

## Definition

**Itô's lemma** is the stochastic calculus analogue of the chain rule. Given a stochastic process $X_t$ and a twice-differentiable function $f(t, X_t)$, it tells us how $f$ evolves over time. The key departure from ordinary calculus is an extra second-order term that arises because $(dW_t)^2 = dt$.

**Notation $(t, X_t)$:** the two arguments of a function. $t$ is time, and $X_t$ is the value of the process at time $t$ (a single random number). $f(t, X_t)$ means: take an ordinary function $f(t, x)$ of two variables and substitute the random value $X_t$ for $x$, which makes $f(t, X_t)$ itself random. The partial derivatives refer to these two slots: $\frac{\partial f}{\partial t}$ is the change in $f$ as time moves with $x$ held fixed, and $\frac{\partial f}{\partial x}$, $\frac{\partial^2 f}{\partial x^2}$ are the changes as the process value moves with time held fixed. Likewise, $\mu(t, X_t)$ and $\sigma(t, X_t)$ say the drift and volatility may depend on time and on the current level of the process.

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
- Itô's lemma is used directly to derive the **Black-Scholes PDE**: apply it to the option price $V(t, S_t)$, then construct a risk-free portfolio to eliminate the $dW_t$ term. $V$ depends on both arguments (the stock price and time decay towards expiry), which is where the $\frac{\partial V}{\partial t}$ term comes from; $\ln S_t$ in the example above depends only on the second argument, so its $\frac{\partial f}{\partial t} = 0$.
- In quantitative finance, every time you see a function of a stochastic process, Itô's lemma is the tool that lets you differentiate it.
