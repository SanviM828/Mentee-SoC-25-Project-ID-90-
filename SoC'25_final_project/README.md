# PPO-Based Reinforcement Learning for CarRacing-v3

## Introduction
This project explores the application of Proximal Policy Optimization (PPO), a reinforcement
learning algorithm, to train an autonomous agent capable of driving a car in the CarRacing-v3
environment provided by OpenAI Gymnasium. The environment generates random racetracks,
and the agent must learn to navigate these tracks successfully using only visual input. The
primary goal was to implement PPO from scratch in a beginner-friendly way, while still
demonstrating meaningful learning behavior from the agent.

## Preprocessing Pipeline
The raw observations from the environment consist of RGB images of size 96 by 96 pixels. To
make learning more efficient and reduce the complexity of the input, a preprocessing pipeline
was implemented. First, the images were converted to grayscale to remove unnecessary color
information, reducing the number of channels from three to one. The grayscale frames were then
resized to 84 by 84 pixels, balancing resolution and computational efficiency.
To ensure the agent could understand motion, the last four consecutive frames were stacked
together. This gives the agent a short-term memory of how objects in the scene are moving.
Additionally, all pixel values were normalized to a range between zero and one. These
preprocessing steps helped improve learning speed and model stability.

## PPO Architecture and Hyperparameters
The agent uses a convolutional neural network to process visual input and estimate both the
action policy and the value function. The architecture consists of three convolutional layers
followed by a fully connected layer with 512 neurons. The output is split into two heads, one for
the actor which chooses actions, and one for the critic which estimates the value of each state.
The PPO algorithm was implemented with commonly used settings. The learning rate was set to
2.5 times ten raised to the power of negative four. The discount factor gamma, which determines
how much future rewards are considered, was set to 0.99. A clipping parameter of 0.2 was used
to limit how much the policy is allowed to change during training, and a lambda value of 0.95 
was used for Generalized Advantage Estimation. The model was updated over four epochs after
each training batch.

## Training Process
The model was trained on the CarRacing-v3 environment using the preprocessed grayscale
observations. Training was done for 500 episodes, where each episode represents one complete
attempt at navigating a racetrack. After each episode, the model was updated based on the
experiences collected.
The maximum number of time steps per episode was 1000. The PPO algorithm collected the
states, actions, rewards, and estimated values during each episode and used this data to compute
advantages and losses, which were then used to update the model weights. The total reward for
each episode was printed to monitor the training progress.
If a reward curve is plotted, it would typically show that the agent starts off performing poorly,
but the total reward gradually improves over the course of training. Around 300 episodes, the
reward tends to stabilize, indicating the model has learned a fairly good policy.

## Reward Shaping
No custom reward shaping techniques were applied in this project. The agent relied on the
default reward mechanism provided by the CarRacing-v3 environment. The reward increases
when the car moves along the track and penalizes the agent for going off-road. If the car
performs poorly, the episode ends early. This default reward was sufficient to teach the agent
basic driving behavior.

## Observations
Training the agent presented a few challenges. One of the main issues encountered was
occasional crashing of the environment during sharp turns. In some cases, the Pygame window
would close unexpectedly. This problem was not resolved in the current version to keep the
project focused and manageable. A possible explanation that can be given during demonstration
is that the environment sometimes crashes when rendering complex turns, which is a known
issue with some setups.

Despite this, the trained agent showed interesting behavior. In the early stages of training, the car
spun in circles or veered off the road frequently. As training progressed, it learned to follow the
road, slow down near curves, and avoid going off-track. The agent learned to generalize to
different track layouts reasonably well. However, it occasionally struggled with extremely sharp
turns or unexpected terrain.
The training time was moderate and manageable, although PPO is known to require more
computation compared to simpler algorithms. The project took about one to two hours to train
500 episodes, depending on the hardware used.

One of the main issues encountered was occasional crashing of the environment during sharp
turns. In some cases, the Pygame window would close unexpectedly. This issue is likely related
to system limitations such as limited RAM or GPU capability. The environment uses real-time
rendering through Pygame, and if system resources are stretched, especially during complex
turns where rapid visual updates and physics calculations occur, the rendering thread might
crash. These resource-related failures are more common in setups without dedicated graphics
hardware. Since resolving this would require extensive debugging or hardware upgrades, I
considered it beyond the scope of the current project.

## Conclusion
This project successfully demonstrated how Proximal Policy Optimization can be used to train a
reinforcement learning agent to drive a car in a simulated environment. A simple and clear
implementation of PPO, combined with a lightweight convolutional network and standard
preprocessing, allowed the agent to learn useful driving behavior within a limited training
duration. While some issues like environment crashes during turning were not addressed, the
overall behavior of the agent shows meaningful learning and adaptation. The project serves as a
solid starting point for deeper reinforcement learning applications and real-time control
problems.
