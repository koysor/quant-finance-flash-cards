# Mixed Partial Derivatives

**Topic:** Calculus
**Tags:** mixed partials, second-order derivatives, clairaut, vanna, cross-gamma, options
**Created:** 2026-04-05
**Author:** Claude Sonnet 4.6

---

## Definition

A **mixed partial derivative** is a second-order partial derivative in which differentiation is performed with respect to two *different* variables in succession. For a function $f(x, y)$, the mixed partial $\frac{\partial^2 f}{\partial y \, \partial x}$ means: first differentiate with respect to $x$, then differentiate the result with respect to $y$.

**Clairaut's theorem** (symmetry of mixed partials): provided both mixed partials are continuous, the order of differentiation does not matter:

$$\frac{\partial^2 f}{\partial y \, \partial x} = \frac{\partial^2 f}{\partial x \, \partial y}$$

## Key Formula

For $f(x, y)$, the two mixed second-order partials are:

$$f_{xy} = \frac{\partial^2 f}{\partial y \, \partial x} = \frac{\partial}{\partial y}\!\left(\frac{\partial f}{\partial x}\right)$$

$$f_{yx} = \frac{\partial^2 f}{\partial x \, \partial y} = \frac{\partial}{\partial x}\!\left(\frac{\partial f}{\partial y}\right)$$

Clairaut's theorem states $f_{xy} = f_{yx}$ whenever both are continuous. The **Hessian matrix** collects all second-order partials:

$$H = \begin{pmatrix} f_{xx} & f_{xy} \\ f_{yx} & f_{yy} \end{pmatrix}$$

The off-diagonal entries are the mixed partials; by Clairaut's theorem $H$ is symmetric.

## Example

Let $f(S, \sigma) = S \cdot \sigma^2$, a toy model for option value growing with spot and variance.

**First-order partials:**

$$\frac{\partial f}{\partial S} = \sigma^2 \qquad \frac{\partial f}{\partial \sigma} = 2S\sigma$$

**Mixed partial** (differentiate $\partial f / \partial S$ with respect to $\sigma$):

$$\frac{\partial^2 f}{\partial \sigma \, \partial S} = \frac{\partial}{\partial \sigma}(\sigma^2) = 2\sigma$$

**Mixed partial** (differentiate $\partial f / \partial \sigma$ with respect to $S$):

$$\frac{\partial^2 f}{\partial S \, \partial \sigma} = \frac{\partial}{\partial S}(2S\sigma) = 2\sigma$$

Both mixed partials equal $2\sigma$, confirming Clairaut's theorem.

## Remember

In options trading, mixed partial derivatives appear as **cross-Greeks** that measure how one Greek changes as a *different* risk factor moves:

- **Vanna** $= \dfrac{\partial^2 V}{\partial S \, \partial \sigma} = \dfrac{\partial \Delta}{\partial \sigma} = \dfrac{\partial \mathcal{V}}{\partial S}$ — how delta changes as volatility shifts (and equivalently, how vega changes as spot moves). A positive vanna means delta rises when vol rises, so a delta-neutral book becomes long delta in a vol spike.
- **Volga** (vomma) $= \dfrac{\partial^2 V}{\partial \sigma^2}$ — the pure second-order vol sensitivity (not a mixed partial, but closely related).
- **Charm** $= \dfrac{\partial^2 V}{\partial S \, \partial t}$ — how delta decays with time.

Clairaut's theorem guarantees that $\partial \Delta / \partial \sigma = \partial \mathcal{V} / \partial S$, so a vol surface trader can compute vanna either way. Cross-Greeks matter most for hedging barrier options and exotic products, where large spot moves and vol moves interact and can cause unexpected P&L.
