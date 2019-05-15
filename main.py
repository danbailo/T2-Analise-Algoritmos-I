# n // número de itens
# W // capacidade da mochila

# v_1 p_1 //valor e peso do item 1
# v_2 p_2 //valor e peso do item 2
# …       //valor e peso do item i
# v_n p_n //valor e peso do item n

from os import listdir
from os.path import isfile, join
from sys import argv
from timeit import timeit

def mochila(weight_max,number_items,weight_items, values_items):
	number_items=len(weight_items)
	dotVec=lambda x,bs:sum((x[i]for i in range(len(x)) if bs[i]=="1"))
	bs="".zfill(number_items)
	ans=0
	while "0" in bs:
		if dotVec(weight_items,bs)<=weight_max:
			ans=max(ans,dotVec(values_items,bs))
		bs=bin(int(bs,2)+1)[2::].zfill(number_items)
	return ans

if __name__ == "__main__":
    t0=timeit('mochila(50, 3, [10, 20, 30], [60, 100, 120])', 'from __main__ import mochila', number=1)
    print('t0:',t0)

    all_files = sorted([f for f in listdir('./instancias') if isfile(join('./instancias', f))])

    # print(all_files)

    all_instaces = {}

    # with open('./instancias/s000.kp') as instance:
    #     for line in instance:
    #         if line != '\n': lines.append(line.split())

lines = []
i = -1
for file in all_files:
    i +=1
    with open('./instancias/'+file) as instance:
        for line in instance:
            if line != '\n': lines.append(line.split())
    print(file)
    all_instaces[file] = lines
    lines = []
    # print(lines)

print(all_instaces.keys())

print(all_instaces['s000.kp'])
print(all_instaces['s002.kp'])