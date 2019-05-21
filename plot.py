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
        plt.annotate(txt, (time_iterative[i], result_iterative[i]), fontsize=7)
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

    plt.title('Instância/Resultado - Iterativo')
    plt.xlabel('Instância')
    plt.ylabel('Resultado')
    plt.plot(name_instance, result_iterative, color='orange')
    plt.xticks(rotation=90, ha='right',fontsize=7)
    # plt.legend()
    plt.grid()
    plt.savefig('./img/instancia_iterative_recursive.pdf')
    plt.show()      

    plt.title('Instância/Tempo - Iterativo')
    plt.xlabel('Tempo/s')
    plt.ylabel('Resultado')
    plt.plot(name_instance, time_iterative, color='orange')
    plt.xticks(rotation=90, ha='right',fontsize=7)
    # plt.legend()
    plt.grid()
    plt.savefig('./img/instacia_tempo_iterative.pdf')
    plt.show()  

def plot_recursive(name_instance, time_recursive, result_recursive):
    time_recursive_sorted = sorted(time_recursive)
    plt.style.use('default')
    plt.title('Resultado do algoritmo recursivo')
    plt.xlabel('Tempo/s')
    plt.ylabel('Resultado')
    plt.scatter(time_recursive, result_recursive, marker='.', color='k',label='Instâncias')
    for i, txt in enumerate(name_instance):
        plt.annotate(txt, (time_recursive[i], result_recursive[i]))
    plt.plot(time_recursive, result_recursive)
    plt.legend()
    plt.grid()

    plt.savefig('./img/recursive.pdf')
    plt.show()

    plt.title('Resultado do algoritmo iterativo, ordenado')
    plt.xlabel('Tempo/s')
    plt.ylabel('Resultado')
    plt.scatter(time_recursive_sorted, result_recursive, marker='.', color='k',label='Instâncias')
    for i, txt in enumerate(name_instance):
        plt.annotate(txt, (time_recursive_sorted[i], result_recursive[i]), fontsize=7)    
    plt.plot(time_recursive_sorted, result_recursive)
    plt.grid()
    plt.savefig('./img/recursive_sorted.pdf')
    plt.show()  

    plt.title('Instância/Resultado - Recursivo')
    plt.xlabel('Instância')
    plt.ylabel('Resultado')
    plt.plot(name_instance, result_recursive)
    plt.xticks(rotation=90, ha='right',fontsize=7)
    # plt.legend()
    plt.grid()
    plt.savefig('./img/instacia_resultado_recursive.pdf')
    plt.show()      

    plt.title('Instância/Tempo - Recursivo')
    plt.xlabel('Tempo/s')
    plt.ylabel('Resultado')
    plt.plot(name_instance, time_recursive)
    plt.xticks(rotation=90, ha='right',fontsize=7)
    # plt.legend()
    plt.grid()
    plt.savefig('./img/instacia_tempo_recursive.pdf')
    plt.show()  

def plot_it_vs_rec(name_instance, time_iterative, result_iterative,time_recursive, result_recursive):
    time_iterative_sorted = sorted(time_iterative)
    time_recursive_sorted = sorted(time_recursive)

    plt.style.use('default')
    plt.title('Resultado das duas versões do algoritmo')
    plt.xlabel('Tempo/s')
    plt.ylabel('Resultado')
    plt.scatter(time_iterative, result_iterative, marker='.', color='c',label='Iterativo')
    plt.scatter(time_recursive, result_recursive, marker='.', color='m',label='Recursivo')
    for i, txt in enumerate(name_instance):
        plt.annotate(txt, (time_iterative[i], result_iterative[i]),fontsize=7)
        plt.annotate(txt, (time_recursive[i], result_recursive[i]),fontsize=7)
    plt.plot(time_iterative, result_iterative, label='Iterativo')
    plt.plot(time_recursive, result_recursive, label='Recursivo')
    plt.legend()
    plt.grid()

    plt.savefig('./img/iterative_recursive.pdf')
    plt.show()

    plt.title('Resultado das duas versões do algoritmo, ordenado')
    plt.xlabel('Tempo/s')
    plt.ylabel('Resultado')
    plt.scatter(time_iterative_sorted, result_iterative, marker='.', color='c',label='Iterativo')
    plt.scatter(time_recursive_sorted, result_recursive, marker='.', color='m',label='Recursivo')
    for i, txt in enumerate(name_instance):
        plt.annotate(txt, (time_iterative_sorted[i], result_iterative[i]),fontsize=7)    
        plt.annotate(txt, (time_recursive_sorted[i], result_recursive[i]),fontsize=7)  

    plt.plot(time_iterative_sorted, result_iterative, label='Iterativo')
    plt.plot(time_recursive_sorted, result_recursive, label='Recursivo')
    plt.legend()
    plt.grid()
    plt.savefig('./img/iterative_recursive_sorted.pdf')
    plt.show()  

    plt.title('Instância/Resultado - Iterativo vs Recursivo')
    plt.xlabel('Instância')
    plt.ylabel('Resultado')
    plt.plot(name_instance, result_iterative, label='Iterativo')
    plt.plot(name_instance, result_recursive, label='Recursivo')
    plt.xticks(rotation=90, ha='right',fontsize=7)
    plt.legend()
    plt.grid()
    plt.savefig('./img/instancia_result_iterative_recursive.pdf')
    plt.show()      

    plt.title('Instância/Tempo - Iterativo')
    plt.xlabel('Tempo/s')
    plt.ylabel('Resultado')
    plt.plot(name_instance, time_iterative, label='Iterativo')
    plt.plot(name_instance, time_recursive, label='Recursivo')
    plt.xticks(rotation=90, ha='right',fontsize=7)
    plt.legend()
    plt.grid()
    plt.savefig('./img/instancia_tempo_iterative_recursive.pdf')
    plt.show()      

if __name__ == "__main__":
    with open("result.json") as f:
	    result = json.load(f)

    name_instance = list(result.keys())
    result_iterative = list(element['result iterative'] for element in result.values())
    time_iterative = list(element['time iterative'] for element in result.values())
    result_recursive = list(element['result recursive'] for element in result.values())
    time_recursive = list(element['time recursive'] for element in result.values())

    # plot_iterative(name_instance, time_iterative, result_iterative)
    # plot_recursive(name_instance, time_recursive, result_recursive)
    plot_it_vs_rec(name_instance, time_iterative, result_iterative,time_recursive, result_recursive)