

import entropy_gains
import test_data
import high_model
import low_model

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

for t in range(12):
	lposc[t]=low_model.p_theory_data(t, dcol, normalized=True)
	hposc[t]=high_model.p_theory_data(t, dcol, normalized=True)

	lposs[t]=low_model.p_theory_data(t, dsha, normalized=True)
	hposs[t]=high_model.p_theory_data(t, dsha, normalized=True)

	lposi[t]=low_model.p_theory_data(t, dind, normalized=True)
	hposi[t]=high_model.p_theory_data(t, dind, normalized=True)
	#lpos[t]=low_model.p_data_theory([], t)
	#hpos[t]=high_model.p_data_theory([], t)
	
print "color_ "
for t in range(12):
	print "t: {0}, low: {1:.3f}, high: {2:.3f}, ratio: {3:.3f}".format(t,lposc[t], hposc[t], lposc[t]/hposc[t])
print "shape_ "
for t in range(12):
	print "t: {0}, low: {1:.3f}, high: {2:.3f}, ratio: {3:.3f}".format(t,lposs[t], hposs[t], lposs[t]/hposs[t])
print "indep_ "
for t in range(12):
	print "t: {0}, low: {1:.3f}, high: {2:.3f}, ratio: {3:.3f}".format(t,lposi[t], hposi[t], lposi[t]/hposi[t])



print "low: {0}, high: {1}".format(sum(lposc), sum(hposc))




