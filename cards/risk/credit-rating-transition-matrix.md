# Credit Rating Transition Matrix

**Topic:** Risk
**Tags:** transition matrix, credit rating, default probability, migration risk, markov chain, credit risk
**Created:** 2026-06-15
**Author:** Claude Sonnet 4.6

---

## Definition

A **credit rating transition matrix** gives the probability that a bond issuer migrates from one credit rating to another (or defaults) over a fixed horizon, typically one year. It is estimated from historical rating data by rating agencies and models the dynamics of credit quality as a Markov chain.

## Key Formula

The one-year transition matrix $\mathbf{P}$ has entries $p_{ij}$ = probability of moving from rating $i$ to rating $j$:

$$\mathbf{P} = \begin{pmatrix} p_{\text{AAA}\to\text{AAA}} & p_{\text{AAA}\to\text{AA}} & \cdots & p_{\text{AAA}\to D} \\ p_{\text{AA}\to\text{AAA}} & p_{\text{AA}\to\text{AA}} & \cdots & p_{\text{AA}\to D} \\ \vdots & & \ddots & \vdots \\ 0 & 0 & \cdots & 1 \end{pmatrix}$$

Default is an **absorbing state**: $p_{D\to D} = 1$. Each row sums to 1.

For multi-period default probabilities, raise the matrix to the $n$-th power:

$$\mathbf{P}^{(n)} = \mathbf{P}^n$$

The continuous-time equivalent uses a **generator matrix** $\mathbf{G}$ where $\mathbf{P}(\Delta t) = e^{\mathbf{G}\Delta t}$.

## Example

A simplified 3-rating system (Investment Grade IG, High Yield HY, Default D):

$$\mathbf{P} = \begin{pmatrix} 0.92 & 0.07 & 0.01 \\ 0.05 & 0.88 & 0.07 \\ 0.00 & 0.00 & 1.00 \end{pmatrix}$$

A BBB-rated issuer (approximated as IG) has a 1% one-year default probability. Over two years, the 2-step probability of defaulting is approximately $1\% + 0.92\% = 1.92\%$ — obtained from $\mathbf{P}^2$.

## Remember

Transition matrices are central to **CVA** (Credit Valuation Adjustment) calculation: when pricing the counterparty credit risk on a derivatives portfolio, the bank must model how the counterparty's credit quality evolves over the life of the trade, not just whether it defaults. Basel II's Internal Ratings-Based (IRB) approach requires banks to estimate one-year PDs by rating grade — effectively the last column of the transition matrix — and to stress-test how those PDs rise in a downturn. The key risk transition matrices fail to capture is **ratings momentum**: issuers that were recently downgraded are more likely to be downgraded again than the Markov property implies.
