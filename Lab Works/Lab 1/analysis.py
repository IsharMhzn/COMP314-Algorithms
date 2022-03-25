import random, time
# from turtle import color
from matplotlib import pyplot as plt
from numpy import sort
# from linear_search import linear_search
from binary_search import binary_search

def exec_time(search, *args):
    start = time.time()
    print(start)
    search(*args)
    print(time.time())
    return (time.time() - start)

def search():

    exec_records = {
        'input_size': [], 
        'linear_best': [],
        'linear_worst':[],
        'binary_best':[],
        'binary_worst': [],
        }

    for size in range(10000, 110000, 10000):
        randomInputs = sort(random.sample(range(100000), size))
        
        exec_records['input_size'].append(size)

        ## linear search
        # best case - target is the first element
        # exec_records['linear_best'].append(exec_time(linear_search, randomInputs, randomInputs[0]))
        # # worst case - target is the last element or not in the list
        # exec_records['linear_worst'].append(exec_time(linear_search, randomInputs, randomInputs[-1]))

        ## binary search
        # best case - target is the middle element
        exec_records['binary_best'].append(exec_time(binary_search, randomInputs, randomInputs[size//2]))

        # worst case - target is the first or last element or not in the list
        exec_records['binary_worst'].append(exec_time(binary_search, randomInputs, randomInputs[0]))

    return exec_records

def plot_exec_records(plot_datas):
   
    fig, [linear_search_time, binary_search_time] = plt.subplots(2, 1)

    # Linear Search Execution Times Plot
    # linear_search_time.plot(
    #     plot_datas['input_size'], plot_datas['linear_best'], color='orange', label='Best Case')
    # linear_search_time.plot(
    #     plot_datas['input_size'], plot_datas['linear_worst'], color='green', label='Worst Case')
    # linear_search_time.set_title('Linear Search', loc='left')
    # linear_search_time.set_xlabel('Input Sizes')
    # linear_search_time.set_ylabel('Execution Times')
    # linear_search_time.legend()

    # Binary Search Execution Times Plot
    binary_search_time.plot(
        plot_datas['input_size'], plot_datas['binary_best'], color='orange', label='Best Case')
    binary_search_time.plot(plot_datas['input_size'], plot_datas['binary_worst'], color='green', label='Worst Case')
    binary_search_time.set_title('Binary Search', loc='left')
    binary_search_time.set_xlabel('Input Sizes')
    binary_search_time.set_ylabel('Execution Times')
    binary_search_time.legend()

    plt.show()

if __name__ == "__main__":
    exec_records = search()
    plot_exec_records(exec_records)