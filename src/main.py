from knapsack import Knapsack, read_instances, organize_instances
from result import number_solutions, get_solutions
from sys import argv

if __name__ == "__main__":
    all_instances = read_instances('../Trabalho II/instancias/')
    number_items, weight_max, values_items, weight_items = organize_instances(all_instances)
    try:
        if argv[1] == 'n_sol': number_solutions(argv[2])
        if argv[1] == 'get_sol': get_solutions(all_instances, number_items, weight_max, values_items, weight_items)
    except IndexError as err: 
        print('\nERROR:',err)
        print('$ python3 main.py [USE]')
        print('View the README to see how to execute the code!\n')