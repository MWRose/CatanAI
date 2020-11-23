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
    pop = env.create_population()
    for ind in pop:
        print(ind.genome)
    new_pop = []

    for i in range(0, steps):
        print("new step: " + str(i))
        for individual in pop:
            fitness = individual.calculate_fitness()
            print("individual with genome: " + str(individual.genome))
            print("fitness: " + str(fitness))
        
        pop.sort()
        evolve_step(pop, new_pop, env, keep, select)
        pop, new_pop = new_pop, pop
    
    for individual in pop:
        individual.calculate_fitness()
    pop = sorted(pop)

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
    competitors.sort()
    return [competitors[0], competitors[1]]


def main():
    POP = 4 #population size
    KEEP = 0.25 #percentage of best MCTSIndividuals we keep
    SELECT = 0.5 # portion of new pop we generate with mutate + crossover
    STEPS = 2 #number of times we generate a new population

    env = Environment(POP)
    # print("Starting population: ", env)
    # for p in env:
    #     print(p)
    #new_pop
    end_pop = ga(env, POP, KEEP, SELECT, STEPS)
    print("Ending population: ", end_pop)


if __name__ == "__main__":
    main()