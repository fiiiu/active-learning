
import random
import utils
import world
import entropy_gains


class ActiveLearner(object):
	"""docstring for ActiveLearner"""
	def __init__(self):
		self.experience=[]
		
	def choose_action(self, prev_data=[]):#None):
		mingain=1000
		astars=[]
		for a in world.possible_actions():
			this_gain=self.expected_final_entropy(a, prev_data)
			if this_gain < mingain:
				astars=[a]
				mingain=this_gain
			elif this_gain == mingain:
				astars.append(a)
		while True:
			choice=random.choice(astars)
			if len(prev_data)==0:
				break
			elif choice!=prev_data[-1].action:
				break
		self.experience.append(world.make_action(choice))
		return choice

	def play(self, n_actions):
		for i in range(n_actions):
			self.choose_action(self.experience)
		return self.experience


class RandomLearner(ActiveLearner):
	"""docstring for RandomLearner"""
	def __init__(self):
		super(RandomLearner, self).__init__()
		
		
	def expected_final_entropy(self, action, data=None):
		return 0 #all equivalent!


class TheoryLearner(ActiveLearner):
	"""docstring for TheoryLearner"""
	def __init__(self):
		super(TheoryLearner, self).__init__()
		
	
	def expected_final_entropy(self, action, data=None):
		#print entropy_gains.theory_entropy_gain(action, data)
		return entropy_gains.theory_expected_final_entropy(action, data)
	


class JointLearner(ActiveLearner):
	"""docstring for JointLearner"""
	def __init__(self):
		super(JointLearner, self).__init__()
		
		
	def expected_final_entropy(self, action, data=None):
		return entropy_gains.joint_expected_final_entropy(action, data)


class HypothesesLearner(ActiveLearner):
	"""docstring for HypothesesLearner"""
	def __init__(self):
		super(HypothesesLearner, self).__init__()
		
		
	def expected_final_entropy(self, action, data=None):
		return entropy_gains.hypotheses_expected_final_entropy(action, data)

	