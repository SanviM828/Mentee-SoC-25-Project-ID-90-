import gymnasium as gym
import cv2
import numpy as np
from collections import deque
from gymnasium import spaces

# Preprocess one frame: grayscale + resize + normalize
def preprocess_frame(frame, resolution=(84, 84)):
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    frame = cv2.resize(frame, resolution)
    frame = frame.astype(np.float32) / 255.0  # Normalize to [0, 1]
    return frame  # Shape: (84, 84)

# Simple manual frame stacker
class FrameStack:
    def __init__(self, k=4):
        self.k = k
        self.frames = deque([], maxlen=k)

    def reset(self, frame):
        processed = preprocess_frame(frame)
        self.frames = deque([processed] * self.k, maxlen=self.k)
        return np.stack(self.frames, axis=-1)  # Shape: (84, 84, 4)

    def step(self, frame):
        processed = preprocess_frame(frame)
        self.frames.append(processed)
        return np.stack(self.frames, axis=-1)

# Wrapper class for environment
class PreprocessedCarRacing(gym.Wrapper):
    def __init__(self, env, stack_size=4):
        super().__init__(env)
        self.stack_size = stack_size
        self.framestack = FrameStack(k=stack_size)
        self.observation_space = spaces.Box(
            low=0.0, high=1.0, shape=(84, 84, stack_size), dtype=np.float32
        )

    def reset(self, **kwargs):
        obs, info = self.env.reset(**kwargs)
        return self.framestack.reset(obs), info

    def step(self, action):
        obs, reward, terminated, truncated, info = self.env.step(action)
        stacked = self.framestack.step(obs)
        return stacked, reward, terminated, truncated, info

# Function to create the environment
def make_env(render_mode="human"):
    env = gym.make("CarRacing-v3", render_mode=render_mode)
    env = PreprocessedCarRacing(env, stack_size=4)
    return env
