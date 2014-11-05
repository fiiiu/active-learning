
import utils
#import newmodel as model
import world

import high_model
import low_model

def ave_theory_expected_entropy(sequence):
	jumps=0
	ave_entropies=0
	entropies=[]#theory_expected_final_entropy(sequence[0].action)]
	for i,datapoint in enumerate(sequence):
		entropy=theory_expected_final_entropy(datapoint.action, sequence[:i])
		entropies.append(entropy)
		ave_entropies+=entropy
		if i>0:
			jumps-=entropies[i]-entropies[i-1]
		
	return float(ave_entropies)/len(sequence), entropies#float(jumps)/(len(sequence)), entropies



def theory_expected_final_entropy(action, data=None):
	expval=0
	# #normalize???
	norm=0
	for d in world.possible_data(action):
	 	norm+=model.p_data_action(d,action,data)

	for d in world.possible_data(action):
		alldata=[d] if data is None else [d]+data
		#print utils.H(lambda t: model.p_theory_data(t, alldata), model.t_space)
		#print 'p_d_a', model.p_data_action(d,action,data)
		expval+=utils.H(lambda t: model.p_theory_data(t, alldata, normalized=True), model.t_space)*\
				model.p_data_action(d,action,data)

	# print action, data, expval/norm
	#print [t.kind for t in model.t_space]
	return expval/norm


def joint_entropy_gain(action, data=None):
	expval=0
	for d in world.possible_data(action):
		alldata=[d] if data is None else [d]+data
		expval+=utils.H(lambda (t,hs): model.p_theoryhypothesis_data(t,hs,alldata),\
					model.th_space)*model.p_data_action(d,action,data)
	return expval



