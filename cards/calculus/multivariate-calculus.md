# Multivariate Calculus

**Topic:** Calculus
**Tags:** multivariate calculus, partial derivatives, total derivative, gradient, multi-asset pricing
**Created:** 2026-04-05
**Author:** Claude Sonnet 4.6

---

## Definition

**Multivariate calculus** is the extension of single-variable calculus to functions of two or more variables. A function $f(x_1, x_2, \ldots, x_n)$ assigns a single output to each combination of $n$ inputs. Rates of change are captured by **partial derivatives** (holding all but one variable fixed) and combined into the **total derivative**, which accounts for simultaneous changes in all inputs. The **gradient** $\nabla f$ collects all partial derivatives into a vector pointing in the direction of steepest increase.

## Key Formula

**Total derivative** — the change in $f$ due to small simultaneous changes in all variables:

$$df = \frac{\partial f}{\partial x_1} dx_1 + \frac{\partial f}{\partial x_2} dx_2 + \cdots + \frac{\partial f}{\partial x_n} dx_n = \sum_{i=1}^{n} \frac{\partial f}{\partial x_i} dx_i$$

**Gradient vector:**

$$\nabla f = \left(\frac{\partial f}{\partial x_1},\, \frac{\partial f}{\partial x_2},\, \ldots,\, \frac{\partial f}{\partial x_n}\right)$$

**Chain rule for a composed path** — if each $x_i = x_i(t)$:

$$\frac{df}{dt} = \sum_{i=1}^{n} \frac{\partial f}{\partial x_i} \frac{dx_i}{dt} = \nabla f \cdot \mathbf{x}'(t)$$

## Example

A two-asset option has value $V(S_1, S_2) = \max(S_1 + S_2 - 200, 0)$ near the money where $V \approx S_1 + S_2 - 200$. Then:

$$\frac{\partial V}{\partial S_1} = 1, \quad \frac{\partial V}{\partial S_2} = 1$$

If $S_1$ rises by $£2$ and $S_2$ falls by $£0.50$ simultaneously, the total change in value is:

$$dV \approx 1 \times 2 + 1 \times (-0.50) = £1.50$$

The total derivative combines both sensitivities in a single linear approximation.

## Remember

In multi-asset option pricing, a basket option depends on several correlated underlyings $S_1, S_2, \ldots, S_n$ simultaneously. The total derivative underpins Itô's lemma for multiple assets: applying the multivariate chain rule to a stochastic function $V(t, S_1, \ldots, S_n)$ produces cross-derivative terms $\frac{\partial^2 V}{\partial S_i \partial S_j}$ that capture correlation-driven risk. These mixed partials are zero for independent assets but non-zero when $\rho \neq 0$, so ignoring multivariate structure in a basket product leads to systematic mispricing.
