

import matplotlib.pyplot as plt
import numpy as np


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
	filename='full-kids-'+str(n)+'_tru-1'+'_treal-5'+'_rreal.txt'
	fulldata=np.loadtxt(data_directory+filename)
	plt.hist(fulldata[:,1]-fulldata[:,0])
	plt.hist(fulldata[:,2]-fulldata[:,0])
	plt.show()

def plot_sequential(n):	
	for i in range(1,n+1):
		filename='full-kids-'+str(i)+'_tru-1'+'_treal-5'+'_rreal.txt'
		fulldata=np.loadtxt(data_directory+filename)
		plt.subplot(2,2,i)
		plt.hist(fulldata[:,1]-fulldata[:,0],bins=6)
		plt.hist(fulldata[:,2]-fulldata[:,0],bins=6)
	plt.show()



def main():
	#plot_entropy()
	#plot_sequential(4)
	plot_truncated_eig(1)

if __name__ == '__main__':
	main()
