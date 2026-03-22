# Margin Lending Rate

**Topic:** Short Selling
**Tags:** margin lending rate, leverage, borrowing cost, prime broker, interest rate
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

The margin lending rate is the interest rate charged by a broker or prime broker on funds borrowed to purchase securities on margin. It is typically quoted as a benchmark rate (such as SOFR or the broker's base rate) plus a spread that depends on the loan size, client relationship, and collateral quality. The margin lending rate is a direct cost of leverage and must be exceeded by the portfolio's return for the leveraged strategy to be profitable.

## Key Formula

The **interest cost** on a margin loan:

$$C_{\text{margin}} = L \times (r_{\text{base}} + s) \times \frac{t}{360}$$

where $L$ is the loan amount, $r_{\text{base}}$ is the benchmark rate, $s$ is the broker's spread, and $t$ is the number of days.

The **leveraged return** net of borrowing costs:

$$R_{\text{leveraged}} = R_{\text{portfolio}} + \frac{L}{E} \times \bigl(R_{\text{portfolio}} - r_{\text{margin}}\bigr)$$

where $E$ is the investor's equity and $r_{\text{margin}} = r_{\text{base}} + s$ is the annualised margin rate. Leverage amplifies returns only when $R_{\text{portfolio}} > r_{\text{margin}}$.

## Example

A trader has £200,000 in equity and borrows £300,000 at a margin lending rate of SOFR (4.80%) + 0.50% = 5.30%. The total portfolio of £500,000 returns 8% over one year.

$$C_{\text{margin}} = £300{,}000 \times 0.053 \times 1 = £15{,}900$$

Portfolio gain: $£500{,}000 \times 0.08 = £40{,}000$

Net profit: $£40{,}000 - £15{,}900 = £24{,}100$

Return on equity: $\frac{£24{,}100}{£200{,}000} = 12.05\%$

Without leverage the return would have been 8%. Leverage added 4.05 percentage points, but if the portfolio had returned only 4%, the leveraged return on equity would be:

$$R = 0.04 + \frac{300{,}000}{200{,}000} \times (0.04 - 0.053) = 0.04 - 0.0195 = 2.05\%$$

Leverage would have destroyed value because the portfolio return was below the borrowing cost.

## Remember

The margin lending rate is the hurdle rate for any leveraged strategy — if your expected return does not exceed it, leverage destroys rather than creates value. In quantitative finance, this rate directly affects optimal portfolio construction: the two-fund separation theorem assumes borrowing at the risk-free rate, but in practice the margin rate includes a spread that shifts the efficient frontier and reduces the attractiveness of leverage. During market stress, brokers can raise margin rates or reduce credit lines, forcing deleveraging at precisely the worst time.
