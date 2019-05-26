from os import listdir
from os.path import isfile, join
from collections import defaultdict
from time import time

class Knapsack:       
    def __knapsack_topDown(self, number_items, weight_max, values_items, weight_items):
        if number_items == 0 or weight_max == 0: return 0
        if weight_items[number_items-1] > weight_max: return self.__knapsack_topDown(number_items-1, weight_max, values_items, weight_items)
        if self.mem[number_items][weight_max] is not False: return self.mem[number_items][weight_max]
        temp = max(self.__knapsack_topDown(number_items-1, weight_max-weight_items[number_items-1], values_items, weight_items)+values_items[number_items-1], self.__knapsack_topDown(number_items-1, weight_max, values_items, weight_items))
        self.mem[number_items][weight_max] = temp
        return temp

    def __knapsack_bottomUp(self, number_items, weight_max, values_items, weight_items): 
        K = [[0 for x in range(weight_max + 1)] for x in range(number_items + 1)]
        for i in range(number_items + 1): 
            for w in range(weight_max + 1): 
                if i == 0 or w == 0: K[i][w] = 0
                elif weight_items[i-1] <= w: K[i][w] = max(values_items[i-1] + K[i-1][w-weight_items[i-1]],  K[i-1][w]) 
                else: K[i][w] = K[i-1][w] 
        return K[number_items][weight_max]

    def get_result(self, all_instances, number_items, weight_max, values_items, weight_items):
        result_topDown = []
        time_topDown = []
        result_bottomUp = []
        time_bottomUp = []
        for instance in all_instances:
            start = time()
            result_bottomUp.append(self.__knapsack_bottomUp(int(number_items[instance][0][0]),int(weight_max[instance][0][0]),values_items[instance],weight_items[instance]))
            time_bottomUp.append(time()-start)
            self.mem = [[False for i in range(int(weight_max[instance][0][0])+1)] for j in range(int(number_items[instance][0][0])+1)]
            start = time()
            result_topDown.append(self.__knapsack_topDown(int(number_items[instance][0][0]),int(weight_max[instance][0][0]),values_items[instance],weight_items[instance]))
            time_topDown.append(time()-start)
        return result_bottomUp, time_bottomUp, result_topDown, time_topDown

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

if __name__ == "__main__":
    all_instances = read_instances('./instancias/')
    number_items, weight_max, values_items, weight_items = organize_instances(all_instances)
    print(Knapsack().get_result(all_instances, number_items, weight_max, values_items, weight_items))