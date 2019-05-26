from knapsack import Knapsack, read_instances, organize_instances
from platform import system
from os import path,mkdir
import numpy as np
from scipy.stats import sem
import matplotlib.pyplot as plt
import json

class Plot:
    def __init__(self):
        self.__plot_topDown(name_instance, time_topDown, result_topDown)
        self.__plot_bottomUp(name_instance, time_bottomUp, result_bottomUp)
        self.__plot_two(name_instance, time_bottomUp, result_bottomUp,time_topDown, result_topDown)
        self.__plot_average(name_instance, avg_bottomUp, avg_topDown, number_of_results)
        self.__plot_mixed(name_instance, time_bottomUp, time_topDown, avg_bottomUp, avg_topDown, number_of_results)

    def __plot_topDown(self, name_instance, time_topDown, result_topDown):
        plt.title('Resultado do algoritmo Top-Down a partir de 1 execução')
        plt.xlabel('Resultado')
        plt.ylabel('Tempo/s')
        plt.scatter(result_topDown, time_topDown, marker='.', color='steelblue',label='Instâncias')
        plt.legend(loc='upper left')
        plt.grid()
        plt.savefig('../img/scatter_topDown.pdf')
        plt.show()

        plt.title('Instância/Resultado - Top-Down')
        plt.xlabel('Instância')
        plt.ylabel('Resultado')
        plt.plot(name_instance, result_topDown, color='steelblue')
        plt.xticks(rotation=90, ha='right',fontsize=7)
        plt.grid()
        plt.savefig('../img/result_topDown.pdf')
        plt.show()      

        plt.title('Instância/Tempo - Top-Down')
        plt.xlabel('Instância')
        plt.ylabel('Tempo/s')
        plt.plot(name_instance, time_topDown, color='steelblue')
        plt.xticks(rotation=90, ha='right',fontsize=7)
        plt.grid()
        plt.savefig('../img/time_topDown.pdf')
        plt.show()

    def __plot_bottomUp(self, name_instance, time_bottomUp, result_bottomUp):
        plt.title('Resultado do algoritmo Bottom-Up a partir de 1 execução')
        plt.xlabel('Resultado')
        plt.ylabel('Tempo/s')
        plt.scatter(result_bottomUp, time_bottomUp, marker='.', color='orange',label='Instâncias')
        plt.legend(loc='upper left')
        plt.grid()
        plt.savefig('../img/scatter_bottomUp.pdf')
        plt.show() 

        plt.title('Instância/Resultado - Bottom-Up')
        plt.xlabel('Instância')
        plt.ylabel('Resultado')
        plt.plot(name_instance, result_bottomUp, color='orange')
        plt.xticks(rotation=90, ha='right',fontsize=7)
        plt.grid()
        plt.savefig('../img/result_bottomUp.pdf')
        plt.show()      

        plt.title('Instância/Tempo - Bottom-Up')
        plt.xlabel('Instância')
        plt.ylabel('Tempo/s')
        plt.plot(name_instance, time_bottomUp, color='orange')
        plt.xticks(rotation=90, ha='right',fontsize=7)
        plt.grid()
        plt.savefig('../img/time_bottomUp.pdf')
        plt.show()  

    def __plot_two(self, name_instance, time_bottomUp, result_bottomUp,time_topDown, result_topDown):
        plt.title('Resultado das duas versões do algoritmo')
        plt.xlabel('Resultado')
        plt.ylabel('Tempo/s')
        plt.scatter(result_topDown, time_topDown, marker='.', color='steelblue', label='Top-Down')
        plt.scatter(result_bottomUp, time_bottomUp, marker='.', color='orange', label='Bottom-Up')
        plt.legend()
        plt.grid()
        plt.savefig('../img/scatter_two.pdf')
        plt.show()

        plt.title('Instância/Resultado - Bottom-Up vs Top-Down')
        plt.xlabel('Instância')
        plt.ylabel('Resultado')
        plt.plot(name_instance, result_topDown, color='steelblue', label='Top-Down')
        plt.plot(name_instance, result_bottomUp, ':', color='orange', label='Bottom-Up')
        plt.xticks(rotation=90, ha='right', fontsize=7)
        plt.legend(loc='upper left')
        plt.grid()
        plt.savefig('../img/result_two.pdf')
        plt.show()      

        plt.title('Instância/Tempo - Tempo médio para execução de uma instância')
        plt.xlabel('Instância')
        plt.ylabel('Tempo/s')
        plt.plot(name_instance, time_topDown, color='steelblue', label='Top-Down')
        plt.plot(name_instance, time_bottomUp, color='orange', label='Bottom-Up')
        plt.xticks(rotation=90, ha='right', fontsize=7)
        plt.legend(fontsize=7,loc='upper left')
        plt.grid()
        plt.savefig('../img/time_two.pdf')
        plt.show()      

    def __plot_average(self, name_instance, avg_bottomUp, avg_topDown, number_result):
        plt.title('Resultado a partir da média de {} execuções'.format(number_result))
        plt.xlabel('Tempo/s')
        plt.ylabel('Resultado')
        plt.scatter(avg_topDown, result_topDown, marker='.', color='steelblue', label='Top-Down')
        plt.scatter(avg_bottomUp, result_bottomUp, marker='.', color='orange', label='Bottom-Up')
        plt.legend()
        plt.grid()
        plt.savefig('../img/avg_scatter.pdf')
        plt.show()    

        plt.title('Resultado a partir da média de {} execuções'.format(number_result))
        plt.xlabel('Instâncias')
        plt.ylabel('Tempo/s')    
        plt.plot(name_instance, avg_topDown, color='steelblue', label='Top-Down')
        plt.plot(name_instance, avg_bottomUp, color='orange', label='Bottom-Up')
        # plt.text(0.5,1.2,'test',fontsize=7)
        plt.xticks(rotation=90, ha='right',fontsize=7)
        plt.legend(fontsize=7, loc='upper left')
        plt.grid()
        plt.savefig('../img/avg_result.pdf')
        plt.show()  

    def __plot_mixed(self, name_instance,time_bottomUp, time_topDown, avg_bottomUp, avg_topDown, number_result):
        plt.title('Resultado a partir da média de {} execuções'.format(number_result))
        plt.xlabel('Tempo/s')
        plt.ylabel('Resultado')
        plt.scatter(time_topDown, result_topDown, marker='.', color='steelblue', label='Top-Down')
        plt.scatter(time_bottomUp, result_bottomUp, marker='.', color='orange', label='Bottom-Up')    
        plt.scatter(avg_topDown, result_topDown, marker='.', color='b', label='Top-Down AVG')
        plt.scatter(avg_bottomUp, result_bottomUp, marker='.', color='orangered', label='Bottom-Up AVG')
        plt.legend()
        plt.grid()
        plt.savefig('../img/mixed_scatter.pdf')
        plt.show()    

        plt.title('Resultado a partir da média de {} execuções'.format(number_result))
        plt.xlabel('Instâncias')
        plt.ylabel('Tempo/s')    
        plt.plot(name_instance, time_topDown, color='steelblue', label='Top-Down')
        plt.plot(name_instance, time_bottomUp, color='orange', label='Bottom-Up')    
        plt.plot(name_instance, avg_topDown, color='b', label='Top-Down AVG')
        plt.plot(name_instance, avg_bottomUp, color='orangered', label='Bottom-Up AVG')
        plt.xticks(rotation=90, ha='right',fontsize=7)
        plt.legend(fontsize=7, loc='upper left')
        plt.grid()
        plt.savefig('../img/mixed_result.pdf')
        plt.show() 

def get_average(number_result,lenght):
        time_bottomUp = np.zeros(lenght)
        time_topDown = np.zeros(lenght)
        for n in range(1,number_result+1):
            with open('../result/result'+str(n)+'.json','r') as file:
                result = json.load(file)
                time_bottomUp += np.array(list(element['time bottomUp'] for element in result.values()))
                time_topDown += np.array(list(element['time topDown'] for element in result.values()))
        return time_bottomUp/number_result, time_topDown/number_result 
  
if __name__ == '__main__':
    with open('./number_of_results.txt') as result_txt: number_of_results = int(result_txt.readline())
    if number_of_results == 0: 
        print('\nImpossible generate a graphic without results!\n')
        exit(-1)
    with open('../result/result1.json') as result_json: result = json.load(result_json)
    if not path.isdir('../img'):
        if system() == 'Linux': mkdir('../img')
        elif system() == 'Windows': mkdir('../img')
        elif system() == 'Darwin': mkdir('../img')        
    name_instance = list(result.keys())
    result_topDown = list(element['result topDown'] for element in result.values())
    time_topDown = list(element['time topDown'] for element in result.values())
    result_bottomUp = list(element['result bottomUp'] for element in result.values())
    time_bottomUp = list(element['time bottomUp'] for element in result.values())
    avg_bottomUp, avg_topDown= get_average(number_of_results, len(name_instance))

    print('1 execucao')
    print('temp topdown max:',np.amax(time_topDown))
    print('instancia que demorou mais tempo topdown:',np.where(time_topDown == np.amax(time_topDown))[0][0])
    print('temp bottomUp max:',np.amax(time_bottomUp))
    print('instancia que demorou mais tempo bottomup:',np.where(time_bottomUp == np.amax(time_bottomUp))[0][0])    
    print('media topdown:',np.mean(time_topDown))
    print('media bottomup:',np.mean(time_bottomUp))    
    print('tempo total topdown:',np.sum(time_topDown))
    print('tempo total bottomup:',np.sum(time_bottomUp))

    print()
    print('{} execucoes'.format(number_of_results))
    print('temp topdown max:',np.amax(avg_topDown))
    print('em media, a mais demorada foi a:',np.where(avg_topDown == np.amax(avg_topDown))[0][0])    
    print('temp bottomUp max:',np.amax(avg_bottomUp))
    print('em media, a mais demorada foi a:',np.where(avg_bottomUp == np.amax(avg_bottomUp))[0][0])

    print('media topdown:',np.mean(avg_topDown)*number_of_results)
    print('media topdown:',np.mean(avg_bottomUp)*number_of_results)

    print('tempo total topdown:',np.mean(avg_topDown)*number_of_results*len(name_instance))
    print('tempo total bottomup:',np.mean(avg_bottomUp)*number_of_results*len(name_instance))

