
import newmodel
import learners
import entropy_gains
import world
import Datapoint
import test_data


dcol=test_data.dat_col

rl=learners.RandomLearner()
print entropy_gains.theory_entropy_gain(rl.choose_action(dcol))

tl=learners.TheoryLearner()
#print tl.choose_action(dcol)

print entropy_gains.theory_entropy_gain(((0,0),(2,0)))
#print entropy_gains.theory_entropy_gain(tl.choose_action(dcol))


# import test_data
# d0=test_data.dat_col[0]
# #print 'oh! ', newmodel.p_data_hypothesis([d0], 0, (0,0))
# print 'oh! ', newmodel.p_singledata_hypothesis(d0, 2, (0,0))
# d0.display()

# suma=0
# count=0
# for m in world.machines:
# 	for t in world.available_toys:
# 		for r in [True,False]:
# 			d=Datapoint.Datapoint((t,m),r)
# 			d.display()
# 			prob=newmodel.p_singledata_hypothesis(d,2,(2,0))
# 			print 'prob: ', prob
# 			suma+=prob
# 			count+=1

# print 'suma={0}, count={1}'.format(suma,count)

# for h in newmodel.singleh_space:
# 	print 'oh! ', newmodel.p_hypothesis_theory(h, (0,1), 8)


# import utils

# def f(x):
# 	return 2

# print utils.H(f,[0,1])