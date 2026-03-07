# Reverse Repo

**Topic:** Financial Mathematics
**Tags:** reverse repo, cash lending, collateral, central bank, money market
**Created:** 2026-03-07
**Author:** Claude Opus 4.6

---

## Definition

A reverse repurchase agreement (reverse repo) is the mirror side of a repo transaction — the party that buys the security and lends cash. The cash lender receives the security as collateral and earns the repo rate as interest. Central banks use reverse repos as a monetary policy tool to drain excess liquidity from the banking system.

## Key Formula

The **return to the cash lender** in a reverse repo:

$$\text{Interest Earned} = \text{Cash Lent} \times r_{\text{repo}} \times \frac{t}{360}$$

The **collateral coverage ratio** ensures the lender is protected:

$$\text{Coverage} = \frac{\text{Market Value of Collateral}}{\text{Cash Lent}} = \frac{1}{1 - h}$$

where $h$ is the haircut. With a 2% haircut, coverage is $1/0.98 = 1.02$, meaning the lender holds £102 of collateral for every £100 lent.

## Example

A money market fund lends £50 million overnight to a bank via reverse repo at a rate of 4.25%, receiving £51 million of gilts as collateral (haircut ≈ 2%).

$$\text{Interest} = £50{,}000{,}000 \times 0.0425 \times \frac{1}{360} = £5{,}903$$

$$\text{Coverage} = \frac{51{,}000{,}000}{50{,}000{,}000} = 1.02$$

The fund earns £5,903 overnight with minimal risk — if the bank defaults, the fund keeps £51 million of gilts to recover its £50 million loan.

## Remember

Reverse repos are the safest short-term investment available, combining a secured return with government bond collateral. They are the primary investment vehicle for money market funds and corporate treasuries parking excess cash. Central banks use reverse repo facilities to set a floor on short-term interest rates — the Federal Reserve's overnight reverse repo facility (ON RRP) absorbed over $2 trillion at its peak in 2022, demonstrating its role as a critical monetary plumbing tool. For quantitative analysts, the reverse repo rate is the practical "risk-free rate" — it represents what an investor actually earns on secured overnight lending, making it more relevant than theoretical constructs for pricing and discounting.
