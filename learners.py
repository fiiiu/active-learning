
import random
import utils
import model
import world
import entropy_gains


class ActiveLearner(object):
	"""docstring for ActiveLearner"""
	def __init__(self):
		pass
		
	def choose_action(self, prev_data=None):
		mingain=1000
		astars=[]
		for a in world.possible_actions():
			this_gain=self.entropy_gain(a, prev_data)
			#print a, this_gain
			if this_gain <= mingain:
				astars.append(a)
				mingain=this_gain
		return random.choice(astars)



class RandomLearner(ActiveLearner):
	"""docstring for RandomLearner"""
	def __init__(self):
		super(RandomLearner, self).__init__()
		#self.model = Model.Model()
		
	def choose_action(self, prev_data=None):
		return random.choice(world.possible_actions())
		


class TheoryLearner(ActiveLearner):
	"""docstring for TheoryLearner"""
	def __init__(self):
		super(TheoryLearner, self).__init__()
		#self.model = Model.Model()
	
	def entropy_gain(self, action, data=None):
		#print entropy_gains.theory_entropy_gain(action, data)
		return entropy_gains.theory_entropy_gain(action, data)
	


class JointLearner(ActiveLearner):
	"""docstring for JointLearner"""
	def __init__(self):
		super(JointLearner, self).__init__()
		#self.model = Model.Model()
		
	def entropy_gain(self, action, data=None):
		return entropy_gains.joint_entropy_gain(action, data)


	