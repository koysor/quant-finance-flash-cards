# Relative Return

**Topic:** Financial Mathematics
**Tags:** relative return, benchmark, tracking error, active management, performance attribution
**Author:** Claude Opus 4.6

---

## Definition

Relative return is the difference between the return of a portfolio and the return of a benchmark index over the same period. It measures how much value an active manager has added (or lost) compared to a passive strategy. A positive relative return means the portfolio outperformed its benchmark; a negative one means it underperformed.

## Key Formula

$$R_{\text{rel}} = R_p - R_b$$

where $R_p$ is the portfolio return and $R_b$ is the benchmark return.

The volatility of relative return is called **tracking error**:

$$\text{TE} = \sigma(R_p - R_b)$$

The **information ratio** measures relative return per unit of tracking error:

$$\text{IR} = \frac{\bar{R}_{\text{rel}}}{\text{TE}} = \frac{\bar{R}_p - \bar{R}_b}{\sigma(R_p - R_b)}$$

## Example

A UK equity fund returns 11% over a year while the FTSE 100 returns 8%:

$$R_{\text{rel}} = 0.11 - 0.08 = 0.03$$

The fund outperformed by 3 percentage points. If the monthly tracking error is 1.5%, annualised tracking error is:

$$\text{TE}_{\text{annual}} = 0.015 \times \sqrt{12} = 0.052$$

$$\text{IR} = \frac{0.03}{0.052} = 0.58$$

An information ratio of 0.58 suggests the manager delivered meaningful outperformance relative to the risk taken against the benchmark.

## Remember

Relative return is the language of traditional asset management — pension funds and mutual funds judge their managers on whether they beat the index, not on whether they made money in absolute terms. A fund that loses 5% when the market loses 10% has a positive relative return of +5%, even though the investor lost money. This distinction between beating a benchmark and actually making money is why hedge funds and their investors often prefer absolute return targets instead.
