# Tactical Asset Allocation

**Topic:** Portfolio Theory & Asset Pricing
**Tags:** tactical allocation, active management, market timing, strategic allocation, information ratio, benchmark
**Created:** 2026-06-06
**Author:** Claude Sonnet 4.6

---

## Definition

Tactical asset allocation (TAA) is the short-term, active adjustment of portfolio weights away from the long-run **strategic asset allocation (SAA)** benchmark, based on near-term market views, valuation signals, or momentum. TAA adds value only when the timing signal persistently forecasts relative asset-class returns accurately enough to overcome transaction costs; empirical evidence shows most discretionary TAA destroys value after costs.

## Key Formula

If the benchmark (SAA) weight is $w^b$ and the active (TAA) weight is $w^a$, the **active tilt** is:

$$\delta w = w^a - w^b$$

The active return contribution from the tilt over period $T$ is:

$$\alpha_{\text{TAA}} = \delta w^\top (R_{\text{asset}} - R_{\text{benchmark}})$$

The **information ratio** evaluates whether tilts are consistently profitable:

$$\text{IR} = \frac{\mathbb{E}[\alpha_{\text{TAA}}]}{\text{std}(\alpha_{\text{TAA}})}$$

An IR above 0.5 sustained over 3+ years is considered evidence of genuine TAA skill.

## Example

A pension fund's SAA is 60% equities, 35% bonds, 5% cash. A macro analyst forecasts equities will outperform over the coming quarter and sets $w^a = $ 70% equities, 25% bonds, 5% cash. The equity tilt is $\delta w_{\text{eq}} = +10\%$.

If equities outperform bonds by 4% that quarter: active return $= 0.10 \times 4\% = 0.40\%$. If a round-trip rebalancing trade costs 0.10%, net alpha is 0.30%. Over 20 such calls with an IC (information coefficient) of 0.05, the expected active return is $0.05 \times 4\% \times \sqrt{20} \approx 0.89\%$ per year — a thin margin.

## Remember

The Fundamental Law of Active Management states that IR $\approx \text{IC} \times \sqrt{\text{Breadth}}$: a TAA manager making four asset-class calls per year (low breadth) needs an IC of 0.25 to achieve IR = 0.5 — a very high bar. This is why systematic, rules-based TAA — using persistent, documented signals such as CAPE valuation, trend-following momentum, or carry — has largely replaced discretionary TAA at sophisticated asset managers. Rules-based TAA is also more transparent, cheaper to run, and easier to attribute in ex-post performance analysis.
