# n // número de itens
# W // capacidade da mochila

# v_1 p_1 //valor e peso do item 1
# v_2 p_2 //valor e peso do item 2
# …       //valor e peso do item i
# v_n p_n //valor e peso do item n

from timeit import timeit

pesos = [10, 20, 30] 
valores = [60, 100, 120]
def mochila(w,n):
	n=len(pesos)
	dotVec=lambda x,bs:sum((x[i]for i in range(len(x)) if bs[i]=="1"))
	bs="".zfill(n)
	ans=0
	while "0" in bs:
		if dotVec(pesos,bs)<=w:
			ans=max(ans,dotVec(valores,bs))
		bs=bin(int(bs,2)+1)[2::].zfill(n)
		# print(bs)
	return ans

def knapSack(W, wt, val, n): 
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]

    for i in range(n + 1): 
        for w in range(W + 1): 
            if i == 0 or w == 0: 
                K[i][w] = 0
            elif wt[i-1] <= w: 
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w]) 
            else: 
                K[i][w] = K[i-1][w] 
    return K[n][W] 

def knapSack_brute(W, wt, val, n): 

    if n == 0 or W == 0 : 
        return 0

    if (wt[n-1] > W): 
        return knapSack(W, wt, val, n-1) 
    else: 
        return max(val[n-1] + knapSack(W-wt[n-1], wt, val, n-1), knapSack(W, wt, val, n-1)) 

if __name__ == "__main__":
    # Driver program to test above function     
    # val = [60, 100, 120] 
    # wt = [10, 20, 30] 
    # W = 50
    # n = len(val) 
    # print(knapSack(W, wt, val, n)) 
    # print(mochila(W,n))

    t0=timeit('knapSack(50, [10, 20, 30], [60, 100, 120], 3)', 'from __main__ import knapSack', number=1)
    t1=timeit('knapSack_brute(50, [10, 20, 30], [60, 100, 120], 3)', 'from __main__ import knapSack_brute', number=1)
    t2=timeit('mochila(50,3)', 'from __main__ import mochila', number=1)

    print('t0:',t0)
    print('t1:',t1)
    print('t2:',t2)