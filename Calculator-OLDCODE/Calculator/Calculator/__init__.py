from gym.envs.registration import register
from Calculator.envs import CBR_Env

env = CBR_Env.CBREnv()
register(
    id='CBRFinder-v0',
    entry_point=env
)