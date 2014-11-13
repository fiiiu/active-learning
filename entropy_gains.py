
import utils
#import newmodel as model
import world

import high_model
import low_model

model=low_model


def ave_theory_expected_entropy_gain(sequence):
	ave_entropies=0
	entropies=[]
	for i,datapoint in enumerate(sequence):
		entropy=theory_expected_entropy_gain(datapoint.action, sequence[:i])
		#entropy=theory_expected_final_entropy(datapoint.action, sequence[:i])

		entropies.append(entropy)
		ave_entropies+=entropy
	
	return ave_entropies/len(sequence), entropies


def theory_expected_entropy_gain(action, data=None):
	
	#normalize p_data_action
	#p_theory_data SHOULD BE NORMALIZED.
	norm=0
	for d in world.possible_data(action):
	 	norm+=model.p_data_action(d,action,data)

	expval=0
	for d in world.possible_data(action):
		alldata=[d] if data is None else [d]+data
		#print utils.H(lambda t: model.p_theory_data(t, alldata), model.t_space)
		#print 'p_d_a', model.p_data_action(d,action,data)
		expval+=(utils.H(lambda t: model.p_theory_data(t, alldata, normalized=True)\
				, model.t_space)-\
				 utils.H(lambda t: model.p_theory_data(t, data, normalized=True)\
				, model.t_space))*\
				model.p_data_action(d,action,data)

	return expval/norm



def theory_expected_final_entropy(action, data=None, normalized=False):
	
	#normalize p_data_action, p_theory_data not necessarily, just tell me
	norm=0
	for d in world.possible_data(action):
	 	norm+=model.p_data_action(d,action,data)

	expval=0
	for d in world.possible_data(action):
		alldata=[d] if data is None else [d]+data
		expval+=utils.H(lambda t: model.p_theory_data(t, alldata, normalized=normalized),\
						 model.t_space, normalized=normalized)*\
				model.p_data_action(d,action,data)

	return expval/norm


def joint_expected_final_entropy(action, data=None, normalized=False):

	#normalize p_data_action, p_theory_data not necessarily, just tell me
	norm=0
	for d in world.possible_data(action):
	 	norm+=model.p_data_action(d,action,data)

	expval=0
	for d in world.possible_data(action):
		alldata=[d] if data is None else [d]+data
		expval+=utils.H(lambda (t,hs): model.p_theoryhypothesis_data(t,hs,alldata),\
					model.th_space, False)*model.p_data_action(d,action,data)
	
	return expval/norm


def hypotheses_expected_final_entropy(action, data=None, normalized=False):

	#normalize p_data_action, p_theory_data not necessarily, just tell me
	norm=0
	for d in world.possible_data(action):
	 	norm+=model.p_data_action(d,action,data)

	expval=0
	for d in world.possible_data(action):
		alldata=[d] if data is None else [d]+data
		expval+=utils.H(lambda hs: model.p_hypotheses_data(hs,alldata),\
					model.fullh_space, False)*model.p_data_action(d,action,data)
	
	return expval/norm


def expected_final_entropy(level, action, data=None, normalized=False):
	if level=='theory':
		return theory_expected_final_entropy(action, data, normalized)
	elif level=='hypotheses':
		return	hypotheses_expected_final_entropy(action, data, normalized)
	elif level=='joint':
		return	joint_expected_final_entropy(action, data, normalized)

