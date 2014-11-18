
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
from multiprocessing import Process

# for kid in data.get_kids():
# 	print "Kid {0}: {1}, RandomLearner: {2}, TheoryLearner: {3}".format(kid, keg, reg, teg)
	

def main(player, n):
	#random.seed(0)

	starttime=time.clock()
	data=Data.Data()
	data.read(astext=False)
	n_kids=parameters.n_kids
	truncate=int(n)
	#n_r_theo=parameters.n_r_theo
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
		n_r=n_r_random
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




	elif player=='theoryfull':

		n_long_kids=sum([data.get_kid_nactions(kid)>=truncate \
						 for kid in data.get_kids()])
		eig=np.zeros((n_long_kids,3))
		tlactions=[]
		rlactions=[]

		
		k=0
		for ki,kid in enumerate(data.get_kids()[:n_kids]):
			if data.get_kid_nactions(kid)<truncate:
				continue
			
			#get kid's action sequence
			kidseq=data.data[kid][:truncate]
			#keg, kents=entropy_gains.ave_theory_expected_entropy_gain(kidseq)
			#keg=entropy_gains.theory_expected_entropy_gain(kidseq[-1].action,kidseq[:-1])
			keg=entropy_gains.theory_expected_final_entropy(kidseq[-1].action,kidseq[:-1])
			
			#print 'kid {0} entropies: {1}'.format(k,kents)
			
			#compute optimal choice entropy gain with kid's action sequence
			tl=learners.TheoryLearner()
			tlaction=tl.choose_action(kidseq[:truncate-1])
			tlactions.append(tlaction)
			yokedseq=kidseq[:-1]+[Datapoint.Datapoint(tlaction, False)]#this False is generic, shouldn't be taken into account
			#tleg, tlents=entropy_gains.ave_theory_expected_entropy_gain(yokedseq)
			#tleg=entropy_gains.theory_expected_entropy_gain(tlaction, kidseq[:-1])
			tleg=entropy_gains.theory_expected_final_entropy(tlaction, kidseq[:-1])
			
			#print tlents

			reg=0
			rlactions.append([])
			for r in range(n_r_random):
				rl=learners.RandomLearner()
				#rseq=rl.play(truncate)
				rlaction=rl.choose_action(kidseq[:truncate-1])
				rlactions[k].append(rlaction)
				yokedseqr=kidseq[:-1]+[Datapoint.Datapoint(rlaction, False)]#this False is generic, shouldn't be taken into account
				#reg+=entropy_gains.ave_theory_expected_entropy_gain(yokedseqr)[0]
				#reg+=entropy_gains.theory_expected_entropy_gain(rlaction, kidseq[:-1])
				reg+=entropy_gains.theory_expected_final_entropy(rlaction, kidseq[:-1])
				
			reg/=n_r_random
			

			eig[k,0]=tleg
			eig[k,1]=reg
			eig[k,2]=keg
			#print 'k: {0}, r:{1}, t:{2}'.format(keg, reg, tleg)
			k+=1


	elif player=='jointfull':

		n_long_kids=sum([data.get_kid_nactions(kid)>=truncate \
						 for kid in data.get_kids()])
		eig=np.zeros((n_long_kids,3))
		tlactions=[]
		rlactions=[]

		
		k=0
		for ki,kid in enumerate(data.get_kids()[:n_kids]):
			if data.get_kid_nactions(kid)<truncate:
				continue
			
			#get kid's action sequence
			kidseq=data.data[kid][:truncate]
			#keg, kents=entropy_gains.ave_theory_expected_entropy_gain(kidseq)
			#keg=entropy_gains.theory_expected_entropy_gain(kidseq[-1].action,kidseq[:-1])
			keg=entropy_gains.joint_expected_final_entropy(kidseq[-1].action,kidseq[:-1])
			
			#print 'kid {0} entropies: {1}'.format(k,kents)
			
			#compute optimal choice entropy gain with kid's action sequence
			tl=learners.JointLearner()
			tlaction=tl.choose_action(kidseq[:truncate-1])
			tlactions.append(tlaction)
			yokedseq=kidseq[:-1]+[Datapoint.Datapoint(tlaction, False)]#this False is generic, shouldn't be taken into account
			#tleg, tlents=entropy_gains.ave_theory_expected_entropy_gain(yokedseq)
			#tleg=entropy_gains.theory_expected_entropy_gain(tlaction, kidseq[:-1])
			tleg=entropy_gains.joint_expected_final_entropy(tlaction, kidseq[:-1])
			
			#print tlents

			reg=0
			rlactions.append([])
			for r in range(n_r_random):
				rl=learners.RandomLearner()
				#rseq=rl.play(truncate)
				rlaction=rl.choose_action(kidseq[:truncate-1])
				rlactions[k].append(rlaction)
				yokedseqr=kidseq[:-1]+[Datapoint.Datapoint(rlaction, False)]#this False is generic, shouldn't be taken into account
				#reg+=entropy_gains.ave_theory_expected_entropy_gain(yokedseqr)[0]
				#reg+=entropy_gains.theory_expected_entropy_gain(rlaction, kidseq[:-1])
				reg+=entropy_gains.joint_expected_final_entropy(rlaction, kidseq[:-1])
				
			reg/=n_r_random
			

			eig[k,0]=tleg
			eig[k,1]=reg
			eig[k,2]=keg
			#print 'k: {0}, r:{1}, t:{2}'.format(keg, reg, tleg)
			k+=1

	elif player=='hypfull':

		n_long_kids=sum([data.get_kid_nactions(kid)>=truncate \
						 for kid in data.get_kids()])
		eig=np.zeros((n_long_kids,3))
		tlactions=[]
		rlactions=[]

		
		k=0
		for ki,kid in enumerate(data.get_kids()[:n_kids]):
			if data.get_kid_nactions(kid)<truncate:
				continue
			
			#get kid's action sequence
			kidseq=data.data[kid][:truncate]
			#keg, kents=entropy_gains.ave_theory_expected_entropy_gain(kidseq)
			#keg=entropy_gains.theory_expected_entropy_gain(kidseq[-1].action,kidseq[:-1])
			keg=entropy_gains.hypotheses_expected_final_entropy(kidseq[-1].action,kidseq[:-1])
			
			#print 'kid {0} entropies: {1}'.format(k,kents)
			
			#compute optimal choice entropy gain with kid's action sequence
			tl=learners.HypothesesLearner()
			tlaction=tl.choose_action(kidseq[:truncate-1])
			tlactions.append(tlaction)
			yokedseq=kidseq[:-1]+[Datapoint.Datapoint(tlaction, False)]#this False is generic, shouldn't be taken into account
			#tleg, tlents=entropy_gains.ave_theory_expected_entropy_gain(yokedseq)
			#tleg=entropy_gains.theory_expected_entropy_gain(tlaction, kidseq[:-1])
			tleg=entropy_gains.hypotheses_expected_final_entropy(tlaction, kidseq[:-1])
			
			#print tlents

			reg=0
			rlactions.append([])
			for r in range(n_r_random):
				rl=learners.RandomLearner()
				#rseq=rl.play(truncate)
				rlaction=rl.choose_action(kidseq[:truncate-1])
				rlactions[k].append(rlaction)
				yokedseqr=kidseq[:-1]+[Datapoint.Datapoint(rlaction, False)]#this False is generic, shouldn't be taken into account
				#reg+=entropy_gains.ave_theory_expected_entropy_gain(yokedseqr)[0]
				#reg+=entropy_gains.theory_expected_entropy_gain(rlaction, kidseq[:-1])
				reg+=entropy_gains.hypotheses_expected_final_entropy(rlaction, kidseq[:-1])
				
			reg/=n_r_random
			

			eig[k,0]=tleg
			eig[k,1]=reg
			eig[k,2]=keg
			#print 'k: {0}, r:{1}, t:{2}'.format(keg, reg, tleg)
			k+=1



	if player in ['random', 'theory', 'kids']:
		filename=parameters.output_directory+'out-'+player+'-'+str(truncate)+'_tru-'+str(n_r)+'_real.txt'
		np.savetxt(filename, eg)

	if player in ['random', 'theory']:
		filenameall=parameters.output_directory+'all-'+player+'-'+str(truncate)+'_tru-'+str(n_r)+'_real.txt'
		np.savetxt(filenameall, egall)
	
	if player in ['theoryfull', 'jointfull', 'hypfull']:
		filename=parameters.output_directory+player+'-'+str(truncate)+'_tru-'\
				+str(n_r_random)+'_rreal.txt'
		np.savetxt(filename, eig)

		with open(parameters.output_directory+player+'-modelactions-'+str(truncate)+'_tru-'+\
			str(n_r_random)+'_rreal.txt','w') as f:
			for kact in tlactions:
				f.write(str(kact)+'\n')

		with open(parameters.output_directory+player+'-randomactions-'+str(truncate)+'_tru-'+\
			str(n_r_random)+'_rreal.txt','w') as f:
			for kact in rlactions:
				f.write(str(kact)+'\n')


	print 'time elapsed for run {0}: {1:.0f} s'.format(filename, time.clock()-starttime)





if __name__ == '__main__':
	n=1
	parallel=False
	if len(sys.argv)==1:
		player='kids'		
	else:
		player=sys.argv[1]
		if len(sys.argv)>2:
			n=int(sys.argv[2])
			if len(sys.argv)>3:
				parallel=bool(sys.argv[3])

	if parallel:
		for i in range(1,n+1):
			p=Process(target=main, args=(player, i,))
			p.start()
		p.join()
			#main(player, i)
	else:
		main(player,n)


