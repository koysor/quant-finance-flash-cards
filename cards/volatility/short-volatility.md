# Short Volatility

**Topic:** Volatility
**Tags:** short volatility, vega, options, premium selling, risk, theta
**Created:** 2026-04-03
**Author:** Claude Opus 4.6

---

## Definition

A short volatility position is any portfolio or strategy that profits when the volatility of an underlying asset decreases or remains low. The simplest example is selling (writing) options, which generates premium income but creates exposure to losses if volatility spikes. Any position with negative **vega** — negative sensitivity to implied volatility — is described as short volatility. Short volatility strategies harvest the variance risk premium but carry significant tail risk.

## Key Formula

The P&L contribution from a change in implied volatility $\Delta\sigma$ for a position with vega $\mathcal{V}$:

$$\text{P\&L}_{\text{vol}} \approx \mathcal{V} \times \Delta\sigma$$

For a short volatility position, $\mathcal{V} < 0$, so a rise in $\sigma$ produces a loss. For a delta-hedged short option, the realised P&L over a small interval is:

$$d\text{P\&L} = \frac{1}{2}\,\Gamma\,S^2\left(\sigma_{\text{implied}}^2 - \sigma_{\text{realised}}^2\right)dt$$

A short volatility position profits when $\sigma_{\text{realised}} < \sigma_{\text{implied}}$.

## Example

A trader sells 100 ATM put options on a FTSE 100 stock, collecting £3.00 per option (£300 total premium). The position vega is $-$£600 per 1 percentage point change in implied volatility. If implied volatility drops from 22% to 18%:

$$\text{P\&L}_{\text{vol}} \approx (-£600) \times (-4) = £2{,}400$$

The position gains approximately £2,400 from the volatility decrease, plus the ongoing theta decay. However, if a market shock pushes implied volatility from 22% to 40%:

$$\text{P\&L}_{\text{vol}} \approx (-£600) \times 18 = -£10{,}800$$

The loss from a single spike can dwarf months of collected premium.

## Remember

Short volatility is the natural position of option sellers, structured product issuers, and many systematic hedge fund strategies. The variance risk premium — the persistent gap where implied volatility exceeds realised — makes short volatility profitable on average, which is why it attracts capital. However, the return profile is concave: frequent small gains punctuated by rare catastrophic losses. This is the classic "picking up pennies in front of a steamroller" risk. In quantitative finance, understanding that many institutional portfolios carry hidden short volatility exposure (through structured notes, risk premia strategies, or leveraged positions that force selling in drawdowns) is essential for stress testing and systemic risk analysis.
