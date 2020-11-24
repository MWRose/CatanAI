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

def ga(env: Environment, pop_count: int, keep: float, select: float, steps: int):
    pop = env.create_population
    pop_with_fitness = []
    new_pop = []

    for i in range(0, steps):
        for individual in pop:
            f = individual.calculate_fitness()
            pop_with_fitness.append({'pop_index': i, 'fitness': f})

        pop_with_fitness = sorted(pop_with_fitness, key=itemgetter('fitness'), reverse=True)

        pop, new_pop = new_pop, pop
def evolve_step(pop, new_pop, env, rng, keep, select):
    new_pop.clear()
    keep_val = int(pop.len() * keep)

    #add all 0..keep values from pop to new pop

    #add the rest via mutation, crossover and randoms

def main():
    POP = 16 #population size
    KEEP = 0.125 #percentage of best MCTSIndividuals we keep
    SELECT = 0.75 #portion of new pop we generate with mutate + crossover
    STEPS = 10 #number of times we generate a new population