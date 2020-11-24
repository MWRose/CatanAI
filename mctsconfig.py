from datetime import datetime
import os
import pandas as pd
import glob

os.environ['MAIN_DIR'] = "/Users/evanvonoehsen/Documents/ai/"
configs_directory = os.getenv('MAIN_DIR') + "CatanAI/configs/"

class MCTSConfig:
    """
    Creates an holds an MCTS config.
    Keeps track of different MCTS parameters and where they are stored.
    """

    def __init__(self, iterations: int, cp: float,
                 max_tree_size: int, min_visits: int, rave: bool, puct: bool, num_games: int):
        self.iterations = iterations
        self.cp = cp
        self.max_tree_size = max_tree_size
        self.min_visits = min_visits
        self.rave = rave
        self.puct = puct
        self.mcts_line = ""
        self.name = str(datetime.now().time())
        self.config_path = configs_directory + self.name
        self.num_games = num_games
        self.fitness = 0.0
        self.seconds = 0
        self.turns = 0
        self.create_mcts_line()
        self.create_config_file()


    def create_mcts_line(self):
        """
        Creates the line to be added to the config file
        """
        
        # Configure the line to be added to the config file
        self.mcts_line = "Agent=1,TypedMCTS,mcts,MCTS_ITERATIONS:{iterations}|MCTS_THREADS:4|MCTS_Cp:{cp}|MCTS_TYPED_ROLLOUTS|MCTS_MINVISITS:{min_visits}|MCTS_MAX_TREE_SIZE:{max_tree_size}|MCTS_OFFERS_LIMIT:3".format(
              iterations=self.iterations, cp=self.cp, min_visits=self.min_visits, max_tree_size=self.max_tree_size)
        if self.rave:
            self.mcts_line += "|MCTS_UCT_RAVE:3"
        elif self.puct:
            self.mcts_line += "|MCTS_PUCT"

            
    def create_config_file(self):
        """
        Generates a config file for the run in the ./config folder
        """

        # Structure of the config file
        assert self.mcts_line, "MCTS Line not created"
        lines = [
            "Games=" + str(self.num_games),
            "Log=false",
            "UseParser=false",
            "ChatNegotiation=true",
            "FullyObservable=true",
            "PlayerToStart=0",
            "~",
            self.name,
            self.mcts_line,
            "Agent=3,Random,random"
        ]

        # If there is a file path write it
        assert self.config_path, "File path not specified for config {}".format(self.name)
        with open(self.config_path, "w") as config_file:
            join_lines = "\n".join(lines)
            config_file.write(join_lines)


    def set_fitness(self):
        """
        Takes a MCTSConfig and returns its fitness (win rate)
        """

        file_name = glob.glob('results/'+ self.get_name() + '*' + '/summary.txt')[0]
        print("glob found results file:")
        print(file_name)

        with open(file_name, "r") as file:
            lines = file.readlines()
            self.games = lines[0].strip()[6:]
            self.seconds = lines[1].strip()[8:]
            self.turns = lines[2].strip()[15:]
            for line in lines:
                line_sep = line.split()
                if len(line_sep) > 0 and line_sep[0] == "TypedMCTS":
                    self.fitness = float(line_sep[1])
                    break

        return self.fitness


    def get_iterations(self):
        return self.iterations

    def get_cp(self):
        return self.cp

    def get_max_tree_size(self):
        return self.max_tree_size

    def get_min_visits(self):
        return self.min_visits

    def get_rave(self):
        return self.rave

    def get_num_games(self):
        return self.num_games

    def get_config_path(self):
        return self.config_path

    def get_name(self):
        return self.name

    def get_fitness(self):
        return self.fitness

    def get_seconds(self):
        return self.seconds

    def get_turns(self):
        return self.turns

    def set_puct(self, puct):
        self.puct = puct
