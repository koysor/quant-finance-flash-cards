# Securities Lending

**Topic:** Short Selling
**Tags:** securities lending, short selling, borrowing, collateral, rebate rate
**Created:** 2026-03-07
**Author:** Claude Opus 4.6

---

## Definition

Securities lending is the temporary transfer of shares or bonds from a lender (typically an institutional investor or custodian) to a borrower, in exchange for collateral and a fee. The borrower uses the securities — most commonly to facilitate short selling — and must return identical securities on demand or at an agreed date.

## Key Formula

The **borrowing cost** paid by the short seller to the lender is:

$$C_{\text{borrow}} = \text{Market Value} \times r_{\text{borrow}} \times \frac{t}{365}$$

where $r_{\text{borrow}}$ is the annualised borrow rate and $t$ is the number of days.

The **rebate rate** received by the borrower on posted cash collateral is:

$$r_{\text{rebate}} = r_{\text{risk\text{-}free}} - r_{\text{borrow}}$$

The **net cost of carry** for a short position is therefore:

$$C_{\text{net}} = \text{Market Value} \times (r_{\text{borrow}} - r_{\text{risk\text{-}free}}) \times \frac{t}{365}$$

## Example

A hedge fund borrows 10,000 shares of a stock trading at £15 for 90 days. The annualised borrow rate is 3% and the risk-free rate is 5%.

$$C_{\text{borrow}} = £150{,}000 \times 0.03 \times \frac{90}{365} = £1{,}110$$

The fund posts £150,000 cash collateral and earns:

$$\text{Rebate} = £150{,}000 \times (0.05 - 0.03) \times \frac{90}{365} = £740$$

Net borrowing cost: $£1{,}110 - £740 = £370$. For "hard-to-borrow" stocks, $r_{\text{borrow}}$ can exceed 20%, making the short position expensive to maintain.

## Remember

Securities lending is the invisible infrastructure behind short selling and many arbitrage strategies. The borrow rate acts as a friction that reduces short-selling profits and can make certain trades uneconomical. In quantitative finance, the "special" or hard-to-borrow rate is itself a signal — academic research shows that stocks with high borrow costs tend to be overvalued, and their subsequent returns are on average negative. Market makers also rely on securities lending to fulfil their obligation to provide liquidity, and central counterparties use it to manage settlement failures.
