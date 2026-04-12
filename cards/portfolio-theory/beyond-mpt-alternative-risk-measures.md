# Beyond MPT — Alternative Risk Measures

**Topic:** Portfolio Theory & Asset Pricing
**Tags:** risk measures, var, cvar, skewness, kurtosis, fat tails
**Created:** 2026-04-12
**Author:** Claude Sonnet 4.6

---

## Definition

Modern Portfolio Theory (MPT) assumes investors care only about the mean and variance of returns, which is only sufficient when returns are normally distributed. In reality, equity and option returns exhibit **skewness** (asymmetry) and **excess kurtosis** (fat tails), so variance alone understates true risk.

The four moments of a return distribution:

| Moment | Measure | Role |
|--------|---------|------|
| 1st | Mean $\mu$ | Central tendency |
| 2nd | Variance $\sigma^2$ | Spread (MPT stops here) |
| 3rd | Skewness | Asymmetry of the distribution |
| 4th | Kurtosis | Weight of the tails |

Three alternative risk measures that go beyond variance:

- **Value at Risk (VaR):** the minimum loss exceeded with probability $1-\alpha$
- **Conditional Value at Risk (CVaR) / Expected Shortfall:** the expected loss *given* that the loss exceeds VaR
- **Shortfall probability:** the probability that portfolio return falls below a target level $R_L$

## Key Formula

**VaR at confidence level $\alpha$:**

$$\text{VaR}_\alpha = \inf\{ l : P(\text{Loss} > l) \leq 1 - \alpha \}$$

**CVaR at confidence level $\alpha$:**

$$\text{CVaR}_\alpha = \mathbb{E}[\text{Loss} \mid \text{Loss} > \text{VaR}_\alpha]$$

**Shortfall probability:**

$$P(R_\Pi < R_L)$$

where $R_\Pi$ is the portfolio return and $R_L$ is the minimum acceptable (liability) return.

CVaR is a **coherent risk measure** (satisfies sub-additivity, monotonicity, homogeneity, and translation invariance); VaR is not, because it ignores the severity of losses beyond the threshold.

## Example

Suppose a portfolio has daily returns roughly normally distributed with mean 0 and standard deviation 1%. At $\alpha = 99\%$:

- $\text{VaR}_{99\%} \approx 2.33\%$ — the portfolio loses more than this on only 1% of days
- $\text{CVaR}_{99\%} \approx 2.67\%$ — on those worst 1% of days, the average loss is 2.67%

For a fat-tailed (leptokurtic) distribution the gap between VaR and CVaR widens significantly, revealing the extra tail risk that variance-based MPT hides entirely.

## Remember

In the 2008 financial crisis, many banks held portfolios with "acceptable" VaR figures yet suffered catastrophic losses — because VaR said nothing about what happened *beyond* its threshold. CVaR averages over those tail events, making it the preferred measure for regulators (Basel/FRTB replaced VaR with Expected Shortfall for the trading book) and for portfolio managers who need to price the real cost of a bad day.
