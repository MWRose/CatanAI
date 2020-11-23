from typing import Iterable
from mctsconfig import MCTSConfig
import subprocess
import os
import pandas as pd
import numpy as np
import glob
import matplotlib.pyplot as plt
import csv

"""
- Continue collecting data from MCTS vs Stac
    - Cons: Takes forever, Isn't consistent
    - Pros: Most specific to our task in that it compares MCTS changes
            There might be some learning techniques we can modify

- Create a StacSettler Config file and use that to do a genetic algorithm to optimize
    - Cons: Doesn't include MCTS (would have to pair it with above option)
    - Pros: Is an ai system that we can write and talk about strategically
            tailored mroe directly to Catan and might give more presentable data
            
- Run Original MCTS package
    - Cons: Can't match up opponents wtih different strategies
    - Pros: Runs fast, lots of transparency in the code
"""
os.environ['MAIN_DIR'] = os.getenv('MAIN_DIR') 
configs_directory = os.getenv('MAIN_DIR') + "CatanAI/configs/"
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
#     df = pd.read_csv('os.getenv('MAIN_DIR') + "StacSettlers/target/' + file_name, sep='\t')
#     total_wins = sum(df['Winner1'])
#     win_rate = total_wins/num_games
#     return win_rate


# Iterations test
def test_iterations(iters):
    mcts_config_iterations = []
    for iterations in iters:
        mcts_config = MCTSConfig(iterations, .5, 1000000, 1, False, 1)
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
    os.chdir(os.getenv('MAIN_DIR') + "StacSettlers/target")
    # print(os.getcwd())
    # simulate('../StacSettlers/target/config-simple.txt')
    iteration_configs = test_iterations(range(100, 300, 100))
    fitnesses = []
    iterations = []
    games = []
    seconds = []
    turns = []
    for config in iteration_configs:
        fitnesses.append(config.get_fitness())
        iterations.append(config.get_iterations())
        games.append(config.get_num_games())
        seconds.append(config.get_seconds())
        turns.append(config.get_turns())

    with open(os.getenv('MAIN_DIR') + "CatanAI/results/fitnesses.csv", "w", newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(["iterations", "fitness", "games", "seconds", "turns"])
        for i in range(len(fitnesses)):
            spamwriter.writerow([iterations[i], fitnesses[i], games[i], seconds[i], turns[i]])

    plt.plot(iterations, fitnesses)
    plt.xlabel("Iterations")
    plt.ylabel("Win Rate")
    plt.show()

    


    # Exploration test
    # test_cp(range(0, 1, .1))


if __name__ == "__main__":
    main()