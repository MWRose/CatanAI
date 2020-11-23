from mctsconfig import MCTSConfig
import random
import numpy as np
import os

os.environ['MAIN_DIR'] = os.getenv('MAIN_DIR') 

class MCTSPlayer:
    def __init__(self):

        self.GENOME_SIZE = 3

        self.MAX_ITERATIONS = 10000
        self.MAX_CP = 5
        self.RAVE_THRESHOLD = 0.333
        self.PUCT_THRESHOLD = 0.666
    
        self.fitness = 0.0

        #min visits
        # self.config = MCTSConfig(0,0,0,0,0,0)
        self.genome = np.random.uniform(low=0.0, high=1.0, size=(self.GENOME_SIZE))
        self.config = self.update_config()
        self.config.create_config_file()
        
        # don't want to generate fitness here
        

    def mutate(self):
        for i in range(0,self.GENOME_SIZE):
            self.genome[i] = random.random() if random.randint(0,1) == 0 else self.genome[i]
        self.config = self.update_config()

    def crossover_uniform(self, other):
        new_player = MCTSPlayer()

        for i in range(0,self.GENOME_SIZE):
            new_player.genome[i] = other.genome[i] if random.randint(0,1) == 0 else self.genome[i]
        new_player.config = new_player.update_config()

    def fitness(self) -> float:
        return self.fitness

    def calculate_fitness(self):
        #run the simulations
        self.run_config()
        self.fitness = self.config.set_fitness()

    def __eq__(self, other):
        return self.fitness == other.fitness

    def __lt__(self, other):
        return self.fitness < other.fitness

    def update_config(self):
        # self.config = self.config
        iterations = self.genome[0] * self.MAX_ITERATIONS
        cp = self.genome[1] * self.MAX_CP
        
        #enable our selection strategy, will default to regular UCT if value is less than RAVE_THRESHOLD
        rave = self.genome[2] >= self.RAVE_THRESHOLD and self.genome[2] < self.PUCT_THRESHOLD
        puct = self.genome[2] >= self.PUCT_THRESHOLD
        num_games = 4
        tmpconfig = MCTSConfig(int(iterations), cp, 10000, 1, rave, puct, num_games)
        # self.config = tmpconfig
        return tmpconfig

    def run_config(self):

        os.chdir(os.getenv('MAIN_DIR') + "StacSettlers/target")
        """ Take a MCTSConfig and run the specified simulation """
        config_file = self.config.get_config_path()
        print(config_file)
        # Might cause concurrent errors
        stream = os.popen("java -cp STACSettlers-1.0-bin.jar soc.robot.stac.simulation.Simulation " + config_file).read()

    def __str__(self):
        return "[" + str(self.config.iterations) + ", " + str(self.config.cp) + ", " +  str(self.config.max_tree_size) + ", " + str(self.fitness) + "]"

        
