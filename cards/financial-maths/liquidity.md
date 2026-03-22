# Liquidity

**Topic:** Financial Mathematics
**Level:** A Level Mathematics
**Tags:** liquidity, market depth, turnover, illiquidity premium, trading cost
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

Liquidity is the ease with which an asset can be bought or sold in the market without significantly affecting its price. A highly liquid asset (e.g. a large-cap stock or government bond) can be traded in large quantities with minimal price impact; an illiquid asset (e.g. a small-cap stock, real estate, or distressed debt) requires price concessions to attract a counterparty. Liquidity has multiple dimensions: **tightness** (bid-ask spread), **depth** (volume available near the mid price), **resilience** (speed at which prices recover after a large trade), and **immediacy** (time to execute).

## Key Formula

The **Amihud illiquidity ratio** (the most widely used cross-sectional liquidity measure):

$$\text{ILLIQ}_i = \frac{1}{D} \sum_{d=1}^{D} \frac{|r_{i,d}|}{\text{Volume}_{i,d}}$$

where $|r_{i,d}|$ is the absolute daily return, $\text{Volume}_{i,d}$ is the daily trading volume in currency, and $D$ is the number of trading days. Higher values indicate less liquidity (more price impact per unit of volume).

The **turnover ratio**:

$$\text{Turnover} = \frac{\text{Total Volume Traded}}{\text{Shares Outstanding}}$$

## Example

Two stocks over 5 trading days:

| Stock | Avg $|r|$ | Avg daily volume | Amihud ratio |
|-------|----------|-----------------|-------------|
| A (large-cap) | 0.8% | £50,000,000 | $\frac{0.008}{50{,}000{,}000} = 1.6 \times 10^{-10}$ |
| B (small-cap) | 1.5% | £500,000 | $\frac{0.015}{500{,}000} = 3.0 \times 10^{-8}$ |

Stock B is 188 times more illiquid than Stock A by the Amihud measure. A £1 million trade in Stock A would move the price negligibly, but the same trade in Stock B (twice its daily volume) could move the price by several percent.

## Remember

Liquidity is one of the most important and least understood concepts in quantitative finance. The **illiquidity premium** — the extra return investors demand for holding hard-to-sell assets — is a well-documented risk factor that explains a significant fraction of cross-sectional return variation. Liquidity is also procyclical: it is abundant in calm markets and evaporates during crises, precisely when it is needed most. This "liquidity spiral" (Brunnermeier and Pedersen, 2009) creates a feedback loop where falling prices reduce collateral values, triggering margin calls and forced selling that further drains liquidity. For portfolio managers, liquidity determines strategy capacity — the maximum amount of capital a strategy can deploy before market impact erodes its alpha to zero.
