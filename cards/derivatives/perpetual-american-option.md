# Perpetual American Option

**Topic:** Derivatives
**Tags:** perpetual American option, optimal stopping, smooth pasting, exercise boundary, closed form, ODE
**Created:** 2026-06-13
**Author:** Claude Sonnet 4.6

---

## Definition

A **perpetual American option** is an American option with no expiry date ($T \to \infty$). Because time-to-expiry is no longer a variable, the optimal exercise boundary $S^*$ is a **constant**, and the pricing problem reduces from a PDE to an ordinary differential equation (ODE). This gives a rare closed-form solution for an American-style contract, making the perpetual option the canonical worked example of the smooth pasting method.

## Key Formula

In the continuation region $S > S^*$ (for a put), the value $V(S)$ satisfies the time-independent Black-Scholes ODE:

$$\frac{1}{2}\sigma^2 S^2 V'' + rS V' - rV = 0$$

The general solution is $V(S) = AS^\alpha + BS^\beta$ where $\alpha > 0$ and $\beta < 0$ are roots of $\frac{1}{2}\sigma^2 x(x-1) + rx - r = 0$. Since $V \to 0$ as $S \to \infty$, only the negative root $\beta$ survives:

$$\beta = \frac{1}{2} - \frac{r}{\sigma^2} - \sqrt{\left(\frac{r}{\sigma^2} - \frac{1}{2}\right)^2 + \frac{2r}{\sigma^2}} < 0$$

**Smooth pasting** (value matching + derivative matching at $S^*$):

$$V(S^*) = K - S^* \quad \text{and} \quad V'(S^*) = -1$$

Solving jointly gives the **optimal exercise boundary**:

$$S^* = \frac{K\beta}{\beta - 1} = K \cdot \frac{\lvert\beta\rvert}{\lvert\beta\rvert + 1} < K$$

**Option value** for $S > S^*$:

$$V(S) = (K - S^*)\!\left(\frac{S}{S^*}\right)^{\!\beta}$$

## Example

Perpetual American put: $K = 100$, $r = 5\%$, $\sigma = 25\%$.

$$\beta = \frac{1}{2} - \frac{0.05}{0.03125} - \sqrt{\left(\frac{0.05}{0.03125} - \frac{1}{2}\right)^2 + \frac{0.10}{0.03125}} = 0.5 - 1.6 - \sqrt{1.21 + 3.2} = -1.1 - 2.1 = -3.2 \approx -3.2$$

More precisely, $\beta \approx -3.20$, so:

$$S^* = 100 \times \frac{3.20}{4.20} \approx \pounds76.19$$

$$V(100) = (100 - 76.19)\left(\frac{100}{76.19}\right)^{-3.20} \approx 23.81 \times 0.447 \approx \pounds10.64$$

At the boundary $V(76.19) = £23.81$, which exactly equals the intrinsic value $100 - 76.19 = £23.81$ ✓. The delta at $S^*$ is $\beta(K-S^*)/S^* = -3.20 \times 23.81/76.19 = -1.0$ ✓.

## Remember

The perpetual American put is the simplest problem where early exercise is genuinely optimal, and it has a completely explicit solution — unusual for American options. The exercise boundary $S^* = K|\beta|/(|\beta|+1)$ shows the two key drivers: higher volatility (more negative $\beta$) **raises** $S^*$ toward $K$, making early exercise less attractive because waiting preserves more option value; lower interest rate also raises $S^*$, since low $r$ reduces the cost of deferring the receipt of $K$. The ODE approach extends to real option problems (invest when NPV hits a threshold) and credit (restructure debt when firm value hits a floor), wherever the time-stationarity assumption makes $T = \infty$ a reasonable approximation.
