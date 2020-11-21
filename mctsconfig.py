from datetime import datetime
import os
import pandas as pd
import glob

configs_directory = "/home/max/Documents/ai/CatanAI/configs/"

class MCTSConfig:
    """Creates an holds an MCTS config"""

    def __init__(self, iterations: int, cp: float,
                 max_tree_size: int, min_visits: int, rave: bool, num_games: int):
        self.iterations = iterations
        self.cp = cp
        self.max_tree_size = max_tree_size
        self.min_visits = min_visits
        self.rave = rave
        self.mcts_line = ""
        self.name = str(datetime.now().time())
        self.config_path = configs_directory + self.name
        self.num_games = num_games
        self.fitness = 0.0
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
            self.mcts_line += "|MCTS_UCT_RAVE"
            

    def create_config_file(self):

        # Structure of the config file
        assert self.mcts_line, "MCTS Line not created"
        lines = [
            "Games=" + str(self.num_games),
            "Log=false",
            "UseParser=false",
            "ChatNegotiation=true",
            "FullyObservable=true",
            "PlayerToStart=-1",
            "~",
            self.name,
            self.mcts_line,
            "Agent=3,Stac,stac,TRY_N_BEST_BUILD_PLANS:0|FAVOUR_DEV_CARDS:-5"
        ]

        # If there is a file path write it
        assert self.config_path, "File path not specified for config {}".format(self.name)
        with open(self.config_path, "w") as config_file:
            join_lines = "\n".join(lines)
            config_file.write(join_lines)

    def set_fitness(self):
        """ Takes a MCTSConfig and returns its fitness (win rate)"""
        file_name = glob.glob('results/'+ self.get_name() + '*' + '/results.txt')[0]
        num_games = self.get_num_games()
        # Look in results folder for this name
        df = pd.read_csv('/home/max/Documents/ai/StacSettlers/target/' + file_name, sep='\t')
        total_wins = sum(df['Winner1'])
        self.fitness = total_wins/num_games

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



def main():
    pass

if __name__ == "__main__":
    main()
