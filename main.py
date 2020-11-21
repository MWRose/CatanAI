from typing import Iterable
from mctsconfig import MCTSConfig
import subprocess
import os
import pandas as pd
import numpy as np
import glob
import matplotlib.pyplot as plt

configs_directory = "/home/max/Documents/ai/CatanAI/configs/"
ITERATION_RANGE = 1000


def simulate(args) -> int:
    #run_config()
    #parse_result()
    pass

def run_config(config: MCTSConfig):
    """ Take a MCTSConfig and run the specified simulation """
    config_file = config.get_config_path()

    # Might cause concurrent errors
    stream = os.popen("java -cp STACSettlers-1.0-bin.jar soc.robot.stac.simulation.Simulation " + config_file).read()
 
# def parse_result(config: MCTSConfig) -> float:
#     """ Takes a MCTSConfig and returns its fitness (win rate)"""
#     file_name = glob.glob('results/'+ config.get_name() + '*' + '/results.txt')[0]
#     num_games = config.get_num_games()
#     # Look in results folder for this name
#     df = pd.read_csv('/home/max/Documents/ai/StacSettlers/target/' + file_name, sep='\t')
#     total_wins = sum(df['Winner1'])
#     win_rate = total_wins/num_games
#     return win_rate


# Iterations test
def test_iterations(iters):
    mcts_config_iterations = []
    for iterations in iters:
        mcts_config = MCTSConfig(iterations, .5, 100000, 1, False, 5)
        run_config(mcts_config)
        mcts_config.set_fitness()
        mcts_config_iterations.append(mcts_config)

    return mcts_config_iterations

# def test_cp(cps):
#     mcts_configs_cp = []
#     for cp in cps:
#         mcts_config = MCTSConfig(2000, cp, 10000, 1, False, 10)
#         run_config(mcts_config)
#         mcts_config.set_fitness()

#     return mcts_configs_cp
    

# call our ga() function here
def main():
    os.chdir("/home/max/Documents/ai/StacSettlers/target")
    # print(os.getcwd())
    # simulate('../StacSettlers/target/config-simple.txt')
    iteration_configs = test_iterations([3000, 5000])
    fitnesses = []
    iterations = []
    for config in iteration_configs:
        fitnesses.append(config.get_fitness())
        iterations.append(config.get_iterations())
    
    plt.plot(iterations, fitnesses)
    plt.xlabel("Iterations")
    plt.ylabel("Win Rate")
    plt.show()

    # Exploration test
    # test_cp(range(0, 1, .1))


if __name__ == "__main__":
    main()