# Poisson Process

**Topic:** Stochastic Processes
**Tags:** poisson process, counting process, inter-arrival time, jump process, memoryless, intensity
**Created:** 2026-06-06
**Author:** Claude Sonnet 4.6

---

## Definition

A **Poisson process** $N(t)$ is a continuous-time counting process that models the number of random events occurring by time $t$, where events arrive at a constant average rate $\lambda > 0$ (the **intensity**), independently of when previous events occurred. It is the continuous-time analogue of a sequence of independent Bernoulli trials, and is characterised by three properties: $N(0) = 0$; increments over non-overlapping intervals are independent; and the number of events in any interval of length $s$ follows a Poisson distribution with mean $\lambda s$.

## Key Formula

**Number of arrivals** in $[0, t]$:

$$P(N(t) = k) = \frac{e^{-\lambda t}\,(\lambda t)^k}{k!}, \qquad k = 0, 1, 2, \ldots$$

**Expected arrivals** and variance: $\mathbb{E}[N(t)] = \lambda t$, $\operatorname{Var}(N(t)) = \lambda t$.

**Inter-arrival times** — the waiting time $T_n$ between the $(n-1)$-th and $n$-th event:

$$T_n \sim \operatorname{Exp}(\lambda), \qquad P(T_n > t) = e^{-\lambda t}$$

The **memoryless property**: $P(T_n > s + t \mid T_n > s) = P(T_n > t)$ — the probability of waiting at least another $t$ units is the same regardless of how long you have already waited.

## Example

A credit desk models bond defaults using a Poisson process with intensity $\lambda = 0.03$ per year (a 3% annual default rate).

**Probability of no default in 5 years:**
$$P(N(5) = 0) = e^{-0.03 \times 5} = e^{-0.15} \approx 85.9\%$$

**Expected number of defaults in 10 years:** $\lambda t = 0.03 \times 10 = 0.3$ defaults.

**Probability of exactly 2 defaults in 10 years:**
$$P(N(10) = 2) = \frac{e^{-0.3}(0.3)^2}{2!} = \frac{0.7408 \times 0.09}{2} \approx 3.3\%$$

**Mean waiting time until the first default:** $1/\lambda = 1/0.03 \approx 33.3$ years.

## Remember

The Poisson process is the simplest model for **jump arrivals** in finance: it is the jump-counting backbone inside Merton's jump-diffusion model, the arrival process for defaults in credit risk, and the event generator in operational risk loss models. Its key practical limitation is the **constant intensity** $\lambda$ — real default rates vary over time (clustering during recessions) and real order arrivals accelerate near market close. This motivates extensions such as the **Cox process** (doubly stochastic Poisson process), where $\lambda$ is itself a stochastic process, and the **Hawkes process**, where each event temporarily raises the rate of future events. Whenever you see "$N(t)$" in a derivatives or credit model, you are looking at a Poisson process or one of these extensions.
