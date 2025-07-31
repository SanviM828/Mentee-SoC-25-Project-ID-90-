import numpy as np

def compute_advantages(rewards, values, dones, gamma=0.99, lam=0.95):
    advantages = []
    gae = 0
    values = np.append(values, 0.0)
    for t in reversed(range(len(rewards))):
        delta = rewards[t] + gamma * values[t+1] * (1 - dones[t]) - values[t]
        gae = delta + gamma * lam * (1 - dones[t]) * gae
        advantages.insert(0, gae)
    return advantages
