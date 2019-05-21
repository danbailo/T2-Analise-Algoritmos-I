from knapsack import Knapsack, read_instances, organize_instances
import json

if __name__ == "__main__":
    all_instances = read_instances('./instancias/')
    number_items, weight_max, values_items, weight_items = organize_instances(all_instances)
    result_iterative, time_iterative, result_recursive, time_recursive = \
    Knapsack().get_result(all_instances, number_items, weight_max, values_items, weight_items)

    data = {}
    k = 0
    for instance in all_instances:
        data[instance] = {
            'result iterative':result_iterative[k], 'time iterative':time_iterative[k],\
            'result recursive':result_recursive[k], 'time recursive':time_recursive[k]}
        k += 1

    with open('result.json','w') as file: file.write(json.dumps(data,indent=4)) 