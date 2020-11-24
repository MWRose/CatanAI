"""
Test different parameters in the MCTS package using the repo found at
https://github.com/sorinMD/StacSettlers

Requires a ./config folder and a ./results folder
Generates files config files in ./config showing the various configurations
Output csv files in ./results with the results of the given test

More specific information from each run can be found in the
StacSettlers target/results folder
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
    and generate a csv file of the results
    """
    mcts_config_iterations = []
    for iterations in iters:

        # Create new config and run it
        mcts_config = MCTSConfig(iterations, .5, 1000000, 1, False, False, 30)
        run_config(mcts_config)

        # Make sure the fitness is set
        mcts_config.set_fitness()
        mcts_config_iterations.append(mcts_config)
    
    write_to_csv("iterations")

def test_min_visits(iters):
    """
    Loop through iters (tuple of min visit vals) and run them
    and generate a csv file of the results
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

    write_to_csv("min_visits")


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
    
    write_to_csv("cp")


def write_to_csv(test_name, configs):
    # Create value lists to be added to the csv
    fitnesses = []
    test_type = []
    games = []
    seconds = []
    turns = []
    for config in configs:
        fitnesses.append(config.get_fitness())
        test_type.append(config.get_cp())
        games.append(config.get_num_games())
        seconds.append(config.get_seconds())
        turns.append(config.get_turns())
    # Write to the csv
    with open(os.getenv('MAIN_DIR') + "CatanAI/results/" + test_name + ".csv", "w", newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(
            [test_name, "fitness", "games", "seconds", "turns"])
        for i in range(len(fitnesses)):
            spamwriter.writerow(
                [test_type[i], fitnesses[i], games[i], seconds[i], turns[i]])

    plt.plot(test_name, fitnesses)
    title = ""
    if test_name == "iterations":
        title = "Iterations"
    elif test_name == "cp":
        title = "Exploration Constant"
    elif test_name == "min_visits":
        title = "Min Visits"
    plt.xlabel(title)
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
