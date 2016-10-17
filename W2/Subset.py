#####################################
##                                 ##
##  Heuristics and Metaheuristics  ##
##        PDEEC 2016 / 2017        ##
##              Week 2             ##
##                                 ##
#####################################

#############
## CLASSES ##
#############

class Subset():
	## Class of Subsets.

	def __init__(self, id, cost):
		self.id = id
		self.cost = cost
		self.elements = []

	# Returns the weight as the cost / #elements
	def weight(self):

		if len(self.elements) > 0:
			weight = float(self.cost) / len(self.elements) 
		else:
			weight = None

		return weight

	def test_function(self):
		# NOT WORKING! WHY?
		pass
