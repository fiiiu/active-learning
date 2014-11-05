
import itertools
import world
import scipy.misc
import Datapoint





class Theory():

	def __init__(self, kind):
		self.kind=kind
		self.machines=world.machines
		self.hf=HypothesisFactory()

	def unnormalized_posterior(self, data=None):
		if data is None:
			return self.prior()
		else:
			return self.data_likelihood(data)*self.prior()

	def data_likelihood(self, data=None):
		#hf=HypothesisFactory.HypothesisFactory()
		lik=1
		for machine in self.machines:
			hyp_lik=0
			allhyp=self.hf.create_all_hypotheses(machine)
			for hyp in allhyp:
				hyp_lik+=hyp.likelihood(data)*self.hypothesis_likelihood(hyp)
			lik*=hyp_lik

		return lik


	def prior(self):
		return 1.0/n_theories

	def hypothesis_likelihood(self, hypothesis):
		
		if self.kind==0:
			return float(hypothesis.kind==0)
		
		elif self.kind==1:
			return float(hypothesis.kind==1)

		elif self.kind==2: #color match
			if hypothesis.kind==2 and hypothesis.color==hypothesis.machine[0]:
				return 1.
			else:
				return 0
		
		elif self.kind==3: #shape match
			if hypothesis.kind==3 and hypothesis.shape==hypothesis.machine[1]:
				return 1.
			else:
				return 0

		elif self.kind==4: #color AND shape match
			if hypothesis.kind==4 and hypothesis.color==hypothesis.machine[0]\
				and hypothesis.shape==hypothesis.machine[1]:
				return 1.
			else:
				return 0

		elif self.kind==5: #color OR shape match
			if hypothesis.kind==5 and (hypothesis.color==hypothesis.machine[0]\
				and hypothesis.shape==hypothesis.machine[1]): #check this and. only 1 gets support.
				return 1.
			else:
				return 0

		elif self.kind==6: #specific color (ANY color)
			if hypothesis.kind==2: 
				return 1./world.n_colors
			else:
				return 0

		elif self.kind==7: #specific shape (ANY shape)
			if hypothesis.kind==3:
				return 1./world.n_shapes
			else:
				return 0

		elif self.kind==8: #specific shape AND color (ANY)
			if hypothesis.kind==4:
				return 1./world.n_colors/world.n_shapes
			else:
				return 0

		elif self.kind==9: #NOT match color
			if hypothesis.kind==2 and hypothesis.color!=hypothesis.machine[0]:
				return 1./(world.n_colors-1)
			else:
				return 0
		
		elif self.kind==10: #NOT match shape
			if hypothesis.kind==3 and hypothesis.shape!=hypothesis.machine[1]:
				return 1./(world.n_shapes-1)
			else:
				return 0

		elif self.kind==11: #INDEPENDENT
			return 1./self.hf.n_hypotheses(hypothesis.machine)

		#CHECK CHECK CHECK THIS SALADDD



class Hypothesis():

	def __init__(self, machine, kind, color=None, color2=None, shape=None, shape2=None):
		self.n_colors=world.n_colors
		self.n_shapes=world.n_shapes
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
		if self.kind==2: #color fixed
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
	
	#I shouldn't be calling this!! :)		
	# def unnormalized_posterior(self, data=None):
	# 	if data is None:
	# 		return self.prior()
	# 	else:
	# 		return self.likelihood(data)*self.prior()


	def single_likelihood(self, datapoint):
		if self.is_consistent(datapoint):
			return 1
		else:
			return epsilon

	def is_consistent(self, datapoint):
		if self.machine != datapoint.machine:
			return True
		else:
			if self.kind==0:
				return not datapoint.active
			elif self.kind==1:
				return datapoint.active
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
					



class HypothesisFactory():

	def __init__(self):
		pass

	def create_all_hypotheses(self, machine):
		all_hypotheses=[]
		
		all_hypotheses.append(Hypothesis(machine, 0))
		
		all_hypotheses.append(Hypothesis(machine, 1))
		
		for color in world.colors:
			all_hypotheses.append(Hypothesis(machine, 2, color=color))
		
		for shape in world.shapes:
			all_hypotheses.append(Hypothesis(machine, 3, shape=shape))
		
		for color in world.colors:
			for shape in world.shapes:
				all_hypotheses.append(Hypothesis(machine, 4, color=color,\
				 shape=shape))

		for color in world.colors:
			for shape in world.shapes:
				all_hypotheses.append(Hypothesis(machine, 5, color=color,\
				 shape=shape))

		for color, color2 in itertools.combinations(world.colors,2):
			all_hypotheses.append(Hypothesis(machine, 6, color=color,\
			 color2=color2)) 

		for shape, shape2 in itertools.combinations(world.shapes,2):
			all_hypotheses.append(Hypothesis(machine, 7, shape=shape,\
				 shape2=shape2))

		return all_hypotheses


	def n_hypotheses(self, machine):
		return len(self.create_all_hypotheses(machine))





n_theories=12
epsilon=1e-3

t_space=[Theory(t) for t in range(n_theories)]
hf=HypothesisFactory()

pre_all_hypotheses=[hf.create_all_hypotheses(machine) for machine in world.machines]
all_hypotheses=list(itertools.product(*pre_all_hypotheses))

th_space=[(t, h) for t in t_space for h in all_hypotheses]



def p_theory_data(theory, data=None, normalized=False):
	#theory=Theory(t)
	if normalized:
		norm=sum([tt.unnormalized_posterior(data) for tt in t_space])
		return theory.unnormalized_posterior(data)/norm
	else:
		return theory.unnormalized_posterior(data)

def p_data_theory(d, t):
	theory=Theory(t)
	return theory.data_likelihood(d)


def p_data_action(datapoint, action, prev_data=None):
	if datapoint in world.possible_data(action):
		pda=0
		machine=action[1]
		for t in t_space:
			for h in hf.create_all_hypotheses(machine):
				pda+=h.single_likelihood(datapoint)*\
					 t.hypothesis_likelihood(h)*t.prior()
						#h.unnormalized_posterior(prev_data)
		return pda
	else:
		return 0

def p_theoryhypothesis_data(theory, hypotheses, data):
	prob=1
	for h in hypotheses:
		prob*=h.likelihood(data)*theory.hypothesis_likelihood(h)
	prob*=theory.prior()
	return prob


