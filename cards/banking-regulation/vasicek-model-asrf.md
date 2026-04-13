# Vasicek Model (ASRF)

**Topic:** Banking Regulation
**Tags:** vasicek, asrf, credit portfolio, irb approach, asset correlation
**Created:** 2026-04-13
**Author:** Claude Sonnet 4.6

---

## Definition

The Asymptotic Single Risk Factor (ASRF) model, attributed to Vasicek (2002), is the mathematical foundation of the Basel IRB credit risk capital formula. It models each borrower's asset return as driven by a single common economic factor and an idiosyncratic shock; in a large, granular portfolio the idiosyncratic risk diversifies away completely, leaving only systematic risk — which determines capital requirements.

## Key Formula

Each borrower's normalised asset return is:

$$A_i = \sqrt{\rho}\, X + \sqrt{1 - \rho}\, Z_i, \qquad X, Z_i \overset{\text{i.i.d.}}{\sim} \mathcal{N}(0,1)$$

where $X$ is the single common factor (the economy), $Z_i$ is idiosyncratic, and $\rho$ is asset correlation.

Conditional on a worst-case economic scenario $X = \Phi^{-1}(0.001)$ (the 0.1th percentile), the conditional default rate at the 99.9% confidence level is:

$$\text{CDR}_{99.9\%} = \Phi\!\left(\frac{\Phi^{-1}(PD) - \sqrt{\rho}\,\Phi^{-1}(0.001)}{\sqrt{1-\rho}}\right)$$

Capital $= (CDR_{99.9\%} - PD) \times LGD \times EAD$ (unexpected loss at 99.9%).

## Example

A corporate loan: $PD = 1\%$, $LGD = 45\%$, $\rho = 0.20$ (Basel corporate correlation).

$$CDR_{99.9\%} = \Phi\!\left(\frac{\Phi^{-1}(0.01) - \sqrt{0.20}\,\Phi^{-1}(0.001)}{\sqrt{0.80}}\right) = \Phi\!\left(\frac{-2.326 - 0.447 \times (-3.090)}{0.894}\right) \approx \Phi(0.651) \approx 7.42\%$$

Capital charge $= (7.42\% - 1\%) \times 45\% \times EAD \approx 2.89\% \times EAD$.

## Remember

The ASRF model embeds a crucial regularity result: in a perfectly granular portfolio, the only capital-relevant risk is systematic (correlated with the economy). This is why the Basel formula uses a fixed asset correlation parameter $\rho$ — calibrated by asset class — rather than an estimated portfolio correlation matrix. Quants implementing IRB systems must understand that $\rho$ is the lever driving capital sensitivity to the economic cycle: a higher $\rho$ means the portfolio is more exposed to recessions, leading to higher capital requirements precisely when the economy is weakest (procyclicality).
