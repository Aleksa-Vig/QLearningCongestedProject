import Environment

import Environment

import pickle
import gymnasium as gym
import random
import numpy as np

# env = gym.make('Taxi-v3')

# Create a Qtable of 500 x 6
q_table = np.zeros([env.observation_space.n, env.action_space.n]) # type: ignore

# reset environment to a new, random state
# Hyperparameters
alpha = 0.1 #learning rate
gamma = 0.9 #discount factor
epsilon = 0.1 #the exploration rate

# For plotting metrics
all_epochs = []
all_penalties = []

print("training started...")

for i in range(1, 100000):
    state = env.reset() #state[0] gives state number
    currentStateNumber = state[0]

    epochs, reward, = 0, 0
    terminated = False
    
    while not terminated:
        if random.uniform(0, 1) < epsilon:
            action = env.action_space.sample() # Explore action space
        else:
            action = np.argmax(q_table[currentStateNumber]) # Exploit learned values

        # next_state, reward, done, info = env.step(action) 
        next_state, reward, terminated, truncated, info = env.step(action)
        
        #get the old q value of the state we just moved from
        old_value = q_table[currentStateNumber, action]
        next_max = np.max(q_table[next_state])
        
        #create the new qvalue for the state we just visited
        new_value = (1 - alpha) * old_value + alpha * (reward + gamma * next_max)
        q_table[currentStateNumber, action] = new_value

        currentStateNumber = next_state
        epochs += 1

print("Training finished.\n")

with open('q_table.pickle', "wb") as f:
        pickle.dump(q_table, f)