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

class Solution():
	## Class of Solution Representation.

	def __init__(self, id, CH, cost, subsets, elements):
		self.id = id
		self.CH = CH
		self.cost = cost # Maybe not needed?
		self.subsets = subsets
		self.elements = elements


	def test_function(self):
		# NOT WORKING! WHY?
		pass

	def getCost(self, subsets):

		cost = 0;

		for subset in self.subsets:
			cost += subsets[subset-1].cost

		# self.cost = cost;
		return cost

		# print "Potential Solution: Swap " + str(removedSubset) + " with " + str(subset) + " (COST " + str(tentativeCost) + ")"

	def getElementsMissing(self, elements):

		missingElementsList = []

		for potentialMissingElement in xrange(1, len(elements)+1):
			if potentialMissingElement not in self.elements:
				missingElementsList.append(potentialMissingElement)

		return missingElementsList


	def validSolution(self, elements):

		missingElementsList = getElementsMissing(elements);

		if len(missingElementsList) is 0:
			return true;
		else:
			return false;



