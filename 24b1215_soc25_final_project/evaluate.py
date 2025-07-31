from stable_baselines3 import PPO
from env_wrappers import make_env

def evaluate_model(model_path):
    env = make_env(render_mode="human")  # Opens window
    model = PPO.load(model_path)

    obs, _ = env.reset()
    done = False
    total_reward = 0

    while not done:
        action, _ = model.predict(obs, deterministic=True)
        obs, reward, terminated, truncated, _ = env.step(action)
        total_reward += reward
        done = terminated or truncated

    print("Total Reward:", total_reward)
    env.close()

if __name__ == "__main__":
    evaluate_model("models/ppo_carracing")
