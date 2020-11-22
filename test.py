

""" Takes a MCTSConfig and returns its fitness (win rate)"""
file_name = "/home/max/Documents/ai/StacSettlers/target/results/19:21:51.502961_Sat_Nov_21_19_21_51_PST_2020_b1152fe5-3163-4f87-806e-d158a17ce5f7/summary.txt"
# Look in results folder for this name
fitness = 0
with open(file_name, "r") as file:
    lines = file.readlines()
    print(lines[0], lines[1], lines[2])
    for line in lines:
        line_sep = line.split()
        if len(line_sep) > 0 and line_sep[0] == "TypedMCTS":
            fitness = float(line_sep[1])
            break

print(fitness)