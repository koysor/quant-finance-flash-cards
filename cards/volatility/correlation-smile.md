# Correlation Smile

**Topic:** Volatility
**Tags:** correlation smile, implied correlation, dispersion trading, index options, basket options
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

The **correlation smile** (or correlation skew) is the empirical pattern where the implied correlation between index constituents varies with the strike of index options. Implied correlation is backed out by comparing index option implied volatility with the implied volatilities of the constituent single-stock options. At lower index strikes (deeper out-of-the-money puts), implied correlation is higher — reflecting the market's expectation that stocks move together more during sell-offs. This phenomenon is the correlation analogue of the volatility smile.

## Key Formula

**Implied correlation** $\rho_{\text{impl}}$ for an equally weighted index of $n$ stocks:

$$\sigma_{\text{index}}^2 \approx \frac{1}{n}\bar{\sigma}^2 + \frac{n-1}{n}\rho_{\text{impl}}\,\bar{\sigma}^2$$

Solving for implied correlation:

$$\rho_{\text{impl}} = \frac{\sigma_{\text{index}}^2 - \frac{1}{n}\bar{\sigma}^2}{\frac{n-1}{n}\bar{\sigma}^2}$$

where $\bar{\sigma}^2$ is the average single-stock implied variance. In the large-$n$ limit:

$$\rho_{\text{impl}} \approx \frac{\sigma_{\text{index}}^2}{\bar{\sigma}^2}$$

The correlation smile emerges because $\sigma_{\text{index}}(K)$ increases more steeply at low strikes than $\bar{\sigma}(K)$ does.

## Example

The S&P 500 has ATM implied vol of 18% and average single-stock ATM implied vol of 30%. Using the large-$n$ approximation:

$$\rho_{\text{ATM}} \approx \frac{0.18^2}{0.30^2} = \frac{0.0324}{0.0900} = 0.36$$

At 90% moneyness, index implied vol rises to 25% while average single-stock implied vol rises to 33%:

$$\rho_{90\%} \approx \frac{0.25^2}{0.33^2} = \frac{0.0625}{0.1089} = 0.57$$

Implied correlation jumps from 36% to 57% as the strike moves lower — the market prices in much higher correlation during sell-offs.

## Remember

The correlation smile drives **dispersion trading**, one of the most important relative-value strategies on equity derivatives desks. A dispersion trader sells index options (where high implied correlation makes them expensive) and buys single-stock options (where individual implied vols are relatively cheaper), profiting when realised correlation is lower than implied. The trade is essentially short correlation. The correlation smile exists because during market crashes, diversification breaks down — all stocks fall together, correlations spike towards one, and index volatility rises disproportionately. This asymmetry in correlation (low in calm markets, high in crises) is a form of systematic risk that index option buyers are willing to pay a premium to hedge.
