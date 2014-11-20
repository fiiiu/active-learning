
import Data
import numpy as np

d=Data.Data()
d.read(astext=False)

table=np.zeros((3,3))
mtable=np.zeros((3,3))

condition=['']*29
acts1=[d.get_index_experience(i)[0] for i in range(29)]
acts2=[d.get_index_experience(i)[1] for i in range(29)]

macts1=[((1, 2), (0, 2)),\
((2, 1), (2, 0)),\
((1, 2), (0, 2)),\
((2, 1), (1, 1)),\
((1, 2), (0, 2)),\
((1, 2), (1, 1)),\
((1, 2), (0, 2)),\
((2, 1), (2, 0)),\
((0, 0), (0, 2)),\
((0, 0), (2, 0)),\
((2, 1), (1, 1)),\
((0, 0), (2, 0)),\
((0, 0), (0, 2)),\
((1, 2), (1, 1)),\
((1, 2), (0, 2)),\
((2, 1), (1, 1)),\
((2, 1), (1, 1)),\
((1, 2), (0, 2)),\
((1, 2), (0, 2)),\
((2, 1), (1, 1)),\
((2, 1), (2, 0)),\
((0, 0), (0, 2)),\
((1, 2), (1, 1)),\
((2, 1), (2, 0)),\
((2, 1), (2, 0)),\
((2, 1), (2, 0)),\
((2, 1), (1, 1)),\
((2, 1), (1, 1)),\
((1, 2), (0, 2))]
#,\((2, 1), (1, 1)),\((1, 2), (1, 1))]
print len(macts1)

macts2=[((0, 0), (0, 2)), ((2, 1), (1, 1)), ((2, 1), (2, 0)),\
((2, 1), (2, 0)),\
((2, 1), (1, 1)),\
((2, 1), (1, 1)),\
((1, 2), (0, 2)),\
((0, 0), (0, 2)),\
((1, 2), (0, 2)),\
((1, 2), (1, 1)),\
((0, 0), (2, 0)),\
((0, 0), (0, 2)),\
((2, 1), (1, 1)),\
((0, 0), (2, 0)),\
((1, 2), (1, 1)),\
((1, 2), (1, 1)),\
((0, 0), (2, 0)),\
((1, 2), (1, 1)),\
((1, 2), (0, 2)),\
((2, 1), (1, 1)),\
((0, 0), (2, 0)),\
((1, 2), (1, 1)),\
((2, 1), (2, 0)),\
((0, 0), (0, 2)),\
((0, 0), (0, 2)),\
((2, 1), (1, 1)),\
((2, 1), (2, 0)),\
((2, 1), (1, 1)),\
((2, 1), (2, 0))]
#((1, 2), (0, 2))]
print len(macts2)
colus=np.zeros((29,1),dtype=int)
for i in range(29):

	if acts1[i].active:
		row=0
		if acts1[i].machine[0]==acts1[i].toy[0]:
			condition[i]='color'
			colus[i]=0
		else:
			condition[i]='shape'
	else:
		if acts1[i].machine[0]!=acts1[i].toy[0] and acts1[i].machine[1]!=acts1[i].toy[1]:
			row=2
			colus[i]=2
		else:
			row=1
			if acts1[i].machine[1]==acts1[i].toy[1]:
		 		condition[i]='color'
		 		colus[i]=1
			else:
		 		condition[i]='shape'

	if acts2[i].active:
		col=0
		if acts2[i].machine[0]==acts2[i].toy[0]:
			condition[i]='color'
		else:
			condition[i]='shape'
	else:
		if acts2[i].machine[0]!=acts2[i].toy[0] and acts2[i].machine[1]!=acts2[i].toy[1]:
			col=2
		else:
			col=1

	table[row,col]+=1

import world
wacts=world.possible_actions()
kacts=np.zeros((29,3))
for i in range(29):
	if condition[i]=='color':
		
	if acts1[i].toy==acts2[i].toy:
		if acts 


		ro=wacts.index((acts2[i].toy,acts2[i].machine))
		print ro
		kacts[ro][colus[i]]+=1
	else:


print kacts






for i in range(29):

	if (condition[i]=='color' and macts1[i][0][0]==macts1[i][1][0]) or\
	   (condition[i]=='shape' and macts1[i][0][1]==macts1[i][1][1]):
	    #	print macts1[i]
	    row=0
	else:
		if macts1[i][0][0]!=macts1[i][1][0] and macts1[i][0][1]!=macts1[i][1][1]:
			row=2
		else:
			row=1

	if (condition[i]=='color' and macts2[i][0][0]==macts2[i][1][0]) or\
	   (condition[i]=='shape' and macts2[i][0][1]==macts2[i][1][1]):
		col=0
	else:
		if macts2[i][0][0]!=macts2[i][1][0] and macts2[i][0][1]!=macts2[i][1][1]:
			col=2
		else:
			col=1


	mtable[row,col]+=1

print table
print mtable

print condition


#import final_entropys as eg
import learners
import world
# machines=[(2,0), (1,1), (0,2)]
# available_toys=[(2,1), (0,0), (1,2)]
import Datapoint
dac=[Datapoint.Datapoint(((0,0),(0,2)),True)]
dis=[Datapoint.Datapoint(((0,0),(2,0)),False)]
dnon=[Datapoint.Datapoint(((0,0),(1,1)),False)]

tl=learners.TheoryLearner()
ents=np.zeros((len(world.possible_actions()),3))
for i,action in enumerate(world.possible_actions()):
	ents[i,0]=tl.expected_final_entropy(action, dac)
	ents[i,1]=tl.expected_final_entropy(action, dis)
	ents[i,2]=tl.expected_final_entropy(action, dnon)

acts=world.possible_actions()
for r in range(len(acts)):
	print r, acts[r], ents[r], kacts[r]

