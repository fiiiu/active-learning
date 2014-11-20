


import sys
import matplotlib.pyplot as plt
import numpy as np
import Data
import Datapoint
import entropy_gains
import learners
import world
import numpy
import time
import parameters
import random



def main(player, n):
	
	#random.seed(0)
	starttime=time.clock()
	data=Data.Data()
	data.read(astext=False)
	n_kids=parameters.n_kids
	truncate=int(n)
	#n_r_theo=parameters.n_r_theo
	n_r_random=parameters.n_r_random
	epsilons=[0.001, 0.005, 0.01, 0.05, 0.1, 0.25]
	epsilons=[0.25]#001]
	#epsilons=[0.002, 0.003, 0.004, 0.006, 0.007, 0.008, 0.009]
	#epsilons=[0.006]

	for epsilon in epsilons:
		entropy_gains.model.epsilon=epsilon
		#eg=np.zeros(len(data.get_kids()[:n_kids]))
		
		if player in ['theory', 'joint', 'hypotheses']:

			n_long_kids=sum([data.get_kid_nactions(kid)>=truncate \
							 for kid in data.get_kids()])
			eig=np.zeros((n_long_kids,3))
			olactions=[]
			rlactions=[]

			k=0
			for ki,kid in enumerate(data.get_kids()[:n_kids]):
			#for ki,kid in enumerate(data.get_kids()[5:6]):
				if data.get_kid_nactions(kid)<truncate:
					continue
				
				#get kid's action sequence
				kidseq=data.data[kid][:truncate]
				keg=entropy_gains.expected_final_entropy(player, kidseq[-1].action,kidseq[:-1])
				
				#compute optimal choice entropy gain with kid's action sequence
				if player=='theory':
					ol=learners.TheoryLearner()
				elif player=='joint':
					ol=learners.JointLearner()
				elif player=='hypotheses':
					ol=learners.HypothesesLearner()

				olaction=ol.choose_action(kidseq[:truncate-1])
				olactions.append(olaction)
				yokedseq=kidseq[:-1]+[Datapoint.Datapoint(olaction, False)]#this False is generic, shouldn't be taken into account
				oleg=entropy_gains.expected_final_entropy(player, olaction, kidseq[:-1])
				
				reg=0
				rlactions.append([])
				for r in range(n_r_random):
					rl=learners.RandomLearner()
					rlaction=rl.choose_action(kidseq[:truncate-1])
					rlactions[k].append(rlaction)
					yokedseqr=kidseq[:-1]+[Datapoint.Datapoint(rlaction, False)]#this False is generic, shouldn't be taken into account
					reg+=entropy_gains.expected_final_entropy(player, rlaction, kidseq[:-1])
					
				reg/=n_r_random
			
				eig[k,0]=oleg
				eig[k,1]=reg
				eig[k,2]=keg
				k+=1


		# save this epsilons
		filename=parameters.output_directory+player+'-'+str(truncate)+'_tru-'\
					+str(n_r_random)+'_rreal-'+str(epsilon)+'.txt'
		np.savetxt(filename, eig)

		with open(parameters.output_directory+player+'-modelactions-'+str(truncate)+'_tru-'+\
			str(n_r_random)+'_rreal-'+str(epsilon)+'.txt','w') as f:
			for kact in olactions:
				f.write(str(kact)+'\n')

		with open(parameters.output_directory+player+'-randomactions-'+str(truncate)+'_tru-'+\
			str(n_r_random)+'_rreal-'+str(epsilon)+'.txt','w') as f:
			for kact in rlactions:
				f.write(str(kact)+'\n')




if __name__ == '__main__':
	n=1
	if len(sys.argv)==1:
		player='kids'		
	else:
		player=sys.argv[1]
		if len(sys.argv)>2:
			n=int(sys.argv[2])
			
	main(player,n)


