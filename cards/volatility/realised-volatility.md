# Realised Volatility

**Topic:** Volatility
**Tags:** realised volatility, historical volatility, variance, options, risk management
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

**Realised volatility** (also called historical or actual volatility) is the standard deviation of an asset's log returns measured over a past period. Unlike implied volatility, which is forward-looking and extracted from option prices, realised volatility is a backward-looking statistic computed directly from observed price data.

## Key Formula

The annualised realised volatility over $n$ return observations is:

$$\sigma_{\text{real}} = \sqrt{\frac{252}{n-1} \sum_{i=1}^{n} \left(\ln \frac{S_i}{S_{i-1}} - \bar{r}\right)^2}$$

where $\bar{r}$ is the mean log return and the factor 252 scales daily variance to an annual figure (assuming 252 trading days).

When the mean return is small relative to the standard deviation (as is typical for short horizons), a simpler **zero-mean** estimator is often used:

$$\sigma_{\text{real}} \approx \sqrt{\frac{252}{n} \sum_{i=1}^{n} \left(\ln \frac{S_i}{S_{i-1}}\right)^2}$$

## Example

Suppose the last 5 daily log returns of a stock are: $+0.8\%$, $-1.2\%$, $+0.5\%$, $-0.3\%$, $+1.0\%$.

Using the zero-mean estimator:

$$\text{Sum of squares} = 0.008^2 + (-0.012)^2 + 0.005^2 + (-0.003)^2 + 0.010^2$$

$$= 0.0000640 + 0.0001440 + 0.0000250 + 0.0000090 + 0.0001000 = 0.0003420$$

$$\sigma_{\text{real}} = \sqrt{\frac{252}{5} \times 0.0003420} = \sqrt{0.01724} \approx 13.1\%$$

## Remember

Realised volatility is the key input for evaluating whether options are cheap or expensive. If a trader buys an option at 20% implied volatility but the underlying subsequently realises only 13% volatility, the option was overpriced and the long position loses on a delta-hedged basis. This comparison between implied and realised volatility — the **variance risk premium** — is one of the most important trading signals in options markets. Realised volatility also underpins risk models (VaR, EWMA, GARCH) and is the settlement measure for variance swaps.
