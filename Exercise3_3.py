'''
Created on Mar 16, 2013

@author: jason
'''

import math
import copy

def PercentileRank(scores, your_score):
    count = 0
    for score in scores:
        if score <= your_score:
            count += 1
            
    rank = 100.0 * count / len(scores)
    return rank

def Percentile(scores, rank):
    scores_copy = copy.copy(scores)
    scores_copy.sort()
    for score in scores_copy:
        if PercentileRank(scores_copy, score) >= rank:
             return score

def PercentileIndex(scores, rank):
    scores_copy = copy.copy(scores)
    scores_copy.sort()
    index =  int(rank * (len(scores_copy) - 1) // 100)
    return scores_copy[index]


def Percentile1(scores, percentile_rank):
    """Computes the value that corresponds to a given percentile rank. """
    scores_copy = copy.copy(scores)
    scores_copy.sort()
    for score in scores_copy:
        if PercentileRank(scores_copy, score) >= percentile_rank:
            return score

def Percentile2(scores, percentile_rank):
    """Computes the value that corresponds to a given percentile rank.

    Slightly more efficient.
    """
    scores_copy = copy.copy(scores)
    scores_copy.sort()
    index = int(percentile_rank * (len(scores_copy)-1) / 100)
    return scores_copy[index]
            
if __name__ == '__main__':
    scores = [66, 33, 88, 44, 22]
    
    for x in range(0, 100, 11) :
        rank = PercentileRank(scores, x)
        print x, rank, Percentile(scores, rank), PercentileIndex(scores, rank), Percentile1(scores, rank), Percentile2(scores, rank)
