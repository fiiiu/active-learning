
import parameters

class Datapoint():

	def __init__(self, machine, toy_color, toy_shape, active):
		self.machine_color=machine[0]
		self.machine_shape=machine[1]
		self.machine=machine
		self.toy_color=toy_color
		self.toy_shape=toy_shape
		self.active=active
