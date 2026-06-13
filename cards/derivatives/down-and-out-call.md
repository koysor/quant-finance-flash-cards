# Down-and-Out Call Option

**Topic:** Derivatives
**Tags:** down-and-out call, barrier option, knock-out, reflection principle, exotic options, structured products
**Created:** 2026-06-13
**Author:** Claude Sonnet 4.6

---

## Definition

A **down-and-out call** (DOC) is a barrier call option that expires worthless if the underlying price ever falls to or below a knock-out barrier $B < S_0$ during the option's life. If the barrier is never touched, it pays the standard call payoff $\max(S_T - K, 0)$ at maturity. It is cheaper than a vanilla call because paths that fall to $B$ — which would be painful for the hedger — eliminate the option entirely.

## Key Formula

The DOC payoff ($B < \min(S_0, K)$):

$$\Pi_{\text{DOC}} = \max(S_T - K,\; 0)\cdot\mathbf{1}\!\left\{\min_{0 \leq t \leq T} S_t > B\right\}$$

Under GBM with continuous monitoring, the closed-form price via the **reflection principle** is:

$$C_{\text{DOC}} = C_{\text{BS}}(S_0, K) - \left(\frac{B}{S_0}\right)^{2\lambda - 2} C_{\text{BS}}\!\left(\frac{B^2}{S_0},\, K\right)$$

where $\lambda = (r + \tfrac{1}{2}\sigma^2)/\sigma^2$ and $B^2/S_0$ is the **reflected spot** — the image of $S_0$ around the barrier in log-space. In-out parity gives the companion price for free: $C_{\text{DIC}} = C_{\text{BS}} - C_{\text{DOC}}$.

## Example

$S_0 = 100$, $K = 100$ (ATM), $B = 90$ (10% below spot), $r = 5\%$, $\sigma = 20\%$, $T = 1$ year.

$$\lambda = \frac{0.05 + 0.02}{0.04} = 1.75, \qquad 2\lambda - 2 = 1.5$$

$$\left(\frac{90}{100}\right)^{1.5} \approx 0.854, \qquad \frac{B^2}{S_0} = \frac{8{,}100}{100} = 81$$

$$C_{\text{BS}}(100, 100) \approx \pounds10.45 \quad\text{(ATM vanilla)}$$
$$C_{\text{BS}}(81, 100) \approx \pounds2.09 \quad\text{(deep OTM call at reflected spot)}$$

$$C_{\text{DOC}} \approx 10.45 - 0.854 \times 2.09 \approx \pounds8.65$$

The DOC costs about 17% less than the vanilla — the discount is the market price of the knock-out risk.

## Remember

The DOC is the most commonly issued barrier option in equity structured products. Banks embed it when building capital-protected participation notes for retail investors: the client gets upside on an equity index via a DOC, with the barrier typically set at 70–80% of the initial index level. The lower option cost makes the note cheaper to produce, and the structure is marketed as "protected upside unless markets collapse." The formula reveals a direct connection to static hedging: at zero rates, $C_{\text{DOC}} = C_{\text{BS}}(S_0, K) - (S_0/B)\cdot C_{\text{BS}}(B^2/S_0, K)$, which is precisely the static replicating portfolio — the pricing formula and the hedge are the same expression.
