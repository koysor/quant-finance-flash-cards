# Credit Default Swap

**Topic:** Financial Mathematics
**Tags:** credit default swap, cds, credit risk, recovery rate, credit spread, fixed income
**Created:** 2026-03-11
**Author:** claude-sonnet-4-6

---

## Definition

A **credit default swap (CDS)** is a bilateral derivative contract in which the protection buyer pays a periodic premium (the **CDS spread**) to the protection seller in exchange for a contingent payment if a specified reference entity defaults. It functions like insurance on a bond: the protection buyer transfers default risk to the seller without necessarily holding the underlying bond.

## Key Formula

The CDS spread $s$ is set so the present value of premium payments equals the present value of the expected contingent payment:

$$\underbrace{s \cdot \sum_{i=1}^{n} \Delta_i \cdot P(\text{survival to } t_i)}_{\text{premium leg (fee payments)}} = \underbrace{(1 - R) \cdot \int_0^T e^{-rt} \lambda e^{-\lambda t} \, dt}_{\text{protection leg (loss on default)}}$$

where $R$ is the **recovery rate** (fraction of notional recovered in default), $\lambda$ is the hazard rate (instantaneous default intensity), $r$ is the risk-free rate, and $\Delta_i$ is the day-count fraction for period $i$.

Under constant hazard rate and continuous compounding, the fair CDS spread simplifies to:

$$s \approx \lambda \cdot (1 - R)$$

This shows that the CDS spread equals the risk-neutral default intensity scaled by loss given default $(1 - R)$.

## Example

A 5-year CDS references a corporate bond. The market-implied hazard rate is $\lambda = 2\%$ per year, and the expected recovery rate is $R = 40\%$.

$$s \approx 0.02 \times (1 - 0.40) = 0.02 \times 0.60 = 0.012 = 120 \text{ basis points per year}$$

The protection buyer pays 120 bps annually on the notional (e.g. £120,000 per year on £10 million notional). If the issuer defaults, the seller pays £6 million (the loss given default: $(1 - 0.40) \times £10\text{m}$).

## Remember

The CDS spread is theoretically equal to the bond's credit spread adjusted for recovery rate — this is the **CDS-bond basis**. When this basis diverges from zero, arbitrageurs can buy the cheaper instrument and sell the dearer one (e.g. buy the bond and buy CDS protection if the bond spread exceeds the CDS spread). In practice, the basis can persist due to funding costs, counterparty risk, and the difficulty of shorting bonds. CDS are also used to extract market-implied default probabilities: given an observed CDS spread and an assumed recovery rate, traders can back out $\lambda$ and price other credit instruments consistently.
