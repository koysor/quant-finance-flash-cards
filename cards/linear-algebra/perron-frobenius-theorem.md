# Perron–Frobenius Theorem

**Topic:** Linear Algebra
**Tags:** perron-frobenius, eigenvalue, stochastic matrix, stationary distribution, markov chain, spectral gap
**Created:** 2026-06-15
**Author:** Claude Sonnet 4.6

---

## Definition

The **Perron–Frobenius theorem** states that an irreducible non-negative matrix $A$ has a unique largest real eigenvalue $\lambda_1 > 0$ (the **Perron root**) with a corresponding eigenvector of all strictly positive entries. For a **stochastic matrix** (row sums equal 1), $\lambda_1 = 1$ exactly, and the positive left eigenvector is the unique stationary distribution $\pi$.

## Key Formula

For an irreducible stochastic matrix $P$ (a Markov chain transition matrix with all entries $\geq 0$ and all row sums $= 1$):

$$\pi P = \pi, \qquad \pi_i > 0\ \forall i, \qquad \sum_i \pi_i = 1$$

The eigenvalues satisfy $1 = \lambda_1 > |\lambda_2| \geq |\lambda_3| \geq \cdots$. The **spectral gap** $\delta = 1 - |\lambda_2|$ governs how fast the chain forgets its starting state:

$$\|P^n \mathbf{p}_0 - \pi\|_{\mathrm{TV}} \leq C \cdot |\lambda_2|^n$$

for any starting distribution $\mathbf{p}_0$.

## Example

A 3-state credit rating model (A, BBB, CCC) has an irreducible transition matrix $P$ with all positive entries. Perron–Frobenius guarantees $P$ has a unique stationary distribution $\pi = (\pi_A, \pi_\text{BBB}, \pi_\text{CCC})$ with all positive entries, obtainable by solving $\pi P = \pi$, $\sum_i \pi_i = 1$. If the second eigenvalue is $|\lambda_2| = 0.85$, after $n = 20$ quarters the total variation distance to stationarity is at most $C \cdot 0.85^{20} \approx 0.039C$ — the rating distribution has nearly converged to $\pi$ within five years.

## Remember

Credit portfolio models that rely on Markov chain rating migration matrices implicitly invoke Perron–Frobenius. When the matrix is irreducible (every rating can eventually transition to every other), the theorem guarantees a unique long-run rating distribution — the steady-state assumption underpinning Basel IRB through-the-cycle probability-of-default estimates. If an absorbing state (default) is present, the matrix is no longer irreducible and a sub-stochastic Perron–Frobenius argument applies: the Perron root falls below 1, reflecting the certainty of eventual absorption into default.
