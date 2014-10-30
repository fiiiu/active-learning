
import HypothesisFactory
import Theory
import Hypothesis
import Datapoint
import parameters

h0=Hypothesis.Hypothesis((0,0),2,0)
h1=Hypothesis.Hypothesis((1,0),2,0)
h2=Hypothesis.Hypothesis((1,0),2,1)
#d00t=Datapoint.Datapoint(-1,-1,0,0,True)

t_col=Theory.Theory(2)
t_sha=Theory.Theory(3)

dat_col=[Datapoint.Datapoint(parameters.machines[0],2,1,True),\
		Datapoint.Datapoint(parameters.machines[1],1,2,True)]
dat_sha=[Datapoint.Datapoint(parameters.machines[0],0,0,True),\
		Datapoint.Datapoint(parameters.machines[1],2,1,True)]


print t_col.unnormalized_posterior(), t_sha.unnormalized_posterior()
print t_col.unnormalized_posterior(dat_col), t_sha.unnormalized_posterior(dat_col)
print t_col.unnormalized_posterior(dat_sha), t_sha.unnormalized_posterior(dat_sha)

#print t_col.likelihood(h0),t_col.likelihood(h1),t_col.likelihood(h2)


# #hyp factory test
# hf=HypothesisFactory.HypothesisFactory()
# allh=hf.create_all_hypotheses((0,0))
# [h.display() for h in allh]
# print len(allh)
