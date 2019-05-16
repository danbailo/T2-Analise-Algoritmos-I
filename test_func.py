from timeit import timeit
from time import time

def timeFunction(f,*args):
	start=time()
	ans=f(*args)
	return (time()-start)

def knapSack(number_items, weight_max, values_items, weight_items): 
    K = [[0 for x in range(weight_max + 1)] for x in range(number_items + 1)]

    for i in range(number_items + 1): 
        for w in range(weight_max + 1): 
            if i == 0 or w == 0: 
                K[i][w] = 0
            elif weight_items[i-1] <= w: 
                K[i][w] = max(values_items[i-1] + K[i-1][w-weight_items[i-1]],  K[i-1][w]) 
            else: 
                K[i][w] = K[i-1][w] 
    return K[number_items][weight_max]

if __name__ == "__main__":
    t0=timeit("knapSack(50, 14778, [845, 758, 421, 259, 512, 405, 784, 304, 477, 584, 909, 505, 282, 756, 619, 251, 910, 983, 811, 903, 311, 730, 899, 684, 473, 101, 435, 611, 914, 967, 478, 866, 261, 806, 549, 15, 720, 399, 825, 669, 2, 494, 868, 244, 326, 871, 192, 568, 239, 968], [804, 448, 81, 321, 508, 933, 110, 552, 707, 548, 815, 541, 964, 604, 588, 445, 597, 385, 576, 291, 190, 187, 613, 657, 477, 90, 758, 877, 924, 843, 899, 924, 541, 392, 706, 276, 812, 850, 896, 590, 950, 580, 451, 661, 997, 917, 794, 83, 613, 487])", "from __main__ import knapSack", number=1)
    print('t0:',t0)
    print(knapSack(50, 14778, [845, 758, 421, 259, 512, 405, 784, 304, 477, 584, 909, 505, 282, 756, 619, 251, 910, 983, 811, 903, 311, 730, 899, 684, 473, 101, 435, 611, 914, 967, 478, 866, 261, 806, 549, 15, 720, 399, 825, 669, 2, 494, 868, 244, 326, 871, 192, 568, 239, 968], [804, 448, 81, 321, 508, 933, 110, 552, 707, 548, 815, 541, 964, 604, 588, 445, 597, 385, 576, 291, 190, 187, 613, 657, 477, 90, 758, 877, 924, 843, 899, 924, 541, 392, 706, 276, 812, 850, 896, 590, 950, 580, 451, 661, 997, 917, 794, 83, 613, 487]))

    # t = time.process_time()
    # print(knapSack(50, 14778, [845, 758, 421, 259, 512, 405, 784, 304, 477, 584, 909, 505, 282, 756, 619, 251, 910, 983, 811, 903, 311, 730, 899, 684, 473, 101, 435, 611, 914, 967, 478, 866, 261, 806, 549, 15, 720, 399, 825, 669, 2, 494, 868, 244, 326, 871, 192, 568, 239, 968], [804, 448, 81, 321, 508, 933, 110, 552, 707, 548, 815, 541, 964, 604, 588, 445, 597, 385, 576, 291, 190, 187, 613, 657, 477, 90, 758, 877, 924, 843, 899, 924, 541, 392, 706, 276, 812, 850, 896, 590, 950, 580, 451, 661, 997, 917, 794, 83, 613, 487]))
    # elapsed_time = time.process_time() - t
    # print(elapsed_time)

    start=time()
    knapSack(50, 14778, [845, 758, 421, 259, 512, 405, 784, 304, 477, 584, 909, 505, 282, 756, 619, 251, 910, 983, 811, 903, 311, 730, 899, 684, 473, 101, 435, 611, 914, 967, 478, 866, 261, 806, 549, 15, 720, 399, 825, 669, 2, 494, 868, 244, 326, 871, 192, 568, 239, 968], [804, 448, 81, 321, 508, 933, 110, 552, 707, 548, 815, 541, 964, 604, 588, 445, 597, 385, 576, 291, 190, 187, 613, 657, 477, 90, 758, 877, 924, 843, 899, 924, 541, 392, 706, 276, 812, 850, 896, 590, 950, 580, 451, 661, 997, 917, 794, 83, 613, 487])
    print(time()-start)