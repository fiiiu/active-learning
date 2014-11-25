	
import numpy as np

output_directory='/Users/alejo/Neuro/ActiveLearning/Output/'
today='141119/'
#batch='ep-0.05/'
batch='varyep/'
data_directory=output_directory+today#+batch

n_act=2

model='jointfull'
filename=model+'-'+str(n_act)+'_tru-20'+'_rreal.txt'
datajoi=np.loadtxt(data_directory+filename)
print data_directory+filename

model='hypfull'
filename=model+'-'+str(n_act)+'_tru-20'+'_rreal.txt'
datahyp=np.loadtxt(data_directory+filename)
print data_directory+filename

for i in range(len(datahyp)):
	print datahyp[i,2]-datahyp[i,0], datajoi[i,2]-datajoi[i,0] 


import entropy_gains as eg

import world
pa=world.possible_actions()
print eg.hypotheses_expected_final_entropy(pa[0],[])-eg.hypotheses_expected_final_entropy(pa[1],[])
print eg.joint_expected_final_entropy(pa[0],[])-eg.hypotheses_expected_final_entropy(pa[1],[])



