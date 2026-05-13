# Underfitting

**Topic:** Computational Finance
**Tags:** underfitting, bias, model complexity, supervised learning, model selection, generalisation
**Created:** 2026-04-22
**Author:** Claude Sonnet 4.6

---

## Definition

**Underfitting** occurs when a model is too simple to capture the true relationship in the data, producing high bias and low variance. Both training error and test error are high because the model fails to learn the underlying pattern — not just the noise.

## Key Formula

For a model with squared-error loss, the expected prediction error decomposes as:

$$\mathbb{E}\!\left[(y - \hat{f}(\mathbf{x}))^2\right] = \underbrace{\left(\mathbb{E}[\hat{f}] - f\right)^2}_{\text{Bias}^2} + \underbrace{\mathbb{E}\!\left[(\hat{f} - \mathbb{E}[\hat{f}])^2\right]}_{\text{Variance}} + \sigma^2_\varepsilon$$

Underfitting corresponds to the regime where $\text{Bias}^2 \gg \text{Variance}$: the model is systematically wrong regardless of which training sample is drawn.

## Example

Fit a simple linear model $\hat{r}_t = \alpha + \beta_1 r_{t-1}$ to monthly equity returns that follow a regime-switching pattern (positive autocorrelation in bull markets, negative in bear markets). Training $R^2 = 0.03$ and test $R^2 = 0.02$ — both are near zero. Switching to a two-regime hidden Markov model raises training $R^2$ to 0.31 and test $R^2$ to 0.27, showing the linear model was underfitting the non-linear structure.

## Remember

In quantitative finance, underfitting is as dangerous as overfitting but less discussed. A linear factor model applied to credit spreads or implied volatility surfaces — which are demonstrably non-linear — will systematically misprice instruments across the entire range of inputs. The signal that a model is underfitting is simultaneous high error on both training and validation sets; adding model complexity (more features, non-linear terms, or a richer architecture) is the correct remedy, not regularisation.
