import matplotlib.pyplot as plt
import time
from Game import Game

#
# This module has two methods that graph different aspects of the three algorithms
#


# Graphs the average number of weeks each algorithm takes to reach the end of the game
def graph_weeks():
    x = 100     # Number of times each algorithm is run

    # Averages the first algorithm weeks
    avg_remove = 0
    for i in range(x):
        g = Game()
        a = g.run_game('remove_alg')
        avg_remove += a
    avg_remove = avg_remove/x

    # Averages the second algorithm weeks
    avg_brute = 0
    for i in range(x):
        g = Game()
        b = g.run_game('brute_force_alg')
        avg_brute += b
    avg_brute = avg_brute/x

    # Averages the third algorithm weeks
    avg_random = 0
    for i in range(x):
        g = Game()
        c = g.run_game('complete_random_alg')
        avg_random += c
    avg_random = avg_random/x

    # Creates the graph
    plt.figure()
    algs = ['remove_alg', 'brute_force_alg', 'complete_random_alg']
    weeks = [avg_remove, avg_brute, avg_random]
    plt.bar(algs, weeks)
    plt.yscale('log')
    plt.xlabel('Algorithms')
    plt.ylabel('Average number of weeks')
    #plt.savefig('average_weeks.png')        # Took about 25 minutes to make
    
    # plt.show()

# Graphs the average runtimes of each of the three algorithms
def graph_times():
    x = 10000           # Number of times each algorithm is run
    scale = 1000        # Scale factor for all the times
    
    # Avereages the first algorithm runtimes
    avg_remove_time = 0
    for i in range(x):
        g = Game()
        start_a = time.time()
        g.run_game('remove_alg')
        end_a = time.time() - start_a
        avg_remove_time += end_a
    
    avg_remove_time = (avg_remove_time/x)*scale

    # Avereages the second algorithm runtimes
    avg_brute_time = 0
    for i in range(x):
        g = Game()
        start_b = time.time()
        g.run_game('brute_force_alg')
        end_b = time.time() - start_b
        avg_brute_time += end_b
    
    avg_brute_time = (avg_brute_time/x)*scale

    # Avereages the third algorithm runtimes
    avg_random_time = 0
    for i in range(3):
        g = Game()
        start_c = time.time()
        g.run_game('complete_random_alg')
        end_c = time.time() - start_c
        avg_random_time += end_c
    
    avg_random_time = (avg_random_time/3)*scale

    # Creates the graph
    plt.figure()
    algs = ['remove_alg', 'brute_force', 'complete_random_alg']
    times = [avg_remove_time, avg_brute_time, avg_random_time]
    plt.bar('complete_random_algs', avg_random_time)
    plt.yscale('log')
    plt.xlabel('Algorithms')
    plt.ylabel('Average time taken (s)')
    #plt.savefig('average_times_3.png')
    #plt.show()

# Graphs the spread of the number of weeks it takes for the remove alogrithm to reach a win
def graph_spread_weeks_remove():
    x = 10000           # Number of times the alg runs
    y = []              # Where the spread of data is saved

    for i in range(x):
        g = Game()
        w = g.run_game('remove_alg')
        y.append(w)
    b = max(y) - min(y) + 1
    
    # Plots the spread in a histogram
    plt.figure()
    plt.hist(y, b)
    plt.title('Spead of Weeks It Takes for remove_alg')
    plt.xlabel('Number of Weeks')
    plt.ylabel('Frequency')
    plt.savefig('weeks_spread_remove.png')
    plt.show()

# Graphs the spread of the number of weeks it takes for the brute force alogrithm to reach a win
def graph_spread_weeks_brute():
    x = 10000               # Number of times the alg runs
    y = []                  # Where the spread of data is saved

    for i in range(x):
        g = Game()
        w = g.run_game('brute_force')
        y.append(w)
    b = max(y) - min(y) + 1
    
    # Plots the spread in a histogram
    plt.figure()
    plt.hist(y, b)
    plt.title('Spead of Weeks It Takes for brute_force_alg')
    plt.xlabel('Number of Weeks')
    plt.ylabel('Frequency')
    plt.savefig('weeks_spread_brute_force.png')
    plt.show()

# Graphs the spread of the number of weeks it takes for the brute force alogrithm to reach a win
def graph_spread_weeks_random():
    x = 5                  # Number of times the alg runs
    y = []                  # Where the spread of data is saved

    for i in range(x):
        g = Game()
        w = g.run_game('complete_random_alg')
        y.append(w)
    b = max(y) - min(y) + 1
    
    # Plots the spread in a histogram
    plt.figure()
    plt.hist(y, b)
    plt.title('Spead of Weeks It Takes for complete_random_alg')
    plt.xscale('log')
    plt.xlabel('Number of Weeks')
    plt.ylabel('Frequency')
    plt.savefig('weeks_spread_random.png')
    plt.show()

if __name__ == '__main__':
    graph_spread_weeks_random()
    # g = Game()
    # start = time.time()
    # g.run_game('complete_random_alg')
    # end = time.time() - start
    # print(end)