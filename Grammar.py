
import numpy as np
import random
import Hypothesis

COLORS=['red', 'blue', 'green']
SHAPES=['rectangle', 'circle', 'triangle']

class Grammar():

	def __init__(self):
		pass

	def produce_hypothesis(self):
		hypothesis=Hypothesis.Hypothesis()
		n_disj_terms=0

		#set number of disjunctions
		while 1:
			if(np.random.binomial(1,0.5)):
				n_disj_terms+=1
			else:
				break

		#each term a conjunction
		for i in range(n_disj_terms):
			new_conjunction=self.generate_conjunction()
			hypothesis.add_term(new_conjunction)

		#hypothesis.display()
		return hypothesis


	def generate_conjunction(self):
		color_clause=self.instantiate_clause('color', random.choice([0,1,2,3,4]))
		shape_clause=self.instantiate_clause('shape', random.choice([0,1,2,3,4]))
		conjunction=[color_clause, shape_clause]
		return [item for sublist in conjunction for item in sublist] #flatten

	def instantiate_clause(self, clause_variable, clause_type):

		if clause_variable=='color':
			variable_space=[0,1,2]
			variable_value=0
		elif clause_variable=='shape':
			variable_space=[0,1,2]
			variable_value=1

		if clause_type==0:
			var1=random.choice(variable_space)
			var2=random.choice(variable_space)
			return [((variable_value,0),(var1,)),((variable_value,1),(var2,))]
		elif clause_type==1:
			var=random.choice(variable_space)
			return [((variable_value, 0),(var,))]
		elif clause_type==2:
			var=random.choice(variable_space)
			return [((variable_value, 1),(var,))]
		elif clause_type==3:
			return [((variable_value,1),(variable_value,0))]
		elif clause_type==4:
			return [((1,))]		

	# def instantiate_clause(self, clause_variable, clause_type):
	# 	if clause_variable=='color':
	# 		variable_space=COLORS
	# 		variable_name='Color'
	# 	elif clause_variable=='shape':
	# 		variable_space=SHAPES
	# 		variable_name='Shape'

	# 	if clause_type==0:
	# 		var1=random.choice(variable_space)
	# 		var2=random.choice(variable_space)
	# 		return "{0}(o)={1} ^ {0}(m)={2}".format(variable_name, var1, var2)
	# 	elif clause_type==1:
	# 		var=random.choice(variable_space)
	# 		return "{0}(o)={1}".format(variable_name, var)
	# 	elif clause_type==2:
	# 		var=random.choice(variable_space)
	# 		return "{0}(m)={1}".format(variable_name, var)
	# 	elif clause_type==3:
	# 		return "{0}(o)={0}(m)".format(variable_name)
	# 	elif clause_type==4:
	# 		return ""




	# def choose_production(self, symbol):
	# 	if symbol=='S':
	# 		return 'D'
	# 	if symbol=='D':
	# 		return random.choice(['False', True])
	# 	if symbol=='C':
	# 		return 'True'

	# 		