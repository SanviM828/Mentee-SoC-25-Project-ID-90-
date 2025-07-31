import torch
import torch.nn as nn
from torch.distributions import Normal

class CNNPolicy(nn.Module):
    def __init__(self, action_dim):
        super().__init__()
        self.conv = nn.Sequential(
            nn.Conv2d(4, 32, 8, 4),  # input: (4, 96, 96)
            nn.ReLU(),
            nn.Conv2d(32, 64, 4, 2),
            nn.ReLU(),
            nn.Conv2d(64, 64, 3, 1),
            nn.ReLU()
        )
        self.fc = nn.Sequential(
            nn.Linear(64 * 7 * 7, 512),
            nn.ReLU()
        )

        self.actor_mean = nn.Linear(512, action_dim)
        self.actor_logstd = nn.Parameter(torch.zeros(action_dim))
        self.critic = nn.Linear(512, 1)

    def forward(self, x):
        x = x.permute(0, 3, 1, 2)  # NHWC -> NCHW
        x = self.conv(x)
        x = x.view(x.size(0), -1)
        x = self.fc(x)

        mean = self.actor_mean(x)
        std = torch.exp(self.actor_logstd)
        dist = Normal(mean, std)

        value = self.critic(x)
        return dist, value
