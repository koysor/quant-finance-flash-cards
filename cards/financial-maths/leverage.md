# Leverage

**Topic:** Financial Mathematics
**Tags:** leverage, borrowing, margin, risk, amplification, portfolio management
**Created:** 2026-03-07
**Author:** Claude Opus 4.6

---

## Definition

Financial leverage is the use of borrowed capital to increase the size of an investment position beyond what the investor's own equity would allow. It amplifies both gains and losses proportionally, making it a powerful but dangerous tool in portfolio management.

## Key Formula

The **leveraged return** for a portfolio funded partly by borrowing at rate $R_f$ is:

$$R_{\text{lev}} = L \cdot R_u - (L - 1) \cdot R_f$$

where $L = \frac{\text{Total Assets}}{\text{Equity}}$ is the leverage ratio and $R_u$ is the unlevered return.

The **leveraged volatility** scales linearly:

$$\sigma_{\text{lev}} = L \cdot \sigma_u$$

## Example

An investor has £50,000 of equity and borrows £100,000 at 4% per annum, giving a leverage ratio of $L = \frac{150{,}000}{50{,}000} = 3$. If the unlevered portfolio returns 8%:

$$R_{\text{lev}} = 3 \times 0.08 - (3 - 1) \times 0.04 = 0.24 - 0.08 = 0.16$$

The leveraged return is 16%. But if the unlevered return is $-5\%$:

$$R_{\text{lev}} = 3 \times (-0.05) - 2 \times 0.04 = -0.15 - 0.08 = -0.23$$

A modest 5% loss becomes a 23% loss — nearly half the equity is wiped out.

## Remember

Leverage is the mechanism through which hedge funds, banks, and proprietary trading desks amplify returns — but it also amplifies Value at Risk by the same factor. Crucially, leverage does **not** improve the Sharpe ratio — it stretches both excess return and volatility by the same factor $L$. The 2008 financial crisis demonstrated that institutions running leverage ratios of 30:1 or more had almost no margin for error. Understanding the linear scaling of both return and volatility with leverage is essential for any quantitative risk assessment.
