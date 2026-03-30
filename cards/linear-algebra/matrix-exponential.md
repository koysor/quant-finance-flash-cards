# Matrix Exponential

**Topic:** Linear Algebra
**Tags:** matrix exponential, power series, differential equations, credit transitions, mean reversion
**Author:** Claude Opus 4.6

---

## Definition

The matrix exponential $e^{A}$ generalises the scalar exponential function to square matrices. It is defined by the convergent power series $e^{A} = \sum_{k=0}^{\infty} \frac{A^k}{k!}$, where $A^0 = I$ (the identity matrix). The matrix exponential is the unique solution operator for the linear system of ordinary differential equations $\frac{d\mathbf{x}}{dt} = A\mathbf{x}$, giving $\mathbf{x}(t) = e^{At}\mathbf{x}(0)$.

## Key Formula

The **power series definition**:

$$e^{A} = I + A + \frac{A^2}{2!} + \frac{A^3}{3!} + \cdots = \sum_{k=0}^{\infty} \frac{A^k}{k!}$$

When $A$ is **diagonalisable** as $A = PDP^{-1}$, where $D = \operatorname{diag}(\lambda_1, \lambda_2, \ldots, \lambda_n)$:

$$e^{A} = P \, e^{D} \, P^{-1} = P \, \operatorname{diag}(e^{\lambda_1}, e^{\lambda_2}, \ldots, e^{\lambda_n}) \, P^{-1}$$

A key property: $\det(e^{A}) = e^{\operatorname{tr}(A)}$.

## Example

Let $A = \begin{pmatrix} 1 & 0 \\ 0 & 3 \end{pmatrix}$. Since $A$ is already diagonal, $D = A$ and $P = I$:

$$e^{A} = \begin{pmatrix} e^{1} & 0 \\ 0 & e^{3} \end{pmatrix} = \begin{pmatrix} 2.718 & 0 \\ 0 & 20.086 \end{pmatrix}$$

For a time-scaled version with $t = 2$:

$$e^{At} = e^{2A} = \begin{pmatrix} e^{2} & 0 \\ 0 & e^{6} \end{pmatrix} \approx \begin{pmatrix} 7.389 & 0 \\ 0 & 403.429 \end{pmatrix}$$

## Remember

In quantitative finance, the matrix exponential appears whenever a continuous-time process is described by a system of linear equations. Credit risk models use $e^{Qt}$ (where $Q$ is a generator matrix of transition rates) to compute the probability that a bond migrates from one rating to another over a time horizon $t$ — this underpins credit portfolio VaR and CVA calculations. Mean-reversion models such as Vasicek and Ornstein--Uhlenbeck have closed-form solutions involving $e^{-\kappa t}$, which is the scalar case of the matrix exponential; multi-factor extensions require the full matrix version. Recognising that $e^{At}$ solves $d\mathbf{x}/dt = A\mathbf{x}$ lets you move fluidly between discrete transition matrices and their continuous-time generators.
