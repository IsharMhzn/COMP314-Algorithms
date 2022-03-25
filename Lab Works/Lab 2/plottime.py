import matplotlib.pyplot as plt
import time, random

def time_taken(algorithm, *args):
    '''Calculate time taken to execute the search function'''
    t1 = time.time()
    algorithm(*args)
    return (time.time() - t1) * 100

def plot_graph(title, sizes, *times):
    '''Plot graph of given list of time frames'''
    plt.title(title)
    plt.xlabel("Input Size:")
    plt.ylabel("Execution Time:")

    for t in times:
        plt.plot(sizes, t[1:], label=t[0])
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    ## Import statements
    from insertion import insertion_sort
    from merge import merge_sort

    sizes = [size for size in range(1000, 10001, 1000)]
    it_best = ["Best Case"]
    it_worst = ["Worst Case"]
    mt_best = ["Best Case"]
    mt_worst = ["Worst Case"]

    for size in sizes:
        w_values = random.sample(range(100000), size) # Unsorted random values
        b_values = sorted(w_values) # Sorted values

        ## Insertion Sort
        it_worst.append(time_taken(insertion_sort, w_values))
        it_best.append(time_taken(insertion_sort, b_values))
        ## Merge Sort
        mt_worst.append(time_taken(merge_sort, w_values, 0, size-1))
        mt_best.append(time_taken(merge_sort, b_values, 0, size-1))

    plot_graph("Insertion Sort", sizes, it_best, it_worst)
    plot_graph("Merge Sort", sizes, mt_best, mt_worst)
