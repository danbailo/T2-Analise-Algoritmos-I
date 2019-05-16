from os import listdir
from os.path import isfile, join
from collections import defaultdict
from time import time

def knapSack(number_items, weight_max, values_items, weight_items): 
    K = [[0 for x in range(weight_max + 1)] for x in range(number_items + 1)]
    for i in range(number_items + 1): 
        for w in range(weight_max + 1): 
            if i == 0 or w == 0: 
                K[i][w] = 0
            elif weight_items[i-1] <= w: 
                K[i][w] = max(values_items[i-1] + K[i-1][w-weight_items[i-1]],  K[i-1][w]) 
            else: 
                K[i][w] = K[i-1][w] 
    return K[number_items][weight_max]

def read_instances(directory):
    all_files = sorted([f for f in listdir(directory) if isfile(join(directory, f))])
    all_instances = {}
    for file in all_files:
        lines = []
        with open(directory+file) as instance:
            for line in instance:
                if line != '\n': lines.append(line.split())
        all_instances[file] = lines
    return all_instances

def organize_instances(all_instances):
    number_items = defaultdict(list)
    weight_max = defaultdict(list)
    values_items = defaultdict(list)
    weight_items = defaultdict(list)
    for i in all_instances.items():
        number_items[i[0]].append(i[1].pop(0))
        weight_max[i[0]].append(i[1].pop(0))
    for i in all_instances.items():
        for k in i[1]:
            values_items[i[0]].append(int(k[0]))
            weight_items[i[0]].append(int(k[1]))     
    return number_items, weight_max, values_items, weight_items

def get_result(all_instances, number_items, weight_max, values_items, weight_items):
    result = []
    time_total = []
    for i in all_instances:
        start = time()
        result.append(knapSack(int(number_items[i][0][0]),int(weight_max[i][0][0]),values_items[i],weight_items[i]))
        time_total.append(time()-start)
    return result, time_total