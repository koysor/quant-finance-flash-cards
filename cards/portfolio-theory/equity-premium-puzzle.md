# Equity Premium Puzzle

**Topic:** Portfolio Theory & Asset Pricing
**Tags:** equity premium puzzle, risk aversion, consumption capm, excess return, mehra prescott, macrofinance
**Created:** 2026-06-15
**Author:** Claude Sonnet 4.6

---

## Definition

The **equity premium puzzle** (Mehra and Prescott, 1985) is the empirical observation that the historical excess return of equities over risk-free bonds — approximately 5–7% per year in the US — is far too large to be explained by the Consumption-Based CAPM with plausible levels of risk aversion. Reconciling the observed premium requires either extremely high risk aversion ($\gamma \approx 30$–$100$) or a richer model of investor preferences.

## Key Formula

Under CCAPM, the equity premium is approximately:

$$E[R_{\text{eq}}] - R_f \approx \gamma\,\sigma_c\,\sigma_{\text{eq}}\,\rho_{c,\text{eq}}$$

where $\sigma_c$ is consumption growth volatility, $\sigma_{\text{eq}}$ is equity return volatility, and $\rho_{c,\text{eq}}$ is their correlation.

**Empirical calibration** (US data, 1889–1978):

| Quantity | Empirical value |
|----------|----------------|
| $E[R_{\text{eq}}] - R_f$ | $\approx 6\%$ per year |
| $\sigma_c$ | $\approx 1\%$ per year |
| $\sigma_{\text{eq}}$ | $\approx 20\%$ per year |
| $\rho_{c,\text{eq}}$ | $\approx 0.40$ |

Implied $\gamma$ to match: $\gamma = 6\% / (1\% \times 20\% \times 0.40) \approx 75$.

## Example

An investor with $\gamma = 2$ (modest risk aversion) who optimally invests in equities expects to earn only $2 \times 0.01 \times 0.20 \times 0.40 = 0.16\%$ per year above the risk-free rate. Yet historically, equities have outperformed bills by $\approx 6\%$ per year — suggesting either the model is wrong, the data is anomalous, or investors are extraordinarily risk averse.

## Remember

The equity premium puzzle is not merely academic — it has direct consequences for pension fund design, infrastructure discount rates, and the equity risk premium used in DCF valuations. If the true long-run premium is 6% (as implied by history), then equities are a remarkable bargain at any plausible $\gamma$. If the true premium is 1–2% (as implied by CCAPM with $\gamma = 2$), then many pension funds are systematically overestimating equity returns. The resolution matters enormously for sovereign wealth fund allocations and national pension systems worldwide.
