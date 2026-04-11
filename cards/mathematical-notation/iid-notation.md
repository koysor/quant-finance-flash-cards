# i.i.d. Notation

**Topic:** Mathematical Notation
**Tags:** notation, iid, sample, independent, identically distributed
**Created:** 2026-04-11
**Author:** Claude Sonnet 4.6

---

## Definition

The abbreviation **i.i.d.** (independently and identically distributed) describes a sequence of random variables that are mutually independent and all share the same probability distribution. It is the standard assumption for a random sample.

| Symbol | Read as | Meaning |
|---|---|---|
| $X_1, \ldots, X_n \overset{\text{iid}}{\sim} F$ | "X1 to Xn i.i.d. from F" | Each $X_i$ has distribution $F$; all are mutually independent |
| $X_i \overset{\text{iid}}{\sim} \mathcal{N}(\mu, \sigma^2)$ | "X i i.i.d. normal" | All $X_i$ are independent standard normal random variables |
| $\{X_i\}_{i=1}^{n}$ | "the sequence X1 to Xn" | An indexed sample of $n$ random variables |
| $x_1, \ldots, x_n$ | "the observed values" | Realisations — actual numbers after sampling |
| $n$ | "sample size" | The number of observations |
| $X_{(i)}$ | "i-th order statistic" | The $i$-th smallest value in the sample (see order statistics notation) |

## Key Formula

**i.i.d. sample statistics:**

$$\bar{X} = \frac{1}{n}\sum_{i=1}^n X_i \qquad \text{(sample mean)}$$

$$S^2 = \frac{1}{n-1}\sum_{i=1}^n (X_i - \bar{X})^2 \qquad \text{(unbiased sample variance)}$$

**Joint density of an i.i.d. sample** (factorises because of independence):

$$f_{X_1,\ldots,X_n}(x_1,\ldots,x_n) = \prod_{i=1}^{n} f(x_i)$$

## Example

Assume daily log-returns $R_1, \ldots, R_{252} \overset{\text{iid}}{\sim} \mathcal{N}(\mu, \sigma^2)$. The sample mean $\bar{R}$ estimates $\mu$; the sample standard deviation $S$ estimates $\sigma$. The CLT then gives $\sqrt{252}(\bar{R} - \mu)/\sigma \to \mathcal{N}(0,1)$ — the justification for annualising volatility by multiplying by $\sqrt{252}$.

## Remember

The i.i.d. assumption is ubiquitous in statistics but rarely holds exactly in finance. Return series exhibit volatility clustering (variance changes over time), autocorrelation (past returns predict future ones), and fat tails — all violations of i.i.d. normality. Monte Carlo simulations often assume i.i.d. draws for tractability; the i.i.d. notation signals where this simplifying assumption is being used.
