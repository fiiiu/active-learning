
import scipy.misc
import itertools
import world

epsilon=1e-3

n_colors=world.n_colors
n_shapes=world.n_shapes
machines=world.machines


n_theories=12
n_hypotheses=2+world.n_colors+world.n_shapes+2*world.n_colors*world.n_shapes+\
							int(scipy.misc.comb(world.n_colors,2))+\
							int(scipy.misc.comb(world.n_shapes,2))

t_space=range(n_theories)
singleh_space=range(n_hypotheses)

temp=[singleh_space]*world.n_machines
fullh_space=list(itertools.product(*[singleh_space]*world.n_machines))

th_space=[(t, h) for t in t_space for h in fullh_space]

print len(fullh_space)
print th_space[314420]


def p_theory_data(t, d=None):
	if d is None:
		return p_theory(t)
	else:
		return p_data_theory(d, t)*p_theory(t)

def p_theory(t): #flat prior: argument ignored
	return 1.0/n_theories


def p_data_theory(d, t):
	lik=1
	for m in machines:
		hyp_lik=0
		for h in singleh_space:
			hyp_lik+=p_data_hypothesis(d, h, m)*p_hypothesis_theory(h, m, t)
		lik*=hyp_lik
	return lik


def p_data_hypothesis(data, h, m):
	lik=1	
	for datapoint in data:
		lik*=p_singledata_hypothesis(datapoint, h, m)
	return lik

def p_singledata_hypothesis(datapoint, h, m):
	if m != datapoint.machine:
		return 1
	else:
		if (datapoint.active and \
		   produce_hypothesis(h)[n_colors*datapoint.toy_shape+datapoint.toy_color]==1) or\
		   (not datapoint.active and\
		   produce_hypothesis(h)[n_colors*datapoint.toy_shape+datapoint.toy_color]==0):
			return 1
		else:
			return epsilon 


def produce_hypothesis(h):
	hyp=[0]*n_colors*n_shapes
	if h==1: #any
		hyp=[1]*n_colors*n_shapes
	elif 2 <= h < 2+n_colors: #color fixed
		color=h-2
		for j in range(n_shapes):
			hyp[j*n_colors+color]=1
	elif 2+n_colors <= h < 2+n_colors+n_shapes: #specific shape
		shape=h-2-n_colors
		for i in range(n_colors):
			hyp[n_colors*shape+i]=1
	elif 2+n_colors+n_shapes <= h < 2+n_colors+n_shapes+n_colors*n_shapes: #specific both
		color=(h-2-n_colors-n_shapes) % n_colors
		shape=(h-2-n_colors-n_shapes) / n_colors
		hyp[n_colors*shape+color]=1
	elif 2+n_colors+n_shapes+n_colors*n_shapes <= h < \
		 2+n_colors+n_shapes+2*n_colors*n_shapes:
		#either color or shape
		offset=2+n_colors+n_shapes+n_colors*n_shapes
		color=(h-offset) % n_colors
		shape=(h-offset) / n_colors
		for j in range(n_shapes):
			hyp[j*n_colors+color]=1
		for i in range(n_colors):
			hyp[n_colors*shape+i]=1
	elif 2+n_colors+n_shapes+2*n_colors*n_shapes <= h < \
		 2+n_colors+n_shapes+2*n_colors*n_shapes+int(scipy.misc.comb(n_colors,2)):
		 #color OR color2
		offset=2+n_colors+n_shapes+2*n_colors*n_shapes
		color, color2=[i for i in itertools.combinations(range(n_colors),2)][h-offset]
		for j in range(n_shapes):
			hyp[j*n_colors+color]=1
			hyp[j*n_colors+color2]=1 
	elif 2+n_colors+n_shapes+2*n_colors*n_shapes+int(scipy.misc.comb(n_colors,2)) <= h < \
		 2+n_colors+n_shapes+2*n_colors*n_shapes+int(scipy.misc.comb(n_colors,2))+int(scipy.misc.comb(n_shapes,2)):
		 #shape OR shape2
		offset=2+n_colors+n_shapes+2*n_colors*n_shapes+int(scipy.misc.comb(n_colors,2))
		shape, shape2=[i for i in itertools.combinations(range(n_shapes),2)][h-offset]
		for i in range(n_colors):
			hyp[n_colors*shape+i]=1
			hyp[n_colors*shape2+i]=1

	return hyp





def p_hypothesis_theory(h, m, t):
	if t==0:
		return int(h==0)
	
	elif t==1:
		return int(h==1)

	elif t==2: #color match
		if 0 <= h-2 < n_colors: # 2 <= h < 2+n_colors
			return int(h-t == m[0])
		else:
			return 0
	
	elif t==3: #shape match
		if 0 <= h-2-n_colors < n_shapes:
			return int(h-2-n_colors == m[1])
		else:
			return 0

	elif t==4: #color AND shape match
		if 0 <= h-2-n_colors-n_shapes < n_colors*n_shapes:
			offset=2+n_colors+n_shapes
			color=(h-offset) % n_colors
			shape=(h-offset) / n_colors
			return int(color==m[0] and shape==m[1])
		else:
			return 0

	elif t==5: #color OR shape match
		if 0 <= h-2-n_colors-n_shapes-n_colors*n_shapes < n_colors*n_shapes:
			offset=2+n_colors+n_shapes+n_colors*n_shapes
			color=(h-offset) % n_colors
			shape=(h-offset) / n_colors
			return int(color==m[0] or shape==m[1])
		else:
			return 0

	elif t==6: #specific color (ANY color)
		if 0 <= h-2 < n_colors:
			return 1./n_colors
		else:
			return 0

	elif t==7: #specific shape (ANY shape)
		if 0 <= h-2-n_colors < n_shapes:
			return 1./n_shapes
		else:
			return 0

	elif t==8: #specific shape AND color (ANY)
		if 0 <= h-2-n_colors-n_shapes < n_colors*n_shapes: #kind 4
			return 1./(n_shapes*n_colors)
			# offset=2+n_colors+n_shapes
			# color=(h-offset) % n_colors
			# shape=(h-offset) / n_colors
			# return int(color==m[0] and shape==m[1])
		else:
			return 0

	elif t==9: #NOT match color
		if 0 <= h-2 < n_colors: 
			return float(h-2 != m[0])/(n_colors-1)
		else:
			return 0

	elif t==10: #NOT match shape
		if 0 <= h-2-n_colors < n_shapes: 
			return float(h-2-n_colors != m[1])/(n_shapes-1)
		else:
			return 0

	elif t==11: #INDEPENDENT
		return 1./n_hypotheses
