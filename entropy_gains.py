
import utils
import model
import world

def theory_entropy_gain(action, data=None):
	expval=0
	for d in world.possible_data(action):
		alldata=[d] if data is None else [d]+data
		print utils.H(lambda t: model.p_theory_data(t, alldata), model.t_space)
		print model.p_data_action(d,action,data)
		expval+=utils.H(lambda t: model.p_theory_data(t, alldata), model.t_space)*\
				model.p_data_action(d,action,data)
	print action, data, expval
	print [t.kind for t in model.t_space]
	return expval


def joint_entropy_gain(action, data=None):
	expval=0
	for d in world.possible_data(action):
		alldata=[d] if data is None else [d]+data
		expval+=utils.H(lambda (t,hs): model.p_theoryhypothesis_data(t,hs,alldata),\
					model.th_space)*model.p_data_action(d,action,data)
	return expval

