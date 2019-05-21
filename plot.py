from knapsack import Knapsack, read_instances, organize_instances
import json
import matplotlib.pyplot as plt

#https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html

def plot_iterative(name_instance, time_iterative, result_iterative):
    plt.title('Resultado do algoritmo iterativo')
    plt.xlabel('Tempo/s')
    plt.ylabel('Resultado')
    plt.plot(time_iterative, result_iterative)
    plt.plot(time_iterative, result_iterative, 'k.', label='Instâncias')
    plt.legend()
    plt.grid()

    plt.savefig('./img/iterative.pdf')
    plt.show()

    plt.title('Resultado do algoritmo iterativo')
    plt.xlabel('Tempo/s')
    plt.ylabel('Resultado')
    plt.plot(name_instance, result_iterative)
    #tentar nomear cada ponto do plot https://stackoverflow.com/questions/14432557/matplotlib-scatter-plot-with-different-text-at-each-data-point/14434334
    #plt.annotate
    plt.xticks(rotation=90, ha='right')
    plt.legend()
    plt.grid()

    plt.savefig('./img/iterative_instance.pdf')
    plt.show()  

    plt.title('Resultado do algoritmo iterativo, ordenado')
    plt.xlabel('Tempo/s')
    plt.ylabel('Resultado')
    plt.plot(sorted(time_iterative), result_iterative)
    plt.grid()
    plt.savefig('./img/iterative_sorted.pdf')
    plt.show()        


all_instances = read_instances('./instancias/')
number_items, weight_max, values_items, weight_items = organize_instances(all_instances)
result_iterative, time_iterative, result_recursive, time_recursive = \
Knapsack().get_result(all_instances, number_items, weight_max, values_items, weight_items)

name_instance = list(all_instances.keys())

data = {}
k = 0
for instance in all_instances:
    data[instance] = {
        'result iterative':result_iterative[k], 'time iterative':time_iterative[k],\
        'result recursive':result_recursive[k], 'time recursive':time_recursive[k]}
    k += 1

with open('result.json','w') as file: file.write(json.dumps(data,indent=4))    

# print('result_iterative', result_iterative)
# print('\ntime_iterative', time_iterative)
# print('\ntime_sorted', sorted(time_iterative))
# print('\nresult_recursive', result_recursive)        
# print('\ntime_recursive', time_recursive)
# print('\ntime_sorted', sorted(time_recursive))
print()

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