# Seasons of Code (SoC) 2025 – PPO Agent for CarRacing
This repository contains all the code, assignments, and resources I worked on during the Summer of Code 2025. The program focused on foundational concepts in Python, Neural Networks, Reinforcement Learning, and culminated in a final project where I trained a PPO agent to autonomously drive a car in the CarRacing-v3 environment from OpenAI Gym.

## Project Overview
The final objective was to train a reinforcement learning agent using Proximal Policy Optimization (PPO) to solve the CarRacing-v3 environment using only image input. This problem requires the agent to learn how to control a car efficiently using raw pixel data, by observing frames of the game and determining optimal steering, acceleration, and braking actions to stay on track and complete laps.

The entire training pipeline involved:

- Preprocessing images (resizing, normalization)

- Stacking consecutive frames for temporal understanding

- Using PPO with convolutional policies

- Evaluating and visualizing the agent's performance

## Learning Journey
Over the course of six weeks, I covered a wide range of foundational and advanced topics that prepared me for the final project:

### Week 1 – Python & Pygame
Learned Python syntax, OOP concepts, and game development using Pygame.

Built a basic Snake game and understood game loops and event handling.

### Week 2 – Neural Networks & CNNs
Studied core concepts of neural networks through 3Blue1Brown, Andrew Ng, and TensorFlow Playground.

Explored convolutional layers and their application to vision problems.

Practiced building image classifiers with PyTorch.

### Week 3 – Reinforcement Learning Fundamentals
Followed David Silver’s RL lectures and the book "Reinforcement Learning: An Introduction" by Sutton and Barto.

Understood Markov Decision Processes (MDPs), Q-Learning, and Policy Gradient methods.

### Week 4–5 – Q-Learning and Deep Q-Learning (Snake Game)
Implemented Q-learning with a discrete state space on the Snake game.

Transitioned to Deep Q-Networks using PyTorch with replay buffers and target networks.

Compared tabular Q-learning and DQN performance.

### Week 6 – PPO and OpenAI Gym
Learned Proximal Policy Optimization (PPO) through theory and tutorials.


### Final Project: PPO Agent for CarRacing  
Setup  
Install dependencies:  
`pip install gymnasium[box2d] stable-baselines3 opencv-python numpy torch`

Run training:  
`python main.py`

Run evaluation (renders car driving):
`python evaluate.py`

The Pygame window may crash during sharp turns. This issue is likely due to limited system RAM or GPU capability. Since real-time rendering is involved, performance bottlenecks during fast frame updates can lead to window crashes. Fixing this would require deeper debugging or a stronger system configuration, which is outside the current scope.
