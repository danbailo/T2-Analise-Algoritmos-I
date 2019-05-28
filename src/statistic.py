import numpy as np
import json
from scipy import stats
from statsmodels import robust

def get_average(number_result,lenght):
        time_bottomUp = np.zeros(lenght)
        time_topDown = np.zeros(lenght)
        for n in range(1,number_result+1):
            with open('../result/result'+str(n)+'.json','r') as file:
                result = json.load(file)
                time_bottomUp += np.array(list(element['time bottomUp'] for element in result.values()))
                time_topDown += np.array(list(element['time topDown'] for element in result.values()))
        return time_bottomUp/number_result, time_topDown/number_result

def load_result():
    with open('./number_of_results.txt') as result_txt: number_result = int(result_txt.readline())
    if number_result == 0: 
        print('\nImpossible generate a graphic without results!\n')
        exit(-1)
    with open('../result/result1.json') as result_json: result = json.load(result_json) 
    name_instance = list(result.keys())
    result_topDown = list(element['result topDown'] for element in result.values())
    time_topDown = list(element['time topDown'] for element in result.values())
    result_bottomUp = list(element['result bottomUp'] for element in result.values())
    time_bottomUp = list(element['time bottomUp'] for element in result.values())
    avg_bottomUp, avg_topDown = get_average(number_result, len(name_instance))   
    return number_result, name_instance, time_topDown, result_topDown, time_bottomUp, result_bottomUp, avg_topDown, avg_bottomUp         

if __name__ == "__main__":
    with open('./number_of_results.txt') as result_txt: number_result = int(result_txt.readline())
    if number_result == 0: 
        print('\nImpossible generate a graphic without results!\n')
        exit(-1)
    with open('../result/result1.json') as result_json: result = json.load(result_json)  
    name_instance = list(result.keys())
    result_topDown = list(element['result topDown'] for element in result.values())
    time_topDown = list(element['time topDown'] for element in result.values())
    result_bottomUp = list(element['result bottomUp'] for element in result.values())
    time_bottomUp = list(element['time bottomUp'] for element in result.values())
    avg_bottomUp, avg_topDown = get_average(number_result, len(name_instance))

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
    
    print('\ntempo total topdown:',np.sum(time_bottomUp))
    print('media/instancia topDown:',np.mean(time_bottomUp))
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

    print('avg execucao')
    print('\ntempo total topdown:',np.sum(avg_topDown))
    print('media/instancia topDown:',np.mean(avg_topDown))
    print('temp topdown max:',np.amax(avg_topDown))
    print('temp topdown min:',np.amin(avg_topDown))
    print('instancia que demorou mais tempo topdown:',np.where(avg_topDown == np.amax(avg_topDown))[0][0])
    print('instancia que demorou menos tempo topdown:',np.where(avg_topDown == np.amin(avg_topDown))[0][0])
    print('amplitute(max-min):',np.ptp(avg_topDown))
    print('erro:',stats.sem(avg_topDown))
    print('variancia:',np.var(avg_topDown))
    print('desvio padrao:',np.std(avg_topDown))
    print('desvio absoluto:',robust.mad(avg_topDown))
    print('TEMPO TOTAL PARA EXECUTAR {} VEZES topdown:'.format(number_result),np.sum(avg_topDown)*number_result)
    print('TEMPO MEDIO POR INSTANCIA EM CADA EXECUCAO topdown:',np.mean(avg_topDown)*number_result)

    print('\ntempo total bottomUp:',np.sum(avg_bottomUp))
    print('media/instancia topDown:',np.mean(avg_bottomUp))
    print('temp bottomUp max:',np.amax(avg_bottomUp))
    print('temp bottomUp min:',np.amin(avg_bottomUp))
    print('instancia que demorou mais tempo bottomUp:',np.where(avg_bottomUp == np.amax(avg_bottomUp))[0][0])
    print('instancia que demorou menos tempo bottomUp:',np.where(avg_bottomUp == np.amin(avg_bottomUp))[0][0])
    print('amplitute(max-min):',np.ptp(avg_bottomUp))
    print('erro:',stats.sem(avg_bottomUp))
    print('variancia:',np.var(avg_bottomUp))
    print('desvio padrao:',np.std(avg_bottomUp))
    print('desvio absoluto:',robust.mad(avg_bottomUp))    
    print('TEMPO TOTAL PARA EXECUTAR {} VEZES bottomUp:'.format(number_result),np.sum(avg_bottomUp)*number_result)
    print('TEMPO MEDIO POR INSTANCIA EM CADA EXECUCAO bottomUp:',np.mean(avg_bottomUp)*number_result)