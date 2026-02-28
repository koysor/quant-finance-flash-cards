# Return on Investment

**Topic:** Financial Mathematics
**Level:** A Level Mathematics
**Tags:** returns, investment, relative change, asset pricing
**Created:** 2026-02-28
**Author:** Unknown

---

## Definition

The **return on investment** is the relative change in value of an asset over a period, expressed as a fraction or percentage rather than an absolute cash amount. Using returns instead of raw prices allows fair comparison between assets of different scales.

## Key Formula

$$R = \frac{\Delta S + \text{cashflows}}{S_0}$$

where $S_0$ is the starting price, $\Delta S$ is the change in price, and cashflows include dividends or coupons received.

For a discrete time step from day $i$ to day $i+1$:

$$R_i = \frac{S_{i+1} - S_i}{S_i}$$

## Example

A stock is priced at £80 and rises to £84 over one day, paying no dividend.

$$R = \frac{84 - 80}{80} = \frac{4}{80} = 0.05 = 5\%$$

A second stock priced at £400 also rises by £4, giving $R = 4/400 = 1\%$. The return reveals that the first stock performed better despite the same absolute gain.

## Remember

Returns are the fundamental input to every quantitative model — from the random walk model of asset prices ($dS/S$) to portfolio optimisation and Value at Risk. Always work with returns, never raw prices, when estimating drift, volatility, or correlations.
