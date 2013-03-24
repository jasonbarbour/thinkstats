'''
Created on Mar 22, 2013

@author: jason
'''
import descriptive
import Cdf
import myplot

def main(data_dir='.'):
    pool, firsts, others = descriptive.MakeTables(data_dir)
    firsts.weights = [p.birthwgt_lb for p in firsts.records if p.birthwgt_lb in range(0,20)]
    others.weights = [p.birthwgt_lb for p in others.records if p.birthwgt_lb in range(0,20)]
    
    first_weights = Cdf.MakeCdfFromList(firsts.weights, "first")
    other_weights = Cdf.MakeCdfFromList(others.weights, "other")
    
    print first_weights.Prob(5)
    print first_weights.Percentile(15)
    print other_weights.Prob(5)
    print other_weights.Percentile(15)
    
    myplot.Cdf(first_weights)
    myplot.Cdf(other_weights)
    myplot.Show()

    
if __name__ == '__main__':
    main()