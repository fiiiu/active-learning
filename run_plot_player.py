

import matplotlib.pyplot as plt
import numpy as np
import scipy.stats
import parameters
import seaborn as sns

data_directory=parameters.output_directory    



def plot_sequential(n, plot_type='hist', stats=True):   
    plt.figure(figsize=(12,8))
    for i in range(1,n+1):
        filename='player-'+str(i)+'_tru-20'+'_rreal.txt'
        fulldata=np.loadtxt(data_directory+filename)
        print data_directory+filename

        kids=-np.log(fulldata[:,2]/fulldata[:,0])
        random=-np.log(fulldata[:,1]/fulldata[:,0])

        plt.subplot(np.ceil(float(n+1))/2,2,i, title='N actions: {0}'.format(i))
        if plot_type=='scatter':
            plt.plot(random, kids, 'o')
            m1=plt.xlim()[1]
            m2=plt.ylim()[1]
            mm=max(m1,m2)
            plt.plot(np.linspace(0,mm,2),np.linspace(0,mm,2), 'k-')
            plt.xlim([0, m1])
            plt.ylim([0, m2])

            
        elif plot_type=='hist':           
            bins=plt.hist(random, color='blue')
            print bins[2]
            maxcount=max(bins[0])
            bins2=plt.hist(kids, bottom=maxcount+2, color='red')
            maxcount2=max(bins2[0])
            plt.ylim([0, maxcount+maxcount2+4])

        if stats:
            #sts=scipy.stats.ttest_rel((fulldata[:,1]-fulldata[:,0]), (fulldata[:,2]-fulldata[:,0]))
            sts=scipy.stats.ttest_rel(random, kids)
            
            #print '{0:.3f} & {1:.3f}'.format(sts[0],sts[1])
            print '{0} & {1}'.format(sts[0],sts[1])


    plt.show()


if __name__=='__main__':
    plot_sequential(4, 'scatter')

