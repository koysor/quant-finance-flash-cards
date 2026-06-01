# PowerTransformer

**Topic:** Computational Finance
**Tags:** preprocessing, skewness, feature scaling, yeo-johnson, box-cox, scikit-learn
**Created:** 2026-05-31
**Author:** Claude Sonnet 4.6

---

## Definition

**`PowerTransformer`** is a scikit-learn preprocessing class that applies a monotonic power transformation — either **Yeo-Johnson** (any real values) or **Box-Cox** (strictly positive values) — to map a skewed feature distribution toward a Gaussian shape, then standardises the result to zero mean and unit variance.

## Key Formula

**Yeo-Johnson** transformation with parameter $\lambda$ (estimated by maximum likelihood):

$$\psi(\lambda, y) = \begin{cases} \dfrac{(y+1)^\lambda - 1}{\lambda} & y \geq 0,\; \lambda \neq 0 \\[6pt] \ln(y + 1) & y \geq 0,\; \lambda = 0 \\[6pt] -\dfrac{(-y+1)^{2-\lambda} - 1}{2-\lambda} & y < 0,\; \lambda \neq 2 \\[6pt] -\ln(-y + 1) & y < 0,\; \lambda = 2 \end{cases}$$

When $\lambda = 1$ the transformation is the identity; $\lambda < 1$ compresses right tails (reduces positive skew); $\lambda > 1$ expands them. **Box-Cox** is the equivalent for strictly positive $x$: $\phi(\lambda, x) = (x^\lambda - 1)/\lambda$ for $\lambda \neq 0$, and $\ln x$ for $\lambda = 0$.

## Example

Daily trading volume for a mid-cap equity index is right-skewed: median 50 million shares, mean 120 million, 99th percentile 800 million. Raw skewness $\approx 4.2$. Fitting `PowerTransformer(method='yeo-johnson')` finds $\hat{\lambda} \approx 0.15$, which heavily compresses the right tail. Post-transformation the distribution has skewness $\approx 0.1$, close to symmetric. A logistic regression credit model using this transformed volume feature improves AUC from 0.71 to 0.74 compared with using raw or log-transformed volume.

## Remember

Many financial features are structurally right-skewed because they represent counts, sizes, or prices that have a hard floor at zero but no ceiling: trading volumes, position sizes, option open interest, bid-ask spreads, and market capitalisations all follow this pattern. Models such as logistic regression, linear SVM, and neural networks implicitly assume or perform better with features that are roughly symmetric and have bounded tails. The PowerTransformer's key advantage over a manual log transform is that it estimates the optimal $\lambda$ from the data by maximum likelihood, so it handles features where the log transform over- or under-corrects the skew. It must always be fitted only on training data and applied via `.transform()` on the test set to avoid look-ahead bias.
