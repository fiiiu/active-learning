
import low_model as model
import world
import Datapoint

m0,m1,m2=world.machines
t0,t1,t2=world.available_toys
model.epsilon=1e-3
# print m0
# for h in model.singleh_space:
# 	print 'hyp: {0}, p: {1}'.format(h, model.p_hypothesis(h,m))

d0=[Datapoint.Datapoint((t0,m0), True)]

# print t1, m0
# for h in model.singleh_space:
# 	print 'hyp: {0}, p: {1}, ppost: {2}'.format(h, model.p_hypothesis(h,m0),\
#  													model.p_hypothesis_data(h,m0,d0))

# for t in model.t_space:	
#  	print 't: {0}, p: {1}, ppost: {2}'.format(t, model.p_theory(t),\
#  													model.p_theory_data(t,d0)\
#  													)


d0p=Datapoint.Datapoint((t1,m0), True)
d1=Datapoint.Datapoint((t1,m1), True)
#for h in model.singleh_space:
#print model.p_data_action(d0p, (t1,m0), []), model.p_data_action(d0p, (t1,m0), d0)

action=(t2,m1)
n1=0
n2=0
p1s=[]
p2s=[]

d0[0].display()
print action
for dat in world.possible_data(action):
	p1=model.p_data_action(dat, (t2,m1), [])
	p2=model.p_data_action(dat, (t2,m1), d0)
	
	n1+=p1
	n2+=p2

	p1s.append(p1)
	p2s.append(p2)


print [p/n1 for p in p1s]
print [p/n2 for p in p2s]