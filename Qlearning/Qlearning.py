import gym
import numpy as np
import matplotlib.pyplot as plt


class Qlearning:
    def __init__(self, env, alpha, discount_factor, max_episodes, max_steps):
        self.env = env
        self.alpha = alpha
        self.discount_factor = discount_factor
        self.max_episodes = max_episodes
        self.max_steps = max_steps
        self.q_table = np.zeros((states, actions))
        self.total_reward = list()

    def train(self):
        epsilon = 1
        epsilon_threshold = 0.1
        decay = 0.05
        check = 0
        for episode in range(self.max_episodes):
            done = False
            print(f'Episode {episode} Started')
            current_state = self.env.reset()
            current_state = current_state[0]
            current_reward = 0
            for step in range(self.max_steps):

                if (np.random.uniform(0,1) < epsilon) :
                    print(f'Exploring step {step}')
                    action_choosen = self.env.action_space.sample()
                else:
                    action_choosen = np.argmax(self.q_table[current_state, :])
                    print(f'Exploiting step {step}')
                

                next_state, reward, terminated, truncated, info = self.env.step(action_choosen)
                reward = int(reward)
                
                if reward == 1 and check == 0: 
                    check = 1
                    print(f'Press Enter to continue as the reward is {reward}')
                    input()

                # Update Q table
                self.q_table[current_state, action_choosen] = (1-self.alpha) * self.q_table[current_state, action_choosen] + self.alpha * (
        reward + (self.discount_factor * np.max(self.q_table[next_state, :])))

                # Update reward
                current_reward += reward

                if terminated != done or truncated!= done:break

                # Update Current State
                current_state = next_state
                
            self.total_reward.append(current_reward)
            if (episode % 30 == 0) and (episode != 0):
                if(epsilon > epsilon_threshold):
                    epsilon = epsilon - decay
                    print(f'Epsilon decay executed, epsilon value is {epsilon}')
            if episode % 50 == 0:
                plt.figure(figsize=(10, 6))
                plt.imshow(self.q_table, cmap='hot', interpolation='nearest')
                plt.title(f'Q-Table Convergence - Episode {episode}')
                plt.colorbar()
                plt.savefig(f'q_table_convergence_episode_{episode}.png')  
                plt.show()
            print(self.q_table)
            

if __name__ == "__main__":
    '''
    Attempt 1: Started with explore only once in first episode:: DOES NOT CONVERGE

    Attempt 2: Epsilon Greedy Approach : Epsilon value - 0.1 (1300 Episodes- 100 Max step/Episode):: DID NOT CONVERGE

    Attempt 3: Epsilon Greedy Approach : Epsilon value - 0.1 (100  Episodes= 100 Max step/Episode): explore until reaches goal 
    atleast once(Keeps exploring wrong logic)

    Attempt 4: Epsilon Greedy Approach : Epsilon value - 0.3 (100  Episodes= 100 Max step/Episode):: DID NOT CONVERGE

    Attempt 5: Epsilon Greedy Approach : Epsilon value - 0.4 (1000  Episodes= 100 Max step/Episode):: 
    DID NOT CONVERGEexplore until reaches goal atleast once(Keeps exploring wrong logic)

    Attempt 6: Epsilon Greedy Approach : Epsilon value - 1 (300 Episodes- 50 Max step/Episode): Epsilon decay by 0.1 every 15 episode:: Converged

    Attempt 7: Epsilon Greedy Approach : Epsilon value - 1 (1000 Episodes- 100 Max step/Episode): Epsilon decay by 0.1 every 30 episode:: 

    '''
    env = gym.make('FrozenLake-v1', desc=None, map_name="4x4", is_slippery=False, render_mode="human")

    # Hyper-Parameters
    alpha = 0.1
    discount_factor = 0.99
    max_episodes = 1000
    max_steps = 100

    # Action and State Space
    states = env.observation_space.n
    actions = env.action_space.n
    rewards = env.reward_range

    rl_agent = Qlearning(env, alpha, discount_factor, max_episodes, max_steps)
    rl_agent.train()
    print(rl_agent.total_reward)

