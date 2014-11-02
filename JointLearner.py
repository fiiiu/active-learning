

import utils
import model
import world

class JointLearner():
	"""docstring for ActiveLearner"""
	#def __init__(self):
		#super(ActiveLearner, self).__init__()
		#self.model = Model.Model()
		
	def choose_action(self, prev_data=None):
		mingain=1000
		astar=-1
		for a in world.possible_actions():
			this_gain=self.entropy_gain(a, prev_data)
			#print a, this_gain
			if this_gain < mingain:
				astar=a
				mingain=this_gain
		return astar

	def entropy_gain(self, action, data=None):
		expval=0
		for d in world.possible_data(action):
			alldata=[d] if data is None else [d]+data
			expval+=utils.H(lambda (t,hs): model.p_theoryhypothesis_data(t,hs,alldata),\
						model.th_space)*model.p_data_action(d,action,data)
			#expval+=utils.H(lambda t: model.p_theory_data(t, alldata), model.t_space)*\
			#		model.p_data_action(d,action,data)
		return expval

