# Information Theory

**Topic:** Computational Finance
**Tags:** information theory, entropy, kl divergence, mutual information, shannon, uncertainty
**Created:** 2026-04-25
**Author:** Claude Sonnet 4.6

---

## Definition

**Information theory**, founded by Claude Shannon in 1948, provides a mathematical framework for quantifying uncertainty, information content, and the capacity to transmit or compress data. Its core idea is that learning a low-probability event carries more information than learning a high-probability one.

## Key Formula

**Self-information** (surprisal) of an event with probability $p$:

$$I(x) = -\log_2 p(x) \quad \text{(bits)}$$

**Shannon entropy** — expected information content of a distribution $P$:

$$H(P) = -\sum_x p(x) \log_2 p(x) = \mathbb{E}[-\log_2 p(X)]$$

**KL divergence** — how much distribution $Q$ diverges from a reference $P$:

$$D_{\text{KL}}(P \| Q) = \sum_x p(x) \log_2 \frac{p(x)}{q(x)} \geq 0$$

**Mutual information** — how much knowing $X$ reduces uncertainty about $Y$:

$$I(X; Y) = H(X) - H(X \mid Y) = \sum_{x,y} p(x,y)\log_2 \frac{p(x,y)}{p(x)p(y)}$$

## Example

Consider two asset return distributions over three outcomes (up, flat, down):

- $P$ (prior belief): $(0.5,\; 0.3,\; 0.2)$ — entropy $H(P) = 1.49$ bits
- $Q$ (post-earnings): $(0.1,\; 0.2,\; 0.7)$ — entropy $H(Q) = 1.16$ bits

$D_{\text{KL}}(Q \| P) = 0.1\log_2\frac{0.1}{0.5} + 0.2\log_2\frac{0.2}{0.3} + 0.7\log_2\frac{0.7}{0.2} = 1.03$ bits.

The KL divergence of $1.03$ bits represents the information surprise in the earnings announcement — how much the market must update its beliefs, directly linked to price impact.

## Remember

Information theory has three major applications in quantitative finance:

1. **KL divergence as model risk** — the distance between a risk-neutral pricing measure $Q$ and the physical measure $P$ quantifies how much the model's hedging assumptions differ from reality; maximum-entropy methods use this to choose the least-presumptuous pricing measure consistent with observed market prices.

2. **Mutual information as non-linear correlation** — unlike Pearson correlation, mutual information $I(X;Y)$ captures any statistical dependence between two variables, not just linear. It is used to detect non-linear relationships between alpha signals and forward returns that correlation matrices miss.

3. **Kelly criterion and entropy growth** — the Kelly fraction maximises the expected log-return, which equals the entropy growth rate of the bettor's wealth process. Trading at the Kelly fraction is equivalent to maximising information-theoretic efficiency of capital allocation.
