# Reinforcement Learning

****Deterministic and Stochastic Gym Environment****

  Created deterministic and stochistic enviroment for reinforcement learning.

****Q-Learning****

Implemention uses Frozen Lake Gym Env. 

Action Space
The agent takes a 1-element vector for actions. The action space is (dir), where dir decides direction to move in which can be:

0: LEFT
1: DOWN
2: RIGHT
3: UP

Observation Space
The observation is a value representing the agent’s current position as current_row * nrows + current_col (where both the row and col start at 0). For example, the goal position in the 4x4 map can be calculated as follows: 3 * 4 + 3 = 15. The number of possible observations is dependent on the size of the map. For example, the 4x4 map has 16 possible observations.

Rewards:
Reach goal(G): +1
Reach hole(H): 0
Reach frozen(F): 0

Approaches:

  Approach 1: Started with explore only once in first episode:: DOES NOT CONVERGE as the enviroment does not have any rewards for any state except for the target state where the reward is one. So the agent keeps exploiting an empty Q table repeating the same action without learning.

  Approach 2: Epsilon Greedy Approach : Epsilon value - 0.1 (1300 Episodes- 100 Max step/Episode):: With probability os exploration being too low the agent could reach the target even once. DID NOT CONVERGE

  Approach 3: Epsilon Greedy Approach : Epsilon value - 0.3 (100  Episodes= 100 Max step/Episode):: Even through the probablity was increased the agent could not reach target so that the Q table values could be updated for any state-action pair. DID NOT CONVERGE

  Approach 4: Epsilon Greedy Approach : Epsilon value - 1 (300 Episodes- 50 Max step/Episode): Epsilon decay by 0.1 every 15 episode:: To enable the agent to explore more in the begining and slowly increase the exploting tendancy by reducing epsilon value. CONVERGED
  
Final Approach: Epsilon Greedy Approach : Epsilon value - 1 (1000 Episodes- 100 Max step/Episode): Epsilon decay by 0.1 every 30 episode:: Converged
In order for the agent to start learning the agent has to reach the goal state atleast once in frozen-lake envirnoment. It is due to reward pattern which only gives the agent a reward when it reaches final state and 0 until then. So until the agent reaches the target state atleast once the Q-table values remain empty. As the agent reaches the target state, the Q-table values start getting updated based reward received from the target state.
To confirm the agent's behaviour and effect of Epsilon decay the number of episodes were increased. As the exploring probability goes down and explotation probablity goes up over 1000 episodes the agents learn to select best actions which lead it to the target. 







