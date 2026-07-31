# Weighted Least Squares in Fixed Income

**Topic:** Fixed Income
**Tags:** weighted least squares, dv01, yield curve fitting, calibration, bond pricing, curve construction
**Created:** 2026-06-20
**Author:** Claude Sonnet 4.6

---

## Definition

Weighted least squares (WLS) in fixed income is a yield curve fitting technique that assigns each instrument a weight — typically its DV01 — so that instruments with greater price sensitivity to rate changes receive proportionally more influence in the fitting objective, preventing long-dated bonds from dominating purely due to their larger duration.

## Key Formula

The WLS objective replaces the ordinary unweighted sum with:

$$\min_{\boldsymbol{\theta}} \sum_{i=1}^{N} w_i \left[y_i^{\text{obs}} - y(\tau_i;\,\boldsymbol{\theta})\right]^2, \qquad w_i = \text{DV01}_i$$

Compare with OLS where $w_i = 1$ for all $i$. In matrix form the solution is:

$$\hat{\boldsymbol{\theta}} = (\mathbf{X}^\top \mathbf{W} \mathbf{X})^{-1} \mathbf{X}^\top \mathbf{W}\, \mathbf{y}^{\text{obs}}$$

where $\mathbf{W} = \operatorname{diag}(w_1, \ldots, w_N)$. An equivalent formulation fits to prices rather than yields: because $\Delta P \approx -\text{DV01} \cdot \Delta y$, minimising unweighted price residuals $\sum_i (\hat{P}_i - P_i^{\text{obs}})^2$ automatically applies DV01$^2$ weights to the yield residuals.

## Example

A 1-year bond has DV01 $\approx \$0.01$ per \$100 face; a 30-year bond has DV01 $\approx \$0.15$. Under OLS a 5 bp fitting error in the 30Y contributes $(0.05)^2 = 0.0025$ to the residual sum, against $(0.05)^2 = 0.0025$ for the 1Y — identical, yet the 30Y error represents \$75 of price risk per \$1m versus \$50 for the 1Y. Under DV01-weighting the 30Y residual is scaled by 0.15 and the 1Y by 0.01, so the objective reflects economic importance rather than accident of parameterisation.

## Remember

Central banks (Bank of England, ECB) fit their official yield curves by minimising price errors, which is mathematically equivalent to yield-error minimisation with DV01$^2$ weights. Practitioners who fit to yields but omit DV01 weights risk systematically over-fitting the long end at the expense of the short end — skewing the fitted curve in exactly the tenors most sensitive to monetary policy.
