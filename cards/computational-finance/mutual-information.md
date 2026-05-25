# Mutual Information

**Topic:** Computational Finance
**Tags:** mutual information, information theory, dependence, feature selection, entropy, correlation
**Created:** 2026-05-25
**Author:** Claude Sonnet 4.6

---

## Definition

**Mutual information** $I(X; Y)$ measures the reduction in uncertainty about one random variable given knowledge of another. Unlike Pearson correlation, it captures any statistical dependence — linear or non-linear — and equals zero if and only if $X$ and $Y$ are independent.

## Key Formula

$$I(X; Y) = H(X) + H(Y) - H(X, Y)$$

Equivalently, as a KL divergence between the joint and the product of marginals:

$$I(X; Y) = D_{\text{KL}}\!\left(p(x, y) \;\|\; p(x)\,p(y)\right) = \sum_{x, y} p(x, y) \log \frac{p(x, y)}{p(x)\,p(y)}$$

**Key properties:**
- $I(X; Y) \geq 0$, with equality iff $X \perp Y$
- $I(X; Y) = I(Y; X)$ (symmetric)
- $I(X; Y) = H(X) - H(X \mid Y)$: the information $Y$ carries about $X$

## Example

Two binary signals: yesterday's return sign $X$ and today's return sign $Y$. Estimated from 1,000 trading days:

| | $Y = +1$ | $Y = -1$ |
|---|---|---|
| $X = +1$ | 0.35 | 0.15 |
| $X = -1$ | 0.20 | 0.30 |

$H(X) = H(Y) \approx 0.971$ bits, $H(X, Y) \approx 1.886$ bits.

$$I(X; Y) = 0.971 + 0.971 - 1.886 \approx 0.056 \text{ bits}$$

A small but non-zero MI confirms the signals are not independent, even if their Pearson correlation might be weak.

## Remember

Mutual information is the information-theoretic alternative to correlation for measuring feature relevance in factor models. Pearson correlation only detects linear dependence and collapses to zero for non-linear relationships (e.g. $Y = X^2$); MI detects any statistical dependence. In practice, `sklearn.feature_selection.mutual_info_classif` estimates $I(X; Y)$ using a $k$-NN density estimator and is used to rank potential predictors for credit scoring or default probability models before fitting. A feature with $I(X; Y) = 0$ carries no information about the target and can be discarded without loss; a feature with high MI is worth including even if uncorrelated with the label.
