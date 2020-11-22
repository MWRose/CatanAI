from mctsconfig import MCTSConfig
import random
import numpy as np

class MCTSPlayer:
    def __init__(self):

        MAX_ITERATIONS = 10000
        MAX_CP = 5
        RAVE_THRESHOLD = 0.333
        PUCT_THRESHOLD = 0.666
        GENOME_SIZE = 3


        self.config = MCTSConfig(0,0,0,0,0,0)
        self.genome = np.random.uniform(low=0.0, high=1.0, size=(GENOME_SIZE))
        self.update_config()
        self.config.create_config_file
        # don't want to generate fitness here
        

    def mutate(self):
        for i in range(0,self.GENOME_SIZE):
            self.genome[i] = random.random() if random.randint(0,1) == 0 else self.genome[i]
        self.update_config()

    def crossover_uniform(self, other):
        new_player = MCTSPlayer()

        for i in range(0,self.GENOME_SIZE):
            new_player.genome[i] = other.genome[i] if random.randint(0,1) == 0 else self.genome[i]
        new_player.update_config()

    def fitness(self) -> float:
        return self.fitness

    def calculate_fitness(self):
        #run the simulations
        fitness = self.config.set_fitness()

    def update_config(self):
        config = self.config
        config.iterations = self.genome[0] * self.MAX_ITERATIONS
        config.cp = self.genome[1] * self.MAX_CP
        
        #enable our selection strategy, will default to regular UCT if value is less than RAVE_THRESHOLD
        config.rave = self.genome[2] >= self.RAVE_THRESHOLD and self.genome[2] < self.PUCT_THRESHOLD
        config.puct = self.genome[2] >= self.PUCT_THRESHOLD



        
