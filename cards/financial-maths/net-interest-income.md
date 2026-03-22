# Net Interest Income

**Topic:** Financial Mathematics
**Tags:** NII, interest income, banking, net interest margin, ALM, IRRBB
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

**Net Interest Income (NII)** is the difference between the interest a bank earns on its assets (loans, mortgages, bonds) and the interest it pays on its liabilities (deposits, wholesale funding). It is the primary revenue source for most commercial banks and the earnings-based lens through which IRRBB is assessed. The related metric **Net Interest Margin (NIM)** expresses NII as a percentage of average earning assets.

## Key Formula

$$\text{NII} = \text{Interest income} - \text{Interest expense}$$

$$\text{NIM} = \frac{\text{NII}}{\text{Average earning assets}} \times 100\%$$

The sensitivity of NII to a parallel rate shift over a horizon $H$ is approximated by the **repricing gap**:

$$\Delta\text{NII} \approx \sum_{i=1}^{H} \text{Gap}_i \times \Delta r$$

where $\text{Gap}_i = \text{RSA}_i - \text{RSL}_i$ is rate-sensitive assets minus rate-sensitive liabilities repricing in period $i$.

## Example

A bank has £5bn of floating-rate loans repricing in 3 months and £3bn of deposits repricing in the same period. The remaining £2bn of assets are fixed for 5 years.

**3-month repricing gap** = £5bn − £3bn = **+£2bn**

If rates rise by 50 bps:

$$\Delta\text{NII} \approx 2\text{bn} \times 0.005 = +£10\text{m} \text{ (annualised)}$$

The bank benefits because more assets reprice higher than liabilities. If rates fell by 50 bps, NII would drop by £10m.

## Remember

NII is the short-to-medium-term earnings measure of IRRBB, typically assessed over a 1–2 year horizon. It complements EVE, which takes the long-run present-value view. A bank can have stable NII in the short term (because most cash flows are locked in) while facing a large EVE loss (because the discounted value of distant cash flows has changed). Treasury and ALM teams actively manage NII sensitivity by adjusting the repricing profile — for example, entering receive-fixed swaps converts floating-rate income into fixed, reducing NII volatility but increasing duration and EVE risk. Regulators require banks to report both NII and EVE sensitivities under the Basel IRRBB framework.
