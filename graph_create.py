"""
Script for creating visualizations of the results from different parameters.
Set csv_file_name to the folder containing the generated csv
"""


import csv
from matplotlib import pyplot as plt

columnone = []
fitness = []
games = []
seconds = []
turns = []

csv_file_name = "./results/min_visits.csv"
with open(csv_file_name, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",", quotechar="|")
    next(csvreader)

    # Add necessary information
    for row in csvreader:
        columnone.append(round(float(row[0]), 2))
        fitness.append(round(float(row[1]), 2))
        games.append(round(float(row[2]), 2))
        seconds.append(round(float(row[3]) / games[0], 2))
        turns.append(round(float(row[4]), 2))

    
    ### ITERATIONS ###
    # plt.plot(columnone, fitness, "-o")
    # plt.title("Win Rates for Iterations")
    # plt.xlabel("Iterations")
    # plt.ylabel("Win Rate ({} games)".format(int(games[0])))
    # plt.gca().set_ylim([0, 1])
    # plt.show()

    # plt.plot(columnone, turns, "-o")
    # plt.title("Average Turns for Different Iterations")
    # plt.xlabel("Iterations")
    # plt.ylabel("Average Turns ({} games)".format(int(games[0])))
    # plt.show()

    # plt.plot(columnone, seconds, "-o")
    # plt.title("Average Game Time for Different Iterations")
    # plt.xlabel("Iterations")
    # plt.ylabel("Average time (seconds)")
    # plt.show()


    ### EXPLOTARTION PARAMETER ###
    # plt.plot(columnone, fitness, "-o")
    # plt.title("Win Rates for Different Exploration Constant")
    # plt.xlabel("Exploration Constant")
    # plt.ylabel("Win Rate ({} games)".format(int(games[0])))
    # plt.gca().set_ylim([0, 1])
    # plt.show()

    # plt.plot(columnone, turns, "-o")
    # plt.title("Average Turns for Different Exploration Constants")
    # plt.xlabel("Exploration Constant")
    # plt.ylabel("Average Turns ({} games)".format(int(games[0])))
    # plt.show()

    # plt.plot(columnone, seconds, "-o")
    # plt.title("Average Game Time for Different Exploration Constants")
    # plt.xlabel("Exploration Constant")
    # plt.ylabel("Average time (seconds)")
    # plt.show()


    ### MIN VISITS ###
    # plt.plot(columnone, fitness, "-o")
    # plt.title("Win Rates for Different Minimum Visits")
    # plt.xlabel("Minimum Visits")
    # plt.ylabel("Win Rate ({} games)".format(int(games[0])))
    # plt.gca().set_ylim([0, 1])
    # plt.show()


    


