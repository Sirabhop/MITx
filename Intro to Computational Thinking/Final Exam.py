from os import lseek
import random, pylab
from re import L, S
from threading import activeCount

# Problem 3

# In a lecture, there are 3 things you might do: listen, sleep, or Facebook (in a single lecture, you might do all, some, or none of them). Lectures are independent of each other, the probabilities associated with the activities are independent of each other, and they are all > 0. You are given the following class, Lecture, and the function, get_mean_and_std.
# Write a Monte Carlo simulation called lecture_activities(N, aLecture) that meets the specifications below.
class Lecture(object):
    def __init__(self, listen, sleep, fb):
        self.listen = listen
        self.sleep = sleep
        self.fb = fb
    def get_listen_prob(self):
        return self.listen
    def get_sleep_prob(self):
        return self.sleep
    def get_fb_prob(self):
        return self.fb
     
def get_mean_and_std(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std
        
def lecture_activities(N, aLecture):
    '''
    N: integer, number of trials to run
    aLecture: Lecture object
 
    Runs a Monte Carlo simulation N times.
    Returns: a tuple, (float, float)
             Where the first float represents the mean number of lectures it takes 
             to have a lecture in which all 3 activities take place,
             And the second float represents the total width of the 95% confidence 
             interval around that mean.
    '''
    X = []
    for i in range(N):
        chance = random.random()
        count = 0
        activities = ()
        while activities != (1, 1, 1):
            count += 1
            if random.random() <= aLecture.get_listen_prob():
                if random.random() <= aLecture.get_sleep_prob():
                    if random.random() <= aLecture.get_fb_prob():
                        activities = (1, 1, 1)
        X.append(count)
    mean, sd = get_mean_and_std(X)
    return (mean, 4*sd)

# sample test cases 
a = Lecture(1, 1, 1)
print(lecture_activities(100, a))
# the above test should print out (1.0, 0.0)
b = Lecture(1, 1, 0.5)
print(lecture_activities(100000, b))
# the above test should print out something reasonably close to (2.0, 5.516)

# Problem 4

# You are given this function
def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std

# You are given this class
class Die(object):
    def __init__(self, valList):
        """ valList is not empty """
        self.possibleVals = valList[:]
    def roll(self):
        return random.choice(self.possibleVals)

# Implement this -- Coding Part 1 of 2
def makeHistogram(values, numBins, xLabel, yLabel, title=None):
    """
      - values, a sequence of numbers
      - numBins, a positive int
      - xLabel, yLabel, title, are strings
      - Produces a histogram of values with numBins bins and the indicated labels
        for the x and y axis
      - If title is provided by caller, puts that title on the figure and otherwise
        does not title the figure
    """
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    pylab.title(title)
    pylab.hist(values, numBins)
    pylab.show()
    
                    
# Implement this -- Coding Part 2 of 2
def getAverage(die, numRolls, numTrials):
    """
      - die, a Die
      - numRolls, numTrials, are positive ints
      - Calculates the expected mean value of the longest run of a number
        over numTrials runs of numRolls rolls.
      - Calls makeHistogram to produce a histogram of the longest runs for all
        the trials. There should be 10 bins in the histogram
      - Choose appropriate labels for the x and y axes.
      - Returns the mean calculated
    """
    max_count = []
    for trial in range(numTrials):
        values = []
        for roll in range(numRolls):
            values.append(die.roll())
        max_count.append(values.count(max(values, key = values.count)))
    makeHistogram(max_count, 10, "Bins", "Mean of the longest")
    return getMeanAndStd(max_count)[0]
    
# One test case
print(getAverage(Die([1,2,3,4,5,6,6,6,7]), 500, 10000))


a = [1,1,1,0,2]
a.count(max(a, key = a.count))
max(a, key=a.count)

# Problem 6
def find_combination(choices, total):
    """
    choices: a non-empty list of ints
    total: a positive int
 
    Returns result, a numpy.array of length len(choices) 
    such that
        * each element of result is 0 or 1
        * sum(result*choices) == total
        * sum(result) is as small as possible
    In case of ties, returns any result that works.
    If there is no result that gives the exact total, 
    pick the one that gives sum(result*choices) closest 
    to total without going over.
    """
    result = [0]*len(choices)
    for i in range(len(choices)):
        if choices[i] == total:
            result[i] = 1
            return result
    to_check = []
    for item in choices:
        while sum(to_check) != total:
            to_check.append(item)

choices = [1,1,3,5,3]
total = 5

result = []

st = (bin(total).lstrip('0b'))
st = '0'*(len(choices) - len(st)) + st
for item in st:
    result.append(int(item))
    

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 500
CURRENTFOXPOP = 30

def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP
    prob_rabbit = 1 - CURRENTRABBITPOP/MAXRABBITPOP
    if random.random() <= prob_rabbit:
        CURRENTRABBITPOP += 1
rabbitGrowth()
def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP
    
    prob_fox_eat = CURRENTRABBITPOP/MAXRABBITPOP
    
    if CURRENTRABBITPOP > 10:
        if random.random() <= prob_fox_eat:
            CURRENTRABBITPOP -= 1
            if random.random() <= 1/3:
                CURRENTFOXPOP += 1
        else:
            if (CURRENTFOXPOP > 10) and (random.random() <= 1/10):
                CURRENTFOXPOP -= 1

    
def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """
    rabbit_populations = []
    fox_populations = []
    for step in range(numSteps):
        rabbitGrowth()
        foxGrowth()
        rabbit_populations.append(CURRENTRABBITPOP)
        fox_populations.append(CURRENTFOXPOP)
    
    return (rabbit_populations, fox_populations)
  

  
xVals = []
yVals = []
wVals = []
for i in range(1000):
    xVals.append(random.random())
    yVals.append(random.random())
    wVals.append(random.random())
xVals = pylab.array(xVals)
yVals = pylab.array(yVals)
wVals = pylab.array(wVals)
xVals = xVals + xVals
zVals = xVals + yVals
tVals = xVals + yVals + wVals


pylab.plot(sorted(xVals), yVals)
pylab.show()