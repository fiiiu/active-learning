
import random
import utils
import world
import entropy_gains
import low_model as model


class ActiveLearner(object):
	"""docstring for ActiveLearner"""
	def __init__(self):
		self.experience=[]
		
	def choose_action(self, prev_data=[]):#None):
		mingain=1000
		astars=[]
		for a in world.possible_actions():
			if len(prev_data)>0:
				if a==prev_data[-1].action:
					continue
			this_gain=self.expected_final_entropy(a, prev_data)
			if this_gain < mingain:
				astars=[a]
				mingain=this_gain
			elif this_gain == mingain:
				astars.append(a)
		#while True:
		#	print astars, prev_data[-1].action
		choice=random.choice(astars)
		#	if len(prev_data)==0:
		#		break
		#	elif choice!=prev_data[-1].action:
		#		break
		#self.experience.append(world.make_action(choice))
		return choice


	def choose_action_phase2(self, stage, prev_data):
		maxratio=0
		astars=[]

		selector={'a': world.possible_actions_phase2a, 'b': world.possible_actions_phase2b}
		possible_actions=selector[stage]()

		for a in possible_actions:
			dt=world.make_forced_action(a,True)
			df=world.make_forced_action(a,False)
			pt=model.p_data_action(dt,a,prev_data)
			pf=model.p_data_action(df,a,prev_data)
			print a, pt, pf, pt/pf
			this_ratio=pt/pf
			if this_ratio > maxratio:
				astars=[a]
				maxratio=this_ratio
			elif this_ratio == maxratio:
				astars.append(a)

		#print astars
		choice=random.choice(astars)
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


class ActivePlayer():

	#def __init__(self):
		#self.experience=[]

	def choose_action(self, prev_data=[]):
		#mingain=1000
		maxprob=0
		astars=[]
		for a in world.possible_actions():
			if len(prev_data)>0:
				if a==prev_data[-1].action:
					continue
			#this_gain=self.expected_final_entropy(a, prev_data)
			this_prob=self.success_probability(a, prev_data)
			if this_prob > maxprob:
				astars=[a]
				maxprob=this_prob
				#mingain=this_gain
			#elif this_gain == mingain:
			elif this_prob == maxprob:
				astars.append(a)
		choice=random.choice(astars)
		#self.experience.append(world.make_action(choice))
		return choice


	def success_probability(self, action, prev_data=[]):

		data_no, data_yes=world.possible_data(action)
		p_yes=model.p_data_action(data_yes, action, prev_data)
		p_no=model.p_data_action(data_no, action, prev_data)
		
		return p_yes/(p_yes+p_no)


