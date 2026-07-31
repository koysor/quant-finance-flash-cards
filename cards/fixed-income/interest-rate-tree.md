# Interest Rate Tree

**Topic:** Fixed Income
**Tags:** interest rate tree, binomial tree, backward induction, short rate, calibration, lattice
**Created:** 2026-06-20
**Author:** Claude Sonnet 4.6

---

## Definition

An interest rate tree is a discrete-time lattice in which each node stores a possible short rate at that time step; bond prices and interest rate derivatives are valued by backward induction, discounting at the short rate prevailing at each node rather than a fixed risk-free rate.

## Key Formula

At node $(t, j)$ — where $t$ is the time step and $j$ counts up-moves — the value of a security is:

$$V_{t,j} = e^{-r_{t,j}\,\Delta t}\bigl[\,p\,V_{t+1,j+1} + (1-p)\,V_{t+1,j}\,\bigr]$$

where $r_{t,j}$ is the short rate at that node and $p = \tfrac{1}{2}$ under the symmetric binomial convention. Terminal values $V_{T,j}$ equal the contractual payoff. The tree is **calibrated column by column**: at each step $t$, rates are shifted by a constant $\eta_t$ so the tree exactly reprices the observed zero-coupon bond maturing at $t\,\Delta t$.

## Example

Two-step tree, $\Delta t = 1$ year, $p = \tfrac{1}{2}$, observed 2-year yield = 5.5%.

At $t = 0$: short rate $r_0 = 5.00\%$ (calibrated to the 1-year bond).

At $t = 1$: rates $r_u = 6.20\%$ (up) and $r_d = 5.80\%$ (down) are calibrated to reprice the 2-year zero-coupon bond at $P(0,2) = e^{-0.11} = 0.8958$:

$$P(0,2) = e^{-0.05}\!\left[\tfrac{1}{2}\,e^{-0.062} + \tfrac{1}{2}\,e^{-0.058}\right] = 0.9512 \times 0.9418 \approx 0.8958 \checkmark$$

Pricing a 2-year zero paying £100 by backward induction:

$$V_0 = e^{-0.05}\!\left[\tfrac{1}{2}(e^{-0.062} \times 100) + \tfrac{1}{2}(e^{-0.058} \times 100)\right] = 0.9512 \times 94.18 \approx \textbf{£89.58}$$

## Remember

The decisive distinction between an equity binomial tree and an interest rate tree is what each node stores: equity trees store asset prices and discount at a fixed rate, whereas rate trees store the discount rate itself and reuse it to evolve the lattice forward **and** discount cash flows backward. Calibrating every column to a market zero-coupon bond is not optional — an uncalibrated tree systematically mis-prices plain-vanilla bonds, making any computed credit or option spread meaningless. For callable bonds and Bermudan swaptions where closed-form solutions do not exist, the calibrated rate tree is the standard production pricing tool.
