# Softmax Function

**Topic:** Computational Finance
**Tags:** softmax, multiclass classification, probability, logistic regression, neural networks, cross-entropy
**Created:** 2026-05-13
**Author:** Claude Sonnet 4.6

---

## Definition

The **softmax function** is a generalisation of the sigmoid function to $K > 2$ classes. It converts a vector of real-valued scores $\mathbf{s} \in \mathbb{R}^K$ (one per class) into a valid probability distribution — non-negative values that sum to 1 — making it the standard output layer for multiclass classification.

## Key Formula

For class $k$ given score vector $\mathbf{s} = (s_1, \ldots, s_K)$:

$$\hat{p}_k = \frac{e^{s_k}}{\displaystyle\sum_{j=1}^{K} e^{s_j}}, \qquad \sum_{k=1}^{K} \hat{p}_k = 1$$

The predicted class is $\hat{y} = \arg\max_k \hat{p}_k$.

Trained by minimising **categorical cross-entropy**:

$$\mathcal{L} = -\sum_{k=1}^{K} y_k \ln \hat{p}_k$$

where $\mathbf{y}$ is a one-hot encoded true label. When $K=2$, softmax reduces exactly to the sigmoid function.

## Example

A regime classification model scores three states — bull ($s_1 = 2.1$), bear ($s_2 = 0.8$), crisis ($s_3 = -0.5$). Softmax: $e^{2.1} \approx 8.17$, $e^{0.8} \approx 2.23$, $e^{-0.5} \approx 0.61$; sum $\approx 11.01$. Probabilities: bull 74%, bear 20%, crisis 6%. The model allocates risk capital proportional to the probability of each regime rather than committing to a single state.

## Remember

Softmax is the output layer for every multiclass financial classifier: market regime models (bull/bear/crisis), credit rating migration models (AAA → B), and sector rotation classifiers. Its outputs are probabilities, so they can be used directly in expected value calculations — weight returns by the probability of each regime, or model rating transition matrices for credit portfolio stress testing. The categorical cross-entropy loss it is trained with is the multiclass extension of log-loss, ensuring the model is penalised in proportion to its overconfidence in the wrong class.
