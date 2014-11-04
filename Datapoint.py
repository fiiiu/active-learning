
class Datapoint():

	def __init__(self, action, active):
		
		self.action=action

		self.toy=self.action[0]
		self.machine=self.action[1]

		self.machine_color=self.machine[0]
		self.machine_shape=self.machine[1]
		
		self.toy_color=self.toy[0]
		self.toy_shape=self.toy[1]

		self.active=active


	def __eq__(self, other):
		if isinstance(other, Datapoint):
			return self.toy==other.toy and self.machine==other.machine and self.active==other.active
		else:
			return NotImplemented


	def display(self):
		print "toy: {0}, machine: {1}, active: {2}".format(self.toy, self.machine, self.active)

		