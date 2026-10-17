## Aim
---
Active Reinforcement Learning Using Q-Learning. A robot must navigate a grid from the starting position to the goal position . An obstacle is placed at . The robot can move up, down, left, or right.The robot receives +10 for reaching the goal, −5 for attempting to move into an obstacle, and −1 for every normal move. When the robot hits an obstacle, it remains in its current state. Reaching the Scenario-Based Programming Questions on Reinforcement Learning.
---

## Theory

Q-Learning is an **active reinforcement learning algorithm** used to learn the optimal action for each state in an environment. The agent interacts with the environment, performs actions, receives rewards, and updates its knowledge to maximize the total future reward.

In this scenario, a robot navigates a grid from a starting position to a goal position while avoiding an obstacle. The robot can move in four directions: up, down, left, and right.

The robot receives the following rewards:

- **+10:** Reaching the goal.
- **-5:** Attempting to move into an obstacle. The robot remains in its current state.
- **-1:** Performing a normal move.

Initially, all Q-values are set to zero. During training, the robot explores the grid and learns the best actions using the Q-learning update rule. After several episodes, the robot learns a policy that helps it reach the goal while avoiding obstacles and minimizing unnecessary movements.

### Q-Learning Formula

The Q-learning update equation is:

Q(s, a) = Q(s, a) + α [r + γ max Q(s', a') - Q(s, a)]

Where:

- **Q(s, a):** Current Q-value for taking action `a` in state `s`.
- **α (Alpha):** Learning rate, which determines how much new information affects the current Q-value.
- **r:** Immediate reward received after performing the action.
- **γ (Gamma):** Discount factor, which determines the importance of future rewards.
- **s:** Current state of the robot.
- **a:** Action taken by the robot.
- **s':** Next state reached after performing the action.
- **max Q(s', a'):** Maximum estimated Q-value among all possible actions in the next state.

### Reward Function

The reward function is defined as:

R(s, a, s') = +10, if the goal is reached

R(s, a, s') = -5, if an obstacle is encountered

R(s, a, s') = -1, for a normal move

When the robot attempts to enter an obstacle, its next state remains the same as its current state.

### Action Selection: Epsilon-Greedy Strategy

The epsilon-greedy strategy balances exploration and exploitation.

- **Exploration:** The robot selects a random action to discover new paths.
- **Exploitation:** The robot selects the action with the highest Q-value to obtain the best-known reward.

The probability of exploration is represented by epsilon (ε).

### Working Principle

1. Initialize the Q-table with zeros.
2. Set the starting state, goal state, and obstacle position.
3. Select an action using the epsilon-greedy strategy.
4. Execute the action and observe the reward and next state.
5. Update the Q-value using the Q-learning formula.
6. Repeat the process until the goal is reached or the maximum number of steps is completed.
7. Perform multiple training episodes to improve the Q-values.
8. Use the learned Q-table to determine the robot's optimal path.

## Result

The Q-learning algorithm enables the robot to learn an effective navigation policy through repeated interaction with the grid environment. The robot learns to reach the goal while avoiding obstacles and maximizing its cumulative reward.
