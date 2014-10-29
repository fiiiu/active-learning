

colors=['red', 'blue', 'green']
shapes=['rectangle', 'circle', 'triangle']

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

