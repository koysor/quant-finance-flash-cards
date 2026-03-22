# Locate Requirement

**Topic:** Short Selling
**Tags:** short selling, regulation, securities lending, hard-to-borrow, broker, locate
**Created:** 2026-03-16
**Author:** Claude Sonnet 4.6

---

## Definition

The locate requirement is the regulatory obligation, under SEC Regulation SHO, for a broker-dealer to have reasonable grounds to believe that the security can be borrowed and delivered before accepting a customer's short sale order. It is the first line of defence against naked short selling.

## Key Formula

A short sale is permissible only when a **locate** has been obtained:

$$\text{Short Sale Permitted} \iff \text{Locate Confirmed} = \text{True}$$

The **borrow availability ratio** (used by prime brokers to assess locate feasibility) is:

$$\text{BAR} = \frac{\text{Shares Available to Lend}}{\text{Total Short Demand}}$$

When $\text{BAR} < 1$, the security is **hard to borrow (HTB)** and locates may be denied or carry a premium borrow rate $r_b$:

$$r_b = r_{\text{base}} + \text{HTB Premium}$$

## Example

A hedge fund wants to short 500,000 shares of a small-cap stock. Their prime broker queries its lending pool and finds only 200,000 shares available to lend:

$$\text{BAR} = \frac{200{,}000}{500{,}000} = 0.4$$

The broker can only provide a locate for 200,000 shares. The remaining 300,000 shares cannot be legally shorted until a borrow is sourced. The fund may be quoted a borrow rate of 15% p.a. for the available shares, versus a typical 0.5% for easy-to-borrow securities.

## Remember

The locate requirement directly links securities lending markets to short-selling strategies. For a quant building a long-short model, the locate process sets a hard capacity constraint — a signal may be valid, but if the security cannot be borrowed, the short leg cannot be executed. Borrow availability and cost must be included in any realistic transaction cost model.
