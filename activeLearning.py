
import numpy as np
import matplotlib.pyplot as plt
import utils

#test data. one kid sees objects interact with blicket detector
testdata=[(1,0),(0,0),(2,0),(5,1)]
N=6
epsilon=1e-3
hspace=range(2**N)
actions=range(N)

#hypothesis space: all 2^N combinations.
#data: pair (index, result)

#prior
def prior(h):
	return 1./len(hspace)


#likelihood function
def likelihood(d,h):
	if type(d) is list:
		prob=1
		for di in d:
			prob*=single_likelihood(di,h)#int(is_consistent(di,h))
		return prob
	else:
		return single_likelihood(d,h)

def single_likelihood(d,h):
	binaryh=bin(h)[2:].zfill(N)
	if(d[1]==int(binaryh[d[0]])):
		return 1-epsilon
	else:
		return epsilon

def p_data_action(d,a,prev_data=None):
	if d in possible_data(a):
		pda=0
		for h in hspace:
			pda+=single_likelihood(d,h)*posterior(h, prev_data)
		return pda
	else:
		return 0


# def posterior(h,d):
# 	if d is not None:
# 		return likelihood(d,h)*prior(h)
# 	else:
# 		return prior(h)
def posterior(h,d=None):
	if d is not None:
		return likelihood(d,h)*prior(h)/sum([likelihood(d,h_)*prior(h_) for h_ in hspace])
	else:
		return prior(h)


def entropy_gain(a, prev_data=None):
	expval=0
	for d in possible_data(a):
		alldata=[d] if prev_data is None else [d]+prev_data
		expval+=utils.H(lambda h: posterior(h, alldata), hspace)*p_data_action(d,a,prev_data)
	return expval

def choose_action(prev_data=None):
	mingain=1000
	astar=-1
	for a in actions:
		this_gain=entropy_gain(a, prev_data)
		#print a, this_gain
		if this_gain < mingain:
			astar=a
			mingain=this_gain

	return astar


def possible_data(a):
	return [(a,0), (a,1)]


def main():
	#test likelihood
	#print likelihood((3,1),9)

	#test posterior
	#print posterior(0,testdata[0])

	# posthist=np.empty(2**N)
	# for i in hspace:
	# 	posthist[i]=posterior(i,testdata)

	# plt.plot(hspace, posthist)
	# plt.show()

	#for res in [0,1]:	
	print p_data_action((0,0),0), p_data_action((0,1),0)
	print p_data_action((0,0),0,(0,0)), p_data_action((0,1),0,(0,0))
	print p_data_action((1,0),1,(0,0)), p_data_action((1,1),1,(0,0))

	#test entropy
	# print utils.H(lambda h: posterior(h,(0,0)), hspace)

	#test evalue
	#print evalue(0)
	#print entropy_gain(0,[(0,0),(1,0)])
	print "H prior: ", utils.H(lambda h: prior(h), hspace)
	print "H posterior: ", utils.H(lambda h: posterior(h,[(0,0)]), hspace)
	print "H posterior: ", utils.H(lambda h: posterior(h,[(0,0),(0,0)]), hspace)
	print "H posterior: ", utils.H(lambda h: posterior(h,[(0,0),(0,1)]), hspace)
	print "H posterior: ", utils.H(lambda h: posterior(h,[(0,0),(1,0)]), hspace)
	print "H posterior: ", utils.H(lambda h: posterior(h,[(0,0),(1,1)]), hspace), "\n"


	print entropy_gain(0), entropy_gain(1), entropy_gain(2)
	print entropy_gain(0,[(0,0)]), entropy_gain(1,[(0,0)]), entropy_gain(2,[(0,0)])

	print "action: ", choose_action([(1,0),(0,1),(3,0)])


if __name__ == '__main__':
 	main() 
