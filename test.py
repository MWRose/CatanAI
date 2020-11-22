

""" Takes a MCTSConfig and returns its fitness (win rate)"""
file_name = "/home/max/Documents/ai/StacSettlers/target/results/21:49:50.479644_Sat_Nov_21_21_49_50_PST_2020_ebbb6166-0cbc-470a-9834-43c742801d0f/summary.txt"
# Look in results folder for this name
fitness = 0
with open(file_name, "r") as file:
    lines = file.readlines()
    games = lines[0].strip()[6:]
    seconds = lines[1].strip()[8:]
    turns = lines[2].strip()[15:]
    print(games)
    print(seconds)
    print(turns)
    for line in lines:
        line_sep = line.split()
        if len(line_sep) > 0 and line_sep[0] == "TypedMCTS":
            fitness = float(line_sep[1])
            break

print(fitness)