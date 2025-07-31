import gymnasium as gym
import numpy as np
import torch
from model import CNNPolicy
from ppo import PPOAgent
from utils import compute_advantages
from env_wrappers import make_env

env = make_env()
obs_shape = env.observation_space.shape
action_dim = env.action_space.shape[0]

model = CNNPolicy(action_dim)
agent = PPOAgent(model)

num_episodes = 500
max_timesteps = 1000

for episode in range(num_episodes):
    obs, _ = env.reset()
    obs_buffer, action_buffer, reward_buffer, done_buffer, logprob_buffer, value_buffer = [], [], [], [], [], []

    for t in range(max_timesteps):
        obs_tensor = torch.tensor(obs[None], dtype=torch.float32)
        dist, value = model(obs_tensor)
        action = dist.sample()
        log_prob = dist.log_prob(action).sum(axis=-1)
        
        action_clipped = action.detach().numpy()[0]
        next_obs, reward, terminated, truncated, _ = env.step(action_clipped)
        done = terminated or truncated

        obs_buffer.append(obs)
        action_buffer.append(action_clipped)
        reward_buffer.append(reward)
        done_buffer.append(done)
        logprob_buffer.append(log_prob.detach().numpy())
        value_buffer.append(value.detach().numpy()[0, 0])

        obs = next_obs
        if done:
            break

    last_value = 0 if done else model(torch.tensor(obs[None], dtype=torch.float32))[1].item()
    returns = agent.compute_returns(reward_buffer, done_buffer, last_value, agent.gamma)
    advantages = compute_advantages(reward_buffer, value_buffer, done_buffer)

    agent.update(obs_buffer, action_buffer, logprob_buffer, returns, advantages)

    print(f"Episode {episode+1}, Total reward: {sum(reward_buffer):.2f}")

    if (episode + 1) % 50 == 0:
        torch.save(model.state_dict(), f"models/custom_ppo_episode{episode+1}.pth")

env.close()
