
import Data
import numpy as np

d=Data.Data()
d.read(astext=False)

table=np.zeros((3,3))
mtable=np.zeros((3,3))

condition=['']*30
acts1=[d.get_index_experience(i)[0] for i in range(29)]+[d.get_index_experience(30)[0]]
acts2=[d.get_index_experience(i)[1] for i in range(29)]+[d.get_index_experience(30)[1]]


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
((1, 2), (0, 2)),\
#,\((2, 1), (1, 1)),
((1, 2), (1, 1))]
#print len(macts1)

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
((2, 1), (2, 0)),\
((1, 2), (0, 2))]
#print len(macts2)
nkids=3
colus=np.zeros((30,1),dtype=int)
for i in range(30):

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
kacts=np.zeros((6,3),dtype=int)
for i in range(30):
	toy1=acts1[i].toy
	mac1=acts1[i].machine
	toy2=acts2[i].toy
	mac2=acts2[i].machine
	
	if acts1[i].active:
		col=0
		if toy1[0]==mac1[0]:
			prop1='col_p'
		elif toy1[1]==mac1[1]:
			prop1='sha_p'
	else:
		if toy1[0]==mac1[0]:
			col=1
			prop1='col_m'
		elif toy1[1]==mac1[1]:
			col=1
			prop1='sha_m'
		else:
			col=2
			prop1='none'

	if (toy2[0]==mac2[0] and (prop1=='col_p' or prop1=='col_m')) or\
	   (toy2[1]==mac2[1] and (prop1=='sha_p' or prop1=='sha_m')):
		row=0
	elif toy2[0]!=mac2[0] and toy2[1]!=mac2[1]:
		if mac2==mac1:
			row=3
		elif toy2==toy1:
			row=4
		else:
			row=5
	elif mac2==mac1:
		row=1
	elif toy2==toy1:
		row=2
	elif prop1=='none':
		row=0 #somewhat artificial
		#acts1[i].display(), acts2[i].display()	

	#print row, col
	kacts[row][col]+=1



print kacts
for i,r in enumerate(kacts):
	print '{3} & {0} & {1} & {2} \ '.format(r[0],r[1],r[2], i)


########
import learners
tl=learners.HypothesesLearner()
# # machines=[(2,0), (1,1), (0,2)]
# # available_toys=[(2,1), (0,0), (1,2)]
import Datapoint
dac=[Datapoint.Datapoint(((0,0),(0,2)),True)]
dis=[Datapoint.Datapoint(((0,0),(2,0)),False)]
dnon=[Datapoint.Datapoint(((0,0),(1,1)),False)]

ents=np.zeros((6,3))

learners.entropy_gains.model.epsilon=0.25

ents[0,0]=tl.expected_final_entropy(((2,1),(2,0)), dac)
print 'one'
ents[1,0]=tl.expected_final_entropy(((1,2),(0,2)), dac)
ents[2,0]=tl.expected_final_entropy(((0,0),(2,0)), dac)
ents[3,0]=tl.expected_final_entropy(((2,1),(0,2)), dac)
ents[4,0]=tl.expected_final_entropy(((0,0),(1,1)), dac)
ents[5,0]=tl.expected_final_entropy(((1,2),(2,0)), dac)

ents[0,1]=tl.expected_final_entropy(((2,1),(1,1)), dis)
ents[1,1]=tl.expected_final_entropy(((2,1),(2,0)), dis)
ents[2,1]=tl.expected_final_entropy(((0,0),(0,2)), dis)
ents[3,1]=tl.expected_final_entropy(((1,2),(2,0)), dis)
ents[4,1]=tl.expected_final_entropy(((0,0),(1,1)), dis)
ents[5,1]=tl.expected_final_entropy(((2,1),(0,2)), dis)

ents[0,2]=tl.expected_final_entropy(((2,1),(2,0)), dnon)
ents[1,2]=tl.expected_final_entropy(((1,2),(1,1)), dnon)
ents[2,2]=tl.expected_final_entropy(((0,0),(0,2)), dnon)
ents[3,2]=0#tl.expected_final_entropy(((,),(1,1)), dnon)
ents[4,2]=0#tl.expected_final_entropy(((0,0),(,)), dnon)
ents[5,2]=tl.expected_final_entropy(((2,1),(0,2)), dnon)

print ents
print kacts
for i,r in enumerate(ents):
	print '{3} & {0:.3f} & {1:.3f} & {2:.3f} \ '.format(r[0],r[1],r[2], i)



# #remainders
# rems=np.zeros((4,3))
# rems[0,0]=tl.expected_final_entropy(((2,1),(1,1)), dac)
# rems[1,0]=tl.expected_final_entropy(((1,2),(1,1)), dac)

# rems[0,1]=tl.expected_final_entropy(((1,2),(1,1)), dis)
# rems[1,1]=tl.expected_final_entropy(((1,2),(0,2)), dis)

# rems[0,2]=tl.expected_final_entropy(((1,2),(0,2)), dnon)
# rems[1,2]=tl.expected_final_entropy(((1,2),(2,0)), dnon)
# rems[2,2]=tl.expected_final_entropy(((0,0),(2,0)), dnon)
# rems[3,2]=tl.expected_final_entropy(((2,1),(1,1)), dnon)

#print rems

print learners.entropy_gains.model.epsilon
# for i in range(30):

# 	if (condition[i]=='color' and macts1[i][0][0]==macts1[i][1][0]) or\
# 	   (condition[i]=='shape' and macts1[i][0][1]==macts1[i][1][1]):
# 	    #	print macts1[i]
# 	    row=0
# 	else:
# 		if macts1[i][0][0]!=macts1[i][1][0] and macts1[i][0][1]!=macts1[i][1][1]:
# 			row=2
# 		else:
# 			row=1

# 	if (condition[i]=='color' and macts2[i][0][0]==macts2[i][1][0]) or\
# 	   (condition[i]=='shape' and macts2[i][0][1]==macts2[i][1][1]):
# 		col=0
# 	else:
# 		if macts2[i][0][0]!=macts2[i][1][0] and macts2[i][0][1]!=macts2[i][1][1]:
# 			col=2
# 		else:
# 			col=1


# 	mtable[row,col]+=1

# print table
# print mtable

# print condition


# #import final_entropys as eg
# import learners
# import world
# # machines=[(2,0), (1,1), (0,2)]
# # available_toys=[(2,1), (0,0), (1,2)]
# import Datapoint
# dac=[Datapoint.Datapoint(((0,0),(0,2)),True)]
# dis=[Datapoint.Datapoint(((0,0),(2,0)),False)]
# dnon=[Datapoint.Datapoint(((0,0),(1,1)),False)]

# tl=learners.TheoryLearner()
# ents=np.zeros((len(world.possible_actions()),3))
# for i,action in enumerate(world.possible_actions()):
# 	ents[i,0]=tl.expected_final_entropy(action, dac)
# 	ents[i,1]=tl.expected_final_entropy(action, dis)
# 	ents[i,2]=tl.expected_final_entropy(action, dnon)

# acts=world.possible_actions()
# for r in range(len(acts)):
# 	print r, acts[r], ents[r], kacts[r]

