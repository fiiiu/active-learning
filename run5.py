

import low_model as model
import world
import entropy_gains as eg

for action in world.possible_actions():
	print action, eg.hypotheses_expected_final_entropy(action,[])