
import HypothesisFactory
import parameters


class Theory():

	def __init__(self, kind):
		self.kind=kind
		self.n_theories=parameters.n_theories
		self.machines=parameters.machines
		#self.initialize()

	#def initialize(self):
	#	if self.kind==0: #none

	def unnormalized_posterior(self, data=None):
		if data is None:
			return self.prior()
		else:
			return self.data_likelihood(data)*self.prior()

	def data_likelihood(self, data=None):
		hf=HypothesisFactory.HypothesisFactory()
		lik=1
		for machine in self.machines:
			hyp_lik=0
			allhyp=hf.create_all_hypotheses(machine)
			for hyp in allhyp:
				hyp_lik+=hyp.likelihood(data)*self.hypothesis_likelihood(hyp)
			lik*=hyp_lik

		return lik


	def prior(self):
		return 1.0/self.n_theories

	def hypothesis_likelihood(self, hypothesis):
		
		if self.kind==0:
			return int(hypothesis.kind==0)
		
		elif self.kind==1:
			return int(hypothesis.kind==1)

		elif self.kind==2: #color match
			if hypothesis.kind==2 and hypothesis.color==hypothesis.machine[0]:
				return 1
			else:
				return 0
		
		elif self.kind==3: #shape match
			if hypothesis.kind==3 and hypothesis.shape==hypothesis.machine[1]:
				return 1
			else:
				return 0

		#CASES MISSING






