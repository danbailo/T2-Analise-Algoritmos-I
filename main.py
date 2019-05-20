from functions import *
# from functions import knapsack_recursive, knapsack_iterative, read_instances, organize_instances, get_result
from time import time
import matplotlib.pyplot as plt

if __name__ == "__main__":
    all_instances = read_instances('./instancias/')
    number_items, weight_max, values_items, weight_items = organize_instances(all_instances)
    result_iterative, time_iterative = get_result(all_instances, number_items, weight_max, values_items, weight_items)
    # plt.style.use('default')
    print('result_iterative', result_iterative)
    print('time_iterative', time_iterative)
    print('time_sorted', sorted(time_iterative))

    # plt.title('Trabalho II')
    # plt.xlabel('Tempo/s')
    # plt.ylabel('Resultado')

    # plt.plot(time_iterative, result_iterative)
    # plt.plot(time_iterative, result_iterative)
    # plt.savefig('iterative.png')
    # plt.show()

    # plt.plot(sorted(time_iterative), result_iterative) # red triangulo
    # plt.plot(sorted(time_iterative), result_iterative)
    # plt.savefig('iterative_sorted.png')
    # plt.show()    


    # plt.title('Trabalho II')
    # plt.xlabel('Tempo/s')
    # plt.ylabel('Resultado')
    
    # plt.bar(time, result, width=0.01,edgecolor='black')
    # plt.xticks(time, names, rotation=90)

    # plt.grid()
    # plt.legend()
    # plt.show()

    # x = [0, 1, 2, 3, 4, 20] #onde esta as barras
    # y = [2, 3, 5, 3, 7, 9] #tamanho das barras, eixo y

    # plt.bar(x,y)
    # plt.show()