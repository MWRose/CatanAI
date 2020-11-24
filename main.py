"""
Test different parameters in the MCTS package using the repo found at
https://github.com/sorinMD/StacSettlers

Requires a ./config folder and a ./results folder
Generates files config files in ./config showing the various configurations
Output csv files in the ./results folder with the results of the given test
"""

from typing import Iterable
from mctsconfig import MCTSConfig
import os
import matplotlib.pyplot as plt
import csv


os.environ['MAIN_DIR'] = os.getenv('MAIN_DIR')
configs_directory = os.getenv('MAIN_DIR') + "CatanAI/configs/"


def run_config(config: MCTSConfig):
    """ Take a MCTSConfig and run the specified simulation """
    config_file = config.get_config_path()
    # Might cause concurrent errors
    stream = os.popen(
        "java -cp STACSettlers-1.0-bin.jar soc.robot.stac.simulation.Simulation " + config_file).read()



def test_iterations(iters):
    """
    Loop through iters (tuple of iterations) and run them
    and return the updated config file
    """
    mcts_config_iterations = []
    for iterations in iters:

        # Create new config and run it
        mcts_config = MCTSConfig(iterations, .5, 1000000, 1, False, False, 30)
        run_config(mcts_config)

        # Make sure the fitness is set
        mcts_config.set_fitness()
        mcts_config_iterations.append(mcts_config)

    fitnesses = []
    iteration = []
    games = []
    seconds = []
    turns = []
    for config in mcts_config_iterations:
        fitnesses.append(config.get_fitness())
        iteration.append(config.get_min_visits())
        games.append(config.get_num_games())
        seconds.append(config.get_seconds())
        turns.append(config.get_turns())

    with open(os.getenv('MAIN_DIR') + "CatanAI/results/fitnesses.csv", "w", newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(
            ["iterations", "fitness", "games", "seconds", "turns"])
        for i in range(len(fitnesses)):
            spamwriter.writerow(
                [iteration[i], fitnesses[i], games[i], seconds[i], turns[i]])

    plt.plot(iteration, fitnesses)
    plt.xlabel("Iterations")
    plt.ylabel("Win Rate")
    plt.show()


def test_min_visits(iters):
    """
    Loop through iters (tuple of min visit vals) and run them
    and return the updated config file
    """
    mcts_config_min_visits = []
    for min_visit in iters:

        # Create new config and run it
        mcts_config = MCTSConfig(
            2000, .5, 1000000, min_visit, False, False, 30)
        run_config(mcts_config)

        # Make sure the fitness is set
        mcts_config.set_fitness()
        mcts_config_min_visits.append(mcts_config)

    fitnesses = []
    min_visits = []
    games = []
    seconds = []
    turns = []
    for config in mcts_config_min_visits:
        fitnesses.append(config.get_fitness())
        min_visits.append(config.get_min_visits())
        games.append(config.get_num_games())
        seconds.append(config.get_seconds())
        turns.append(config.get_turns())

    with open(os.getenv('MAIN_DIR') + "CatanAI/results/fitnesses.csv", "w", newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(
            ["min_visits", "fitness", "games", "seconds", "turns"])
        for i in range(len(fitnesses)):
            spamwriter.writerow(
                [min_visits[i], fitnesses[i], games[i], seconds[i], turns[i]])

    plt.plot(min_visits, fitnesses)
    plt.xlabel("Min Visits")
    plt.ylabel("Win Rate")
    plt.show()


def test_cp(cps):
    """
    Loop through cps (tuple of min visit vals) and run them 
    and generate a csv file for the results
    """
    mcts_configs_cp = []
    for cp in cps:

        # Create new config and run it
        mcts_config = MCTSConfig(2000, cp, 10000, 1, False, False, 20)
        run_config(mcts_config)

        # Make sure the fitness is set
        mcts_config.set_fitness()
        mcts_configs_cp.append(mcts_config)

    fitnesses = []
    cps = []
    games = []
    seconds = []
    turns = []
    for config in mcts_configs_cp:
        fitnesses.append(config.get_fitness())
        cps.append(config.get_cp())
        games.append(config.get_num_games())
        seconds.append(config.get_seconds())
        turns.append(config.get_turns())

    with open(os.getenv('MAIN_DIR') + "CatanAI/results/fitnesses.csv", "w", newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(
            ["cp", "fitness", "games", "seconds", "turns"])
        for i in range(len(fitnesses)):
            spamwriter.writerow(
                [cps[i], fitnesses[i], games[i], seconds[i], turns[i]])

    plt.plot(cps, fitnesses)
    plt.xlabel("Exploration Constant")
    plt.ylabel("Win Rate")
    plt.show()


# call our ga() function here
def main():
    # Set directory to the StacSettlers target directory
    os.chdir(os.getenv('MAIN_DIR') + "StacSettlers/target")

    ### TESTS ###
    # Iteration Test
    test_iterations(range(200, 2000, 200))

    # Exploration Parameter Test
    # test_cp(range(0,2,.2))

    # Min Visit Test
    # test_min_visits(range(1, 21, 2))
    
if __name__ == "__main__":
    main()
