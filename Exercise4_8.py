'''
Created on Apr 1, 2013

@author: jason
'''
import descriptive
import Cdf
import myplot
import erf
import thinkstats
import math
import matplotlib.pyplot as pyplot

def RenderNormalCdf(mu, sigma, max, n=50):
    """Generates sequences of xs and ps for a normal CDF."""
    xs = [max * i / n for i in range(n)]    
    ps = [erf.NormalCdf(x, mu, sigma) for x in xs]
    return xs, ps

def MakeNormalModel(lengths):
    """Plot the CDF of birthweights with a normal model."""
    
    # estimate parameters: trimming outliers yields a better fit
    mu, var = thinkstats.TrimmedMeanVar(lengths, p=0.01)
    print 'Mean, Var', mu, var
    
    # plot the model
    sigma = math.sqrt(var)
    print 'Sigma', sigma
    xs, ps = RenderNormalCdf(mu, sigma, 200)

    pyplot.clf()
    pyplot.plot(xs, ps, label='model', linewidth=4, color='0.8')

    # plot the data
    cdf = Cdf.MakeCdfFromList(lengths)
    xs, ps = cdf.Render()
    pyplot.plot(xs, ps, label='data', linewidth=2, color='blue')
 
    myplot.Save('nsfg_lengths_model',
                title='Birth lengths',
                xlabel='birth length',
                ylabel='CDF')

if __name__ == '__main__':
    pool, firsts, others = descriptive.MakeTables(".")
    
    MakeNormalModel(pool.lengths)
    