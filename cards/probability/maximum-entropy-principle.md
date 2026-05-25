# Maximum Entropy Principle

**Topic:** Probability
**Tags:** maximum entropy, jaynes, prior distribution, inference, information theory, entropy
**Created:** 2026-05-25
**Author:** Claude Sonnet 4.6

---

## Definition

The **maximum entropy principle** (Jaynes, 1957) states that, when selecting a probability distribution consistent with known constraints, one should choose the distribution with the highest Shannon entropy. This is the least informative — and therefore least assumptive — choice consistent with the available evidence.

## Key Formula

Maximise entropy subject to constraints:

$$\max_p \; H(p) = -\sum_k p_k \log p_k$$

$$\text{subject to:} \quad \sum_k p_k = 1, \quad \sum_k p_k f_j(k) = \mu_j \; \text{ for } j = 1, \ldots, m$$

The solution has the **Gibbs (exponential family) form**:

$$p_k^* = \frac{1}{Z}\exp\!\left(-\sum_j \lambda_j f_j(k)\right)$$

where $\lambda_j$ are Lagrange multipliers for each constraint and $Z = \sum_k \exp(-\sum_j \lambda_j f_j(k))$ is the normalising constant. Common special cases:

| Constraints | Maximum entropy distribution |
|---|---|
| None (just normalisation) | Uniform |
| Known mean $\mu$ (on $[0,\infty)$) | Exponential with rate $1/\mu$ |
| Known mean $\mu$ and variance $\sigma^2$ | Normal $\mathcal{N}(\mu, \sigma^2)$ |

## Example

An analyst knows only that daily log-returns have mean 0 and variance $\sigma^2 = (0.01)^2$. The maximum entropy principle selects the normal distribution $\mathcal{N}(0, 0.0001)$ — not because returns are guaranteed to be normal, but because this is the least assumptive distribution consistent with those two moments. Any other distribution with the same mean and variance encodes additional structural assumptions not supported by the data.

## Remember

The maximum entropy principle is the information-theoretic justification for using the normal distribution in finance when only the first two moments are known, and for using the exponential distribution for inter-arrival times of trades. In derivatives pricing, it underlies entropy-based methods for extracting risk-neutral distributions from option prices: the maximum entropy distribution consistent with observed market option prices (which fix certain moments of the risk-neutral measure) is taken as the implied distribution — this avoids choosing an arbitrary parametric model for the smile. It is also the foundation of maximum entropy portfolios: weights are treated as a discrete probability distribution and entropy is maximised subject to a budget constraint, producing the most diversified allocation expressible without return forecasts.
