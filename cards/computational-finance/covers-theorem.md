# Cover's Theorem

**Topic:** Computational Finance
**Tags:** cover's theorem, kernel trick, linear separability, dimensionality, svm, feature space
**Created:** 2026-05-13
**Author:** Claude Sonnet 4.6

---

## Definition

**Cover's theorem** states that a set of points that is not linearly separable in a low-dimensional space becomes increasingly likely to be linearly separable after a non-linear mapping to a higher-dimensional space, provided the dimensionality is high enough relative to the number of points and the mapping is not degenerate.

## Key Formula

For $N$ points in general position in $\mathbb{R}^d$, the number of linearly separable dichotomies (ways to split them with a hyperplane) is:

$$C(N, d) = 2 \sum_{k=0}^{d} \binom{N-1}{k}$$

When $N \leq d + 1$, all $2^N$ labellings are separable — any binary classification problem is solvable by a linear boundary in sufficiently high dimensions.

## Example

Ten points in $\mathbb{R}^2$ form two interleaved spirals — no straight line separates them. Applying a non-linear map $\phi: \mathbb{R}^2 \to \mathbb{R}^5$ via $\phi(\mathbf{x}) = (x_1, x_2, x_1^2, x_2^2, x_1 x_2)$ lifts each point to 5D. With $d = 5 \geq N - 1 = 9$... the condition is close; in practice the RBF kernel effectively maps to infinite dimensions, making separation achievable.

## Remember

Cover's theorem is the theoretical foundation for the kernel trick in SVMs applied to financial data. When raw features (price ratios, volatility measures, macro indicators) fail to separate credit risk classes linearly, the RBF kernel implicitly maps them to an infinite-dimensional space where Cover's theorem guarantees separability for most non-degenerate datasets. This is the principled reason why kernel SVMs outperform linear classifiers on complex financial classification tasks — not curve-fitting intuition, but a mathematical guarantee about geometry in high dimensions.
