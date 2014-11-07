

import matplotlib.pyplot as plt
import numpy as np
import scipy.stats

data_directory='/Users/alejo/Neuro/ActiveLearning/Output/'



def plot_entropy():
	filename_theory='out-HIGH-theory-10_tru-1_real.txt'
	filename_random='out-HIGH-random-10_tru-5_real.txt'

	filename_theory='out-theory-10_tru-10_real.txt'
	filename_random='out-random-10_tru-60_real.txt'
	filename_kids='out-kids-10_tru-1_real.txt'

	theory_data=np.loadtxt(data_directory+filename_theory)
	random_data=np.loadtxt(data_directory+filename_random)
	kids_data=np.loadtxt(data_directory+filename_kids)



	plt.hist(theory_data)
	plt.hist(kids_data)
	plt.hist(random_data)
	
	plt.show()


def plot_variance():
	filename_theory='all-HIGH-theory-10_tru-1_real.txt'
	filename_random='all-HIGH-random-10_tru-5_real.txt'

	all_theory_data=np.loadtxt(data_directory+filename_theory)
	all_random_data=np.loadtxt(data_directory+filename_random)
	

def plot_truncated_eig(n):
	filename='full-kids-'+str(n)+'_tru-1'+'_treal-20'+'_rreal.txt'
	fulldata=np.loadtxt(data_directory+filename)
	#plt.hist(fulldata[:,1]-fulldata[:,0],color='blue')
	#plt.hist(fulldata[:,2]-fulldata[:,0],bottom=15, color='red')

	#plt.ylim([0, 43])
	#plt.xlim([0,0.5])
	bins=plt.hist(fulldata[:,1]-fulldata[:,0],color='blue')
	print bins[2]
	maxcount=max(bins[0])
	bins2=plt.hist(fulldata[:,2]-fulldata[:,0],bottom=maxcount+2,color='red')

	plt.show()

def plot_sequential(n, dod=False):	
	for i in range(1,n+1):
		filename='uenfull-kids-'+str(i)+'_tru-1'+'_treal-20'+'_rreal.txt'
		fulldata=np.loadtxt(data_directory+filename)
		plt.subplot(3,2,i, title='N actions: {0}'.format(i))
		#plt.suptitle('{0}'.format(i))
		if dod:
			#plt.ylim([0,0.5])
			#plt.xlim([0,0.25])
			#plt.hist((fulldata[:,2]-fulldata[:,0])-(fulldata[:,1]-fulldata[:,0]))
			plt.plot((fulldata[:,1]-fulldata[:,0]),(fulldata[:,2]-fulldata[:,0]), 'o')
			plt.plot(np.linspace(0,0.25,2),np.linspace(0,0.25,2), 'k-')
			stats=scipy.stats.ttest_rel((fulldata[:,1]-fulldata[:,0]), (fulldata[:,2]-fulldata[:,0]))
			if i==1:
				print "{0} action, t: {1:.3f}, p: {2:.3f}".format(i, stats[0], stats[1])
			else:
				print "{0} actions, t: {1:.3f}, p: {2:.3f}".format(i, stats[0], stats[1])
		else:			
			plt.ylim([0, 43])
			plt.xlim([0,0.5])
			bins=plt.hist(fulldata[:,1]-fulldata[:,0],color='blue')
			print bins[2]
			maxcount=max(bins[0])
			bins2=plt.hist(fulldata[:,2]-fulldata[:,0],bottom=maxcount+2,color='red')
			maxcount2=max(bins2[0])
			plt.ylim([0, maxcount+maxcount2+4])



	plt.show()



def main():
	#plot_entropy()
	plot_sequential(3,True)
	#plot_truncated_eig(1)

if __name__ == '__main__':
	main()
