# Risk Parity

**Topic:** Portfolio Theory & Asset Pricing
**Tags:** risk parity, portfolio construction, risk budgeting, diversification, leverage, equal risk contribution
**Author:** Claude Opus 4.6

---

## Definition

Risk parity is a portfolio construction approach that allocates capital so that each asset (or asset class) contributes equally to the total portfolio risk, rather than allocating equal capital or weighting by market capitalisation. Since bonds are less volatile than equities, risk parity typically overweights bonds and underweights equities relative to a traditional 60/40 portfolio, then uses leverage to achieve the desired return level.

## Key Formula

For an $n$-asset portfolio, the **risk contribution** of asset $i$ is:

$$\text{RC}_i = w_i \cdot \frac{(\Sigma \mathbf{w})_i}{\sigma_p}$$

where $\Sigma$ is the covariance matrix, $\mathbf{w}$ is the weight vector, and $\sigma_p = \sqrt{\mathbf{w}^\top \Sigma \mathbf{w}}$ is the portfolio volatility.

Risk parity requires each asset to contribute equally:

$$\text{RC}_i = \frac{\sigma_p}{n} \quad \text{for all } i$$

For a two-asset portfolio with zero correlation, this simplifies to:

$$\frac{w_1}{w_2} = \frac{\sigma_2}{\sigma_1}$$

## Example

A portfolio holds equities ($\sigma_E = 16\%$) and bonds ($\sigma_B = 4\%$), assumed uncorrelated. For equal risk contribution:

$$\frac{w_E}{w_B} = \frac{\sigma_B}{\sigma_E} = \frac{4}{16} = \frac{1}{4}$$

So $w_E = 20\%$ and $w_B = 80\%$. The portfolio volatility is:

$$\sigma_p = \sqrt{(0.20)^2 \times (0.16)^2 + (0.80)^2 \times (0.04)^2} = \sqrt{0.001024 + 0.001024} = \sqrt{0.002048} = 4.5\%$$

Each asset contributes $\frac{4.5\%}{2} = 2.25\%$ to total risk. To raise the expected return, the entire portfolio is levered — for instance, 2x leverage doubles both return and volatility to 9.0%.

## Remember

Risk parity challenges the conventional wisdom of the 60/40 portfolio by recognising that 60% equities contribute roughly 90% of total risk, making the portfolio far less diversified than it appears. Bridgewater's All Weather fund, one of the largest hedge funds in the world, popularised risk parity by demonstrating that equalising risk contributions across asset classes produces more stable returns across economic regimes. The approach relies heavily on accurate covariance estimation and on the availability of cheap leverage — when borrowing costs rise or correlations spike, the strategy's assumptions can break down.
