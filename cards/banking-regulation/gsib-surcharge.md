# G-SIB Surcharge and Too-Big-To-Fail

**Topic:** Banking Regulation
**Tags:** gsib, systemic risk, bail-in, surcharge, capital buffer
**Created:** 2026-04-13
**Author:** Claude Sonnet 4.6

---

## Definition

Global Systemically Important Banks (G-SIBs) are banks whose failure would cause significant disruption to the wider financial system due to their size, interconnectedness, and complexity. The Basel G-SIB framework imposes an additional CET1 capital surcharge (0.5%–3.5% of RWA) on top of the standard minimum, calibrated annually based on a scoring methodology. The surcharge is the regulatory response to the "too-big-to-fail" problem: the implicit government guarantee that large banks receive, which lowers their funding cost and encourages excessive risk-taking.

## Key Formula

The G-SIB score is calculated from five equally weighted categories:

$$\text{Score} = \frac{1}{5}\left(\text{Size} + \text{Interconnectedness} + \text{Substitutability} + \text{Complexity} + \text{Cross-jurisdiction}\right)$$

Each category is a set of indicator ratios relative to the global aggregate. The score maps to a surcharge bucket:

| Score (bps) | Surcharge |
|---|---|
| 130–229 | 1.0% |
| 230–329 | 1.5% |
| 330–429 | 2.0% |
| 430–529 | 2.5% |
| >529 | 3.5% (empty bucket, deterrence) |

Under the EU's Bank Recovery and Resolution Directive (BRRD), G-SIBs must also maintain minimum TLAC/MREL (loss-absorbing capacity) to enable bail-in rather than government bailout.

## Example

HSBC has a G-SIB score placing it in the 2.0% surcharge bucket. With RWA of approximately $850 bn, the surcharge requires an additional $17 bn of CET1 capital beyond the standard 4.5% minimum. This capital cannot be used to pay dividends or absorb losses in normal conditions — it exists solely as a going-concern buffer to prevent the bank becoming non-viable and requiring resolution.

## Remember

The G-SIB framework directly addresses the moral hazard created by too-big-to-fail: before 2010, large banks enjoyed an implicit government subsidy through their perceived backstop, which artificially reduced their funding costs by 20–80 bps relative to smaller banks. The surcharge increases the cost of being large and systemic, partially internalising the externality. The "empty bucket" at 3.5% is a deliberate deterrence mechanism — no bank currently sits there, but any bank that grew into it would face a surcharge high enough to make that growth economically unattractive. For quant developers, G-SIB status affects every capital calculation in the bank: higher total capital requirements constrain RWA budgets, drive trade compression and portfolio management, and directly influence how aggressively a bank can price capital-intensive products.

