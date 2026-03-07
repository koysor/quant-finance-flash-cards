# Counterparty Credit Risk

**Topic:** Risk
**Tags:** counterparty risk, credit risk, cva, exposure, default, netting
**Created:** 2026-03-07
**Author:** Claude Opus 4.6

---

## Definition

Counterparty credit risk (CCR) is the risk that the other party to an over-the-counter (OTC) financial contract defaults before the contract's final settlement, leaving the surviving party with a loss equal to the positive mark-to-market value of the contract at the time of default.

## Key Formula

The **credit valuation adjustment** (CVA) prices the expected loss from counterparty default:

$$\text{CVA} = \sum_{i=1}^{n} \text{LGD} \times \text{EE}(t_i) \times \text{PD}(t_{i-1}, t_i) \times \text{DF}(t_i)$$

where:
- $\text{LGD}$ is loss given default (typically $1 - \text{recovery rate}$)
- $\text{EE}(t_i)$ is expected exposure at time $t_i$
- $\text{PD}(t_{i-1}, t_i)$ is the probability of default in the interval
- $\text{DF}(t_i)$ is the discount factor

The **potential future exposure** (PFE) at confidence level $\alpha$:

$$\text{PFE}_\alpha(t) = F^{-1}_{\text{MTM}(t)}(\alpha)$$

where $F^{-1}$ is the inverse CDF of the mark-to-market distribution at time $t$.

## Example

A bank has a 5-year interest rate swap with a counterparty. The expected exposure profile peaks at £2 million in year 3. The counterparty has a 1% annual default probability and a 60% LGD.

Simplified CVA for year 3 alone:

$$\text{CVA}_3 = 0.60 \times £2{,}000{,}000 \times 0.01 \times 0.95 = £11{,}400$$

Summing across all years gives a total CVA of approximately £35,000. This is subtracted from the contract's risk-free value — a swap worth £500,000 on a risk-free basis is worth only £465,000 after CVA.

## Remember

Counterparty credit risk became a central concern after the collapse of Lehman Brothers in 2008, which imposed billions in losses on its OTC derivatives counterparties. CVA is now a mandatory capital charge under Basel III and is actively traded via CDS markets. For quantitative analysts, modelling CCR requires simulating the joint distribution of market risk factors and counterparty credit quality — a computationally intensive task because the exposure profile depends on the future path of interest rates, FX rates, and credit spreads. Netting agreements and collateral posting (via CSAs) dramatically reduce exposure, which is why collateral management and central clearing are now regulatory priorities.
