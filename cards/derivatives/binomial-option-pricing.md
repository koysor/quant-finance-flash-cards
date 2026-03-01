# Binomial Option Pricing Model

**Topic:** Derivatives
**Tags:** binomial tree, option pricing, risk-neutral probability, no-arbitrage, CQF, numerical methods

---

## Definition

The **binomial option pricing model** values options by discretising time into $N$ steps of length $\delta t$ and assuming that at each step the stock price either rises by a factor $u$ or falls by a factor $v$ (sometimes written $d$). This two-state framework is the simplest no-arbitrage pricing model and the natural discrete-time counterpart of Black-Scholes.

At each node the option value is obtained by forming a riskless hedge and discounting at the risk-free rate, which is equivalent to taking a risk-neutral expectation. Because the tree **recombines** (an up followed by a down returns to the same price as a down followed by an up), an $N$-step tree has only $N + 1$ terminal nodes rather than $2^N$, making computation tractable.

## Key Formula

**Up and down factors** (moment-matched to the continuous-time volatility $\sigma$):

$$u = 1 + \sigma\sqrt{\delta t}, \qquad v = 1 - \sigma\sqrt{\delta t}$$

**Risk-neutral probability** of an up move:

$$p' = \frac{(1 + r\delta t) - v}{u - v} = \frac{r\delta t + \sigma\sqrt{\delta t}}{2\sigma\sqrt{\delta t}}$$

**One-step pricing formula** — the option value $V$ one step before expiry:

$$V = \frac{1}{1 + r\delta t}\left[p' V^{+} + (1 - p') V^{-}\right]$$

where $V^{+}$ and $V^{-}$ are the option values in the up and down states respectively. This formula is applied recursively (backward induction) from the terminal payoffs to time zero.

**Terminal payoff** at node $j$ after $N$ steps (for a call with strike $K$):

$$V_j = \max\!\left(S_0 \, u^{j} \, v^{N-j} - K,\; 0\right), \qquad j = 0, 1, \ldots, N$$

## Example

A stock trades at $S_0 = \text{£}100$, with $\sigma = 20\%$, $r = 5\%$, and $T = 1$ year. Use a **one-step** tree ($N = 1$, $\delta t = 1$).

1. Compute the factors: $u = 1 + 0.20 \times 1 = 1.20$, $\; v = 1 - 0.20 \times 1 = 0.80$.
2. Stock prices at expiry: $S^{+} = 120$, $\; S^{-} = 80$.
3. Risk-neutral probability: $p' = \frac{1.05 - 0.80}{1.20 - 0.80} = \frac{0.25}{0.40} = 0.625$.
4. Call payoffs ($K = 100$): $V^{+} = 20$, $\; V^{-} = 0$.
5. Present value:

$$V = \frac{1}{1.05}\left(0.625 \times 20 + 0.375 \times 0\right) = \frac{12.50}{1.05} \approx \textbf{£11.90}$$

Adding more steps (e.g. $N = 100$) gives a value that converges towards the Black-Scholes price.

## Remember

- The binomial model is the **simplest demonstration of risk-neutral pricing**: the real-world probability of the stock going up never appears in the formula — only $p'$ does.
- Because the tree recombines, pricing an $N$-step European option requires evaluating only $N + 1$ terminal payoffs and working backwards, giving $O(N^2)$ complexity rather than $O(2^N)$.
- For **American options**, backward induction naturally accommodates early exercise: at each node, compare the continuation value with the immediate exercise value and take the maximum.
- As $N \to \infty$ (equivalently $\delta t \to 0$), the binomial model converges to the **Black-Scholes** continuous-time limit — this is the Cox-Ross-Rubinstein result.
