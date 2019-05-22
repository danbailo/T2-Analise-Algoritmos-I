from knapsack import Knapsack, read_instances, organize_instances
from platform import system
from os import path,mkdir
import numpy as np
import matplotlib.pyplot as plt
import json

def plot_iterative(name_instance, time_iterative, result_iterative):
    plt.title('Resultado do algoritmo iterativo a partir de 1 execução')
    plt.xlabel('Resultado')
    plt.ylabel('Tempo/s')
    plt.scatter(result_iterative, time_iterative, marker='.', color='orange',label='Instâncias')
    plt.legend()
    plt.grid()
    plt.savefig('./img/scatter_iterative.pdf')
    plt.show() 

    plt.title('Instância/Resultado - Iterativo')
    plt.xlabel('Instância')
    plt.ylabel('Resultado')
    plt.plot(name_instance, result_iterative, color='orange')
    plt.xticks(rotation=90, ha='right',fontsize=7)
    plt.grid()
    plt.savefig('./img/result_iterative.pdf')
    plt.show()      

    plt.title('Instância/Tempo - Iterativo')
    plt.xlabel('Tempo/s')
    plt.ylabel('Resultado')
    plt.plot(name_instance, time_iterative, color='orange')
    plt.xticks(rotation=90, ha='right',fontsize=7)
    plt.grid()
    plt.savefig('./img/time_iterative.pdf')
    plt.show()  

def plot_recursive(name_instance, time_recursive, result_recursive):
    plt.title('Resultado do algoritmo recursivo a partir de 1 execução')
    plt.xlabel('Resultado')
    plt.ylabel('Tempo/s')
    plt.scatter(result_recursive, time_recursive, marker='.', color='steelblue',label='Instâncias')
    plt.legend()
    plt.grid()
    plt.savefig('./img/scatter_recursive.pdf')
    plt.show()

    plt.title('Instância/Resultado - Recursivo')
    plt.xlabel('Instância')
    plt.ylabel('Resultado')
    plt.plot(name_instance, result_recursive, color='steelblue')
    plt.xticks(rotation=90, ha='right',fontsize=7)
    plt.grid()
    plt.savefig('./img/result_recursive.pdf')
    plt.show()      

    plt.title('Instância/Tempo - Recursivo')
    plt.xlabel('Tempo/s')
    plt.ylabel('Resultado')
    plt.plot(name_instance, time_recursive, color='steelblue')
    plt.xticks(rotation=90, ha='right',fontsize=7)
    plt.grid()
    plt.savefig('./img/time_recursive.pdf')
    plt.show()  

def plot_two(name_instance, time_iterative, result_iterative,time_recursive, result_recursive):
    plt.title('Resultado das duas versões do algoritmo')
    plt.xlabel('Tempo/s')
    plt.ylabel('Resultado')
    plt.scatter(time_iterative, result_iterative, marker='.', color='orange', label='Iterativo')
    plt.scatter(time_recursive, result_recursive, marker='.', color='steelblue', label='Recursivo')
    plt.legend()
    plt.grid()
    plt.savefig('./img/scatter_two.pdf')
    plt.show()

    plt.title('Instância/Resultado - Iterativo vs Recursivo')
    plt.xlabel('Instância')
    plt.ylabel('Resultado')
    plt.plot(name_instance, result_iterative, color='orange', label='Iterativo')
    plt.plot(name_instance, result_recursive, ':', color='steelblue', label='Recursivo')
    plt.xticks(rotation=90, ha='right', fontsize=7)
    plt.legend(loc='upper left')
    plt.grid()
    plt.savefig('./img/result_two.pdf')
    plt.show()      

    plt.title('Instância/Tempo - Tempo médio para execução de uma instância')
    plt.xlabel('Tempo/s')
    plt.ylabel('Resultado')
    plt.plot(name_instance, time_iterative, color='orange', label='Iterativo = '+str(f'{np.sum(time_iterative):e}')+' seg')
    plt.plot(name_instance, time_recursive, color='steelblue', label='Recursivo = '+str(f'{np.sum(time_recursive):e}')+' seg')
    plt.xticks(rotation=90, ha='right', fontsize=7)
    plt.legend(fontsize=7,loc='upper left')
    plt.grid()
    plt.savefig('./img/time_two.pdf')
    plt.show()      

def get_average(number_result,lenght):
    time_iterative = np.zeros(lenght)
    time_recursive = np.zeros(lenght)
    for n in range(1,number_result+1):
        with open('./result/result'+str(n)+'.json','r') as file:
            result = json.load(file)
            time_iterative += np.array(list(element['time iterative'] for element in result.values()))
            time_recursive += np.array(list(element['time recursive'] for element in result.values()))
    return time_iterative/number_result,time_recursive/number_result, np.mean(time_iterative), np.mean(time_recursive)   

def plot_average(name_instance, avg_iterative, avg_recursive, mean_iterative, mean_recursive, number_result):
    plt.title('Resultado a partir da média de {} execuções'.format(number_result))
    plt.xlabel('Instâncias')
    plt.ylabel('Tempo/s')    
    plt.plot(name_instance, avg_iterative, color='orange', label='Tempo das execuções iterativas = '+str(f'{mean_iterative:e}')+' seg')
    plt.plot(name_instance, avg_recursive, color='steelblue', label='Tempo das execuções recursivas = '+str(f'{mean_recursive:e}')+' seg')
    plt.xticks(rotation=90, ha='right',fontsize=7)
    plt.legend(fontsize=7, loc='upper left')
    plt.grid()
    plt.savefig('./img/avg_result.pdf')
    plt.show()    

if __name__ == '__main__':
    with open('./number_of_results.txt') as result_txt: number_of_results = int(result_txt.readline())
    if number_of_results == 0: 
        print('Impossible generate a graphic without results!')
        exit(-1)
    with open('./result/result1.json') as result_json: result = json.load(result_json)
    if not path.isdir('./img'):
        if system() == 'Linux': mkdir('./img')
        elif system() == 'Windows': mkdir('./img')
        elif system() == 'Darwin': mkdir('./img')        
    name_instance = list(result.keys())
    result_iterative = list(element['result iterative'] for element in result.values())
    time_iterative = list(element['time iterative'] for element in result.values())
    result_recursive = list(element['result recursive'] for element in result.values())
    time_recursive = list(element['time recursive'] for element in result.values())
    avg_iterative, avg_recursive, mean_iterative, mean_recursive = get_average(number_of_results, len(name_instance))

    plot_iterative(name_instance, time_iterative, result_iterative)
    plot_recursive(name_instance, time_recursive, result_recursive)
    plot_two(name_instance, time_iterative, result_iterative,time_recursive, result_recursive)
    plot_average(name_instance, avg_iterative, avg_recursive, mean_iterative, mean_recursive, number_of_results)