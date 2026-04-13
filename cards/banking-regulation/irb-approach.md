# Internal Ratings-Based (IRB) Approach

**Topic:** Banking Regulation
**Tags:** irb, probability of default, risk-weighted assets, credit risk, capital requirement
**Created:** 2026-04-13
**Author:** Claude Sonnet 4.6

---

## Definition

The Internal Ratings-Based (IRB) approach allows banks to use their own statistical estimates of credit risk parameters — rather than regulator-prescribed weights — to compute Risk-Weighted Assets and hence capital requirements. Under Foundation IRB (F-IRB), banks supply only Probability of Default; under Advanced IRB (A-IRB), they supply PD, Loss Given Default, and Exposure at Default, all estimated from internal data and models approved by the regulator.

## Key Formula

The Basel IRB risk weight for a corporate exposure is:

$$RW = LGD \times \left[N\!\left(\frac{N^{-1}(PD) + \sqrt{\rho}\,N^{-1}(0.999)}{\sqrt{1-\rho}}\right) - PD\right] \times \frac{1 + (M - 2.5)b}{1 - 1.5b} \times 12.5$$

where $\rho = 0.12\left(\frac{1-e^{-50PD}}{1-e^{-50}}\right) + 0.24\left(1 - \frac{1-e^{-50PD}}{1-e^{-50}}\right)$ is the asset correlation, $M$ is effective maturity, and $b = (0.11852 - 0.05478\ln PD)^2$ is the maturity adjustment.

The result gives the capital charge per unit of EAD as a fraction, at the 99.9% confidence level.

## Example

A bank estimates $PD = 0.5\%$, $LGD = 45\%$, $M = 2.5$ years for a corporate loan. Using the formula above gives $\rho \approx 0.20$ and a risk weight of approximately **50%**, compared to 100% under the Standardised Approach. For a £10 m loan, IRB requires £10 m × 50% × 8% = **£400,000** capital vs £800,000 under Standardised — halving the capital requirement for a well-rated borrower.

## Remember

The IRB approval process — which typically takes 2–3 years and requires extensive model validation — is a competitive investment: banks with approved IRB models gain a persistent capital advantage over Standardised banks for high-quality loan books. However, Basel IV's output floor (72.5% of Standardised) caps this advantage, ensuring that IRB capital cannot fall below 72.5% of what the Standardised Approach would require — addressing the "RWA variability" criticism that arose when different banks' IRB models produced dramatically different capital for identical portfolios.
