# Recurrence and Transience

**Topic:** Stochastic Processes
**Tags:** recurrence, transience, Markov chain, positive recurrence, stationary distribution, return time
**Created:** 2026-06-15
**Author:** Claude Sonnet 4.6

---

## Definition

A Markov chain state $i$ is **recurrent** if the chain returns to $i$ with probability 1; it is **transient** if there is positive probability of never returning. Among recurrent states, **positive recurrence** means the expected return time is finite — this is the key condition for a unique stationary distribution to exist.

## Key Formula

Let $f_i = \mathbb{P}(\text{chain ever returns to } i \mid X_0 = i)$. Then:

$$\text{recurrent:} \; f_i = 1 \qquad \text{transient:} \; f_i < 1$$

Among recurrent states, let $\mu_i = \mathbb{E}[\text{first return time to } i \mid X_0 = i]$:

$$\text{null recurrent:} \; \mu_i = \infty \qquad \text{positive recurrent:} \; \mu_i < \infty$$

The stationary probability is $\pi_i = 1/\mu_i$. A stationary distribution exists if and only if the chain is irreducible (can reach any state) and positive recurrent.

## Example

A CIR interest rate model $dr_t = \kappa(\theta - r_t)\,dt + \sigma\sqrt{r_t}\,dW_t$ satisfies the Feller condition $2\kappa\theta > \sigma^2$: the process cannot reach zero and is positive recurrent, with mean return time $\mu_i$ finite for every $r_t$. The stationary distribution is Gamma-distributed with mean $\theta$, confirming the ergodic theorem applies: simulating one long path gives the same long-run rate distribution as simulating many paths at a fixed future time.

## Remember

The Feller condition for the CIR model is not just a technicality — it is the condition that makes the model positive recurrent and therefore ergodic. Without it, the short rate could reach zero and become transient, meaning the long-run distribution is undefined and historical estimation of $\theta$ would be meaningless. Positive recurrence is the bridge between the theory of stationary distributions and the practice of calibrating mean-reverting interest rate models.
