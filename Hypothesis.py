
import world

class Hypothesis():

	def __init__(self):
		self.hypothesis=[]

	def add_term(self, term):
		self.hypothesis.append(term)

	def display(self):
		hypstrings=[]
		for disj_term in self.hypothesis:
			print disj_term
			hypstrings.append("(" +  " ^ ".join(map(world.translate_clause, disj_term)) + ")")

		# for i, disjTerm in enumerate(self.hypothesis):
		# 	hypstrings.append(world.translate_clause(clause))
		#  	hypstrings.append("(" +  " ^ ".join(disjTerm) + ")")

		print " v ".join(hypstrings)

		#print self.hypothesis


	def single_likelihood(self, data):
		disjlik=0
		for conjunction in self.hypothesis:
			conjlik=1
			for clause in conjunction:
				clauselik=0
				if len(clause)==1:
					clauselik=1
				else:
					if len(clause[1])==2:
						if data[clause[1][0]]==data[2+clause[1][0]] and data[4]==1:
							clauselik=1
						elif data[clause[1][0]]!=data[2+clause[1][0]] and data[4]==0:
							clauselik=1

					elif len(clause[1])==1:
						if data[clause[0][0]+2*clause[0][1]]==clause[1][0] and data[4]==1:
							clauselik=1
						elif data[clause[0][0]+2*clause[0][1]]!=clause[1][0] and data[4]==0:
							clauselik=1

				if clauselik==0:
					conjlik=0
					break
				#conjlik=1

			if conjlik==1:
				disjlik=1
				break

		return disjlik


	def likelihood(self, data):
		lik=1
		for d in data:
			lik*=single_likelihood(d)
		return lik


	# def translate_clause(self, clause):
	# 	if len(clause)==1:
	# 		return "true"
	# 	elif len(clause[1])==1:
	# 		prop=self.translate_property(clause[0][0])
	# 		obj=self.translate_object(clause[0][1])
	# 		val=self.translate_value(clause[0][0], clause[1][0])
	# 		return "{0}({1})={2}".format(prop, obj, val)


	# def translate_property(self, prop):
	# 	if prop==0:
	# 		return "color"
	# 	elif prop==1:
	# 		return "shape"

	# def translate_object(self, obj):
	# 	if obj==0:
	# 		return "toy"
	# 	elif obj==1:
	# 		return "machine"

	# def translate_value(self, prop, val):
	# 	if prop==0:
	# 		return self.colors[val]
	# 	elif prop==1
	# 		return self.shapes[val]



			