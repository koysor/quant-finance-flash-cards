# Output Gap

**Topic:** Financial Mathematics
**Tags:** output gap, gdp, potential output, taylor rule, recession, monetary policy
**Created:** 2026-06-03
**Author:** Claude Sonnet 4.6

---

## Definition

The output gap is the percentage difference between actual GDP and potential GDP (the level of output consistent with stable inflation), entering the Taylor Rule as the measure of whether the economy is running above or below capacity and therefore whether monetary policy should be tightening or easing.

## Key Formula

$$\text{Output gap} = \frac{Y_t - Y_t^*}{Y_t^*} \times 100\%$$

where $Y_t$ is actual real GDP and $Y_t^*$ is potential output. In the Taylor Rule:

$$r_t = r^* + \pi_t + \alpha(\pi_t - \pi^*) + \beta \underbrace{(Y_t - Y_t^*)/Y_t^*}_{\text{output gap}}$$

A positive output gap (economy above potential) raises the prescribed rate; a negative gap lowers it. Potential output $Y_t^*$ is typically estimated via the Hodrick-Prescott (HP) filter, production function methods, or the Congressional Budget Office model.

## Example

US Q2 2021: actual real GDP \$19.36tn, CBO potential GDP estimate \$19.18tn. Output gap = $(19.36 - 19.18)/19.18 = +0.94\%$. With CPI at 5.4%, the Taylor Rule prescribed $r = 0.5 + 5.4 + 0.5(3.4) + 0.5(0.94) = 8.07\%$. Actual fed funds rate: 0.08\%. The positive output gap confirmed the economy was overheating, reinforcing the signal that policy was far behind the curve and aggressive hikes were coming.

## Remember

The output gap is the hardest Taylor Rule input to estimate in real time: potential GDP is not observed and early estimates are frequently revised by 1-2% as more data arrives. This **real-time estimation problem** explains why central banks sometimes appear to miss the tightening window — their real-time output gap estimate is near zero while the revised estimate is strongly positive. Fixed income traders who track CBO or IMF output gap revisions can anticipate shifts in the Taylor Rule prescription before they are reflected in central bank communications, positioning in the 1-3 year segment of the yield curve ahead of the rate response.
