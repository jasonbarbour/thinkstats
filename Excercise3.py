'''
Created on Mar 7, 2013

@author: jason
'''
import Pmf

def Mode(hist):
    """Exercise 3   The mode of a distribution is the most 
    frequent value (see http://wikipedia.org/wiki/Mode_(statistics)). 
    Write a function called Mode that takes a Hist object and returns 
    the most frequent value. As a more challenging version, write a 
    function called AllModes that takes a Hist object and returns a 
    list of value-frequency pairs in descending order of frequency. 
    Hint: the operator module provides a function called itemgetter 
    which you can pass as a key to sorted."""
    return max(hist.Items(), key=lambda x: x[1])[1]

def AllModes(hist):
    return sorted(hist.Items(), key=lambda x: x[1], reverse=True)
    
if __name__ == '__main__':
    hist = Pmf.MakeHistFromList([3, 3, 1, 2, 2, 3, 4, 3, 5, 3])
    print Mode(hist)
    print AllModes(hist)
