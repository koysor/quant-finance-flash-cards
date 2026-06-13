# Bivariate Normal Distribution

**Topic:** Probability
**Tags:** bivariate normal, joint distribution, correlation, compound options, Geske formula, CDF
**Created:** 2026-06-13
**Author:** Claude Sonnet 4.6

---

## Definition

The **bivariate normal distribution** is the joint distribution of two correlated standard normal random variables $(X, Y)$ with correlation $\rho \in (-1, 1)$. Its key object in option pricing is the **bivariate normal CDF**:

$$N_2(a, b;\, \rho) = \Pr(X \leq a,\; Y \leq b)$$

which gives the probability that both $X \leq a$ and $Y \leq b$ simultaneously. When $\rho = 0$, independence means $N_2(a, b; 0) = N(a)\,N(b)$. The bivariate normal arises whenever an option's payoff depends on the joint behaviour of a stock at two separate dates — a feature that appears in compound options, spread options, and dual-trigger instruments.

## Key Formula

**Joint PDF** of $(X, Y) \sim \mathcal{N}_2(\mathbf{0}, \Sigma)$ with $\Sigma = \bigl[\begin{smallmatrix}1 & \rho \\ \rho & 1\end{smallmatrix}\bigr]$:

$$f(x, y) = \frac{1}{2\pi\sqrt{1-\rho^2}} \exp\!\left(-\frac{x^2 - 2\rho xy + y^2}{2(1-\rho^2)}\right)$$

**Conditioning identity** (used to derive Geske's formula):

$$N_2(a, b;\, \rho) = \int_{-\infty}^{a} N\!\left(\frac{b - \rho x}{\sqrt{1-\rho^2}}\right) \phi(x)\, dx$$

where $\phi(x) = \frac{1}{\sqrt{2\pi}}e^{-x^2/2}$ is the standard normal PDF.

**Geske (1979) call-on-call** with outer strike $X$, outer expiry $T_1 < T_2$, inner strike $K$:

$$C_{\text{CoC}} = S_0\, N_2(b_1, a_1;\, \rho) - K e^{-rT_2} N_2(b_2, a_2;\, \rho) - X e^{-rT_1} N(b_2)$$

where $\rho = \sqrt{T_1/T_2}$, and $b_i$, $a_i$ are Black-Scholes arguments evaluated at the critical stock price $S^*$.

## Example

A compound option has $T_1 = 0.25$ yr, $T_2 = 0.75$ yr, so $\rho = \sqrt{0.25/0.75} = \sqrt{1/3} \approx 0.577$.

Suppose the risk-neutral joint probability that the stock exceeds both the outer threshold at $T_1$ and the inner strike at $T_2$ is needed. With $b_1 = 0.30$, $a_1 = 0.45$:

$$N_2(0.30, 0.45;\, 0.577) \approx 0.279$$

compared with the independence bound $N(0.30)\,N(0.45) \approx 0.618 \times 0.674 \approx 0.417$. The positive correlation ($\rho > 0$) means the events are positively linked but independence overstates the joint probability; the bivariate formula gives the correct value.

## Remember

$N_2$ appears whenever the pricing problem conditions on the asset level at two future dates. In the **Geske compound option**, the first date is when the outer option expires (and the holder decides whether to pay $X$ for the inner option); the second is when the inner option expires. Because the same Brownian motion drives the stock to both dates, the two events are correlated with $\rho = \sqrt{T_1/T_2}$ — a number that encodes how much information the first date conveys about the second. In practice $N_2$ has no closed form and is computed via numerical quadrature; most option pricing libraries include a fast Drezner (1978) approximation accurate to $10^{-7}$.
