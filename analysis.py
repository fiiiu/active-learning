

import Data
import entropy_gains
import learners
import matplotlib.pyplot as plt


def kid_ave_theory_entropy_gain(kid):
	gain=0
	for i,datapoint in enumerate(data.data[kid]):
		gain+=entropy_gains.theory_entropy_gain(datapoint.action, data.data[kid][:i])
	return float(gain)/data.get_kid_nactions(kid)


data=Data.Data()
data.read()

rl=learners.RandomLearner()

for kid in data.get_kids():
	#print kid, kid_ave_theory_entropy_gain(kid)
	rlgain=0
	for i in range(data.get_kid_nactions(kid)):
		rlgain+=entropy_gains.theory_entropy_gain(rl.choose_action())
	print "Kid {0}: {1}, RandomLearner: {2}"\
	.format(kid, kid_ave_theory_entropy_gain(kid),\
	 float(rlgain)/data.get_kid_nactions(kid))




