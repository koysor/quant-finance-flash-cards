# Integral

**Topic:** Calculus
**Tags:** integration, area under curve, accumulation, definite integral, antiderivative
**Created:** 2026-04-05
**Author:** Claude Sonnet 4.6

---

## Definition

An **integral** is a mathematical operation that measures the total accumulated quantity described by a function over an interval. The **definite integral** $\int_a^b f(x)\,dx$ gives the net signed area between the curve $y = f(x)$ and the $x$-axis from $x = a$ to $x = b$. The **indefinite integral** $\int f(x)\,dx = F(x) + C$ finds all antiderivatives of $f$ — functions whose derivative equals $f$.

## Key Formula

**Definite integral** (net signed area / total accumulation):

$$\int_a^b f(x)\,dx = \lim_{n \to \infty} \sum_{i=1}^{n} f(x_i^*)\,\Delta x$$

where $\Delta x = \frac{b-a}{n}$ and $x_i^*$ is any sample point in the $i$-th sub-interval.

**Indefinite integral** (family of antiderivatives):

$$\int f(x)\,dx = F(x) + C, \qquad \text{where } F'(x) = f(x)$$

**Key properties** (linearity):

$$\int_a^b \bigl[\alpha f(x) + \beta g(x)\bigr]\,dx = \alpha\int_a^b f(x)\,dx + \beta\int_a^b g(x)\,dx$$

## Example

A continuous cash flow pays at rate $c(t) = 1000\,e^{0.05t}$ pounds per year. Find the total cash received over the first 3 years.

$$\int_0^3 1000\,e^{0.05t}\,dt = 1000 \left[\frac{e^{0.05t}}{0.05}\right]_0^3 = 20{,}000\bigl(e^{0.15} - 1\bigr) \approx 20{,}000 \times 0.1618 \approx \pounds3{,}236$$

The integral accumulates the cash flow over the interval, just as a sum accumulates discrete payments.

## Remember

The integral is the fundamental tool for converting a **rate** into a **total**. In quantitative finance: the probability density function integrated over a range gives a probability; a continuously paying dividend rate integrated over time gives total dividends; and the discounted payoff density integrated over all terminal stock prices gives an option value. Whenever you see a continuous process in finance, its total effect over time is an integral.
