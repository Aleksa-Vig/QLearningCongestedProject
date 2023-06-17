import gym
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Flatten
from keras.optimizers import Adam
from rl.agents.dqn import DQNAgent
from rl.policy import EpsGreedyQPolicy
from rl.memory import SequentialMemory
from Calculator.envs import CBR_Env

# Sample Program for testing CBR Calculating with Deep Q Learning environment - Brandon Mailloux

# Setting up the environment with episode and iteration lengths.
env = CBR_Env.CBREnv()
num_episodes = 30
max_timesteps = 1000

# Getting the number of actions from the environment
nb_actions = env.action_space.n
# Define the input shape for the neural network model
input_shape = (1,) + env.observation_space.shape

# Define the neural network model architecture
model = Sequential()
model.add(Flatten(input_shape=input_shape))
model.add(Dense(64, activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(nb_actions, activation='linear'))

# Create the epsilon-greedy exploration policy
policy = EpsGreedyQPolicy()

# Create a sequential memory to store experiences for the DQN agent
memory = SequentialMemory(limit=10000, window_length=1)

# Initialize the DQN agent with the model, policy, and memory
dqn = DQNAgent(model=model, nb_actions=nb_actions, memory=memory, nb_steps_warmup=1000,
               target_model_update=1e-2, policy=policy)

# Compile the DQN agent with an Adam optimizer and mean absolute error (MAE) metric
dqn.compile(Adam(learning_rate=1e-3), metrics=['mae'])

# Fit the DQN agent on the environment for a specified number of steps
dqn.fit(env, nb_steps=max_timesteps * num_episodes, verbose=1)

# Close the environment
env.close()