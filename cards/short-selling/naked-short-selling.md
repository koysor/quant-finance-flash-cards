# Naked Short Selling

**Topic:** Short Selling
**Tags:** short selling, regulation, settlement, market abuse, securities lending, locate
**Created:** 2026-03-16
**Author:** Claude Sonnet 4.6

---

## Definition

Naked short selling is the practice of short selling a security without first borrowing it or confirming that it can be borrowed, meaning the seller delivers shares that do not exist at the time of the trade. It is banned in most regulated markets because it can create artificial supply and depress prices.

## Key Formula

In a standard (covered) short, the **settlement obligation** is always met:

$$\text{Shares Sold} \leq \text{Shares Borrowed}$$

In a naked short, this constraint is violated — shares are sold without a confirmed borrow, creating a **fail-to-deliver (FTD)**:

$$\text{FTD} = \text{Shares Sold} - \text{Shares Available to Borrow} > 0$$

Regulators monitor the **FTD rate** as a fraction of average daily volume (ADV):

$$\text{FTD Rate} = \frac{\text{FTD Shares}}{\text{ADV}}$$

## Example

A trader sells 100,000 shares of a stock short without locating a borrow. The ADV is 500,000 shares. At settlement (T+2), the trader cannot deliver:

$$\text{FTD} = 100{,}000 \text{ shares}$$

$$\text{FTD Rate} = \frac{100{,}000}{500{,}000} = 20\%$$

A rate above 0.5% typically triggers regulatory scrutiny. The broker must close out the position under the SEC's Regulation SHO close-out requirements.

## Remember

Naked short selling is relevant to quants because it exposes a gap in the no-arbitrage framework: prices can be artificially depressed if synthetic supply is created without a genuine borrow. Understanding the locate requirement and FTD mechanics is essential when modelling the true cost of short positions in illiquid or hard-to-borrow securities.
