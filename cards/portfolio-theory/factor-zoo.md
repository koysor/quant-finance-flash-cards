# Factor Zoo

**Topic:** Portfolio Theory & Asset Pricing
**Tags:** factor zoo, Fama-French, Carhart, momentum, liquidity, anomalies
**Created:** 2026-04-11
**Author:** Claude Sonnet 4.6

---

## Definition

The **factor zoo** refers to the proliferation of hundreds of factors — beyond the market beta — that researchers have claimed explain cross-sectional differences in expected returns. Each factor represents a systematic risk or behavioural anomaly that the market supposedly prices.

## Key Formula

**Fama-French 3-factor model (1993):**

$$r_i = R_F + \beta_M(r_M - R_F) + \beta_{SMB}\cdot SMB + \beta_{HML}\cdot HML + \varepsilon_i$$

| Factor | Name | Captures |
|---|---|---|
| $r_M - R_F$ | Market premium | Systematic market risk |
| $SMB$ | Small-Minus-Big | Size effect: small caps historically outperform |
| $HML$ | High-Minus-Low | Value effect: high book-to-market stocks outperform |

**Carhart 4-factor (1997):** adds $\beta_{MOM} \cdot MOM$ (past winners minus losers, 12-month momentum)

**Pastor-Stambaugh (2003):** adds $\beta_{LP} \cdot LP$ (illiquid stocks earn a liquidity premium)

## Example

A fund with $\beta_M = 0.9$, $\beta_{SMB} = 0.4$, $\beta_{HML} = 0.2$, $\beta_{MOM} = 0.1$. If market premium = 6%, SMB = 2%, HML = 3%, MOM = 4%: expected excess return = $0.9(6) + 0.4(2) + 0.2(3) + 0.1(4) = 5.4 + 0.8 + 0.6 + 0.4 = 7.2\%$. A manager earning 8% has alpha of only 0.8% once factor exposures are stripped out.

## Remember

The factor zoo matters for performance attribution: what looks like alpha may be undisclosed beta to a known factor. Many published factors fail to replicate out-of-sample or post-publication — a combination of data mining, p-hacking, and the market learning about the anomaly. The practical question for a portfolio manager is whether the factor premium is robust, investable after costs, and not simply a disguised exposure to an already-known risk.
