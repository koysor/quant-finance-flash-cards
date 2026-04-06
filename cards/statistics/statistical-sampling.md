# Statistical Sampling

**Topic:** Statistics
**Tags:** sampling, simple random, stratified, systematic, quota, opportunity, population
**Created:** 2026-04-06
**Author:** Claude Sonnet 4.6

---

## Definition

A **population** is the complete set of items under investigation; a **census** collects data from every member. A **sample** is a subset used to infer properties of the population. The five main sampling methods are: **simple random** (every member equally likely), **systematic** (every $k$-th member), **stratified** (proportional sub-groups), **quota** (non-random target numbers per sub-group), and **opportunity/convenience** (whoever is available).

## Key Formula

**Stratified sampling allocation:**

$$n_i = \frac{N_i}{N} \times n$$

where $N_i$ is the sub-group size, $N$ is the population size, and $n$ is the total sample size.

**Systematic sampling interval:**

$$k = \frac{N}{n}$$

Select a random start $r \in \{1, \ldots, k\}$, then sample members $r, r+k, r+2k, \ldots$

## Example

A bank has 600 retail clients: 200 high-net-worth (HNW), 400 mass-market. A stratified sample of 60 clients allocates:

$$\text{HNW: } \frac{200}{600} \times 60 = 20 \qquad \text{Mass: } \frac{400}{600} \times 60 = 40$$

Simple random sampling within each stratum (e.g. numbered list + random number generator) gives a representative sample. Quota sampling would instead tell an interviewer to find 20 HNW and 40 mass-market clients without random selection — introducing interviewer bias.

## Remember

Sampling design is the **first decision** in any quantitative study and directly affects the validity of inference. In risk modelling, **survivorship bias** is a sampling error — only observing funds that survived excludes the worst performers, upward-biasing estimated returns. Stratified sampling is the basis of **index construction**: a benchmark like the FTSE 100 proportionally represents sectors, ensuring the sample (the index) reflects the population (the whole market). Regulators also require banks to use **representative samples** when backtesting internal models, so that adverse periods are not excluded.
