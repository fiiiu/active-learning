import numpy as np
import scipy.misc
import itertools
import world
import parameters

epsilon=parameters.epsilon

n_colors=world.n_colors
n_shapes=world.n_shapes
machines=world.machines
n_machines=len(machines)
n_toys=len(world.available_toys)

n_comb_2col=int(round(scipy.misc.comb(world.n_colors,2)))
n_comb_2sha=int(round(scipy.misc.comb(world.n_shapes,2)))

color_pairs=[col for col in itertools.combinations(range(n_colors),2)]
shape_pairs=[sha for sha in itertools.combinations(range(n_shapes),2)]

n_theories=12
n_hypotheses=2+world.n_colors+world.n_shapes+2*world.n_colors*world.n_shapes+\
							n_comb_2col+n_comb_2sha

t_space=range(n_theories)
singleh_space=range(n_hypotheses)

#print n_hypotheses**world.n_machines*n_theories
temp=[singleh_space]*world.n_machines
fullh_space=list(itertools.product(*[singleh_space]*world.n_machines))

th_space=[(t, h) for t in t_space for h in fullh_space]

#hypotheses_produced=False
shypotheses=np.zeros((n_hypotheses,n_colors*n_shapes))


#print len(fullh_space)
#print th_space[314420]



# def p_data_action_old(datapoint, action, prev_data=[]):
# 	"""UNNORMALIZED --INDEPENDENT OF PREV_DATA!!!!!"""
# 	if datapoint in world.possible_data(action):
# 		pda=0
# 		machine=action[1]
# 		for t in t_space:
# 			for h in singleh_space:
# 				pda+=p_singledata_hypothesis(datapoint, h, machine)*\
# 					 p_hypothesis_theory(h,machine,t)*p_theory(t)
# 		return pda
# 	else:
# 		return 0

def p_data_action(datapoint, action, prev_data=[]):
	"""UNNORMALIZED --CHECKED"""
	if datapoint in world.possible_data(action):
		pda=0
		machine=action[1]
		for t in t_space:
			for h in singleh_space:
				pda+=p_singledata_hypothesis(datapoint,h,machine)*\
				 	 p_hypothesis_theorydata(h,machine,t,prev_data)*\
					 p_theory_data(t,prev_data)#, normalized=True) I don't need to normalize, this gives an extra constant				
				 
		return pda
	else:
		return 0


def p_hypothesis_theorydata(h, m, t, d=[]):
	"CHECKED"
	dm=parse_data(d)
	di=dm[machines.index(m)]
	#return p_hypothesis_theory(h,m,t)*p_data_hypothesis(di,h,m)/p_data(di,m)
	return p_hypothesis_theory(h,m,t)*p_data_hypothesis(di,h,m)/p_data_theory_single(di,m,t)

def p_data(d, m):
	"CHECKED"
	p=0
	for t in t_space:
		for h in singleh_space:
			p+=p_data_hypothesis(d,h,m)*p_hypothesis_theory(h,m,t)*p_theory(t)
	return p


def parse_data(d):
	"CHECKED" 
	dm=[[],[],[]]
	for dp in d:
		dm[machines.index(dp.machine)].append(dp)
	return dm


# def p_hypothesis_data(h, m, d=[]):
# 	return p_data_hypothesis(d,h,m)*p_hypothesis(h,m)#/norm

def p_hypotheses_data(hs, d=[]):
	"CHECKED --UNNORMALIZED"
	prob=0
	dm=parse_data(d)
	for t in t_space:
		lik=1
		for i,h in enumerate(hs):
			m=world.machines[i]
			lik*=p_data_hypothesis(dm[i],h,m)*p_hypothesis_theory(h,m,t)
		prob+=lik*p_theory(t)
	return prob

# def p_hypothesis(h,m):
# 	prob=0
# 	for t in t_space:
# 		prob+=p_hypothesis_theory(h,m,t)*p_theory(t)
# 	return prob

def p_theoryhypothesis_data(t, hs, d=[]):
	"CHECKED --UNNORMALIZED"
	prob=1
	dm=parse_data(d)
	for i,h in enumerate(hs):
		m=world.machines[i]
		prob*=p_data_hypothesis(dm[i],h,m)*p_hypothesis_theory(h,m,t)
	prob*=p_theory(t)
	return prob

def p_theory_data(t, d=[], normalized=False):
	"""CHECKED""" 
	if normalized:#this could be a tad more efficient, without recomputing t
		norm=sum([p_data_theory(d,tt)*p_theory(tt) for tt in t_space])
		return p_data_theory(d,t)*p_theory(t)/norm
	else:
		return p_data_theory(d,t)*p_theory(t)


def p_theory(t): #flat prior: argument ignored
	"CHECKED"
	return 1.0/n_theories


# def p_data_theory_old(d, t):
# 	"""UNNORMALIZED"""
# 	lik=1
# 	for m in machines:
# 		hyp_lik=0
# 		for h in singleh_space:			
# 			hyp_lik+=p_data_hypothesis(d, h, m)*p_hypothesis_theory(h, m, t)
# 		lik*=hyp_lik
# 	return lik

def p_data_theory_single(d, m, t):
	"""for single machine"""
	prob=0
	for h in singleh_space:
		prob+=p_data_hypothesis(d,h,m)*p_hypothesis_theory(h,m,t)
	return prob


def p_data_theory(d, t):
	"""UNNORMALIZED --CHECKED"""
	lik=1
	#parse data in machines
	dm=parse_data(d)
	#go
	for i,m in enumerate(machines):
		hyp_lik=0
		for h in singleh_space:			
			hyp_lik+=p_data_hypothesis(dm[i], h, m)*p_hypothesis_theory(h, m, t)
		lik*=hyp_lik
	return lik


def p_data_hypothesis(data, h, m):
	"""UNNORMALIZED --CHECKED, MUST USE DATA FROM THIS MACHINE!"""
	lik=1	
	for datapoint in data:
		lik*=p_singledata_hypothesis(datapoint, h, m)
	return lik


def p_singledata_hypothesis(datapoint, h, m):
	"""UNNORMALIZED --CAREFUL. THIS WORKS FOR SAME MACHINE, NOT FOR DIFFERENT!!"""
	if m != datapoint.machine:
		#import pdb; pdb.set_trace()
		print "--CAREFUL. THIS WORKS FOR SAME MACHINE, NOT FOR DIFFERENT!!"
		datapoint.display()
		print h, m
		return 371#./15#n_toys/n_machines/2
	else:
		if (datapoint.active and \
		   shypotheses[h][n_colors*datapoint.toy_shape+datapoint.toy_color]==1) or\
		   (not datapoint.active and\
		   shypotheses[h][n_colors*datapoint.toy_shape+datapoint.toy_color]==0):
			return 1#./15#n_(1-epsilon)/n_toys/n_machines/2
		
		# if (datapoint.active and \
		#    produce_hypothesis(h)[n_colors*datapoint.toy_shape+datapoint.toy_color]==1) or\
		#    (not datapoint.active and\
		#    produce_hypothesis(h)[n_colors*datapoint.toy_shape+datapoint.toy_color]==0):
		# 	return 1#./15#n_(1-epsilon)/n_toys/n_machines/2
		else:
			return epsilon#0#epsilon/n_toys/n_machines/2



def produce_all_hypotheses():
	#if not hypothesis_produced:
	for i,h in enumerate(singleh_space):
		shypotheses[i]=produce_hypothesis(h)
	#hypothesis_produced=True


def produce_hypothesis(h):
	"""CHECKED"""
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
		 2+n_colors+n_shapes+2*n_colors*n_shapes+n_comb_2col:
		 #color OR color2
		offset=2+n_colors+n_shapes+2*n_colors*n_shapes
		color, color2=color_pairs[h-offset]
		for j in range(n_shapes):
			hyp[j*n_colors+color]=1
			hyp[j*n_colors+color2]=1 
	elif 2+n_colors+n_shapes+2*n_colors*n_shapes+n_comb_2col <= h < \
		 2+n_colors+n_shapes+2*n_colors*n_shapes+n_comb_2col+n_comb_2sha:
		 #shape OR shape2
		offset=2+n_colors+n_shapes+2*n_colors*n_shapes+n_comb_2col
		shape, shape2=shape_pairs[h-offset]
		for i in range(n_colors):
			hyp[n_colors*shape+i]=1
			hyp[n_colors*shape2+i]=1

	return hyp





def p_hypothesis_theory(h, m, t):
	"""CHECKED"""
	if t==0:
		return float(h==0)
	
	elif t==1:
		return float(h==1)

	elif t==2: #color match
		if 0 <= h-2 < n_colors: # 2 <= h < 2+n_colors
			return float(h-t == m[0])
		else:
			return 0
	
	elif t==3: #shape match
		if 0 <= h-2-n_colors < n_shapes:
			return float(h-2-n_colors == m[1])
		else:
			return 0

	elif t==4: #color AND shape match
		if 0 <= h-2-n_colors-n_shapes < n_colors*n_shapes:
			offset=2+n_colors+n_shapes
			color=(h-offset) % n_colors
			shape=(h-offset) / n_colors
			return float(color==m[0] and shape==m[1])
		else:
			return 0

	elif t==5: #color OR shape match
		if 0 <= h-2-n_colors-n_shapes-n_colors*n_shapes < n_colors*n_shapes:
			offset=2+n_colors+n_shapes+n_colors*n_shapes
			color=(h-offset) % n_colors
			shape=(h-offset) / n_colors
			return float(color==m[0] and shape==m[1])
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
		if 0 <= h-2 < n_colors: #direct color hypotheses
			return float(h-2 != m[0])/(n_colors-1)
		elif 2+n_colors+n_shapes+2*n_colors*n_shapes <= h <\
			 2+n_colors+n_shapes+2*n_colors*n_shapes+n_comb_2col:
			 #two color hypotheses
			offset=2+n_colors+n_shapes+2*n_colors*n_shapes
			color, color2=color_pairs[h-offset]
			return float(color!=m[0] and color2!=m[0])/\
					(n_comb_2col-(n_colors-1))
		else:
			return 0

	elif t==10: #NOT match shape
		if 0 <= h-2-n_colors < n_shapes: 
			return float(h-2-n_colors != m[1])/(n_shapes-1)
		elif 2+n_colors+n_shapes+2*n_colors*n_shapes+n_comb_2col\
			 <= h <\
			 2+n_colors+n_shapes+2*n_colors*n_shapes+n_comb_2col+\
			 +n_comb_2sha:
			 #two color hypotheses
			offset=2+n_colors+n_shapes+2*n_colors*n_shapes+n_comb_2col
			shape, shape2=shape_pairs[h-offset]
			return float(shape!=m[1] and shape2!=m[1])/\
					(n_comb_2sha-(n_shapes-1))
		else:
			return 0

	elif t==11: #INDEPENDENT
		return 1./n_hypotheses





produce_all_hypotheses()



