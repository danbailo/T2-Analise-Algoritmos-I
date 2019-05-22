from knapsack import Knapsack, read_instances, organize_instances
import sys
import numpy as np
import json

def number_solutions(n):
    with open('./number_of_results.txt', 'w') as result_txt: result_txt.write(n)
    return int(n)

def get_solutions():
    with open('./number_of_results.txt', 'r') as result_txt: n = int(result_txt.readline())
    print('Generating result...')
    for n in range(1, n+1):
        result_iterative, time_iterative, result_recursive, time_recursive = \
        Knapsack().get_result(all_instances, number_items, weight_max, values_items, weight_items)
        data = {}
        k = 0
        for instance in all_instances:
            data[instance] = {
                'result iterative':result_iterative[k], 'time iterative':time_iterative[k],\
                'result recursive':result_recursive[k], 'time recursive':time_recursive[k]}
            k += 1
        with open('./result/result'+str(n)+'.json','w') as file: file.write(json.dumps(data,indent=4))   

if __name__ == "__main__":
    all_instances = read_instances('./instancias/')
    number_items, weight_max, values_items, weight_items = organize_instances(all_instances)
    try:
        if sys.argv[1] == 'n_sol': number_solutions(sys.argv[2])
        if sys.argv[1] == 'get_sol': get_solutions()
    except IndexError: raise 'SEE README!'