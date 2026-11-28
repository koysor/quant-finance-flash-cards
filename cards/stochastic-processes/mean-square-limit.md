# Mean Square Limit

**Topic:** Stochastic Processes
**Tags:** mean square convergence, stochastic integral, quadratic variation, l2 convergence, hedging error
**Created:** 2026-11-28
**Author:** Claude Opus 5.5

---

## Definition

A sequence of random variables $X_n$ has **mean square limit** $X$ if the expected squared distance between them shrinks to zero. This is the sense in which stochastic calculus defines its integrals and identities such as $dW^2 = dt$. It does not say every path converges, only that the typical error, measured by its root mean square, vanishes.

## Key Formula

$$\underset{n \to \infty}{\text{ms-lim}}\; X_n = X \quad\Longleftrightarrow\quad \lim_{n \to \infty} \mathbb{E}\bigl[(X_n - X)^2\bigr] = 0$$

The Itô integral is defined this way, as the mean square limit of sums that use the **left-hand** endpoint of each interval:

$$\int_0^t f(W_s)\,dW_s = \underset{n \to \infty}{\text{ms-lim}} \sum_{j=1}^{n} f(W_{t_{j-1}})\,\bigl(W_{t_j} - W_{t_{j-1}}\bigr)$$

For the sum of squared Brownian increments over $n$ equal steps on $[0, t]$:

$$\mathbb{E}\Bigl[\Bigl(\sum_{j=1}^{n} (\Delta W_j)^2 - t\Bigr)^2\Bigr] = \frac{2t^2}{n} \;\to\; 0$$

so $\sum (\Delta W_j)^2$ has mean square limit $t$, which is the precise meaning of $dW^2 = dt$.

## Example

Take $t = 1$. Each $(\Delta W_j)^2$ has mean $1/n$ and variance $2/n^2$, and the $n$ terms are independent, so the sum has mean $1$ and variance $2/n$.

| Steps $n$ | Mean square error $2/n$ | RMS error $\sqrt{2/n}$ |
|---|---|---|
| 100 | 0.02 | 0.141 |
| 10,000 | 0.0002 | 0.0141 |

A hundred times more steps cuts the typical error by a factor of 10, and in the limit the sum equals $1$ exactly in mean square.

## Remember

Mean square error is how a trader measures **discrete hedging error**. A delta hedge rebalanced $n$ times over the option's life leaves a P&L error whose mean square shrinks like $1/n$, the same scaling as $\sum(\Delta W)^2$ above. So the error's standard deviation falls only like $1/\sqrt{n}$: rebalancing four times as often only halves the hedging error, while transaction costs grow fourfold. A closely related yardstick, the expected path error, defines the **strong convergence** order of simulation schemes such as Euler-Maruyama. It tells you how closely simulated paths track the true ones, which matters for path-dependent payoffs.
