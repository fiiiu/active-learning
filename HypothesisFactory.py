
import Hypothesis
import parameters

class HypothesisFactory():

	def __init__(self):
		pass

	def create_all_hypotheses(self, machine):
		all_hypotheses=[]
		
		all_hypotheses.append(Hypothesis.Hypothesis(machine, 0))
		
		all_hypotheses.append(Hypothesis.Hypothesis(machine, 1))
		
		for color in range(parameters.n_colors):
			all_hypotheses.append(Hypothesis.Hypothesis(machine, 2, color=color))
		
		for shape in range(parameters.n_shapes):
			all_hypotheses.append(Hypothesis.Hypothesis(machine, 3, shape=shape))
		
		for color in range(parameters.n_colors):
			for shape in range(parameters.n_shapes):
				all_hypotheses.append(Hypothesis.Hypothesis(machine, 4, color=color,\
				 shape=shape))

		for color in range(parameters.n_colors):
			for shape in range(parameters.n_shapes):
				all_hypotheses.append(Hypothesis.Hypothesis(machine, 5, color=color,\
				 shape=shape))

		for color in range(parameters.n_colors):
			for color2 in range(color, parameters.n_colors):
				if color==color2:
					continue
				else:
					all_hypotheses.append(Hypothesis.Hypothesis(machine, 6, color=color,\
				 color2=color2))

		for shape in range(parameters.n_shapes):
			for shape2 in range(shape, parameters.n_shapes):
				if shape==shape2:
					continue
				else:
					all_hypotheses.append(Hypothesis.Hypothesis(machine, 7, shape=shape,\
				 shape2=shape2))

		return all_hypotheses


	def n_hypotheses(self, machine):
		return len(self.create_all_hypotheses(machine))

