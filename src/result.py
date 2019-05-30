from knapsack import Knapsack, read_instances, organize_instances
from os import path,mkdir
from platform import system
import json

def number_solutions(n):
    with open('./number_of_results.txt', 'w') as result_txt: result_txt.write(n)
    try:
        number = int(n)
        if number == 0: 
            print('\n0 solutions?\n')
            return False
        print('\nSuccess!')
        print("run '$ python3 main.py get_sol' to get your results and plot them.\n")
        return number
    except ValueError as err:
        print('ERROR:',err)
        print('Please, only numbers!')
        print('View the README to see how to execute the code!')

def get_solutions(all_instances, number_items, weight_max, values_items, weight_items):
    try:
        with open('./number_of_results.txt', 'r') as result_txt: n_result = int(result_txt.readline())
    except FileNotFoundError:
        print("Please, run '$ python3 main.py n_sol 1' by default, before execute 'get_sol'")
        exit(-1)
    except UnboundLocalError:
        print("Please, run '$ python3 main.py n_sol 1' by default, before execute 'get_sol'")
        exit(-1)
    if n_result == 0: 
        print('\n0 results? OK! Done...\n')
        return False
    print('\nGenerating result...')
    print('Generated 0/{} result done!'.format(n_result))
    for n in range(1, n_result+1):
        result_bottomUp, time_bottomUp, result_topDown, time_topDown = \
        Knapsack().get_result(all_instances, number_items, weight_max, values_items, weight_items)
        data = {}
        k = 0
        for instance in all_instances:
            data[instance] = {
                'result topDown':result_topDown[k], 'time topDown':time_topDown[k],\
                'result bottomUp':result_bottomUp[k], 'time bottomUp':time_bottomUp[k]}
            k += 1
        if not path.isdir('../result'):
            if system() == 'Linux': mkdir('../result')            
            elif system() == 'Windows': mkdir('../result')
            elif system() == 'Darwin': mkdir('../result') 
        with open('../result/result'+str(n)+'.json','w') as file: file.write(json.dumps(data,indent=4))
        print('Generated {}/{} result done!'.format(n,n_result))
    print('\nSuccess!')
    print("run '$ python3 statistic.py' to get the statistics")
    print("run '$ python3 plot.py' to see the graphics\n")