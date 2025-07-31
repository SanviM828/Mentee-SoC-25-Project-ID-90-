import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np

class PPOAgent:
    def __init__(self, model, lr=2.5e-4, gamma=0.99, clip_eps=0.2):
        self.model = model
        self.optimizer = optim.Adam(self.model.parameters(), lr=lr)
        self.gamma = gamma
        self.clip_eps = clip_eps

    def compute_returns(self, rewards, dones, last_value, gamma):
        returns = []
        R = last_value
        for r, d in zip(reversed(rewards), reversed(dones)):
            R = r + gamma * R * (1.0 - d)
            returns.insert(0, R)
        return returns

    def update(self, states, actions, old_log_probs, returns, advantages):
        states = torch.tensor(states, dtype=torch.float32)
        actions = torch.tensor(actions, dtype=torch.float32)
        old_log_probs = torch.tensor(old_log_probs, dtype=torch.float32)
        returns = torch.tensor(returns, dtype=torch.float32)
        advantages = torch.tensor(advantages, dtype=torch.float32)

        for _ in range(4):  # epochs
            dist, values = self.model(states)
            log_probs = dist.log_prob(actions).sum(axis=-1)
            ratio = torch.exp(log_probs - old_log_probs)

            surr1 = ratio * advantages
            surr2 = torch.clamp(ratio, 1 - self.clip_eps, 1 + self.clip_eps) * advantages
            actor_loss = -torch.min(surr1, surr2).mean()
            critic_loss = (returns - values.squeeze()).pow(2).mean()

            loss = actor_loss + 0.5 * critic_loss

            self.optimizer.zero_grad()
            loss.backward()
            self.optimizer.step()
