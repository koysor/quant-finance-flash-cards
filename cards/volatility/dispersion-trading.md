# Dispersion Trading

**Topic:** Volatility
**Tags:** dispersion trading, implied correlation, index volatility, single-stock volatility, relative value
**Created:** 2026-04-03
**Author:** Claude Opus 4.6

---

## Definition

Dispersion trading is a volatility arbitrage strategy that exploits the difference between the implied volatility of an index and the implied volatilities of its constituent stocks. Because index implied volatility embeds an implied correlation premium — the market systematically overprices the degree to which stocks move together — a dispersion trade sells index options (or variance) and buys single-stock options (or variance), profiting when realised correlation is lower than implied. It is a pure bet on correlation, isolated from the direction of volatility itself.

## Key Formula

The implied variance of an index with $n$ equally weighted constituents:

$$\sigma_{\text{index}}^2 = \sum_{i=1}^{n} w_i^2 \sigma_i^2 + \sum_{i \neq j} w_i w_j \rho_{ij} \sigma_i \sigma_j$$

With equal weights and uniform pairwise correlation $\bar{\rho}$:

$$\sigma_{\text{index}}^2 \approx \bar{\sigma}^2 \left[\frac{1}{n} + \frac{n-1}{n}\bar{\rho}\right]$$

The **implied correlation** backed out from option prices:

$$\bar{\rho}_{\text{impl}} = \frac{\sigma_{\text{index}}^2 - \sum w_i^2 \sigma_i^2}{\sum_{i \neq j} w_i w_j \sigma_i \sigma_j}$$

The dispersion P&L is approximately proportional to:

$$\text{P\&L} \propto \bar{\rho}_{\text{impl}} - \bar{\rho}_{\text{real}}$$

## Example

The FTSE 100 index has implied volatility of 18%. The weighted average single-stock implied volatility is 25%. Implied correlation is:

$$\bar{\rho}_{\text{impl}} \approx \left(\frac{18}{25}\right)^2 = 0.518$$

A trader sells index variance at 18 vol and buys constituent variance at 25 vol (vega-weighted). Over the next month, realised index volatility is 15% and realised single-stock volatility averages 24%, implying realised correlation of approximately:

$$\bar{\rho}_{\text{real}} \approx \left(\frac{15}{24}\right)^2 = 0.391$$

Since $\bar{\rho}_{\text{real}} < \bar{\rho}_{\text{impl}}$ (0.39 < 0.52), the dispersion trade profits. The index leg gains (sold at 18, realised 15) and the single-stock legs lose slightly (bought at 25, realised 24), but the net effect is positive because the correlation premium was overpriced.

## Remember

Dispersion trading is a cornerstone strategy on equity derivatives desks in London and globally. The implied correlation premium exists because portfolio hedgers buy index puts (pushing index vol up) while single-stock options are driven more by stock-specific supply and demand. For quant developers, implementing dispersion requires building a correlation matrix from option prices, vega-weighting the single-stock legs to be neutral to parallel shifts in volatility, and managing the residual vega and gamma exposures. The strategy lost money spectacularly during the 2008 crisis when realised correlations spiked towards 1.0, making it a cautionary example of how relative value trades can become directional bets during systemic stress.
