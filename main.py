from functions import read_instances, organize_instances, get_result

if __name__ == "__main__":
    all_instances = read_instances('./instancias/')
    number_items, weight_max, values_items, weight_items = organize_instances(all_instances)
    result, time = get_result(all_instances, number_items, weight_max, values_items, weight_items)

    print('result', result)
    print('time', time)