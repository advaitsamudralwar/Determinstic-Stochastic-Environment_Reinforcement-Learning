# Approach:

## Approach 1
The initial approach involved exploring only once in the first episode. However, this approach did not converge because the environment lacked rewards for any state except the target state, where the reward was set to one. Consequently, the agent would repeatedly exploit an empty Q-table by choosing the same action without learning.

## Approach 2
Employed the Epsilon Greedy Approach with an epsilon value of 0.1. Over 1300 episodes, with a maximum of 100 steps per episode, the agent's exploration probability was very low, resulting in rare occurrences of reaching the target state. Unfortunately, this approach did not converge either.

## Approach 3
Implemented the Epsilon Greedy Approach with an increased epsilon value of 0.3. Across 100 episodes with a maximum of 100 steps per episode, the exploration probability was raised. Nevertheless, the agent still struggled to reach the target state, preventing updates to the Q-table values. This approach also failed to converge.

## Approach 4 
Employed the Epsilon Greedy Approach with an initial epsilon value of 1.0, which decayed by 0.1 every 15 episodes. This strategy aimed to encourage exploration at the outset and gradually shift toward exploitation by reducing epsilon. Through 300 episodes, each with a maximum of 50 steps, this approach managed to converge successfully.

## Final Approach
Utilized the Epsilon Greedy Approach with an initial epsilon value of 1.0, decaying by 0.1 every 30 episodes. This approach was further tested with 1000 episodes, each permitting a maximum of 100 steps. The continuous reduction of epsilon fostered increased exploitation while still maintaining exploration. Ultimately, this approach yielded convergence.

To facilitate the agent's learning process, it was essential for the agent to reach the goal state at least once in the frozen-lake environment. The reward structure only granted rewards upon reaching the final state and provided no rewards before that point. Consequently, until the agent successfully reached the target state, the Q-table values remained uninitialized. As soon as the agent achieved the target state, the Q-table values began updating based on the rewards received from the target state. To validate the agent's behavior and evaluate the impact of Epsilon decay, the number of episodes was extended. Over 1000 episodes, as the exploration probability diminished and the exploitation probability increased, the agent progressively learned to select optimal actions leading it to the target state.
