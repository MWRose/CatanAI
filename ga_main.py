from typing import Iterable
from mctsconfig import MCTSConfig
from environment import Environment
from mctsplayer import MCTSPlayer
from operator import itemgetter
import subprocess
import os
import pandas as pd
import numpy as np
import glob
import matplotlib.pyplot as plt
import csv
import random

def ga(env, pop_count, keep, select, steps):
    with open(os.getenv('MAIN_DIR') + "CatanAI/results/fitnesses.csv", "w", newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["Iterations", "Name", "Fitness", "Games", "Seconds", "Turns"])

    pop = env.create_population()
    for ind in pop:
        print(ind.genome)
    new_pop = []
    fitnesses = []

    for i in range(0, steps):
        round_fitnesses = []
        print("new step: " + str(i))
        for j in range(0,len(pop)):
            individual = pop[j]
            fitness = individual.calculate_fitness()
            config = individual.get_config()
            seconds = config.get_seconds()
            
            round_fitnesses.append(fitness)
            
            write_csv(str(i), str(config.get_name()), str(fitness), str(config.get_iterations()), str(seconds), str(config.get_turns())) # round, name, fitness, itereations, seconds, turns
            print("individual with genome: " + str(individual.genome))
            print("fitness for bot " + str(j) + "in step " + str(i)+ ": " + str(fitness))
        fitnesses.append(round_fitnesses)
        
        pop.sort(reverse=True)
        evolve_step(pop, new_pop, env, keep, select)
        pop, new_pop = new_pop, pop

        
    
    for individual in pop:
        individual.calculate_fitness()
    pop = sorted(pop)
    print("Fitnesses:")
    print(round_fitnesses)
    return pop
        
        
def evolve_step(pop, new_pop, env, keep, select):
    new_pop.clear()
    keep_amt = int(len(pop) * keep)

    for i in range(0,keep_amt):
        new_pop.append(pop[i])

    selection_amt = int(len(pop) * select)

    for _ in range(0, selection_amt):
        selections = selection(pop, 4)
        child = selections[0].crossover_uniform(selections[1])
        child.mutate()
        new_pop.append(child)
    
    for _ in range(len(new_pop), len(pop)):
        new_pop.append(MCTSPlayer())

    assert len(pop) == len(new_pop)


# randomly select k competitors and select the strongest one
def selection(pop, k):
    # TODO: make better my just sorting
    competitors = random.sample(pop, k)
    competitors.sort(reverse=True)
    return [competitors[0], competitors[1]]

def write_csv(round_num, name, fitness, iterations, seconds, turns):
    with open(os.getenv('MAIN_DIR') + "CatanAI/results/fitnesses.csv", "a") as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([round_num, name, fitness, iterations, seconds, turns])

def main():
    POP = 4 #population size
    KEEP = 0.25 #percentage of best MCTSIndividuals we keep
    SELECT = 0.5 # portion of new pop we generate with mutate + crossover
    STEPS = 2 #number of times we generate a new population

    env = Environment(POP)

    end_pop = ga(env, POP, KEEP, SELECT, STEPS)
    #print("Ending population: ", end_pop)


if __name__ == "__main__":
    main()


