# Independent Events

**Topic:** Probability
**Tags:** independence, independent events, multiplication rule, uncorrelated, joint probability
**Created:** 2026-04-11
**Author:** Claude Sonnet 4.6

---

## Definition

Two events $A$ and $B$ are **independent** if knowing that one occurred gives no information about whether the other occurred. The probability of both happening equals the product of their individual probabilities.

$$A \text{ and } B \text{ are independent} \iff P(A \cap B) = P(A)\,P(B)$$

Equivalently: $P(A \mid B) = P(A)$ and $P(B \mid A) = P(B)$ — conditioning on one does not change the other.

## Key Formula

**Multiplication rule for independent events:**

$$P(A \cap B) = P(A)\,P(B)$$

**Extended to $n$ mutually independent events:**

$$P(A_1 \cap A_2 \cap \cdots \cap A_n) = \prod_{i=1}^{n} P(A_i)$$

**Independence vs uncorrelated (for random variables):**

| Condition | Definition | Implies the other? |
|---|---|---|
| $X \perp\!\!\!\perp Y$ (independent) | $f_{X,Y} = f_X f_Y$ | Yes: independence $\Rightarrow$ $\text{Cov}=0$ |
| $\text{Cov}(X,Y) = 0$ (uncorrelated) | $E[XY] = E[X]E[Y]$ | No: uncorrelated $\not\Rightarrow$ independence |

## Example

Two bonds from different, unrelated sectors each have $P(D_i) = 3\%$. If defaults are independent:

$$P(D_1 \cap D_2) = 0.03 \times 0.03 = 0.09\%$$

If instead correlation $\rho = 0.4$ drives joint defaults, the probability rises substantially above 0.09% — the independence assumption materially underestimates joint tail risk.

During the 2008 financial crisis, mortgage defaults that were assumed to be largely independent turned out to be highly correlated, causing CDO tranches rated AAA to suffer catastrophic losses.

## Remember

Independence is the strongest form of "no relationship" between events — far stronger than zero correlation. In portfolio construction, true independence between assets would allow complete elimination of idiosyncratic risk. In credit risk, the independence assumption between obligors is convenient but dangerous: correlation can be low in normal markets and spike during crises, precisely when it matters most.
