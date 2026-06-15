# Default Probability

**Topic:** Risk
**Tags:** default probability, probability of default, credit risk, hazard rate, risk-neutral, pd
**Created:** 2026-06-15
**Author:** Claude Sonnet 4.6

---

## Definition

The **probability of default** (PD) is the likelihood that a borrower fails to make a contractual payment over a given horizon. It appears in two forms: the **physical (historical) PD**, estimated from rating agency data on observed defaults, and the **risk-neutral PD**, implied from market credit spreads and higher due to an embedded credit risk premium.

## Key Formula

**From credit spreads** (risk-neutral, continuously compounded):

$$\text{PD}(T) = 1 - e^{-\lambda T} \approx \lambda T \quad \text{for small } \lambda T$$

where the hazard rate $\lambda \approx s / (1-R)$, $s$ is the credit spread, and $R$ is the recovery rate.

**From the Merton model** (physical, structural):

$$\text{PD}(T) = N\!\left(-\frac{\ln(V_0/D) + (\mu - \tfrac{1}{2}\sigma_V^2)T}{\sigma_V\sqrt{T}}\right)$$

where $V_0$ is firm value, $D$ is the debt face value, $\mu$ is the expected firm return, and $\sigma_V$ is firm-value volatility.

## Example

A 5-year BBB bond trades at a credit spread of 150 bp with assumed recovery $R = 40\%$.

**Risk-neutral hazard rate:** $\lambda = 0.015 / 0.60 = 2.5\%$ per year.

**Risk-neutral PD over 5 years:** $1 - e^{-0.025 \times 5} = 1 - e^{-0.125} \approx 11.8\%$

**Historical PD for BBB (S&P data):** roughly 0.20% per year $\Rightarrow$ 5-year PD $\approx 1.0\%$.

The tenfold gap between risk-neutral (11.8%) and historical (1.0%) default probability is the **credit risk premium** — compensation for bearing systematic credit risk.

## Remember

The gap between risk-neutral and physical default probabilities is not a model artefact: it is the credit risk premium, and it is systematically large. During calm markets, investment-grade credit spreads imply far more defaults than historically occur — which is why selling credit protection (writing CDS) has been persistently profitable on average. The gap widens dramatically in crises: in 2009, implied BBB default rates exceeded 20%, dwarfing historical experience, because investors demanded an enormous premium to bear credit risk at that moment.
