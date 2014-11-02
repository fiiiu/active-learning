
import ActiveLearner
import Datapoint
import world
import model

# dat_col=[Datapoint.Datapoint((world.machines[0],(2,1)),True),\
# 		Datapoint.Datapoint((world.machines[1],(1,2)),True)]

dat_col=[Datapoint.Datapoint((world.available_toys[0],world.machines[0]),True),\
		Datapoint.Datapoint((world.available_toys[2],world.machines[1]),True)]

dat_sha=[Datapoint.Datapoint((world.available_toys[1],world.machines[0]),True),\
		Datapoint.Datapoint((world.available_toys[0],world.machines[1]),True)]

dat_indep=[Datapoint.Datapoint((world.available_toys[0],world.machines[0]),True),\
		Datapoint.Datapoint((world.available_toys[0],world.machines[1]),True)]


al=ActiveLearner.ActiveLearner()

print al.choose_action(dat_col)
print al.choose_action(dat_sha)
print al.choose_action(dat_indep)



# action=('')
# utils.H(lambda t: model.p_theory_data(t, dat_col), model.t_space)*\
# 					model.p_data_action(d,action,dat_col)