
####################################################
##### Implementation of Binary Search Algorithm ####
####################################################

import random
import time


def naive_search (l, target):   # l is the list/array
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1   # in case target element is not in list

def binary_search( l , target, low = None, high = None): # l must be sorted for binary search
    if low == None:
        low = 0
    if high == None:
        high= len(l) - 1

    if high < low:
        return -1

    mid = (low + high) // 2

    if l[mid] == target:
        return mid
    elif l[mid] > target:
        return binary_search(l, target, low, mid - 1)
    else:
        return binary_search(l, target, mid + 1, high)


if __name__ == '__main__':
    
    length = 10000
    sorted_list = set()

    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length, 3*length))

    sorted_list = sorted(list(sorted_list))


    # Naive Search evaluation
    start = time.time()
    for target in sorted_list:
        naive_search(sorted_list, target)
    stop = time.time()
    print('Naive Search time: ', (stop - start)/length, ' seconds')

    # Binary Search evaluation
    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    stop = time.time()
    print('Binary Search time: ', (stop - start)/length, ' seconds')
