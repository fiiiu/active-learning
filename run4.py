

import entropy_gains
import test_data
import high_model
import low_model
import time

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

norm=True
lostart=time.clock()
for t in range(12):
	lposc[t]=low_model.p_theory_data(t, dcol, normalized=norm)
	lposs[t]=low_model.p_theory_data(t, dsha, normalized=norm)
	lposi[t]=low_model.p_theory_data(t, dind, normalized=norm)
	
lotime=time.clock()-lostart

histart=time.clock()
for t in range(12):
	hposc[t]=high_model.p_theory_data(t, dcol, normalized=norm)
	hposs[t]=high_model.p_theory_data(t, dsha, normalized=norm)
	hposi[t]=high_model.p_theory_data(t, dind, normalized=norm)
	#lpos[t]=low_model.p_data_theory([], t)
	#hpos[t]=high_model.p_data_theory([], t)
hitime=time.clock()-histart

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




