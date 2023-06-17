#Open AI GYM Environment for calculating CBR - Brandon Mailloux
import gym
import math
import numpy as np
from gym import spaces

class CBREnv(gym.Env):
    def __init__(self):

        #Vehicle density: 1-50 number of vehicles
        #Beacon interval: 0.11-150 ACTION 
        #Theoretically CBR is 0%-100% 

        #State made up of CBR and Vehicle density
        # [Vehicle density, cbr], beacon interval

        # Action space: from 0.11 to 1.50, step 0.01
        self.action_space = spaces.Discrete(140)

        # State space: vehicle_density and beacon_interval
        self.observation_space = spaces.Box(low=0, high=np.inf, shape=(2,), dtype=np.float32)

    #Initializing vehicle density and beacon interval to calculate CBR with
    def initialize_state(self):
        vehicle_density = 0.5  
        beacon_interval = 5 
        return np.array([vehicle_density, beacon_interval])
    
    def step(self, action):
        # Convert action index to value in the range 0.11 to 1.50
        #action_value is new beacon interval calculated during step
        action_value = 0.11 + action * 0.01

        # Calculate CBR based on the current state (vehicle_density and beacon_interval)
        vehicle_density, beacon_interval = self.state

        print(action_value)
        print(beacon_interval)

        # CBR is calucalated on the new beacon inteverval 
        cbr = self.calculate_cbr(vehicle_density, action_value)

        # Calculate reward and check if the episode is done. Checking if CBR Matches the action value
        reward, done = self.calculate_reward(cbr, beacon_interval)

        # Update the state  THIS SHOULD BE VEHICLE DENISTY, BEACON INTERVAL, CBR
        self.state = self.update_state(action_value, beacon_interval)

        return self.state, reward, done, {}

    
    def reset(self):
        # Initialize the environment state
        self.state = self.initialize_state()
        return self.state

    def render(self, mode='human'):
        pass

    def close(self):
        pass
    
    #CBR = Channel busy ratio
    #Function to approximate CBR by Ben
    def calculate_cbr(self, density, beacon_interval):
        cbr = 0
        a = 0.0095*density + 0.0304
        b = 0.0208*(math.log(density)/math.log(math.e)) - 1.0296
        cbr = a*(beacon_interval**b)
        return cbr
		

    def calculate_reward(self, cbr, beacon_interval):
        # My function to calculate reward based on the difference between the approximate CBR and the action state

        #We should add vehicle density in this formula
        eta = 0.6
        reward = beacon_interval * cbr * ((eta - cbr)/abs(eta - cbr))
        done = (reward == 1)
        if done:
            print("FINISHED")
        return reward, done
    

    # New state definition vehicle_density, beacon_interval, and vehicle density 
    # TODO include cbr in state
    # Update new current vehicle density randomly --> change vehicle density by 1 or 2

    def update_state(self, vehicle_density, beacon_interval):
        # Maintaining vehicle density and interval between states, can be changed in a more practical environment
        new_vehicle_density = vehicle_density 
        new_beacon_interval = beacon_interval  
        return np.array([new_vehicle_density, new_beacon_interval])


