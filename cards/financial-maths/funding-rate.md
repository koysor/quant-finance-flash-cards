# Funding Rate

**Topic:** Financial Mathematics
**Tags:** funding rate, cost of carry, repo rate, margin interest, leverage cost
**Created:** 2026-03-07
**Author:** Claude Opus 4.6

---

## Definition

The funding rate is the cost of financing a leveraged trading position. It includes the interest paid on borrowed cash (for long positions) or the rebate earned on posted collateral (for short positions). In practice, funding is typically sourced through repurchase agreements (repos), prime brokerage margin loans, or exchange margin facilities.

## Key Formula

The **total cost of carry** for a leveraged long position:

$$C_{\text{carry}} = V_{\text{borrowed}} \times r_f \times \frac{t}{360}$$

where $r_f$ is the annualised funding rate and $V_{\text{borrowed}}$ is the borrowed amount.

For a **long-short portfolio**, the net funding cost is:

$$C_{\text{net}} = (V_{\text{long}} - E) \times r_{\text{long}} - V_{\text{short}} \times r_{\text{rebate}} + V_{\text{short}} \times r_{\text{borrow}}$$

where $E$ is equity, $r_{\text{long}}$ is the margin loan rate, $r_{\text{rebate}}$ is the short rebate, and $r_{\text{borrow}}$ is the stock borrow rate.

## Example

A fund has £5 million equity, £8 million long, and £6 million short. The margin loan rate is 5%, the short rebate is 4%, and the average stock borrow rate is 1%.

$$C_{\text{long}} = (8{,}000{,}000 - 5{,}000{,}000) \times 0.05 = £150{,}000$$

$$C_{\text{rebate}} = 6{,}000{,}000 \times 0.04 = £240{,}000 \text{ (earned)}$$

$$C_{\text{borrow}} = 6{,}000{,}000 \times 0.01 = £60{,}000$$

$$C_{\text{net}} = £150{,}000 - £240{,}000 + £60{,}000 = -£30{,}000$$

The fund actually earns £30,000 per annum from the funding structure — the short rebate exceeds the borrowing and lending costs. This is possible when the short rebate rate exceeds the spread between margin loan rates and borrow costs.

## Remember

Funding costs are the hidden drag on leveraged strategies that textbook models often ignore. In the CAPM and Black-Scholes frameworks, all investors borrow and lend at the risk-free rate, but in reality, funding spreads vary by institution, creditworthiness, and market conditions. During the 2008 crisis, funding rates spiked as interbank lending froze, forcing leveraged funds to deleverage even when their positions were fundamentally sound. For quantitative portfolio managers, accurate modelling of funding costs is essential — a strategy with attractive gross alpha may have negative net alpha once funding, transaction, and borrow costs are deducted.
