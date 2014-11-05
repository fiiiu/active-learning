
import sys
import matplotlib.pyplot as plt
import Data
import entropy_gains
import learners
import world


# for kid in data.get_kids():
# 	print "Kid {0}: {1}, RandomLearner: {2}, TheoryLearner: {3}".format(kid, keg, reg, teg)
	

def main(player):
	data=Data.Data()
	data.read(astext=False)
	truncate=50

	if player=='kids':
		for kid in data.get_kids():
			kidseq=data.data[kid][:truncate]
			keg=entropy_gains.ave_theory_expected_entropy_gain(kidseq)[0]
			print kid, keg

	elif player=='random':
		rl=learners.RandomLearner()
		for kid in data.get_kids():
			rlseq=rl.play(min(data.get_kid_nactions(kid),truncate))
			reg=entropy_gains.ave_theory_expected_entropy_gain(rlseq)[0]
			print kid, reg
		
		#[d.display() for d in rlseq]
		#print reg

	elif player=='theory':
		tl=learners.TheoryLearner()
		for kid in data.get_kids():
			tlseq=tl.play(min(data.get_kid_nactions(kid),truncate))
			teg=entropy_gains.ave_theory_expected_entropy_gain(tlseq)[0]
			print kid, teg




if __name__ == '__main__':
	if len(sys.argv)==1:
		player='kids'
	else:
		player=sys.argv[1]
	main(player)

