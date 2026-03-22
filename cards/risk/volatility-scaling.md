# Volatility Scaling

**Topic:** Risk
**Level:** A Level Mathematics
**Tags:** volatility scaling, risk management, position sizing, inverse volatility, momentum crash
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

Volatility scaling (also called volatility targeting or inverse-volatility weighting) dynamically adjusts position sizes so that the portfolio maintains a constant level of risk over time. When realised or forecast volatility rises, exposure is reduced; when volatility falls, exposure is increased. The technique transforms a variable-risk return stream into an approximately constant-risk one, improving risk-adjusted returns and reducing the severity of drawdowns during high-volatility episodes.

## Key Formula

The **scaled position** at time $t$:

$$w_t = \frac{\sigma_{\text{target}}}{\hat{\sigma}_t} \times w_{\text{base}}$$

where $\sigma_{\text{target}}$ is the desired annualised volatility, $\hat{\sigma}_t$ is the current volatility estimate (e.g. from EWMA or realised volatility), and $w_{\text{base}}$ is the unscaled position.

The **volatility-scaled return**:

$$r_t^{\text{scaled}} = \frac{\sigma_{\text{target}}}{\hat{\sigma}_t} \times r_t$$

## Example

A momentum strategy has a target volatility of 10% annualised. During a calm period, realised volatility is 8%, so the scaling factor is:

$$w_t = \frac{10\%}{8\%} = 1.25$$

The fund levers up to 125% of base exposure. A month later, a market shock pushes realised volatility to 25%:

$$w_t = \frac{10\%}{25\%} = 0.40$$

Exposure drops to 40% of base. If the unscaled strategy would have lost 15% that month, the scaled loss is:

$$r_t^{\text{scaled}} = 0.40 \times (-15\%) = -6.0\%$$

Volatility scaling reduced the drawdown from 15% to 6%, precisely when losses are most dangerous.

## Remember

Volatility scaling is one of the most effective tools for managing tail risk in factor strategies, particularly momentum. Research by Barroso and Santa-Clara (2015) showed that volatility-scaled momentum nearly doubles the Sharpe ratio and eliminates the worst momentum crashes, because crashes occur precisely when volatility spikes — the same signal that triggers position reduction. The technique is now standard practice in quantitative asset management and is applied to individual factors, multi-factor portfolios, and risk-parity strategies. The key assumption is that high realised volatility predicts continued high volatility (volatility clustering), which is one of the most robust stylised facts in financial data.
