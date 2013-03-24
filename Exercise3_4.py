'''
Created on Mar 16, 2013

@author: jason
'''

import Exercise3_3
import math
import copy

def partition(list, left, right, pivotIndex):
    pivotValue = list[pivotIndex]
    list[pivotIndex], list[right] = list[right], list[pivotIndex]
    storeIndex = left
    for i in range (left, right-1):
        if list[i] < pivotValue:
            list[storeIndex], list[i] = list[i], list[storeIndex]
            storeIndex += 1
    list[right], list[storeIndex] = list[storeIndex], list[right]
    return storeIndex

def select(list, left, right, k):
    if left == right:
        return list[left]
    pivotIndex = int(math.floor(len(list) / 2))
    pivotNewIndex = partition(list, left, right, pivotIndex)
    pivotDist = pivotNewIndex - left + 1
    if pivotDist == k:
        return list[pivotNewIndex]
    elif k < pivotDist:
        return select(list, left, pivotNewIndex - 1, k)
    else:
        return select(list, pivotNewIndex + 1, right, k - pivotDist)

def Selection(scores, rank):
    p_biggest_index = math.ceil(len(scores) * (rank / 100))
    return select(scores, 0, len(scores) - 1, p_biggest_index)

def percentile_selection(scores, p_rank):
    """Calculates the value that is the border to p_rank.
    
    Uses a selection algorithm to improve performance.
    Sorts until the pivot is the index of p_rank(len(scores))"""
    def partition(list, left, right, pivot_index):
        def swap_values(list, idx_1, idx_2):
            val_1 = list[idx_1]
            list[idx_1] = list[idx_2]
            list[idx_2] = val_1
        pivot_value = list[pivot_index]
        list[pivot_index] = list[right]
        list[right] = pivot_value
        store_index = left
        for i in range(left, right):
            if list[i] <= pivot_value:
                val_i = list[i]
                list[i] = list[store_index]
                list[store_index] = val_i
                store_index += 1
        right_val = list[right]
        list[right] = list[store_index]
        list[store_index] = right_val
        return store_index
    def select(list, left, right, idx):
        if left == right:
            return list[left]
        random_pivot = int(math.floor(length / 2))
        new_index = partition(scores, left, right, random_pivot)
        dist = new_index - left + 1
        if dist == p_biggest_index:
            return list[new_index]
        elif dist < p_biggest_index:
            return select(scores, new_index + 1, right, idx)
        else:
            return select(scores, left, new_index - 1, idx)
    length = len(scores)
    p_biggest_index = int(math.ceil(length * (p_rank / 100)))
    return select(scores, 0, length - 1, p_biggest_index)

if __name__ == '__main__':
    scores = [66, 33, 88, 44, 22]
    
    for x in range(0, 100, 11) :
        rank = Exercise3_3.PercentileRank(scores, x)
        print x, rank, Exercise3_3.Percentile(scores, rank), Exercise3_3.PercentileIndex(scores, rank), Exercise3_3.Percentile1(scores, rank), Exercise3_3.Percentile2(scores, rank), percentile_selection(scores, rank)
        
