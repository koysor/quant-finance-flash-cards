# Credit Loss Distribution

**Topic:** Banking Regulation
**Tags:** credit loss, unexpected loss, fat tail, correlation, credit portfolio
**Created:** 2026-04-13
**Author:** Claude Sonnet 4.6

---

## Definition

The credit loss distribution describes the probability of different loss levels from a loan portfolio over a fixed horizon (typically one year). Unlike market risk, which is approximately symmetric, the credit loss distribution is highly right-skewed: most years produce losses near the expected value, but the tail extends far to the right, representing catastrophic correlated defaults in a severe recession.

## Key Formula

For a portfolio of $n$ loans with correlation $\rho$, the portfolio loss $L$ has:

$$EL = \sum_i PD_i \cdot LGD_i \cdot EAD_i \qquad \text{(mean)}$$

$$UL = \text{VaR}_\alpha(L) - EL \qquad \text{(unexpected loss = capital)}$$

The skewness of the distribution increases with:
1. **Default correlation $\rho$:** Higher $\rho$ fattens the right tail
2. **Concentration:** Fewer, larger exposures (lower granularity) raise tail risk
3. **Low PD, high LGD:** Heavy tail from rare but severe defaults

Under the ASRF model with correlation $\rho$, the 99.9% conditional default rate is:

$$CDR_{99.9\%} = \Phi\!\left(\frac{\Phi^{-1}(PD) + \sqrt{\rho}\,\Phi^{-1}(0.999)}{\sqrt{1-\rho}}\right) \gg PD$$

## Example

A portfolio of 1,000 loans each with $PD = 1\%$, $LGD = 50\%$, $EAD = £1\text{m}$. The $EL = £5\text{m}$. With zero correlation (independent), the 99.9% loss is barely above EL (by the CLT). With $\rho = 0.20$, the 99.9% loss rises to approximately £45 m — nine times higher — because in a severe recession nearly all borrowers default together.

## Remember

The convex shape of the right tail means capital requirements grow non-linearly with correlation: doubling $\rho$ more than doubles the unexpected loss. This is the mechanism behind systemic credit crises — individual PDs may be low, but when correlation spikes in a recession, the credit loss distribution shifts dramatically to the right. It is also why Basel's IRB formula embeds a fixed $\rho$ schedule by asset class rather than letting banks estimate correlation freely: underestimating correlation produces falsely thin tails and catastrophically insufficient capital.
