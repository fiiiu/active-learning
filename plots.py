

import matplotlib.pyplot as plt
import numpy as np
import scipy.stats


output_directory='/Users/alejo/Neuro/ActiveLearning/Output/'
today='141118/'
#batch='ep-0.05/'
data_directory=output_directory+today#+batch
	


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

def plot_sequential(model, n, scatter=False):	
	for i in range(1,n+1):
		#filename=model+'-'+str(i)+'_tru-1'+'_treal-20'+'_rreal.txt'
		filename=model+'-'+str(i)+'_tru-20'+'_rreal.txt'
		#fulldata=np.loadtxt(data_directory+today+filename)
		fulldata=np.loadtxt(data_directory+filename)
		#print data_directory+filename
		plt.subplot(np.ceil(float(n+1))/2,2,i, title='N actions: {0}'.format(i))
		#plt.suptitle('{0}'.format(i))
		if scatter:
			#plt.ylim([0,0.5])
			#plt.xlim([0,0.25])
			#plt.hist((fulldata[:,2]-fulldata[:,0])-(fulldata[:,1]-fulldata[:,0]))
			plt.plot((fulldata[:,1]-fulldata[:,0]),(fulldata[:,2]-fulldata[:,0]), 'o')
			m1=plt.xlim()[1]
			m2=plt.ylim()[1]
			mm=max(m1,m2)
			#print plt.xlim(), plt.ylim()
			plt.plot(np.linspace(0,mm,2),np.linspace(0,mm,2), 'k-')
			stats=scipy.stats.ttest_rel((fulldata[:,1]-fulldata[:,0]), (fulldata[:,2]-fulldata[:,0]))
			plt.xlim([0, m1])
			plt.ylim([0, m2])

			if i==1:
				print "{0} action, t: {1:.3f}, p: {2:.3f}".format(i, stats[0], stats[1])
			else:
				print "{0} actions, t: {1:.3f}, p: {2:.3f}".format(i, stats[0], stats[1])
		else:			
			#plt.ylim([0, 43])
			#plt.xlim([0,0.5])
			bins=plt.hist(fulldata[:,1]-fulldata[:,0],color='blue')
			print bins[2]
			maxcount=max(bins[0])
			bins2=plt.hist(fulldata[:,2]-fulldata[:,0],bottom=maxcount+2,color='red')
			maxcount2=max(bins2[0])
			plt.ylim([0, maxcount+maxcount2+4])



	plt.show()


def plot_epsilons(model, kind='hist'):
	epsilons=[0.001, 0.005, 0.01, 0.05, 0.1, 0.25]
	epsilons=[0.002, 0.003, 0.004, 0.007, 0.008, 0.009]
	epsilons=[0.001, 0.002, 0.003, 0.004, 0.005, 0.006, 0.007, 0.008, 0.009]
	tru=2

	for i,epsilon in enumerate(epsilons):
		filename=model+'-'+str(tru)+'_tru-20'+'_rreal-'+str(epsilon)+'.txt'
		#fulldata=np.loadtxt(data_directory+today+filename)
		fulldata=np.loadtxt(data_directory+filename)
		print data_directory+filename
		a,b=np.ceil(float(len(epsilons)+1))/2,2
		a,b=np.ceil(float(len(epsilons)+1))/3,3
		plt.subplot(a,b,i+1, title='epsilon={0}'.format(epsilon))
		
		if kind=='hist':
			bins=plt.hist(fulldata[:,1]-fulldata[:,0],color='blue')
			print bins[2]
			maxcount=max(bins[0])
			bins2=plt.hist(fulldata[:,2]-fulldata[:,0],bottom=maxcount+2,color='red')
			maxcount2=max(bins2[0])
			plt.ylim([0, maxcount+maxcount2+4])

		elif kind=='scatter':
			plt.plot((fulldata[:,1]-fulldata[:,0]),(fulldata[:,2]-fulldata[:,0]), 'o')
			m1=plt.xlim()[1]
			m2=plt.ylim()[1]
			mm=max(m1,m2)
			#print plt.xlim(), plt.ylim()
			plt.plot(np.linspace(0,mm,2),np.linspace(0,mm,2), 'k-')
			stats=scipy.stats.ttest_rel((fulldata[:,1]-fulldata[:,0]), (fulldata[:,2]-fulldata[:,0]))
			plt.xlim([0, m1])
			plt.ylim([0, m2])
			
			print "epsilon: {0}, t: {1:.3f}, p: {2:.3f}".format(epsilon, stats[0], stats[1])

	plt.show()


def main():
	#plot_entropy()
	#model='hypfull'
	model='jointfull'
	#model='theoryfull'
	

	plot_sequential(model,4,True)
	#plot_sequential(model,4,False)
	#plot_truncated_eig(1)

	#model='theory'
	#plot_epsilons(model, 'hist')
	#plot_epsilons(model, 'scatter')

if __name__ == '__main__':
	main()
