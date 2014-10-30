
# n=3 #color dimension
# m=2 #shape dimension

# hypothesis structure
#[ shape0 color0, shape0 color1, .. , shape1 color0, .. ]

import scipy.misc
import parameters
import Datapoint

class Hypothesis():

	def __init__(self, machine, kind, color=None, color2=None, shape=None, shape2=None):
		self.n_colors=parameters.n_colors
		self.n_shapes=parameters.n_shapes
		self.hypothesis=[0]*self.n_colors*self.n_shapes
		self.machine=machine
		self.kind=kind
		self.initialize(color, color2, shape, shape2)
		self.n_hypotheses=2+self.n_colors+self.n_shapes+2*self.n_colors*self.n_shapes+\
							int(scipy.misc.comb(self.n_colors,2))+\
							int(scipy.misc.comb(self.n_shapes,2))

	def display(self):
		print self.hypothesis

	def initialize(self, color, color2, shape, shape2):
		if self.kind==0: #none
			pass #return hyp
		elif self.kind==1: #any
			self.hypothesis=[1]*self.n_colors*self.n_shapes
		elif self.kind==2: #color fixed
			self.color=color
			for j in range(self.n_shapes):
				self.hypothesis[j*self.n_colors+color]=1
		elif self.kind==3: #shape fixed
			self.shape=shape
			for i in range(self.n_colors):
				self.hypothesis[self.n_colors*shape+i]=1
		elif self.kind==4: #shape AND color
			self.color=color
			self.shape=shape
			self.hypothesis[self.n_colors*shape+color]=1
		elif self.kind==5: #shape OR color
			self.color=color
			self.shape=shape
			for j in range(self.n_shapes):
				self.hypothesis[j*self.n_colors+color]=1
			for i in range(self.n_colors):
				self.hypothesis[self.n_colors*shape+i]=1
		elif self.kind==6: #color OR color2
			self.color=color
			self.color2=color2
			for j in range(self.n_shapes):
				self.hypothesis[j*self.n_colors+color]=1
				self.hypothesis[j*self.n_colors+color2]=1
		elif self.kind==7: #shape OR shape2
			self.shape=shape
			self.shape2=shape2
			for i in range(self.n_colors):
				self.hypothesis[self.n_colors*shape+i]=1
				self.hypothesis[self.n_colors*shape2+i]=1


	def prior(self, theory=None):
		if theory is None:
			return 1./self.n_hypotheses

	def likelihood(self, data):
		lik=1
		for datapoint in data:
			lik*=self.single_likelihood(datapoint)
		return lik
			
	def unnormalized_posterior(self, data=None):
		if data is None:
			return self.prior()
		else:
			return self.likelihood(data)*self.prior()


	def single_likelihood(self, datapoint):
		if self.is_consistent(datapoint):
			return 1
		else:
			return parameters.epsilon

	def is_consistent(self, datapoint):
		if self.machine != datapoint.machine:
			return True
		else:
			if self.kind==0:
				return False
			elif self.kind==1:
				return True
			elif self.kind==2:
				if (self.color==datapoint.toy_color and datapoint.active) or\
					(self.color!=datapoint.toy_color and not datapoint.active):
					return True
				else:
					return False
			elif self.kind==3:
				if (self.shape==datapoint.toy_shape and datapoint.active) or\
					(self.shape!=datapoint.toy_shape and not datapoint.active):
					return True
				else:
					return False

			elif self.kind==4:
				if (self.shape==datapoint.toy_shape and self.color==datapoint.toy_color\
					 and datapoint.active) or \
				    ((self.shape!=datapoint.toy_shape or self.color!=datapoint.toy_color) \
				     and not datapoint.active):
				    return True
				else:
					return False

			elif self.kind==5:
				if ((self.shape==datapoint.toy_shape or self.color==datapoint.toy_color)\
					and datapoint.active) or \
					((self.shape!=datapoint.toy_shape and self.color!=datapoint.toy_color)\
					and not datapoint.active):
					return True
				else:
					return False

			elif self.kind==6:
				if ((self.color==datapoint.toy_color or self.color2==datapoint.toy_color)\
					and datapoint.active) or\
					((self.color!=datapoint.toy_color and self.color2!=datapoint.toy_color)\
					and not datapoint.active):
					return True
				else:
					return False

			elif self.kind==7:
				if ((self.shape==datapoint.toy_shape or self.shape2==datapoint.toy_shape)\
					and datapoint.active) or\
					((self.shape!=datapoint.toy_shape and self.shape2!=datapoint.toy_shape)\
					and not datapoint.active):
					return True
				else:
					return False
					
		#Done, check cases!!



# def single_likelihood(d,h):
# 	binaryh=bin(h)[2:].zfill(N)
# 	if(d[1]==int(binaryh[d[0]])):
# 		return 1-epsilon
# 	else:
# 		return epsilon

		


# def produce_hypothesis(kind, shape=None, color=None, shape2=None, color2=None):
# 	hyp=[0]*n*m
# 	if kind==0: #none
# 		return hyp
# 	if kind==1: #any
# 		return [1]*n*m
# 	if kind==2: #color fixed
# 		for j in range(m):
# 			hyp[j*n+color]=1
# 		return hyp
# 	if kind==3: #shape fixed
# 		for i in range(n):
# 			hyp[n*shape+i]=1
# 		return hyp
# 	if kind==4: #shape AND color
# 		hyp[n*shape+color]=1
# 		return hyp
# 	if kind==5: #shape OR color
# 		for j in range(m):
# 			hyp[j*n+color]=1
# 		for i in range(n):
# 			hyp[n*shape+i]=1
# 		return hyp
# 	if kind==6: #shape OR shape2
# 		for i in range(n):
# 			hyp[n*shape+i]=1
# 			hyp[n*shape2+i]=1
# 		return hyp
# 	if kind==7: #color OR color2
# 		for j in range(m):
# 			hyp[j*n+color]=1
# 			hyp[j*n+color2]=1
# 		return hyp










