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

	def test_function(self):
		# NOT WORKING! WHY?
		pass
