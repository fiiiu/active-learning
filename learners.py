
import random
import utils
import world
import entropy_gains


class ActiveLearner(object):
	"""docstring for ActiveLearner"""
	def __init__(self):
		self.experience=[]
		
	def choose_action(self, prev_data=None):
		mingain=1000
		astars=[]
		for a in world.possible_actions():
			this_gain=self.expected_final_entropy(a, prev_data)
			#print a, this_gain
			if this_gain < mingain:
				#astars.append(a)
				astars=[a]
				mingain=this_gain
			elif this_gain == mingain:
				astars.append(a)
		choice=random.choice(astars)
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
		#self.model = Model.Model()
		
	#def choose_action(self, prev_data=None):
	#	return random.choice(world.possible_actions())
	def expected_final_entropy(self, action, data=None):
		return 0 #all equivalent!


class TheoryLearner(ActiveLearner):
	"""docstring for TheoryLearner"""
	def __init__(self):
		super(TheoryLearner, self).__init__()
		#self.model = Model.Model()
	
	def expected_final_entropy(self, action, data=None):
		#print entropy_gains.theory_entropy_gain(action, data)
		return entropy_gains.theory_expected_final_entropy(action, data)
	


class JointLearner(ActiveLearner):
	"""docstring for JointLearner"""
	def __init__(self):
		super(JointLearner, self).__init__()
		#self.model = Model.Model()
		
	def entropy_gain(self, action, data=None):
		return entropy_gains.joint_entropy_gain(action, data)


	