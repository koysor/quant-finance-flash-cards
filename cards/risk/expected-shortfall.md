# Expected Shortfall

**Topic:** Risk
**Tags:** risk, expected shortfall, CVaR, tail risk, coherent risk measure, FRTB
**Author:** Claude Sonnet 4.6

---

## Definition

**Expected Shortfall (ES)**, also called **Conditional Value at Risk (CVaR)**, is the average loss in the worst $(1 - \alpha)$% of scenarios — the expected value of losses that exceed the VaR threshold at confidence level $\alpha$.

Unlike VaR, which only marks a quantile, ES quantifies *how bad* the tail losses are on average, making it a **coherent risk measure** that satisfies the subadditivity axiom.

## Key Formula

For a loss random variable $L$ with confidence level $\alpha$:

$$\text{ES}_\alpha = \frac{1}{1 - \alpha} \int_\alpha^1 \text{VaR}_u(L) \, du$$

Equivalently, using conditional expectation:

$$\text{ES}_\alpha = \mathbb{E}[L \mid L > \text{VaR}_\alpha(L)]$$

For a **normally distributed** portfolio with mean $\mu$ and standard deviation $\sigma$:

$$\text{ES}_\alpha = \mu + \sigma \cdot \frac{\phi(z_\alpha)}{1 - \alpha}$$

where $z_\alpha$ is the $\alpha$-quantile of the standard normal and $\phi$ is the standard normal PDF.

## Example

A portfolio has daily mean $\mu = 0$ and daily standard deviation $\sigma = £100{,}000$.

**1-day 97.5% ES** (the FRTB standard):

$$z_{0.975} = 1.960, \quad \phi(1.960) = 0.0584$$

$$\text{ES}_{0.975} = 0 + 100{,}000 \times \frac{0.0584}{0.025} = £233{,}600$$

Compare: 97.5% VaR $= 1.960 \times £100{,}000 = £196{,}000$.

ES is larger than VaR by design — it averages all losses beyond the VaR threshold, not just the threshold itself.

## Remember

The Basel III **Fundamental Review of the Trading Book (FRTB)** replaced 99% VaR with **97.5% ES** as the headline capital measure for internal model approaches. The switch was motivated by ES being a coherent risk measure (it satisfies subadditivity) and by its ability to capture tail severity, not just tail probability. A desk that passes the VaR backtest can still hold inadequate capital if its tail losses are catastrophic — ES corrects for exactly this gap.
