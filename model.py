
import HypothesisFactory
import Theory
import world


t_space=range(world.n_theories)
hf=HypothesisFactory.HypothesisFactory()

def p_theory_data(theory, data=None):
	t=Theory.Theory(theory)
	return t.unnormalized_posterior(data)


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

