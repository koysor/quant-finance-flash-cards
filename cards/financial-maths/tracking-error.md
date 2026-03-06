# Tracking Error

**Topic:** Financial Mathematics
**Tags:** tracking error, benchmark, active risk, portfolio management, index tracking
**Author:** Claude Opus 4.6

---

## Definition

Tracking error is the standard deviation of the difference between a portfolio's returns and its benchmark's returns over time. It quantifies how closely a portfolio follows its benchmark — a low tracking error means the portfolio behaves like the index, while a high tracking error indicates significant active bets away from the benchmark.

## Key Formula

$$\text{TE} = \sigma(R_p - R_b) = \sqrt{\frac{1}{n-1} \sum_{t=1}^{n} \left[(R_{p,t} - R_{b,t}) - \overline{(R_p - R_b)}\right]^2}$$

where $R_{p,t}$ and $R_{b,t}$ are the portfolio and benchmark returns in period $t$.

To annualise monthly tracking error:

$$\text{TE}_{\text{annual}} = \text{TE}_{\text{monthly}} \times \sqrt{12}$$

## Example

Over 12 months, a fund's monthly excess returns over its benchmark are (in %): 0.3, $-0.1$, 0.5, 0.2, $-0.4$, 0.1, 0.6, $-0.2$, 0.3, 0.0, 0.4, $-0.1$.

The mean excess return is $\bar{d} = 0.133\%$. The monthly tracking error is:

$$\text{TE}_{\text{monthly}} = 0.30\%$$

$$\text{TE}_{\text{annual}} = 0.30\% \times \sqrt{12} = 1.04\%$$

An annualised tracking error of about 1% indicates a portfolio that stays very close to its benchmark — typical of an enhanced index fund.

## Remember

Tracking error sits at the heart of the active-versus-passive debate. Index funds target a tracking error near zero; enhanced index funds aim for 0.5–2%; active managers typically run 3–8%; and unconstrained hedge funds may have tracking errors exceeding 15%. Institutional mandates often specify a maximum tracking error as a hard constraint, forcing portfolio managers to balance their conviction in stock picks against the risk of deviating too far from the benchmark.
