
import itertools
import HypothesisFactory
import Theory
import world


n_theories=12

#t_space=range(n_theories)
t_space=[Theory.Theory(t) for t in range(n_theories)]
hf=HypothesisFactory.HypothesisFactory()
#h_space=[h for h in hf.create_all_hypotheses(machine) for machine in world.machines]
#th_space=[(t,[h for h in hf.create_all_hypotheses(machine)])\
			# for t in t_space for machine in world.machines]

pre_all_hypotheses=[hf.create_all_hypotheses(machine) for machine in world.machines]
all_hypotheses=list(itertools.product(*pre_all_hypotheses))

th_space=[(t, h) for t in t_space for h in all_hypotheses]


#th_space=[(t,[h for h in hf.create_all_hypotheses(machine) for machine in world.machines])\
			 #for t in t_space for machine in world.machines]

# def p_theory_data(theory, data=None):
# 	t=Theory.Theory(theory)
# 	return t.unnormalized_posterior(data)

def p_theory_data(theory, data=None):
	return theory.unnormalized_posterior(data)

def p_data_action(datapoint, action, prev_data=None):
	if datapoint in world.possible_data(action):
		pda=0
		machine=action[1]
		for t in t_space:
			for h in hf.create_all_hypotheses(machine):
				pda+=h.single_likelihood(datapoint)*h.unnormalized_posterior(prev_data)
		return pda
	else:
		return 0

def p_theoryhypothesis_data(theory, hypotheses, data):
	prob=1
	for h in hypotheses:
		prob*=h.likelihood(data)*theory.hypothesis_likelihood(h)
	prob*=theory.prior()
	return prob


