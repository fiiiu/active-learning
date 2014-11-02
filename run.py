
import HypothesisFactory
import Theory
import Hypothesis
import Datapoint
import world
#import parameters

h0=Hypothesis.Hypothesis((0,0),2,0)
h1=Hypothesis.Hypothesis((1,0),2,0)
h2=Hypothesis.Hypothesis((1,0),2,1)
#d00t=Datapoint.Datapoint(-1,-1,0,0,True)

t_col=Theory.Theory(2)
t_sha=Theory.Theory(3)
t_indep=Theory.Theory(11)

# dat_col=[Datapoint.Datapoint(parameters.machines[0],(2,1),True),\
# 		Datapoint.Datapoint(parameters.machines[1],(1,2),True)]
# dat_sha=[Datapoint.Datapoint(parameters.machines[0],(0,0),True),\
# 		Datapoint.Datapoint(parameters.machines[1],(2,1),True)]

# dat_indep=[Datapoint.Datapoint(parameters.machines[0],(2,1),True),\
# 		Datapoint.Datapoint(parameters.machines[1],(2,1),True)]

dat_col=[Datapoint.Datapoint((world.available_toys[0],world.machines[0]),True),\
		Datapoint.Datapoint((world.available_toys[2],world.machines[1]),True)]

dat_sha=[Datapoint.Datapoint((world.available_toys[1],world.machines[0]),True),\
		Datapoint.Datapoint((world.available_toys[0],world.machines[1]),True)]

dat_indep=[Datapoint.Datapoint((world.available_toys[0],world.machines[0]),True),\
		Datapoint.Datapoint((world.available_toys[0],world.machines[1]),True)]



print t_col.unnormalized_posterior(), t_sha.unnormalized_posterior(), t_indep.unnormalized_posterior()
print t_col.unnormalized_posterior(dat_col), t_sha.unnormalized_posterior(dat_col), t_indep.unnormalized_posterior(dat_col)
print t_col.unnormalized_posterior(dat_sha), t_sha.unnormalized_posterior(dat_sha), t_indep.unnormalized_posterior(dat_sha)
print t_col.unnormalized_posterior(dat_indep), t_sha.unnormalized_posterior(dat_indep), t_indep.unnormalized_posterior(dat_indep)

#print t_col.likelihood(h0),t_col.likelihood(h1),t_col.likelihood(h2)


# #hyp factory test
# hf=HypothesisFactory.HypothesisFactory()
# allh=hf.create_all_hypotheses((0,0))
# [h.display() for h in allh]
# print len(allh)


# h=Hypothesis.Hypothesis((0,0), 5, color=0, shape=0)
# # h.display()
# hf=HypothesisFactory.HypothesisFactory()
# allh00=hf.create_all_hypotheses((0,0))

# print len(allh00)

#5 test
# t=Theory.Theory(5)
# hs5=[]
# for h in allh00:
#     if h.kind==5:
#         hs5.append(h)
# print len(hs5)

# for h in hs5:
# 	if t.hypothesis_likelihood(h)==1:
# 		h.display()

# #hs5[0].display()
# print hs5[0].shape,hs5[0].color

# #11 test
# print "\n new test"
# t=Theory.Theory(9)

# for h in allh00:
# 	if t.hypothesis_likelihood(h)>0:
# 		h.display()
# 		print t.hypothesis_likelihood(h)









