import numpy as np
import gym
from gym import spaces

'''
Deterministic Environment with Random Agent until goal state is reached
As the Env is Deterministic the the agent successfully terminates and reaching the goal 
state.
'''
class DeterministicEnv(gym.Env):
    def __init__(self):
        self.nstates = 12
        self.nactions = 4
        self.nrewards = 4

        #Define action and state space
        self.action_space = spaces.Discrete(self.nactions)
        self.observation_space = spaces.Discrete(self.nstates)

        #Define rewards for states
        self.rewards = {
            0: 1,  # Start state
            1: 0,
            2: 0,
            3: 0,
            4: 0, 
            5: 0,
            6: 0,
            7: 0,
            8: 0,
            9: 0, 
            10: 0,
            11: 5
        }

        self.timestep = 0
        self.goal_state = 11
        self.start_state = 3
    
    def step(self, action):
        assert self.action_space.contains(action), "Invalid action"

        if action == 0:
            self.current_state = max(self.current_state-4, 1)
        elif action == 1:
            self.current_state = min(self.current_state+4, 12)
        elif action == 2:
            self.current_state = max(self.current_state-1, 1)
        elif action == 3:
            self.current_state = min(self.current_state+1, 12)

        reward = self.rewards.get(self.current_state)
        self.timestep += 1
        termination_criteria = (self.timestep >= 10)

        return self.current_state, reward, termination_criteria, {}
    
    def reset(self):
        self.current_state = 0
        self.timestep = 0

        return self.current_state
    
    def render(self):
        print('Current State = ', self.current_state)

'''
Stochastic Envirnoment with random transition probabilities.
As the Env is stochastic the agent behaviour is less predictable. 
'''
class StochasticEnv(gym.Env):
    def __init__(self):
        self.nstates = 12
        self.nactions = 4
        self.nrewards = 4

        #Define action and state space
        self.action_space = spaces.Discrete(self.nactions)
        self.observation_space = spaces.Discrete(self.nstates)

        #Define rewards for states
        self.rewards = {
            0: 1,  # Start state
            1: 0,
            2: 0,
            3: 0,
            4: 0, 
            5: 0,
            6: 0,
            7: 0,
            8: 0,
            9: 0, 
            10: 0,
            11: 5
        }

        self.timestep = 0
        self.goal_state = 12
        self.start_state = 5
    
    def step(self, action):
        assert self.action_space.contains(action), "Invalid action"

        #Transition Probability Matrix
        transition_prob = {
            0:[0.7, 0.1, 0.1, 0.1],
            1:[0.1, 0.1, 0.7, 0.1],
            2:[0.1, 0.7, 0.1, 0.1],
            3:[0.1 ,0.1 ,0.1, 0.7]
        } 
        
        prob = transition_prob[action]
        next_state = np.random.choice(range(4), p =prob ) 

        reward = self.rewards.get(self.current_state)
        termination_criteria = (self.timestep >= 10)
        self.current_state = next_state
        self.timestep += 1


        return self.current_state, reward, termination_criteria, {}

    def reset(self):
        self.current_state = 0
        self.timestep = 0

        return self.current_state
    
    def render(self):
        print('Current State = ', self.current_state)
    


if __name__ == '__main__':
    det_env = DeterministicEnv()
    sto_env = StochasticEnv()
    det_reset = det_env.reset()
    sto_reset = sto_env.reset()
    next_state = 0
    
    # Agent run until reaches goal state. 
    while(next_state != 11):
        det_action = det_env.action_space.sample()
        next_state ,reward, termination_criteria, _ = det_env.step(det_action)
        det_env.render()

    '''
      Agent run until reaches goal state but due to the stochastic nature of the transition 
      probabilties agent's behavious is less predictable. 
    '''
    while(next_state != 11):
        sto_action = sto_env.action_space.sample()
        next_state ,reward, termination_criteria, _ = sto_env.step(sto_action)
        sto_env.render()

