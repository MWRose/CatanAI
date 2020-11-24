from mctsplayer import MCTSPlayer


class Environment: 
    def __init__(self, population_size: int):
        self.population_size = population_size
        self.population = []
        self.avg_fitnesses = []

    def create_population(self):
        for i in range(self.population_size):
            self.population.append(MCTSPlayer())
        return self.population

    

def main():
    pass

if __name__ == "__main__":
    main()