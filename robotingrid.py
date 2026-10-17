import numpy as np
import random
ROWS, COLS = 5, 5
START = (0, 0)
GOAL = (4, 4)
OBSTACLE = (2, 2)
ACTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
ACTION_NAMES = ["Up", "Down", "Left", "Right"]
Q = np.zeros((ROWS, COLS, len(ACTIONS)))
alpha = 0.1   
gamma = 0.9      
epsilon = 0.2   
episodes = 2000
max_steps = 100
def move(state, action):
    r, c = state
    dr, dc = ACTIONS[action]
    next_state = (r + dr, c + dc)
    if not (0 <= next_state[0] < ROWS and
            0 <= next_state[1] < COLS):
        return state, -1, False
    if next_state == OBSTACLE:
        return state, -5, False
    if next_state == GOAL:
        return next_state, 10, True
    return next_state, -1, False
for episode in range(episodes):
    state = START
    for step in range(max_steps):
        r, c = state
        if random.random() < epsilon:
            action = random.randint(0, 3)
        else:
            action = np.argmax(Q[r, c])
        next_state, reward, done = move(state, action)
        nr, nc = next_state
        Q[r, c, action] += alpha * (
            reward + gamma * np.max(Q[nr, nc])
            * (not done) - Q[r, c, action]
        )
        state = next_state
        if done:
            break
print("Learned Policy:")
symbols = ["↑", "↓", "←", "→"]
for r in range(ROWS):
    for c in range(COLS):
        state = (r, c)
        if state == START:
            print(" S ", end="")
        elif state == GOAL:
            print(" G ", end="")
        elif state == OBSTACLE:
            print(" X ", end="")
        else:
            print(f" {symbols[np.argmax(Q[r, c])]} ", end="")
    print()
print("\nQ-values at the starting position:")
for i, name in enumerate(ACTION_NAMES):
    print(f"{name}: {Q[START[0], START[1], i]:.3f}")
print("\nRobot's path:")
state = START
path = [state]
for _ in range(ROWS * COLS * 2):
    if state == GOAL:
        break
    r, c = state
    action = np.argmax(Q[r, c])
    state, reward, done = move(state, action)
    path.append(state)
    if done:
        break
print(" -> ".join(map(str, path)))
if state == GOAL:
    print("Goal reached successfully!")
else:
    print("Goal not reached.")