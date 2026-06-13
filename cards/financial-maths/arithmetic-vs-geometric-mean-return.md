# Arithmetic vs Geometric Mean Return

**Topic:** Financial Mathematics
**Tags:** arithmetic mean, geometric mean, compounding, volatility drag, long-run returns, portfolio
**Created:** 2026-06-13
**Author:** Claude Sonnet 4.6

---

## Definition

The **arithmetic mean return** $\bar{r}$ is the simple average of periodic returns and is the correct measure for the expected return in a single period. The **geometric mean return** $g$ is the constant per-period rate that produces the same terminal wealth as the actual sequence of returns and is the correct measure for the growth rate of wealth over multiple periods. The two are related by the **volatility drag**: $g \approx \bar{r} - \tfrac{1}{2}\sigma^2$, where $\sigma^2$ is the variance of returns.

## Key Formula

For $n$ periodic returns $r_1, r_2, \ldots, r_n$:

$$\bar{r} = \frac{1}{n}\sum_{i=1}^n r_i \qquad \text{(arithmetic mean)}$$

$$g = \left(\prod_{i=1}^n (1 + r_i)\right)^{1/n} - 1 \qquad \text{(geometric mean)}$$

**Volatility drag identity** (exact in continuous time under GBM):

$$g = \mu - \tfrac{1}{2}\sigma^2$$

where $\mu$ is the arithmetic mean return (the drift parameter in GBM) and $\sigma^2$ is the variance of log returns. Terminal wealth over $T$ years satisfies:

$$E[W_T] = W_0\, e^{\mu T} \qquad \text{but} \qquad \text{median}(W_T) = W_0\, e^{(\mu - \tfrac{1}{2}\sigma^2) T}$$

The mean is inflated by the right tail of the lognormal; the median (the typical outcome) grows at the geometric rate.

## Example

A fund reports an arithmetic mean annual return of 12% with annual volatility $\sigma = 30\%$.

$$g \approx 12\% - \tfrac{1}{2}(0.30)^2 = 12\% - 4.5\% = 7.5\%\ \text{p.a.}$$

Over 20 years, £10,000 grows to:
- **Arithmetic projection** (compounded at $\bar{r}$): $10{,}000 \times e^{0.12 \times 20} \approx £110{,}232$
- **Geometric (median) wealth**: $10{,}000 \times e^{0.075 \times 20} \approx £44{,}817$

The arithmetic projection overstates the typical outcome by a factor of 2.5. An investor who locks in 7.5% annually on £10,000 ends with the same £44,817 — this is what the geometric mean captures.

## Remember

Volatility drag is one of the most practically important results in investment management and one of the most commonly misunderstood. Fund fact sheets typically quote arithmetic mean returns (higher), whilst long-horizon wealth projections should use the geometric mean (lower by $\tfrac{1}{2}\sigma^2$). A leveraged ETF that rebalances daily to 2× exposure amplifies both $\mu$ and $\sigma$: the arithmetic return doubles, but the variance quadruples, so the volatility drag grows from $\tfrac{1}{2}\sigma^2$ to $\tfrac{1}{2}(2\sigma)^2 = 2\sigma^2$. For a volatile underlying ($\sigma = 25\%$), the annual drag on a 2× ETF is $2 \times 0.0625 = 12.5\%$ p.a. — enough to produce negative geometric returns even when the underlying is flat-to-positive.
