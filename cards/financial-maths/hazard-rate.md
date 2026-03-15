# Hazard Rate

**Topic:** Financial Mathematics
**Tags:** hazard rate, credit risk, default probability, survival probability, cds, credit spread
**Created:** 2026-03-11
**Author:** claude-sonnet-4-6

---

## Definition

The **hazard rate** (also called the **default intensity**) $\lambda(t)$ is the instantaneous conditional probability of default per unit time, given that the entity has survived to time $t$. It answers the question: if a borrower has not yet defaulted, at what rate are they likely to default right now?

## Key Formula

The survival probability — the probability that default has not occurred by time $T$ — is:

$$P(\tau > T) = e^{-\int_0^T \lambda(t) \, dt}$$

Under a **constant** hazard rate $\lambda$, this simplifies to:

$$P(\tau > T) = e^{-\lambda T}$$

The probability of defaulting within $[t, t + dt]$ given survival to $t$ is $\lambda \, dt$. The fair CDS spread then approximates to:

$$s \approx \lambda (1 - R)$$

where $R$ is the recovery rate (fraction of notional recovered on default) and $(1 - R)$ is the **loss given default**.

## Example

A corporate bond issuer has a constant hazard rate of $\lambda = 0.03$ per year and an expected recovery rate of $R = 40\%$.

**Survival probability over 3 years:**

$$P(\tau > 3) = e^{-0.03 \times 3} = e^{-0.09} \approx 0.914$$

There is roughly a 91.4% chance the issuer survives 3 years.

**Implied CDS spread:**

$$s \approx 0.03 \times (1 - 0.40) = 0.03 \times 0.60 = 0.018 = 180 \text{ basis points per year}$$

A protection buyer would pay 180 bps annually on the notional.

## Remember

Given an observed CDS spread $s$ and an assumed recovery rate $R$, traders **back out** the market-implied hazard rate as $\lambda \approx s / (1 - R)$. This is used to price other credit instruments — such as credit-linked notes or basket CDS — consistently with the market. The hazard rate is the credit analogue of the risk-free rate: just as $e^{-rT}$ discounts cash flows for time, $e^{-\lambda T}$ discounts them for credit risk.
