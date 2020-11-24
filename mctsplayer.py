from mctsconfig import MCTSConfig
import random
import numpy as np
import os

os.environ['MAIN_DIR'] = os.getenv('MAIN_DIR')


class MCTSPlayer:
    """
    Creates a Player object, which holds the genome.
    This class makes it accessible to modfiy mcts attributes.
    """
    def __init__(self):

        self.GENOME_SIZE = 5

        self.MAX_ITERATIONS = 5000
        self.MAX_CP = 5
        self.RAVE_THRESHOLD = 0.333
        self.PUCT_THRESHOLD = 0.666
        # NOTE the actual max will be this plus 500 (see update_config)
        self.MAX_TREE_SIZE = 12000
        self.MAX_MIN_VISITS = 5

        self.fitness = 0.0
        self.fitness_runs = 0

        # min visits
        # self.config = MCTSConfig(0,0,0,0,0,0)
        self.genome = np.random.uniform(
            low=0.0, high=1.0, size=(self.GENOME_SIZE))
        self.config = self.update_config()
        self.config.create_config_file()

        # don't want to generate fitness here

    def mutate(self):
        """
        Randomnly assign values to each parameter per gene 
        """
        for i in range(0,self.GENOME_SIZE):
            choice = random.randint(0,3)
            if choice == 0:
                self.genome[i] = self.genome[i]
            elif choice == 1:
                self.genome[i] = self.genome[i] - (random.random() * (self.genome[i] / 2.0))
            else:
                self.genome[i] = self.genome[i] + (random.random() * ((1.0 - self.genome[i]) / 2.0))
            
        self.config = self.update_config()

    def crossover_uniform(self, other):
        """
        For each parameter in our genome, with some probability, assign a player object another genome
        or keep it's original genome
        """
        new_player = MCTSPlayer()
        self_genome = self.get_genome()
        other_genome = other.get_genome()
        for i in range(0, self.GENOME_SIZE):
            new_player.genome[i] = other_genome[i] if random.randint(
                0, 1) == 0 else self_genome[i]
        new_player.config = new_player.update_config()

        return new_player

    def fitness(self) -> float:
        return self.fitness

    def calculate_fitness(self) -> float:
        """
        Calculate fitness for mctsplayer object through a series of function calls
        """
        self.run_config()
        prev_fitness_scaled = self.fitness * self.fitness_runs
        new_fitness = float(self.config.set_fitness()) * \
            (30.0 / float(self.config.get_seconds()))
        self.fitness = (new_fitness + prev_fitness_scaled) / \
            (self.fitness_runs + 1)
        self.fitness_runs += 1
        return self.fitness

    def __eq__(self, other):
        """
        Define equality for object for comparison in ga_main.py
        """
        return self.fitness == other.fitness

    def __lt__(self, other):
        """
        Define inequailty for comparison
        """
        return self.fitness < other.fitness

    def get_genome(self):
        return self.genome

    def get_config(self):
        return self.config

    def update_config(self):
        """
        Instantiates a MCTSConfig object with randomized arguments 
        """
        # self.config = self.config
        iterations = self.genome[0] * self.MAX_ITERATIONS
        cp = self.genome[1] * self.MAX_CP
        
        #enable our selection strategy, will default to regular UCT if value is less than RAVE_THRESHOLD
        rave = self.genome[2] >= self.RAVE_THRESHOLD and self.genome[2] < self.PUCT_THRESHOLD
        puct = self.genome[2] >= self.PUCT_THRESHOLD
        num_games = 4
        max_tree_size = int((self.genome[3] * self.MAX_TREE_SIZE) + 500)
        min_visits = int(self.genome[4] * self.MAX_MIN_VISITS)
        tmpconfig = MCTSConfig(int(iterations), cp, max_tree_size, min_visits, rave, puct, num_games)


        # self.config = tmpconfig
        return tmpconfig

    def run_config(self):
        """
        Runs the STACSettlers jar file with mctsplayer's mctsconfig object
        """
        os.chdir(os.getenv('MAIN_DIR') + "StacSettlers/target")
        """ Take a MCTSConfig and run the specified simulation """
        config_file = self.config.get_config_path()
        print(config_file)
        # Might cause concurrent errors
        stream = os.popen(
            "java -cp STACSettlers-1.0-bin.jar soc.robot.stac.simulation.Simulation " + config_file).read()

    def __str__(self):
        return "[" + str(self.config.iterations) + ", " + str(self.config.cp) + ", " + str(self.config.max_tree_size) + ", " + str(self.fitness) + "]"
