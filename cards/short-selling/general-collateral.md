# General Collateral (GC)

**Topic:** Short Selling
**Tags:** general collateral, GC rate, repo, securities lending, specialness, collateral pool
**Created:** 2026-06-13
**Author:** Claude Sonnet 4.6

---

## Definition

General collateral (GC) refers to the broad pool of interchangeable, liquid securities (principally government bonds) that can be used as collateral in repo or securities lending at a uniform market rate; no specific bond is required.

## Key Formula

$$\text{GC rate} \approx \text{overnight risk-free rate} \pm \text{small basis}$$

$$\text{Specialness of bond } i = \text{GC rate} - \text{repo rate for bond } i$$

A bond is "on special" when its repo rate trades below GC — lenders accept a lower return to obtain that specific bond (e.g. to short it or deliver into futures).

## Example

US Treasury GC overnight rate $= 5.30\%$. The on-the-run 10yr Treasury repos at $5.10\%$ (special by 20bps). A dealer who owns the on-the-run earns 20bps above GC by lending it out. A hedge fund wanting to short the on-the-run must borrow it at $5.10\%$ — paying the specialness in return for supply.

## Remember

The GC–special spread measures how much the market wants to short a specific bond. On-the-run Treasuries are almost always special because they are the cheapest-to-deliver into futures and the most widely used short hedge. Tracking specialness across the curve reveals positioning and demand for specific maturities — a useful signal for fixed income relative value traders.
