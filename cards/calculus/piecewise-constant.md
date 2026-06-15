# Piecewise Constant

**Topic:** Calculus
**Tags:** piecewise constant, step function, interpolation, bootstrapping, hazard rate
**Created:** 2026-06-15
**Author:** Claude Sonnet 4.6

---

## Definition

A **piecewise constant** function (also called a **step function**) takes a single, unchanging value on each interval of its domain. The function is constant within each piece and may jump discontinuously at the breakpoints between intervals.

## Key Formula

$$f(t) = c_i \quad \text{for } t_{i-1} \leq t < t_i, \quad i = 1, 2, \ldots, n$$

where $t_0 < t_1 < \cdots < t_n$ are the **breakpoints** and $c_i$ is the constant value on the $i$-th interval.

The integral is piecewise **linear** — a sum of rectangular strips:

$$\int_0^T f(t)\,dt = \sum_{i: t_i \leq T} c_i\,(t_i - t_{i-1}) + c_k\,(T - t_{k-1})$$

where $t_{k-1} \leq T < t_k$.

## Example

A hazard rate $\lambda(t)$ is bootstrapped piecewise constant across three maturity buckets:

$$\lambda(t) = \begin{cases} 0.02 & 0 \leq t < 1 \\ 0.04 & 1 \leq t < 3 \\ 0.06 & 3 \leq t \leq 5 \end{cases}$$

The survival probability to $T = 3$ is:

$$S(3) = e^{-\int_0^3 \lambda(t)\,dt} = e^{-(0.02 \times 1\; +\; 0.04 \times 2)} = e^{-0.10} \approx 0.905$$

## Remember

In yield curve bootstrapping, instantaneous forward rates are assumed piecewise constant between quoted maturities. Each breakpoint value is solved sequentially so the model exactly reprices the corresponding benchmark instrument — a closed-form strip rather than a global optimisation. The same logic applies to CDS curve bootstrapping (piecewise constant hazard rates) and to Hull–White calibration where the mean-reversion level $\theta(t)$ is chosen piecewise constant to fit market swaption prices one maturity at a time.
