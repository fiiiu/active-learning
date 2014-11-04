
import Datapoint
import csv

class Data():

	def __init__(self):
		self.filename='/Users/alejo/Neuro/ActiveLearning/Data/CPF2_Transcribed110214-2.csv'
		self.data={}

	def read(self, filter=True):
		with open(self.filename, 'r') as datafile:
			filereader = csv.reader(datafile)
			for row in filereader:
				valid_data=[]
				previous_entry=''
				for entry in row[1:]:
					if entry!='' and entry!='::': #the '::' is for one ?wrong entry in the data
						if (filter and entry!=previous_entry) or not filter:
							valid_data.append(self.parse(entry))
					previous_entry=entry
				self.data[row[0]]=valid_data


	def parse(self, entry):
		#replace Orange L by Green Circle.
		#due to counterbalancing, otherwise equivalent. 
		machine_color=entry[0] if entry[0]!='O' else 'G' 
		machine_shape=entry[1] if entry[1]!='L' else 'C'
		toy_color=entry[4] if entry[4]!='O' else 'G'
		toy_shape=entry[5] if entry[1]!='L' else 'C'
		active=entry[6]==1
		return Datapoint.Datapoint(((toy_color,toy_shape),(machine_color, machine_shape)),active)


	def display(self):
		for kid, actions in self.data.iteritems():
			print kid
			for action in actions:
				action.display()


	def get_kids(self):
		return self.data.keys()

	def get_kid_nactions(self, kid):
		return len(self.data[kid])
