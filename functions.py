from os import listdir
from os.path import isfile, join
from collections import defaultdict
from time import time


def mochiladin(w, n, valores, pesos):
    if n == 0 or w == 0: return 0
    ans=memoria.get((w,n),None)
    if ans!=None:return ans
    if pesos[n-1]>w:
        ans=mochiladin(w , n-1, valores, pesos) 
        memoria[w,n]=ans
        return ans
    ans=max(valores[n-1]+mochiladin(w-pesos[n-1],n-1,valores,pesos),mochiladin(w,n-1,valores,pesos)) 
    memoria[w,n]=ans
    return ans

def knapsack_recursive(number_items, weight_max, values_items, weight_items):
    if number_items == 0 or weight_max == 0: return 0
    if weight_items[number_items-1] > weight_max: return knapsack_recursive(number_items-1, weight_max, values_items, weight_items)
    if mem[number_items][weight_max] is not False: return mem[number_items][weight_max]
    temp = max(knapsack_recursive(number_items-1, weight_max-weight_items[number_items-1], values_items, weight_items)+values_items[number_items-1], knapsack_recursive(number_items-1, weight_max, values_items, weight_items))
    mem[number_items][weight_max] = temp
    return temp


def knapsack_iterative(number_items, weight_max, values_items, weight_items): 
    K = [[0 for x in range(weight_max + 1)] for x in range(number_items + 1)]
    for i in range(number_items + 1): 
        for w in range(weight_max + 1): 
            if i == 0 or w == 0: K[i][w] = 0
            elif weight_items[i-1] <= w: K[i][w] = max(values_items[i-1] + K[i-1][w-weight_items[i-1]],  K[i-1][w]) 
            else: K[i][w] = K[i-1][w] 
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
        for k in i[1]:
            values_items[i[0]].append(int(k[0]))
            weight_items[i[0]].append(int(k[1]))     
    return number_items, weight_max, values_items, weight_items

def get_result(all_instances, number_items, weight_max, values_items, weight_items):
    result_iterative = []
    time_total_iterative = []
    result_recursive = []
    time_total_recursive = []    
    for i in all_instances:
        start = time()
        result_iterative.append(knapsack_iterative(int(number_items[i][0][0]),int(weight_max[i][0][0]),values_items[i],weight_items[i]))
        time_total_iterative.append(time()-start)
    return result_iterative, time_total_iterative

def get_result2(all_instances, number_items, weight_max, values_items, weight_items):
    result_list = []
    time_list = [] 
    for instance in all_instances:
        globals()["mem"] = [[False for i in range(int(weight_max[instance][0][0])+1)] for j in range(int(number_items[instance][0][0])+1)]
        start = time()
        result_list.append(knapsack_recursive(int(number_items[instance][0][0]),int(weight_max[instance][0][0]),values_items[instance],weight_items[instance]))
        time_list.append(time()-start)
    return result_list, time_list

if __name__ == "__main__":
    all_instances = read_instances('./instancias/')
    number_items, weight_max, values_items, weight_items = organize_instances(all_instances)

    print(get_result2(all_instances, number_items, weight_max, values_items, weight_items))

    # result_list = []
    # result_dict = []
    # time_list = [] 
    # time_dict = [] 

    # for instance in all_instances:
    #     mem = [[False for i in range(int(weight_max[instance][0][0])+1)] for j in range(int(number_items[instance][0][0])+1)]
    #     memoria = {}
        
    #     start = time()
    #     result_list.append(knapsack_recursive(int(number_items[instance][0][0]),int(weight_max[instance][0][0]),values_items[instance],weight_items[instance]))
    #     time_list.append(time()-start)
        
    #     start = time()
    #     result_dict.append(mochiladin(int(weight_max[instance][0][0]),int(number_items[instance][0][0]),values_items[instance],weight_items[instance]))
    #     time_dict.append(time()-start)

    # print('result_list', result_list)
    # print('time_list', time_list)

    # print('result_dict', result_dict)
    # print('time_dict', time_dict)