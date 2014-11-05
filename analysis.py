
import sys
import matplotlib.pyplot as plt
import numpy as np
import Data
import entropy_gains
import learners
import world
import numpy
import time
import parameters

# for kid in data.get_kids():
# 	print "Kid {0}: {1}, RandomLearner: {2}, TheoryLearner: {3}".format(kid, keg, reg, teg)
	

def main(player):
	starttime=time.clock()
	data=Data.Data()
	data.read(astext=False)
	n_kids=parameters.n_kids
	truncate=parameters.truncate
	n_r_theo=parameters.n_r_theo
	n_r_random=parameters.n_r_random

	eg=np.zeros(len(data.get_kids()[:n_kids]))
	
	if player=='kids':
		n_r=1
		for k,kid in enumerate(data.get_kids()[:n_kids]):
			kidseq=data.data[kid][:truncate]
			keg=entropy_gains.ave_theory_expected_entropy_gain(kidseq)[0]
			#print kid, keg
			eg[k]=keg
			#nkegs

	elif player=='random':
		n_r=n_r_theo
		egall=np.zeros((len(data.get_kids()[:n_kids]), n_r))
		for k,kid in enumerate(data.get_kids()[:n_kids]):
			for r in range(n_r_random):
				rl=learners.RandomLearner()
				rlseq=rl.play(min(data.get_kid_nactions(kid),truncate))
				reg=entropy_gains.ave_theory_expected_entropy_gain(rlseq)[0]
				#print kid, reg
				eg[k]+=reg
				egall[k,r]=reg
			eg[k]/=n_r
		#[d.display() for d in rlseq]
		#print reg

	elif player=='theory':
		n_r=n_r_theo
		egall=np.zeros((len(data.get_kids()[:n_kids]), n_r))
		for k,kid in enumerate(data.get_kids()[:n_kids]):
			for r in range(n_r_theo):
				tl=learners.TheoryLearner()
				tlseq=tl.play(min(data.get_kid_nactions(kid),truncate))
				teg=entropy_gains.ave_theory_expected_entropy_gain(tlseq)[0]
				#print kid, teg
				eg[k]+=teg
				egall[k,r]=teg
			eg[k]/=n_r


	filename='Output/out-HIGH-'+player+'-'+str(truncate)+'_tru-'+str(n_r)+'_real.txt'
	np.savetxt(filename, eg)

	if player in ['random', 'theory']:
		filenameall='Output/all-HIGH-'+player+'-'+str(truncate)+'_tru-'+str(n_r)+'_real.txt'
		np.savetxt(filenameall, egall)
	
	print 'time elapsed for run {0}: {1:.0f} s'.format(filename, time.clock()-starttime)



if __name__ == '__main__':
	if len(sys.argv)==1:
		player='kids'
	else:
		player=sys.argv[1]
	main(player)

