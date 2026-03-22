# Portfolio Manager

**Topic:** Portfolio Theory & Asset Pricing
**Level:** A Level Mathematics
**Tags:** portfolio manager, asset allocation, performance attribution, alpha, benchmark
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

A portfolio manager (PM) is the professional responsible for making investment decisions and managing a pool of assets on behalf of clients or a fund. In quantitative finance, the PM's role is framed mathematically: construct a portfolio that maximises risk-adjusted return relative to a benchmark, subject to constraints on risk, liquidity, and regulatory limits. Performance is judged not by raw returns but by alpha — the return unexplained by systematic factor exposures.

## Key Formula

The **information ratio** measures a PM's skill per unit of active risk:

$$\text{IR} = \frac{R_p - R_b}{\sigma(R_p - R_b)} = \frac{\alpha}{\omega}$$

where $R_p$ is the portfolio return, $R_b$ is the benchmark return, $\alpha = R_p - R_b$ is the active return, and $\omega$ is tracking error (the standard deviation of active returns).

The **fundamental law of active management** links skill, breadth, and performance:

$$\text{IR} \approx \text{IC} \times \sqrt{BR}$$

where $\text{IC}$ is the information coefficient (correlation between forecasts and outcomes) and $BR$ is breadth (number of independent bets per year).

## Example

A PM manages a £500 million equity fund benchmarked to the FTSE 100. Over the year:

- Portfolio return: 12.5%
- Benchmark return: 10.0%
- Tracking error: 4.0%

$$\text{IR} = \frac{12.5\% - 10.0\%}{4.0\%} = \frac{2.5\%}{4.0\%} = 0.625$$

An IR above 0.5 is considered good. If the PM makes 100 independent stock bets per year, the implied IC is:

$$\text{IC} = \frac{\text{IR}}{\sqrt{BR}} = \frac{0.625}{\sqrt{100}} = 0.0625$$

This means the PM's forecasts need only a 6.25% correlation with actual outcomes to achieve this performance — a small but consistent edge compounded across many bets.

## Remember

The fundamental law of active management reveals the two levers available to a portfolio manager: improve forecast accuracy (IC) or increase the number of independent bets (breadth). This is why quantitative portfolio managers tend to outperform discretionary ones over time — systematic strategies can scale breadth by trading hundreds of stocks across multiple signals, whereas a discretionary PM making 20 high-conviction bets needs much higher IC to achieve the same information ratio. The Carhart four-factor model is the standard tool for separating a PM's genuine alpha from mechanical factor exposures, ensuring that performance evaluation is fair and rigorous.
