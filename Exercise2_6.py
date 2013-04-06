'''
Created on Mar 10, 2013

@author: jason
'''

import descriptive
from collections import namedtuple

def ProbEarly(pmf):
    return ProbBin(pmf, lambda x,y: x<=y, 37)

def ProbLate(pmf):
    return ProbBin(pmf, lambda x,y: x>=y, 41)

def ProbOnTime(pmf):
    return ProbBin(pmf, lambda x,y: x==y, 38, 39, 40)

def ProbBin(pmf, criteria, *val):
    prob_bin = 0
    for value, prob in pmf.Items():
        for _ in val:
            if criteria(value, _):
                prob_bin += prob
    return prob_bin

def CalculateProbs(pmf):
    Probs = namedtuple('Probs', ['early', 'ontime', 'late'])
    probs = Probs(ProbEarly(pmf), ProbOnTime(pmf), ProbLate(pmf))
    return probs

def RelativeRisk(x, y):
    return x / y;

def CalculateRelativeRisks(firsts, others):
    Risks = namedtuple('Risks', ['early', 'ontime', 'late'])
    risks = Risks(RelativeRisk(firsts.early, others.early), RelativeRisk(firsts.ontime, others.ontime),
                  RelativeRisk(firsts.late, others.late))
    return risks

def main(name, data_dir=''):
    pool, firsts, others = descriptive.MakeTables(data_dir)
    
    first_probs = CalculateProbs(firsts.pmf)
    other_probs = CalculateProbs(others.pmf)
    print "First", first_probs
    print "Other", other_probs
    risks = CalculateRelativeRisks(first_probs, other_probs)
    print "Risks", risks

if __name__ == '__main__':
    import sys
    main(*sys.argv)