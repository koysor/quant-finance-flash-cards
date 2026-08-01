# Johansen Procedure

**Topic:** Statistics
**Tags:** cointegration, trace statistic, eigenvalues, multivariate, pairs trading, likelihood ratio
**Created:** 2026-08-01
**Author:** Claude Opus 5

---

## Definition

The Johansen procedure is a maximum-likelihood test for the number of cointegrating relationships among several non-stationary series simultaneously. Unlike Engle-Granger, which handles one pair and requires choosing which variable to put on the left, it treats all variables symmetrically and can detect several independent long-run relationships at once.

## Key Formula

The test works on the long-run impact matrix $\Pi$ from the vector error correction form. Its **rank** $r$ is the number of cointegrating relationships. Estimated eigenvalues $\hat\lambda_1 > \hat\lambda_2 > \dots > \hat\lambda_n$ are the squared canonical correlations between $\Delta \mathbf{P}_t$ and $\mathbf{P}_{t-1}$, each lying in $[0,1]$.

Two likelihood-ratio statistics test the rank:

**Maximum eigenvalue**, testing $H_0: r = r^*$ against $H_1: r = r^*+1$:

$$LR_{\max}(r^*) = -T\ln\!\left(1 - \hat\lambda_{r^*+1}\right)$$

**Trace**, testing $H_0: r = r^*$ against $H_1: r > r^*$:

$$LR_{\text{trace}}(r^*) = -T\sum_{i=r^*+1}^{n}\ln\!\left(1 - \hat\lambda_i\right)$$

Testing proceeds upwards from $r^* = 0$ and stops at the first non-rejection.

## Example

A yield-curve study on seven tenors returns eigenvalues $(0.182,\ 0.094,\ 0.031,\ \dots)$ with $T = 500$ observations.

$$LR_{\max}(0) = -500\ln(1 - 0.182) = -500 \times (-0.2010) = 100.5$$

Against a 5% critical value of about 46 for $n = 7$, reject $r = 0$. Moving up:

$$LR_{\max}(1) = -500\ln(1 - 0.094) = 49.3$$

still above its critical value of roughly 40, so reject $r = 1$ too. The third gives 15.8 against about 34 — do not reject. Conclusion: rank 2, so two independent cointegrating relationships exist among the seven tenors.

## Remember

Two practical caveats decide whether the output is tradeable. First, the procedure tells you *how many* relationships exist but not *which variables* participate — with seven tenors, a rank of 2 is consistent with a relationship among three of them or all seven, and identifying the tradeable subset is your judgement, not the test's. Second, the factorisation $\Pi = \alpha\beta'$ identifies only the **space spanned** by the cointegrating vectors, not the vectors themselves: any invertible rotation gives an equally valid answer, which is why raw output arrives unnormalised with weights like 560% and −1455%. Normalising the leading element to one recovers the familiar $[1, -\beta_C]$ hedge ratio, and imposing economically sensible restrictions on the weights is legitimate and often necessary before the relationship can be traded.
