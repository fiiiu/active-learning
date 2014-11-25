
import Datapoint

# colors=['red', 'green', 'blue']
# shapes=['rectangle', 'circle', 'triangle']


#machines=[(2,0), (1,1), (0,2)]
# machines=[('blue', 'rectangle'), ('green', 'circle'), ('red', 'triangle')]
# available_toys=[('blue', 'circle'), ('red', 'rectangle'), ('green', 'triangle')]

#small world
# colors=['green', 'blue']
# shapes=['rectangle', 'circle']
# machines=[('blue', 'rectangle'), ('green', 'circle')]
# available_toys=[()]

colors=['G', 'B', 'R']
shapes=['R', 'T', 'C']
machines=[('B', 'R'), ('G', 'C'), ('R', 'T')]
available_toys=[('B', 'C'), ('R', 'R'), ('G', 'T')]

colors=[0,1,2]
shapes=[0,1,2]
machines=[(2,0), (1,1), (0,2)]
available_toys=[(2,1), (0,0), (1,2)]

phase2a_toys=[(2,2),(1,0),(0,1)]

phase2b_toys=[(5,4),(3,3),(4,5)]
phase2b_machines=[(5,3),(4,4),(3,5)]


n_colors=len(colors)
n_shapes=len(shapes)
n_machines=len(machines)

# #unrunnable:
# colors=[0,1,2,3,4,5]
# shapes=[0,1,2,3,4,5]
# n_colors=len(colors)
# n_shapes=len(shapes)
# machines=[(2,0), (1,1), (0,2), (5,3), (4,4), (3,5)]
# n_machines=len(machines)

def possible_data(action):
	return [Datapoint.Datapoint(action, False), Datapoint.Datapoint(action, True)]

def possible_actions():
	return [(t,m) for t in available_toys for m in machines]

def possible_actions_phase2a():
	return [(t,m) for t in phase2a_toys for m in machines]	

def possible_actions_phase2b():
	return [(t,m) for t in phase2b_toys for m in phase2b_machines]	


def make_action(action, condition):
	if condition=='C':
		return Datapoint.Datapoint(action, action[0][0]==action[1][0])
	elif condition=='S':
		return Datapoint.Datapoint(action, action[0][1]==action[1][1])

def make_forced_action(action, result):
	return Datapoint.Datapoint(action, result)


def translate_clause(clause):
	if len(clause)==1:
		return "true"
	elif len(clause[1])==1:
		prop=translate_property(clause[0][0])
		obj=translate_object(clause[0][1])
		val=translate_value(clause[0][0], clause[1][0])
		return "{0}({1})={2}".format(prop, obj, val)
	elif len(clause[1])==2:
		prop1=translate_property(clause[0][0])
		prop2=translate_property(clause[1][0])
		obj1=translate_object(clause[0][1])
		obj2=translate_object(clause[1][1])
		return "{0}({1})={2}({3})".format(prop1, obj1, prop2, obj2)


def translate_property(prop):
	if prop==0:
		return "color"
	elif prop==1:
		return "shape"

def translate_object(obj):
	if obj==0:
		return "toy"
	elif obj==1:
		return "machine"

def translate_value(prop, val):
	if prop==0:
		return colors[val]
	elif prop==1:
		return shapes[val]

