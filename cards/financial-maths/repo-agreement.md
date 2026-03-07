# Repo Agreement

**Topic:** Financial Mathematics
**Tags:** repo, repurchase agreement, collateral, funding, money market, haircut
**Created:** 2026-03-07
**Author:** Claude Opus 4.6

---

## Definition

A repurchase agreement (repo) is a short-term borrowing arrangement in which one party sells a security to another and simultaneously agrees to repurchase it at a specified higher price on a future date. Economically, the seller is borrowing cash and the buyer is lending it, with the security serving as collateral.

## Key Formula

The **repo rate** is the implied interest rate on the loan:

$$r_{\text{repo}} = \frac{P_{\text{repurchase}} - P_{\text{sale}}}{P_{\text{sale}}} \times \frac{360}{t}$$

where $t$ is the term in days and the convention uses an actual/360 day count.

The **haircut** protects the lender against a fall in collateral value:

$$\text{Haircut} = \frac{\text{Market Value of Collateral} - \text{Cash Lent}}{\text{Market Value of Collateral}} \times 100\%$$

So the cash advanced is:

$$\text{Cash Lent} = \text{Market Value} \times (1 - h)$$

where $h$ is the haircut as a decimal.

## Example

A bank sells £10 million of gilts to a counterparty under a 7-day repo with a haircut of 2% and a repo rate of 4.5% per annum.

Cash received:

$$\text{Cash} = £10{,}000{,}000 \times (1 - 0.02) = £9{,}800{,}000$$

Interest owed after 7 days:

$$\text{Interest} = £9{,}800{,}000 \times 0.045 \times \frac{7}{360} = £8{,}575$$

Repurchase price:

$$P_{\text{repurchase}} = £9{,}800{,}000 + £8{,}575 = £9{,}808{,}575$$

The bank regains its gilts by paying £9,808,575 — an effective 7-day borrowing cost of £8,575.

## Remember

Repos are the primary funding mechanism for leveraged trading positions and the backbone of the money market. Banks and hedge funds use repos to finance bond portfolios at rates close to the risk-free rate, because the collateral reduces credit risk. The repo rate is the practical benchmark for the "risk-free rate" in many pricing models — it is more relevant than government bill yields because it reflects the actual cost of secured funding. During the 2008 crisis, the repo market froze as lenders demanded higher haircuts or refused to roll over repos, triggering a liquidity crisis that forced rapid deleveraging. The September 2019 US repo rate spike (briefly hitting 10%) demonstrated that even in normal times, funding market dislocations can propagate across the entire financial system.
