
class MCTSConfig:
    """Creates an holds an MCTS config"""

    def __init__(self, iterations: int, cp: float, max_tree_size: int, min_visits: int, rave: bool):
        self.iterations = iterations
        self.cp = cp
        self.max_tree_size = max_tree_size
        self.min_visits = min_visits
        self.rave = rave
        self.mcts_line = ""

    def create_line(self):
        """
        Creates the line to be added to the config file
        """

        # Configure the line to be added to the config file
        self.mcts_lineline = "Agent=1,TypedMCTS,mcts,MCTS_ITERATIONS:{iterations}|MCTS_THREADS:4|MCTS_Cp:{cp}|MCTS_TYPED_ROLLOUTS|MCTS_MINVISITS:{min_visits}|MCTS_MAX_TREE_SIZE:{max_tree_size}|MCTS_OFFERS_LIMIT:3".format(
            iterations=self.iterations, cp=self.cp, min_visits=self.min_visits, max_tree_size=self.max_tree_size)
        if self.rave:
            self.mcts_line += "|MCTS_UCT_RAVE"

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
