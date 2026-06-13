# CMS Convexity Adjustment

**Topic:** Fixed Income
**Tags:** CMS, constant maturity swap, convexity adjustment, swap rate, annuity, forward measure
**Created:** 2026-06-11
**Author:** Claude Sonnet 4.6

---

## Definition

A **constant-maturity swap (CMS)** coupon pays the prevailing $n$-year swap rate at each coupon date. The **CMS convexity adjustment** is the positive correction that must be added to the forward swap rate to obtain the fair CMS coupon rate. It arises because the payment is made at the coupon date $T$, not at the swap maturity, so the natural pricing measure (the $T$-forward measure) differs from the annuity measure used to define the forward swap rate.

## Key Formula

Let $F$ be the forward swap rate and $A(T)$ the annuity (present value of \$1 per year over the swap tenor), both observed at coupon date $T$. Under the normal model with swap rate volatility $\sigma$:

$$\text{CMS coupon rate} \approx F + \underbrace{\sigma^2 T \cdot F \cdot \frac{\partial \ln A}{\partial F}}_{\text{convexity adjustment}}$$

For an $n$-year swap with flat rate $F$ the annuity is $A = \frac{1 - (1+F)^{-n}}{F}$, giving:

$$\frac{\partial \ln A}{\partial F} \approx \frac{n}{(1+F)\bigl[(1+F)^n - 1\bigr]} - \frac{1}{F}$$

A rougher approximation often used in practice:

$$\text{CMS adjustment} \approx \frac{\sigma^2 T \cdot D_{\text{swap}}}{1 + F \cdot D_{\text{swap}}}$$

where $D_{\text{swap}}$ is the modified duration of the reference swap.

## Example

10-year CMS coupon, $T = 1$ yr, forward 10y swap rate $F = 4\%$, swap vol $\sigma = 80$ bp $= 0.008$. Duration $D_{\text{swap}} \approx 8.0$ yr.

$$\text{Adjustment} \approx \frac{(0.008)^2 \times 1 \times 8.0}{1 + 0.04 \times 8.0} = \frac{0.000512}{1.32} \approx 3.9 \text{ bp}$$

The CMS coupon is approximately $4\% + 4$ bp $= 4.04\%$, not $4\%$.

## Remember

CMS convexity adjustments are always **positive** because, when rates rise, the annuity shrinks (rates and bond prices move in opposite directions), which means a CMS coupon holder receives more when the annuity is small — a favourable correlation. This is economically equivalent to being long a strip of co-terminal swaptions. Dealers who pay CMS rates to clients hedge the adjustment by buying out-of-the-money receiver swaptions. Ignoring the adjustment on long-maturity CMS structures causes errors of 10–30 bp, which is material in any rate environment.
