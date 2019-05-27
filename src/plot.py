from knapsack import Knapsack, read_instances, organize_instances
from platform import system
from os import path,mkdir
import numpy as np
from scipy import stats
from statsmodels import robust
import matplotlib.pyplot as plt
import json

class Plot:
    def __init__(self, number_result, name_instance, time_topDown, result_topDown, time_bottomUp, result_bottomUp, avg_topDown, avg_bottomUp):
        self.__name_instance = name_instance
        self.__number_result = number_result
        self.__time_topDown = time_topDown
        self.__result_topDown = result_topDown
        self.__time_bottomUp = time_bottomUp
        self.__result_bottomUp = result_bottomUp        
        self.__avg_topDown = avg_topDown
        self.__avg_bottomUp = avg_bottomUp

        self.__plot_topDown()
        self.__plot_bottomUp()
        self.__plot_two()
        self.__plot_average()
        self.__plot_mixed()

    def __plot_topDown(self):
        plt.title('Resultado do algoritmo Top-Down a partir de 1 execução')
        plt.xlabel('Resultado')
        plt.ylabel('Tempo/s')
        plt.scatter(self.__result_topDown, self.__time_topDown, marker='.', color='steelblue',label='Instâncias')
        plt.legend(loc='upper left')
        plt.grid()
        plt.savefig('../img/scatter_topDown.pdf')
        plt.show()

        plt.title('Instância/Resultado - Top-Down')
        plt.xlabel('Instância')
        plt.ylabel('Resultado')
        plt.plot(self.__name_instance, self.__result_topDown, color='steelblue')
        # plt.legend(loc='upper left')
        plt.xticks(rotation=90, ha='right',fontsize=7)
        plt.grid()
        plt.savefig('../img/result_topDown.pdf')
        plt.show()      

        plt.title('Instância/Tempo - Top-Down')
        plt.xlabel('Instância')
        plt.ylabel('Tempo/s')
        plt.plot(self.__name_instance, self.__time_topDown, color='steelblue')
        # plt.legend(loc='upper left')
        plt.xticks(rotation=90, ha='right',fontsize=7)
        plt.grid()
        plt.savefig('../img/time_topDown.pdf')
        plt.show()

    def __plot_bottomUp(self):
        plt.title('Resultado do algoritmo Bottom-Up a partir de 1 execução')
        plt.xlabel('Resultado')
        plt.ylabel('Tempo/s')
        plt.scatter(self.__result_bottomUp, self.__time_bottomUp, marker='.', color='orange',label='Instâncias')
        plt.legend(loc='upper left')
        plt.grid()
        plt.savefig('../img/scatter_bottomUp.pdf')
        plt.show() 

        plt.title('Instância/Resultado - Bottom-Up')
        plt.xlabel('Instância')
        plt.ylabel('Resultado')
        plt.plot(self.__name_instance, self.__result_bottomUp, color='orange')
        # plt.legend(loc='upper left')
        plt.xticks(rotation=90, ha='right',fontsize=7)
        plt.grid()
        plt.savefig('../img/result_bottomUp.pdf')
        plt.show()      

        plt.title('Instância/Tempo - Bottom-Up')
        plt.xlabel('Instância')
        plt.ylabel('Tempo/s')
        plt.plot(self.__name_instance, self.__time_bottomUp, color='orange')
        # plt.legend(loc='upper left')
        plt.xticks(rotation=90, ha='right',fontsize=7)
        plt.grid()
        plt.savefig('../img/time_bottomUp.pdf')
        plt.show()  

    def __plot_two(self):
        plt.title('Resultado das duas versões do algoritmo')
        plt.xlabel('Resultado')
        plt.ylabel('Tempo/s')
        plt.scatter(self.__result_topDown, self.__time_topDown, marker='.', color='steelblue', label='Top-Down')
        plt.scatter(self.__result_bottomUp, self.__time_bottomUp, marker='.', color='orange', label='Bottom-Up')
        plt.legend(fontsize=10,loc='upper left')
        plt.grid()
        plt.savefig('../img/scatter_two.pdf')
        plt.show()

        plt.title('Instância/Resultado - Bottom-Up vs Top-Down')
        plt.xlabel('Instância')
        plt.ylabel('Resultado')
        plt.plot(self.__name_instance, self.__result_topDown, color='steelblue', label='Top-Down')
        plt.plot(self.__name_instance, self.__result_bottomUp, ':', color='orange', label='Bottom-Up')
        plt.xticks(rotation=90, ha='right', fontsize=7)
        plt.legend(fontsize=10,loc='upper left')
        plt.grid()
        plt.savefig('../img/result_two.pdf')
        plt.show()      

        plt.title('Instância/Tempo - Tempo médio para execução de uma instância')
        plt.xlabel('Instância')
        plt.ylabel('Tempo/s')
        plt.plot(self.__name_instance, self.__time_topDown, color='steelblue', label='Top-Down')
        plt.plot(self.__name_instance, self.__time_bottomUp, color='orange', label='Bottom-Up')
        plt.xticks(rotation=90, ha='right', fontsize=7)
        plt.legend(fontsize=10,loc='upper left')
        plt.grid()
        plt.savefig('../img/time_two.pdf')
        plt.show()      

    def __plot_average(self):
        plt.title('Resultado a partir da média de {} execuções'.format(self.__number_result))
        plt.xlabel('Resultado')
        plt.ylabel('Tempo/s')
        plt.scatter(self.__result_topDown, self.__avg_topDown, marker='.', color='steelblue', label='Top-Down')
        plt.scatter(self.__result_bottomUp, self.__avg_bottomUp, marker='.', color='orange', label='Bottom-Up')
        plt.legend(fontsize=10, loc='upper left')
        plt.grid()
        plt.savefig('../img/avg_scatter.pdf')
        plt.show()    

        plt.title('Resultado a partir da média de {} execuções'.format(self.__number_result))
        plt.xlabel('Instâncias')
        plt.ylabel('Tempo/s')    
        plt.plot(self.__name_instance, self.__avg_topDown, color='steelblue', label='Top-Down')
        plt.plot(self.__name_instance, self.__avg_bottomUp, color='orange', label='Bottom-Up')
        # plt.text(0.5,1.2,'test',fontsize=7)
        plt.xticks(rotation=90, ha='right',fontsize=7)
        plt.legend(fontsize=10, loc='upper left')
        plt.grid()
        plt.savefig('../img/avg_result.pdf')
        plt.show()  

    def __plot_mixed(self):
        plt.title('Resultado a partir da média de {} execuções'.format(self.__number_result))
        plt.xlabel('Resultado')
        plt.ylabel('Resultado')
        plt.scatter(self.__result_topDown, self.__time_topDown, marker='.', color='steelblue', label='Top-Down')
        plt.scatter(self.__result_bottomUp,self.__time_bottomUp,  marker='.', color='orange', label='Bottom-Up')    
        plt.scatter(self.__result_topDown, self.__avg_topDown, marker='.', color='b', label='Top-Down AVG')
        plt.scatter(self.__result_bottomUp,self.__avg_bottomUp,  marker='.', color='orangered', label='Bottom-Up AVG')
        plt.legend(fontsize=10, loc='upper left')
        plt.grid()
        plt.savefig('../img/mixed_scatter.pdf')
        plt.show()    

        plt.title('Resultado a partir da média de {} execuções'.format(self.__number_result))
        plt.xlabel('Instâncias')
        plt.ylabel('Tempo/s')    
        plt.plot(self.__name_instance, self.__time_topDown, color='steelblue', label='Top-Down')
        plt.plot(self.__name_instance, self.__time_bottomUp, color='orange', label='Bottom-Up')    
        plt.plot(self.__name_instance, self.__avg_topDown, color='b', label='Top-Down AVG')
        plt.plot(self.__name_instance, self.__avg_bottomUp, color='orangered', label='Bottom-Up AVG')
        plt.xticks(rotation=90, ha='right',fontsize=7)
        plt.legend(fontsize=10, loc='upper left')
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
    with open('./number_of_results.txt') as result_txt: number_result = int(result_txt.readline())
    if number_result == 0: 
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
    avg_bottomUp, avg_topDown= get_average(number_result, len(name_instance))

    # Plot(number_result, name_instance, time_topDown, result_topDown, time_bottomUp, result_bottomUp, avg_topDown, avg_bottomUp)

    print('1 execucao')
    print('\ntempo total topdown:',np.sum(time_topDown))
    print('media/instancia topDown:',np.mean(time_topDown))
    print('temp topdown max:',np.amax(time_topDown))
    print('temp topdown min:',np.amin(time_topDown))
    print('instancia que demorou mais tempo topdown:',np.where(time_topDown == np.amax(time_topDown))[0][0])
    print('instancia que demorou menos tempo topdown:',np.where(time_topDown == np.amin(time_topDown))[0][0])
    print('amplitute(max-min):',np.ptp(time_topDown))
    print('erro:',stats.sem(time_topDown))
    print('variancia:',np.var(time_topDown))
    print('desvio padrao:',np.std(time_topDown))
    print('desvio absoluto:',robust.mad(time_topDown))


    
    print('\nmedia/instancia topDown:',np.mean(time_bottomUp))
    print('tempo total topdown:',np.sum(time_bottomUp))
    print('temp topdown max:',np.amax(time_bottomUp))
    print('temp topdown min:',np.amin(time_bottomUp))
    print('instancia que demorou mais tempo topdown:',np.where(time_bottomUp == np.amax(time_bottomUp))[0][0])
    print('instancia que demorou menos tempo topdown:',np.where(time_bottomUp == np.amin(time_bottomUp))[0][0])
    print('amplitute(max-min):',np.ptp(time_bottomUp))
    print('erro:',stats.sem(time_bottomUp))
    print('variancia:',np.var(time_bottomUp))
    print('desvio padrao:',np.std(time_bottomUp))
    print('desvio absoluto:',robust.mad(time_bottomUp))

    print('='*50)

    print('{} execucoes'.format(number_result))

    print('\nmedia/instancia topDown:',np.mean(avg_topDown))
    print('tempo total topdown:',np.sum(avg_topDown))
    print('temp topdown max:',np.amax(avg_topDown))
    print('instancia que demorou mais tempo topdown:',np.where(avg_topDown == np.amax(avg_topDown))[0][0])    
    print('desvio padrao:',np.std(avg_topDown))
    print('variancia:',np.var(avg_topDown))
    print('TEMPO TOTAL PARA EXECUTAR {} VEZES topdown:'.format(number_result),np.sum(avg_topDown)*number_result)
    print('TEMPO MEDIO POR INSTANCIA EM CADA EXECUCAO topdown:',np.mean(avg_topDown)*number_result)


    print('\nmedia/instancia bottomUp:',np.mean(avg_bottomUp))
    print('tempo total bottomUp:',np.sum(avg_bottomUp))
    print('temp bottomUp max:',np.amax(avg_bottomUp))
    print('instancia que demorou mais tempo bottomUp:',np.where(avg_bottomUp == np.amax(avg_bottomUp))[0][0])    
    print('desvio padrao:',np.std(avg_bottomUp))
    print('variancia:',np.var(avg_bottomUp))
    print('TEMPO TOTAL PARA EXECUTAR {} VEZES bottomUp:'.format(number_result),np.sum(avg_bottomUp)*number_result)
    print('TEMPO MEDIO POR INSTANCIA EM CADA EXECUCAO bottomUp:',np.mean(avg_bottomUp)*number_result)
