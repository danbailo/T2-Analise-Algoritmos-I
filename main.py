from os import listdir
from os.path import isfile, join
from time import time
from collections import defaultdict

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

if __name__ == "__main__":

    all_files = sorted([f for f in listdir('./instancias') if isfile(join('./instancias', f))])
    all_instaces = {}
    for file in all_files:
        lines = []
        with open('./instancias/'+file) as instance:
            for line in instance:
                if line != '\n': lines.append(line.split())
        all_instaces[file] = lines

    number_items = defaultdict(list)
    weight_max = defaultdict(list)
    values_items = defaultdict(list)
    weight_items = defaultdict(list)

    for i in all_instaces.items():
        number_items[i[0]].append(i[1].pop(0))
        weight_max[i[0]].append(i[1].pop(0))

    for i in all_instaces.items():
        for k in i[1]:
            values_items[i[0]].append(int(k[0]))
            weight_items[i[0]].append(int(k[1]))

    for i in all_instaces:
        print(knapSack(int(number_items[i][0][0]),int(weight_max[i][0][0]),values_items[i],weight_items[i]))

    time_total = []
    for i in all_instaces:
        start=time()
        knapSack(int(number_items[i][0][0]),int(weight_max[i][0][0]),values_items[i],weight_items[i])
        time_total.append(time()-start)

    print(time_total)
