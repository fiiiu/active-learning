
import Data
import entropy_gains
import test_data
import high_model
import low_model
import time
import world

dcol=test_data.dat_col
dsha=test_data.dat_sha
dind=test_data.dat_indep
[d.display() for d in dcol]

print 'low'
#entropy_gains.model=low_model
#print entropy_gains.ave_theory_expected_entropy(dcol)
#print low_model.p_theory_data(3, dcol)

print 'high'
#entropy_gains.model=high_model
#print entropy_gains.ave_theory_expected_entropy(dcol)
#print high_model.p_theory_data(3, dcol)

lposc=[0]*12
hposc=[0]*12
lposs=[0]*12
hposs=[0]*12
lposi=[0]*12
hposi=[0]*12

data=Data.Data()
data.read(astext=False)
dind=data.data[data.get_kids()[3]]

[d.display() for d in dind]
#dind[-1].active=False

print low_model.p_data_action(dind[0], world.possible_actions()[3])
print high_model.p_data_action(dind[0], world.possible_actions()[3])

dind[0].active=True

print low_model.p_data_action(dind[0], world.possible_actions()[3])
print high_model.p_data_action(dind[0], world.possible_actions()[3])


norm=True
lostart=time.clock()
for t in range(12):
	lposc[t]=low_model.p_theory_data(t, dcol, normalized=norm)
	lposs[t]=low_model.p_theory_data(t, dsha, normalized=norm)
	lposi[t]=low_model.p_theory_data(t, dind, normalized=norm)
	

# l=[]
# h=[]
# for i in range(len(dind)):
# 	l.append(low_model.p_data_action(dind[i], world.possible_actions()[0], dind[:-i]))
# 	h.append(high_model.p_data_action(dind[i], world.possible_actions()[0], dind[:-i]))
# 	print l[i], h[i]



lotime=time.clock()-lostart

histart=time.clock()
for ti in range(12):
	t=high_model.Theory(ti)
	#hposc[ti]=high_model.p_theory_data(t, dcol, normalized=norm)
	#hposs[ti]=high_model.p_theory_data(t, dsha, normalized=norm)
	hposi[ti]=high_model.p_theory_data(t, dind, normalized=norm)
	#lpos[t]=low_model.p_data_theory([], t)
	#hpos[t]=high_model.p_data_theory([], t)
	h=high_model.p_data_action(dind[-1], world.possible_actions()[0],dind[:-1])

hitime=time.clock()-histart

print 'newtest h: {0}, l: {1}'.format(h,l)

print 'lotime: {0}, hitime: {1}'.format(lotime,hitime)	

#UNNORM: lotime: 0.019557, hitime: 0.241791
#NORM: lotime: 0.281807, hitime: 3.077572

# print "color_ "
# for t in range(12):
# 	print "t: {0}, low: {1:.3f}, high: {2:.3f}, ratio: {3:.3f}".format(t,lposc[t], hposc[t], lposc[t]/hposc[t])
# print "shape_ "
# for t in range(12):
# 	print "t: {0}, low: {1:.3f}, high: {2:.3f}, ratio: {3:.3f}".format(t,lposs[t], hposs[t], lposs[t]/hposs[t])
# print "indep_ "
# for t in range(12):
# 	print "t: {0}, low: {1:.3f}, high: {2:.3f}, ratio: {3:.3f}".format(t,lposi[t], hposi[t], lposi[t]/hposi[t])



# print "low: {0}, high: {1}".format(sum(lposc), sum(hposc))




