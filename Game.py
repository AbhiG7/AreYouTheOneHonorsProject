import random

# This module has 2 classes
# The Contestant class keeps track of each individual contestant
# The Game class takes care of all the game related methods and the different algorithms

class Contestant:
    def __init__(self, match):
        self.name = "Riley"
        self.match = match        # Specific value that only matches one other contestant, which will determine perfect pair
    
    def __str__(self):
        return "My name is {}. My match is {}".format(self.name, self.match)


class Game:
    def __init__(self):
        self.num_perf_pairs = 0
        perf_nums = [1, 2, 3, 4, 5, 6, 7, 8]                                            # List of numbers created to be used to determine who the perfect matches are
        random.shuffle(perf_nums)                                                       # Shuffles the perfect match value list so that matches are created randomly
        self.contestants = [Contestant(perf_nums[i % 8]) for i in range(16)]            # Initializes a list of contestants with a value that their perfect match will share
        self.pairs = []                                                                 # Initializes an empty list for pairs to be stored in
        self.perfect_pairs = []                                                         # Initializes an empty list for final perfect pairs to be stored in
        self.weeks = 0                                                                  # Initializes a counter to keep track of how many weeks each algorithm takes
        #for i in self.contestants: print(i)
        
    def create_pairs(self):
        random.shuffle(self.contestants)                                                                                    # Shuffles the contestants list so that pairs are created randomly
        self.pairs = [[self.contestants[i], self.contestants[i+1]] for i in range(0, len(self.contestants)-1, 2)]           # Creates a list of pairs (each pair is a list)
        #for i in self.pairs: print("{}, {}".format(i[0], i[1]))
    
    # Does Truth Box part of game: Determines if the inputed pair is a perfect pair or not
    def truth_box(self, pair):
        return pair[0].match == pair[1].match

    # Only used if perfect pair, will move pair to the perfect pairs list
    def move_pair(self, pair):
        self.perfect_pairs.append((pair[0], pair[1]))
        self.pairs.remove(pair)
    
    # Evaluates the remaining pairs past in to see how many of these pairs are perfect pairs
    def evaluate_rest(self, rest):
        perf = 0
        for p in rest:
            if p[0].match == p[1].match:
                perf += 1
        return perf
    
    # This algorithm will remove the already perfect pair, determined by Truth Box, from list and randomize the rest of the pairs
    def remove_alg(self, list_of_pairs):
        self.weeks += 1                                                                                     # Weeks incremented every time method recurses to symbolize the passage of a week
        pair = list_of_pairs[0]                                                                             # Grabs first pair of list to send to truth box
        rest = list_of_pairs[1:]
        pair_truth = self.truth_box(pair)                                                                   # Sends a pair to the truth box
        if pair_truth:
            self.num_perf_pairs += 1
            self.move_pair(pair)
        perf_rest = self.evaluate_rest(rest)                                                                # Evaluates how many other perfect pairs there are
        if self.num_perf_pairs + perf_rest != 8:                                                            # If not all perfect pairs, randomizes rest and recurses through algorithm
            remaining = []
            for i in self.pairs:
                for c in i:
                    remaining.append(c)
            random.shuffle(remaining)
            self.pairs = [[remaining[i], remaining[i+1]] for i in range(0, len(remaining)-1, 2)]
            self.remove_alg(self.pairs)
        else:
            self.perfect_pairs += self.pairs                                                                # If all perfect pairs, moves remaining pairs into perfect pairs list (mainly just for the debugging method)
    
    # This algorithm will brute force each person into finding their pair first through the truth box and then moves on to the next contestants
    def brute_force_alg(self, contestants):
            i = 0                                                                                   # Keeps track of what the current contestant we're trying to find a pair for is
            nxt = 2                                                                                 # Keeps track of what the next contestant we should sub in is
            while i < len(contestants):
                self.weeks += 1                                                                     # Increments weeks
                pair = [contestants[i], contestants[i+1]]                                           # Creates a pair to be tested
                pair_truth = self.truth_box(pair)                                                   # Sends a pair to the truth box
                if self.num_perf_pairs == 8:                                                        # If we have reached all perfect pairs, end the loop
                    break
                elif pair_truth:                                                                    # If  perfect pair, add to perfect pairs list, increment number of perfect pairs we have, and change the counters keeping track of position to the next pairing
                    self.perfect_pairs.append(pair)
                    self.num_perf_pairs += 1
                    i += 2
                    nxt = i + 2
                else:                                                                               # Otherwise, keep the first contestant in the pairing the same and move the second one to the next contestant
                    contestants[i+1], contestants[nxt] = contestants[nxt], contestants[i+1]
                    nxt += 1
    
    # This algorithm will completely randomize all pairs until all the pairs are perfect pairs
    def complete_random_alg(self, list_of_pairs):
        self.num_perf_pairs, perf_rest = 0, 0

        while self.num_perf_pairs + perf_rest != 8:                 # As long as all the pairs are not perfect, repeat through the loop
            self.weeks += 1
            self.num_perf_pairs = 0
            self.num_perf_pairs = self.evaluate_rest(self.pairs)
            if self.num_perf_pairs != 8:
                self.create_pairs()
        self.perfect_pairs = self.pairs
    
    
    
    # This algorithm still needs more work
    # This algorithm will remove the already perfect pair and randomize the number of non-perfect pairs determined by evaluate_rest (seems to go on forever)
    def specific_random_alg(self, list_of_pairs):
        self.num_perf_pairs, perf_rest = 0, 0

        while self.num_perf_pairs + perf_rest != 8:
            self.weeks += 1
            pair = list_of_pairs[0]
            rest = list_of_pairs[1:]
            pair_truth = self.truth_box(pair)
            if pair_truth:
                self.move_pair(pair)
            perf_rest = self.evaluate_rest(rest)
            if self.num_perf_pairs + perf_rest != 8:
                remaining = []
                for i in range(len(self.pairs)-perf_rest):
                    for c in self.pairs[i]:
                        remaining.append(c)
                random.shuffle(remaining)
                self.pairs = self.pairs[(len(self.pairs)-perf_rest):] + [[remaining[i], remaining[i+1]] for i in range(0, len(remaining)-1, 2)]
                #self.specific_random_alg(self.pairs)
        
        self.debug_prints()

    # This helps debug by printing all the pairs to make sure they are paired with their perfect pair at the end
    def debug_prints(self):
        print("Game Over, Everybody Won!")
        print("It took {} weeks to match everyone up!".format(self.weeks))
        for i in self.perfect_pairs:
            print(i[0], i[1], sep=" :: ")

    # This is the method that will initiate the game. It takes a string or number in as a parameter which chooses what algorithm to run with
    def run_game(self, alg):
        self.create_pairs()                                         # Creates a set of random pairs to start with
        if alg == 'remove_alg' or alg == 1:
            self.remove_alg(self.pairs)
        elif alg == 'specific_random_alg' or alg == 2:
            self.specific_random_alg(self.pairs)
        elif alg == 'complete_random_alg' or alg == 3:
            self.complete_random_alg(self.pairs)
        elif alg == 'brute_force_alg' or alg == 4:
            self.brute_force_alg(self.contestants)
        else:
            return "Please write a valid algorithm name"
        return self.weeks                                           # Returns the number of weeks at the end for the stats module to use
    

if __name__ == "__main__":
    # g1 = Game()
    # g1.run_game(1)
    # g1.debug_prints()

    print(15+13+11+9+7+5+3+1)

    """ g1.create_pairs()

    for i in g1.pairs:
        print(i) """

    #print("{} ::: {}".format(g1.perfect_pairs, g1.pairs))
    '''g1.truth_box(g1.pairs[0])
    print("{} ::: {}".format(g1.perfect_pairs, g1.pairs))'''