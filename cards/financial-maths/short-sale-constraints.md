# Short Sale Constraints

**Topic:** Financial Mathematics
**Tags:** short sale constraints, regulation, uptick rule, short selling ban, market efficiency
**Created:** 2026-03-07
**Author:** Claude Opus 4.6

---

## Definition

Short sale constraints are regulatory, institutional, or market-based restrictions that limit the ability to sell securities short. These include uptick rules (requiring short sales to occur at a price above the last trade), outright bans on short selling during crises, disclosure requirements for large short positions, and the practical difficulty of locating shares to borrow.

## Key Formula

The **overpricing bound** implied by short sale constraints:

$$P_{\text{observed}} \leq P_{\text{fundamental}} + \Delta P_{\text{constraint}}$$

where $\Delta P_{\text{constraint}}$ is the maximum overpricing that cannot be corrected because pessimistic investors are unable to short.

The **Miller (1977) model** predicts that with heterogeneous beliefs and short sale constraints:

$$P = E_{\text{optimistic}}[V]$$

rather than the average expectation, because pessimists cannot express their views by shorting.

## Example

Two groups of investors value a stock differently: optimists at £50 and pessimists at £30. With no constraints, arbitrage would push the price towards the consensus value of approximately £40.

With a short-selling ban, pessimists cannot sell short, so only optimists participate. The stock trades at £50 — overpriced by £10 relative to the consensus.

When the ban is lifted, pessimists can now short the stock. The price adjusts downward towards £40, and the short sellers earn $£50 - £40 = £10$ per share.

## Remember

Short sale constraints are a major source of mispricing in financial markets. Academic research (notably Miller 1977, and Lamont & Thaler 2003) shows that constrained stocks are systematically overpriced — they deliver lower subsequent returns because negative information is not fully reflected in prices. For quantitative funds, constraints create both **opportunities** (overpriced stocks can be identified and shorted when constraints ease) and **risks** (inability to hedge or express bearish views). During the 2008 crisis, temporary short-selling bans in the US, UK, and Europe disrupted hedge fund strategies and widened bid-ask spreads, demonstrating that constraints reduce market quality even when intended to stabilise prices.
