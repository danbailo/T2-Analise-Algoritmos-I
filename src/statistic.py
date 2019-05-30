import numpy as np
import json
from scipy import stats
from statsmodels import robust

class Statistic:
    def __init__(self):
        with open('./number_of_results.txt') as result_txt: self.__number_result = int(result_txt.readline())
        if self.__number_result == 0: 
            print('\nImpossible calculate the statistics without results!\n')
            exit(-1)
        with open('../result/result1.json') as result_json: self.result = json.load(result_json)  
        self.__name_instance = list(self.result.keys())
        self.__result_topDown = list(element['result topDown'] for element in self.result.values())
        self.__time_topDown = list(element['time topDown'] for element in self.result.values())
        self.__result_bottomUp = list(element['result bottomUp'] for element in self.result.values())
        self.__time_bottomUp = list(element['time bottomUp'] for element in self.result.values())
        self.__avg_bottomUp, self.__avg_topDown = self.__get_average(self.__number_result, len(self.__name_instance))        

    def __get_average(self, number_result, lenght):
            time_bottomUp = np.zeros(lenght)
            time_topDown = np.zeros(lenght)
            for n in range(1,number_result+1):
                with open('../result/result'+str(n)+'.json','r') as file:
                    result = json.load(file)
                    time_bottomUp += np.array(list(element['time bottomUp'] for element in result.values()))
                    time_topDown += np.array(list(element['time topDown'] for element in result.values()))
            return time_bottomUp/number_result, time_topDown/number_result

    def load_result(self):
        return self.__number_result, self.__name_instance, self.__time_topDown, self.__result_topDown, \
        self.__time_bottomUp, self.__result_bottomUp, self.__avg_topDown, self.__avg_bottomUp

    def get_topDown(self):
        return self.__time_topDown
    def get_bottomUp(self):
        return self.__time_bottomUp   
    def get_AVG_topDown(self):
        return self.__avg_topDown   
    def get_AVG_bottomUp(self):
        return self.__avg_bottomUp
    def get_number_result(self):
        return self.__number_result                 

def get_statistic(result, number_result):
    print('\ntempo total:',np.sum(result))
    print('media/instancia:',np.mean(result))
    print('temp max:',np.amax(result))
    print('temp min:',np.amin(result))
    print('instancia que demorou mais tempo:',np.where(result == np.amax(result))[0][0])
    print('instancia que demorou menos tempo:',np.where(result == np.amin(result))[0][0])
    print('amplitute(max-min):',np.ptp(result))
    print('erro:',stats.sem(result))
    print('variancia:',np.var(result))
    print('desvio padrao:',np.std(result))
    print('desvio absoluto:',robust.mad(result))

def get_time_total(result, number_result):
    print('\nTEMPO TOTAL PARA EXECUTAR {} VEZES:'.format(number_result),np.sum(result)*number_result)
    print('TEMPO MEDIO POR INSTANCIA EM CADA EXECUCAO:',np.mean(result)*number_result)    

if __name__ == "__main__":

    get_statistic(Statistic().get_topDown(), Statistic().get_number_result())
    get_statistic(Statistic().get_bottomUp(), Statistic().get_number_result())
    get_statistic(Statistic().get_AVG_topDown(), Statistic().get_number_result())
    get_statistic(Statistic().get_AVG_bottomUp(), Statistic().get_number_result())

    get_time_total(Statistic().get_AVG_topDown(), Statistic().get_number_result())
    get_time_total(Statistic().get_AVG_bottomUp(), Statistic().get_number_result())