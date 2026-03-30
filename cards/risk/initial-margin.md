# Initial Margin

**Topic:** Risk
**Tags:** initial margin, SIMM, margin, counterparty risk, clearing, regulation
**Author:** Claude Opus 4.6

---

## Definition

Initial margin (IM) is the upfront collateral that a counterparty must post at trade inception to cover the estimated potential future exposure over the **margin period of risk** (MPOR). Unlike variation margin, which settles realised daily P&L, initial margin protects against losses that could accumulate between the last margin exchange and the close-out of a defaulting counterparty's positions. Since 2016, uncleared margin rules (UMR) require bilateral IM posting for non-centrally cleared derivatives, commonly calculated using the ISDA Standard Initial Margin Model (SIMM).

## Key Formula

The ISDA SIMM aggregates risk-factor sensitivities across asset classes. Within a single risk class, the IM contribution is:

$$\text{IM}_{\text{class}} = \sqrt{\sum_{k} \left(\sum_{i \in k} \text{WS}_i\right)^2 + \sum_{k \neq l} \gamma_{kl} \left(\sum_{i \in k} \text{WS}_i\right)\left(\sum_{j \in l} \text{WS}_j\right)}$$

where $\text{WS}_i = \text{RW}_i \times s_i$ is the weighted sensitivity (risk weight $\text{RW}_i$ multiplied by the net sensitivity $s_i$), $k$ and $l$ index buckets within the risk class, and $\gamma_{kl}$ is the prescribed cross-bucket correlation.

For centrally cleared derivatives, the CCP typically sets IM using a confidence interval:

$$\text{IM} \geq \text{ES}_{99\%}(h)$$

where $h$ is the MPOR (commonly 5 days for cleared OTC, 10 days for bilateral).

## Example

A bank holds a portfolio of interest rate swaps with sensitivities to the 5-year and 10-year GBP tenors. The SIMM risk weights are $\text{RW}_{5y} = 51\text{ bp}$ and $\text{RW}_{10y} = 51\text{ bp}$, and the intra-bucket correlation is $\rho = 0.98$.

Net sensitivities: $s_{5y} = £200{,}000$ per basis point and $s_{10y} = -£150{,}000$ per basis point.

Weighted sensitivities: $\text{WS}_{5y} = 51 \times 200{,}000 = £10.2\text{m}$ and $\text{WS}_{10y} = 51 \times (-150{,}000) = -£7.65\text{m}$.

$$\text{IM} = \sqrt{10.2^2 + (-7.65)^2 + 2 \times 0.98 \times 10.2 \times (-7.65)} = \sqrt{104.04 + 58.52 - 152.96} \approx £3.10\text{m}$$

The high correlation between tenors provides significant netting benefit, reducing IM from roughly £17.85m (standalone sum) to £3.10m.

## Remember

Initial margin is one of the largest hidden costs of derivatives trading and a critical input to any portfolio optimisation. The bilateral IM requirement under UMR has reshaped the OTC derivatives market: trades that were once uncollateralised now demand upfront funding, making the **margin valuation adjustment** (MVA) — the present value of expected future IM funding costs — a material component of derivatives pricing alongside CVA and FVA. For quantitative analysts, the sensitivity-based structure of SIMM means that IM can be reduced by constructing offsetting positions within the same netting set, turning margin optimisation into a constrained portfolio problem.
