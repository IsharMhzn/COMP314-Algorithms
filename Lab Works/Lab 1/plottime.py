from search_algos import linear_search, binary_search
from collections import namedtuple
import matplotlib.pyplot as plt

import time, random

def time_taken(search, *args):
    '''Calculate time taken to execute the search function'''
    t1 = time.time()
    search(*args)
    return time.time() - t1

def fetch_plotdatas():
    '''Grab execution times for best and worst cases
     of linear and binary searches'''
    PlotData = namedtuple('PlotData', ["size", "ls_best", "ls_worst", 
                                        "bs_best", "bs_worst"])
    plotdatas = []
    for size in range(10000, 110000, 10000):
        linear_sample = random.sample(range(100000), size)
        binary_sample = list(range(size))

        ## Linear Search
        # Best case - search the first element
        target = linear_sample[0]
        ls_b = time_taken(linear_search, linear_sample, target)

        #Worst case - search for the last element
        target = linear_sample[-1]
        ls_w = time_taken(linear_search, linear_sample, target)

        ## Binary Search
        # Best case - Search for element in middle
        target = binary_sample[(size-1)//2]
        bs_b = time_taken(binary_search, binary_sample, target, 0, size)

        # Worst case - Search for first or last element
        target = binary_sample[-1]
        bs_w = time_taken(binary_search, binary_sample, target, 0, size)

        plotdatas.append(PlotData(size, ls_b, ls_w, bs_b, bs_w))
    return plotdatas

def plot_graph(plotdatas):
    '''Plot graph between input size and execution time for best and worst'''
    sizes = [plotdata.size for plotdata in plotdatas]

    fig, (pl1,pl2) = plt.subplots(nrows=2, ncols=1)
    pl1.set_title("Binary Search Algorithm:")
    pl1.set_xlabel("Input Size:")
    pl1.set_ylabel("Execution Time:")
    pl1.plot(sizes,[pd.bs_best for pd in plotdatas],color='b',linestyle='--', label='Best')
    pl1.plot(sizes,[pd.bs_worst for pd in plotdatas],color='b',linestyle='-', label="Worst")
    # pl1.plot(x,b_avg,color='b',linestyle=':', label="Average of 100:")
    pl1.legend()

    pl2.set_title("Linear Search Algorithm:")
    pl2.set_xlabel("Input Size:")
    pl2.set_ylabel("Execution Time:")
    pl2.plot(sizes,[pd.ls_best for pd in plotdatas],color="g",linestyle='--', label="Best")
    pl2.plot(sizes,[pd.ls_worst for pd in plotdatas],color='g',linestyle='-', label="Worst")
    # pl2.plot(x,l_avg,color='g',linestyle=':', label="Average of 100:")
    pl2.legend()

    plt.tight_layout()
    plt.show()

if __name__=="__main__":
    plotdatas = fetch_plotdatas() #fetch graph plot datas
    plot_graph(plotdatas) #plot input-size vs execution-time graph
