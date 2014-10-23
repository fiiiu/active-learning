
import numpy as np
import matplotlib.pyplot as plt


#test data. one kid sees objects interact with blicket detector
testdata=[(1,0),(0,0),(2,0),(5,1)]
N=6
epsilon=1e-1

#hypothesis space: all 2^N combinations.
#data: pair (index, result)

#prior
def prior(h):
	return 1./(2**N)


#likelihood function
def likelihood(d,h):
	prob=1
	for di in d:
		prob*=single_likelihood(di,h)#int(is_consistent(di,h))

	return prob


def single_likelihood(d,h):
	binaryh=bin(h)[2:].zfill(N)
	if(d[1]==int(binaryh[d[0]])):
		return 1
	else:
		return epsilon


# #hypothesis enumeration

# def is_consistent(d,h):
# 	binaryh=bin(h)[2:].zfill(N)
# 	return d[1]==int(binaryh[d[0]])


def posterior(h,d):
	return likelihood(d,h)*prior(h)
	

def main():
	#test likelihood
	#print likelihood((3,1),9)

	#test posterior
	#print posterior(0,testdata[0])

	posthist=np.empty(2**N)
	for i in range(2**N):
		posthist[i]=posterior(i,testdata)

	plt.plot(range(2**N), posthist)
	plt.show()


if __name__ == '__main__':
 	main() 
