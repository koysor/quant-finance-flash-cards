# Target Network

**Topic:** Machine Learning
**Tags:** target network, dqn, bellman equation, training stability, q-learning, deep reinforcement learning
**Created:** 2026-06-02
**Author:** Claude Sonnet 4.6

---

## Definition

A **target network** is a periodically frozen copy of the main Q-network (or value network) used solely to compute Bellman regression targets during training. Without it, the targets move every gradient step — chasing a moving target — causing oscillation and divergence. The frozen copy stabilises training by holding the targets fixed for $C$ steps before syncing.

## Key Formula

The Bellman loss with a target network (parameters $\theta^-$, updated every $C$ steps):

$$\mathcal{L}(\theta) = \mathbb{E}\!\left[\Bigl(r + \gamma\,\max_{a'} Q(s', a';\,\theta^-) - Q(s, a;\,\theta)\Bigr)^2\right]$$

Two update strategies for $\theta^-$:

**Hard update** (DQN): every $C$ steps, copy $\theta^- \leftarrow \theta$.

**Soft update** (DDPG/TD3): every step, exponentially smooth:
$$\theta^- \leftarrow \tau\,\theta + (1 - \tau)\,\theta^-, \qquad \tau \ll 1 \text{ (e.g. } 0.005\text{)}$$

In the TDBP model the same principle appears: the time-$(t+1)$ network $f_{t+1}(\cdot;\theta_{t+1})$ acts as a fixed target when training the time-$t$ network $f_t$, because $\theta_{t+1}$ is already trained and held frozen.

## Example

DQN without a target network is trained on CartPole. After 200 episodes, Q-value estimates diverge: the network updates towards a target that itself jumped because the same network generates both the prediction and the target. Adding a hard target network ($C = 100$ steps): Q-values stabilise after 150 episodes and the agent solves CartPole consistently. In financial RL, the analogous instability produces wild swings in the estimated option price across training epochs — target networks eliminate this.

## Remember

The target network is a deliberate introduction of **staleness** to gain **stability**: the Bellman targets lag the current weights by up to $C$ steps, but this lag prevents the destructive feedback loop where each gradient step invalidates the targets it was trained against. In TDBP the backward-induction structure achieves the same result architecturally — each time-step network is trained to completion before the next time step begins, so the target never moves during the training of any single network. Soft updates (small $\tau$) are preferred in continuous-action settings (option hedging) because they provide smoother target evolution than the discontinuous hard reset.
