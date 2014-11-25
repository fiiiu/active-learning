
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas
import Data


output_directory='/Users/alejo/Neuro/ActiveLearning/Output/'
today='141119/'
#batch='ep-0.05/'
batch='varyep/'
data_directory=output_directory+today#+batch


data=Data.Data()
data.read(astext=False)


axes=[[],[],[],[]]

for n_act in range(1,3):
	phase2list=[]
	for k,kid in enumerate(data.get_kids()):
		if data.get_kid_nactions(kid) >= n_act:
			phase2list.append(data.data2[kid])
	phase2=np.array(phase2list)
	print phase2[:,0]
	#read kids' analysis data
	model='jointfull'
	filename=model+'-'+str(n_act)+'_tru-20'+'_rreal.txt'
	fulldata=np.loadtxt(data_directory+filename)

	kids_reig=fulldata[:,2]-fulldata[:,0]
	kids_ph2aves=(phase2[:,0]+phase2[:,1])/2


	seadat={"eig": kids_reig, "First": map(bool, phase2[:,0]), "Second": map(bool, phase2[:,1])}
	df = pandas.DataFrame(data=seadat)#, index=index)

	#sns.lmplot("eig", "ph2a", df, y_jitter=.05, logistic=True)
	#sns.lmplot("eig", "ph2b", df, y_jitter=.05, logistic=True)
	#sns.pairplot(kids_reig, kids_ph2aves)
	#plt.show()
	df_long = pandas.melt(df, "eig", var_name="Test Phase", value_name="ph2bo")

	
	#sns.factorplot("eig", hue="ph2w", y="ph2bo", data=df_long)#, kind="box")
	axes[n_act-1]=sns.lmplot("eig", "ph2bo", df_long, hue="Test Phase",\
							 y_jitter=.05, logistic=True, size=6, aspect=1.25)

	#g = sns.PairGrid(df, y_vars=["ph2a","ph2b"], x_vars=["eig"], size=4)

	axes[n_act-1].set(xlabel="Relative Expected Information Gain", ylabel="Response Correct")



plt.show()