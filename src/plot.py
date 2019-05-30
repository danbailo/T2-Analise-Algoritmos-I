from statistic import Statistic
from platform import system
from os import path,mkdir
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
        if not path.isdir('../img'):
            if system() == 'Linux': mkdir('../img')
            elif system() == 'Windows': mkdir('../img')
            elif system() == 'Darwin': mkdir('../img')       
    
    def plot_all(self):
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
        plt.xticks(rotation=90, ha='right',fontsize=7)
        plt.grid()
        plt.savefig('../img/result_topDown.pdf')
        plt.show()      

        plt.title('Instância/Tempo - Top-Down')
        plt.xlabel('Instância')
        plt.ylabel('Tempo/s')
        plt.plot(self.__name_instance, self.__time_topDown, color='steelblue')
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

        plt.title('Instância/Tempo - Comparando resultados para 1 execução')
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
  
if __name__ == '__main__':

    number_result, name_instance, time_topDown, result_topDown, time_bottomUp, result_bottomUp, avg_topDown, avg_bottomUp\
         = Statistic().load_result()
    plot = Plot(number_result, name_instance, time_topDown, result_topDown, time_bottomUp, result_bottomUp, avg_topDown, avg_bottomUp)
    plot.plot_all()
