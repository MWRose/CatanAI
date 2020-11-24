from mctsplayer import MCTSPlayer


class Environment: 
    """
    Creates and holds our population
    """
    def __init__(self, population_size: int):
        self.population_size = population_size
        self.population = []

    def create_population(self):
        for i in range(self.population_size):
            self.population.append(MCTSPlayer())
        return self.population

def main():
    pass

if __name__ == "__main__":
    main()