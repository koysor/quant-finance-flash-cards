# Floor and Ceiling Functions

**Topic:** Mathematical Notation
**Tags:** floor function, ceiling function, integer part, rounding, discrete time
**Author:** Claude Sonnet 4.6

---

## Definition

The **floor function** $\lfloor x \rfloor$ returns the greatest integer less than or equal to $x$; the **ceiling function** $\lceil x \rceil$ returns the smallest integer greater than or equal to $x$.

$$\lfloor x \rfloor = \max\{n \in \mathbb{Z} : n \leq x\} \qquad \lceil x \rceil = \min\{n \in \mathbb{Z} : n \geq x\}$$

Both functions map a real number to the nearest integer — floor rounds down, ceiling rounds up. For any integer $n$, $\lfloor n \rfloor = \lceil n \rceil = n$.

## Key Formula

$$\lfloor x \rfloor \leq x < \lfloor x \rfloor + 1 \qquad \lceil x \rceil - 1 < x \leq \lceil x \rceil$$

The **fractional part** of $x$ is defined as:

$$\{x\} = x - \lfloor x \rfloor \in [0,1)$$

For a simulation with time horizon $T$, step size $\Delta t$, and a continuous time $t$, the discrete time index is:

$$i = \lfloor t / \Delta t \rfloor$$

## Example

Let $x = 2.7$ and $y = -1.3$:

$$\lfloor 2.7 \rfloor = 2, \quad \lceil 2.7 \rceil = 3$$
$$\lfloor -1.3 \rfloor = -2, \quad \lceil -1.3 \rceil = -1$$

**Day-count fraction:** a bond with settlement date $s$ and maturity date $m$ has an actual/365 coupon period of $\tau = (m - s)/365$ days. The number of full coupon periods remaining is $\lfloor \tau \cdot f \rfloor$, where $f$ is the coupon frequency (e.g. $f = 2$ for semi-annual).

**Monte Carlo time grid:** given annual volatility $\sigma$ and $N = \lfloor T/\Delta t \rfloor$ steps, each Euler–Maruyama step uses $\Delta W_i = \varepsilon_i \sqrt{\Delta t}$ for $i = 0, 1, \ldots, N-1$.

## Remember

Floor and ceiling functions are the bridge between continuous mathematics and the discrete grids that computers and bond markets actually use. Whenever you discretise time — in a Monte Carlo simulation, an Euler–Maruyama scheme, or a coupon schedule — you are implicitly applying $\lfloor \cdot \rfloor$ or $\lceil \cdot \rceil$ to map a real-valued quantity onto an integer index or period count.
