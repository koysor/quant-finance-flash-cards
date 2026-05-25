# Conditional Entropy

**Topic:** Probability
**Tags:** conditional entropy, information theory, entropy, information gain, uncertainty, decision tree
**Created:** 2026-05-25
**Author:** Claude Sonnet 4.6

---

## Definition

**Conditional entropy** $H(X \mid Y)$ measures the average remaining uncertainty about $X$ after observing $Y$. Observing $Y$ can only reduce (or leave unchanged) the uncertainty about $X$ — it can never increase it.

## Key Formula

$$H(X \mid Y) = -\sum_{x, y} p(x, y) \log p(x \mid y)$$

**Relation to joint entropy** (chain rule):

$$H(X, Y) = H(Y) + H(X \mid Y)$$

**Bounds:**

$$0 \leq H(X \mid Y) \leq H(X)$$

The lower bound $H(X \mid Y) = 0$ is achieved when $Y$ determines $X$ completely. The upper bound $H(X \mid Y) = H(X)$ is achieved when $X \perp Y$ — observing $Y$ tells us nothing about $X$.

**Information gain** is the reduction in conditional entropy:

$$IG(X, Y) = H(X) - H(X \mid Y) = I(X; Y)$$

## Example

Predicting tomorrow's return direction $X \in \{+1, -1\}$ from a momentum signal $Y \in \{0, 1\}$. Estimated from 500 trading days:

| | $X = +1$ | $X = -1$ |
|---|---|---|
| $Y = 0$ | 0.30 | 0.20 |
| $Y = 1$ | 0.15 | 0.35 |

$H(X \mid Y = 0) = -(0.60\log 0.60 + 0.40\log 0.40) \approx 0.971$ bits  
$H(X \mid Y = 1) = -(0.30\log 0.30 + 0.70\log 0.70) \approx 0.881$ bits  
$H(X \mid Y) = 0.50 \times 0.971 + 0.50 \times 0.881 \approx 0.926$ bits

The prior entropy is $H(X) = -(0.45 \log 0.45 + 0.55 \log 0.55) \approx 0.993$ bits. Information gain $= 0.993 - 0.926 = 0.067$ bits — the signal modestly reduces uncertainty.

## Remember

Conditional entropy is the quantity that decision tree algorithms minimise at each split: the splitting criterion "maximise information gain" is equivalent to "minimise $H(\text{label} \mid \text{feature split})$". In credit scoring, a split on "debt-to-income $> 0.4$" is chosen because it produces the largest drop in conditional entropy of the default label, concentrating defaulters and non-defaulters into purer child nodes. The chain rule $H(X,Y) = H(Y) + H(X \mid Y)$ is also the foundation for mutual information $I(X;Y) = H(X) - H(X \mid Y)$ and transfer entropy — conditional entropy is the fundamental building block of the entire information-theoretic toolkit.
