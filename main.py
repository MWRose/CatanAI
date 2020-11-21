from subprocess import *

def simulate(*args) -> int:
    process = Popen(['java', '-cp', 'STACSettlers-1.0-bin.jar', 'soc.robot.stac.simulation.Simulation']+'../StacSettlers/target/config-simple.txt', stdout=PIPE, stderr=PIPE)
    ret = []
    while process.poll() is None:
        line = process.stdout.readline()
        if line != '' and line.endswith('\n'):
            ret.append(line[:-1])
    stdout, stderr = process.communicate()
    ret += stdout.split('\n')
    if stderr != '':
        ret += stderr.split('\n')
    ret.remove('')

    return ret


# call our ga() function here
def main():
    simulate('../StacSettlers/target/config-simple.txt')

if __name__ == "__main__":
    main()