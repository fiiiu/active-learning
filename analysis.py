

import Data
import entropy_gains
import learners
import matplotlib.pyplot as plt
import world

# def kid_ave_theory_entropy_gain(kid):
# 	gain=0
# 	for i,datapoint in enumerate(data.data[kid]):
# 		gain+=entropy_gains.theory_entropy_gain(datapoint.action, data.data[kid][:i])
# 	return float(gain)/data.get_kid_nactions(kid)


data=Data.Data()
data.read(astext=False)


# print entropy_gains.ave_theory_entropy_gain(data.data[data.get_kids()[0]])
# print kid_ave_theory_entropy_gain(data.get_kids()[0])

print data.data.values()[0][0].toy_shape

rl=learners.RandomLearner()
tl=learners.TheoryLearner()

# for kid in data.get_kids():
# 	#print kid, kid_ave_theory_entropy_gain(kid)
# 	rlgain=0
# 	for i in range(data.get_kid_nactions(kid)):
# 		rlgain+=entropy_gains.theory_entropy_gain(rl.choose_action())
# 	print "Kid {0}: {1}, RandomLearner: {2}"\
# 	.format(kid, kid_ave_theory_entropy_gain(kid),\
# 	 float(rlgain)/data.get_kid_nactions(kid))


for kid in data.get_kids():
	kidseq=data.data[kid]
	rlseq=rl.play(data.get_kid_nactions(kid))
	tlseq=tl.play(data.get_kid_nactions(kid))
	teg=entropy_gains.ave_theory_expected_entropy(tlseq)[0]
	reg=entropy_gains.ave_theory_expected_entropy(rlseq)[0]
	keg=entropy_gains.ave_theory_expected_entropy(kidseq)[0]
	print "Kid {0}: {1}, RandomLearner: {2}, TheoryLearner: {3}".format(kid, keg, reg, teg)
	


