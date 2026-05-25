# Joint Entropy

**Topic:** Computational Finance
**Tags:** joint entropy, information theory, entropy, chain rule, dependence, multivariate
**Created:** 2026-05-25
**Author:** Claude Sonnet 4.6

---

## Definition

**Joint entropy** $H(X, Y)$ measures the total uncertainty in a pair of random variables simultaneously. It is always at least as large as either marginal entropy alone, and equals their sum only when $X$ and $Y$ are independent.

## Key Formula

$$H(X, Y) = -\sum_{x}\sum_{y} p(x, y)\log p(x, y)$$

**Chain rule** — decomposes joint into marginal plus conditional:

$$H(X, Y) = H(X) + H(Y \mid X) = H(Y) + H(X \mid Y)$$

**Bounds:**

$$\max\!\bigl(H(X),\, H(Y)\bigr) \leq H(X, Y) \leq H(X) + H(Y)$$

The upper bound is achieved when $X \perp Y$; the lower bound is approached when one variable almost determines the other.

## Example

Two binary market signals: momentum ($X$) and value ($Y$), each taking values $\{0, 1\}$ with $p(0,0) = 0.4$, $p(0,1) = 0.1$, $p(1,0) = 0.1$, $p(1,1) = 0.4$.

$$H(X, Y) = -2(0.4\log 0.4) - 2(0.1\log 0.1) \approx 1.722 \text{ bits}$$

Marginals: $H(X) = H(Y) = 1$ bit. Since $H(X, Y) < H(X) + H(Y) = 2$ bits, the signals share information — knowing one reduces uncertainty about the other by $2 - 1.722 = 0.278$ bits, which is the mutual information $I(X; Y)$.

## Remember

Joint entropy is the foundational quantity for multivariate information theory: mutual information $I(X; Y) = H(X) + H(Y) - H(X, Y)$, so every calculation of mutual information between two financial signals requires estimating their joint entropy. In portfolio construction, joint entropy also quantifies the total information content of a pair of factors — two highly correlated factors have joint entropy barely above either marginal, confirming they are near-redundant and that adding both adds little to a model's explanatory power. This makes joint entropy a principled criterion for detecting and pruning redundant features from factor models.
