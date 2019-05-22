from knapsack import Knapsack, read_instances, organize_instances
import numpy as np
import json

def get_solutions(n):
    """ n of results """

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
        with open('result'+str(n)+'.json','w') as file: file.write(json.dumps(data,indent=4))   

if __name__ == "__main__":
    all_instances = read_instances('./instancias/')
    number_items, weight_max, values_items, weight_items = organize_instances(all_instances)
    get_solutions(1)