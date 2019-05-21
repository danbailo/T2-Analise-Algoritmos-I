from knapsack import Knapsack, read_instances, organize_instances
import json
import matplotlib.pyplot as plt

#https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html

def plot_iterative(name_instance, time_iterative, result_iterative):
    time_iterative_sorted = sorted(time_iterative)
    plt.style.use('default')
    plt.title('Resultado do algoritmo iterativo')
    plt.xlabel('Tempo/s')
    plt.ylabel('Resultado')
    plt.scatter(time_iterative, result_iterative, marker='.', color='k',label='Instâncias')
    for i, txt in enumerate(name_instance):
        plt.annotate(txt, (time_iterative[i], result_iterative[i]))
    plt.plot(time_iterative, result_iterative, color='orange')
    plt.legend()
    plt.grid()

    plt.savefig('./img/iterative.pdf')
    plt.show()

    plt.title('Resultado do algoritmo iterativo, ordenado')
    plt.xlabel('Tempo/s')
    plt.ylabel('Resultado')
    plt.scatter(time_iterative_sorted, result_iterative, marker='.', color='k',label='Instâncias')
    for i, txt in enumerate(name_instance):
        plt.annotate(txt, (time_iterative_sorted[i], result_iterative[i]))    
    plt.plot(time_iterative_sorted, result_iterative, color='orange')
    plt.grid()
    plt.savefig('./img/iterative_sorted.pdf')
    plt.show()  

    plt.title('Instância/Resultado')
    plt.xlabel('Instância')
    plt.ylabel('Resultado')
    plt.plot(name_instance, result_iterative, color='orange')
    plt.xticks(rotation=90, ha='right',fontsize=7)
    # plt.legend()
    plt.grid()
    plt.savefig('./img/instacia_resultado.pdf')
    plt.show()      

    plt.title('Instância/Tempo')
    plt.xlabel('Tempo/s')
    plt.ylabel('Resultado')
    plt.plot(name_instance, time_iterative, color='orange')
    plt.xticks(rotation=90, ha='right',fontsize=7)
    # plt.legend()
    plt.grid()
    plt.savefig('./img/instacia_tempo.pdf')
    plt.show()  

if __name__ == "__main__":
    with open("result.json") as f:
	    result = json.load(f)

    name_instance = list(result.keys())
    result_iterative = list(element['result iterative'] for element in result.values())
    time_iterative = list(element['time iterative'] for element in result.values())
    result_recursive = list(element['result recursive'] for element in result.values())
    time_recursive = list(element['time recursive'] for element in result.values())

    plot_iterative(name_instance, time_iterative, result_iterative)

    plt.title('Resultado do algoritmo recursivo')
    plt.xlabel('Tempo/s')
    plt.ylabel('Resultado')
    plt.plot(time_recursive, result_recursive)
    plt.xticks(rotation=90, ha='right')

    plt.legend()
    plt.grid()
    plt.savefig('./img/recursive.pdf')
    # plt.show()

    plt.title('Resultado do algoritmo recursivo, ordenado')
    plt.xlabel('Tempo/s')
    plt.ylabel('Resultado')
    plt.plot(sorted(time_recursive), result_recursive)
    plt.xticks(rotation=90, ha='right')
    plt.grid()
    plt.savefig('./img/recursive_sorted.pdf')
    # plt.show()   

    ############################################################################

    plt.title('Iterative vs Recursive')
    plt.xlabel('Tempo/s')
    plt.ylabel('Resultado')
    plt.plot(time_iterative, result_iterative, label='Iterativo')
    plt.plot(time_recursive, result_recursive, label='Recursivo')
    plt.xticks(rotation=90, ha='right')
    plt.legend()
    plt.grid()
    plt.savefig('./img/iterative_vs_recursive.pdf')
    # plt.show()   

    plt.title('Iterative vs Recursive SORTED')
    plt.xlabel('Tempo/s')
    plt.ylabel('Resultado')
    plt.plot(sorted(time_iterative), result_iterative, label='Iterativo')
    plt.plot(sorted(time_recursive), result_recursive, label='Recursivo')
    plt.xticks(rotation=90, ha='right')
    plt.legend()
    plt.grid()
    plt.savefig('./img/iterative_vs_recursive_sorted.pdf')
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