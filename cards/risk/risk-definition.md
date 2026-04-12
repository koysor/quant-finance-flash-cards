# Risk Definition and Goals of Risk Measurement

**Topic:** Risk
**Tags:** risk, uncertainty, downside risk, economic capital, risk management, regulatory capital
**Created:** 2026-04-12
**Author:** Claude Sonnet 4.6

---

## Definition

**Financial risk** is the possibility that the actual outcome of an investment or position deviates from the expected outcome in a way that results in loss. Risk measurement translates this possibility into a quantitative figure — a number of pounds, a probability, or a capital charge — so that it can be compared, aggregated, limited, and priced.

The key distinction: **risk as uncertainty** (any deviation, up or down) versus **risk as downside** (only adverse deviations). VaR and Expected Shortfall measure downside risk; variance and standard deviation measure symmetric uncertainty.

## Key Formula

Three goals of risk measurement, each associated with a specific metric:

| Goal | Metric | Formula |
|---|---|---|
| **Regulatory compliance** | VaR at 99% (Basel) or ES at 97.5% (FRTB) | $\text{VaR}_\alpha = F^{-1}(1-\alpha)$ |
| **Economic capital allocation** | Expected Shortfall | $\text{ES}_\alpha = \mathbb{E}[L \mid L > \text{VaR}_\alpha]$ |
| **Capital preservation** | Maximum drawdown | $\text{MDD} = \max_{t \leq T}\bigl(W_{\text{peak}} - W_t\bigr)$ |

where $F^{-1}$ is the quantile function of the loss distribution, $\alpha$ is the confidence level, and $W_t$ is portfolio wealth at time $t$.

## Example

A trading desk runs three risk metrics simultaneously:

- **VaR (99%, 1-day) = £2 m** — the regulatory metric. On 99 out of 100 days, losses will be below £2 m. Required by Basel III to size the market risk capital charge.
- **ES (97.5%, 1-day) = £3.5 m** — the FRTB metric. On the 2.5% of worst days, the average loss is £3.5 m. Used to allocate economic capital across desks.
- **Maximum drawdown = £8 m** — the capital preservation metric. The largest peak-to-trough loss recorded in the last year. Used by risk committees to set hard limits on sustained losses.

All three measure risk, but each answers a different question about the same loss distribution.

## Remember

Risk measurement exists to serve three masters: **regulators** (who set the methodology and confidence level, e.g. FRTB mandates 97.5% ES), **shareholders** (who want economic capital allocated efficiently so return on equity is maximised), and **management** (who need limits that prevent a single desk from threatening the whole firm). A model that satisfies one master — a low reported VaR — may fail the others if it understates tail losses. This tension between reported risk and true risk is what the London Whale episode (2012) exposed: switching to a lower-VaR model met the regulatory metric whilst obscuring economic reality.
