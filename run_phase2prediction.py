
import numpy as np
import Data
import low_model as model
import learners
import world

#read kids data
data=Data.Data()
data.read(astext=False)

#learners
tl=learners.TheoryLearner()
#tl=learners.HypothesesLearner()

successes=np.empty((len(data.get_kids()),2))
#model.epsilon=0.25

phase='a'
for k,kid in enumerate(data.get_kids()):
	
	taction=tl.choose_action_phase2(phase, data.get_index_experience(k))
	dp=world.make_action(taction, data.condition[kid])

	if phase=='a':
		ksuc=data.data2[kid][0]
	elif phase=='b':
		ksuc=data.data2[kid][1]
	successes[k,:]=(ksuc,int(dp.active))
	
	[dap.display() for dap in data.get_index_experience(k)]
	print taction, data.condition[kid]
	print ksuc, dp.active




