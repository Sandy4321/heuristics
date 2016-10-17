#####################################
##                                 ##
##  Heuristics and Metaheuristics  ##
##        PDEEC 2016 / 2017        ##
##              Week 2             ##
##                                 ##
#####################################

#############
## IMPORTS ##
#############

from Element import Element
from Subset import Subset

######################
## GLOBAL VARIABLES ##
######################

subsets = [];
elements = [];
# totalCost = 0;
# subsetsCosts = [];
# elements_in_subsets = [];
# chosen_subsets = [];

###############
## FUNCTIONS ##
###############

# Reads a file in a given directory and creates a list.
def read_file(directory, file):
	
	path = str(directory) + "/" + str(file)

	f = open(path, "r");
	x = f.read().strip().split();

	return x;


# Makes an analysis on the list of input data.
def list_analysis(inputList):

	n_elements = int(inputList.pop(0));
	n_subsets = int(inputList.pop(0));

	print "Number of Elements: " + str(n_elements);
	print "Number of Subsets: " + str(n_subsets);

	# Construction of Subset list:
	global subsets

	for i in xrange(0,n_subsets):
		subset = Subset(i+1, int(inputList.pop(0)));
		subsets.append(subset);

	# Construction of Element list:
	global elements

	nElements = 0;

	while inputList:

		element = Element(nElements+1)

		nSubsets = int(inputList.pop(0))

		for i in xrange(0, nSubsets):
			element.subsets.append(int(inputList.pop(0)))

		elements.append(element)

		nElements += 1;

	# Computes which elements are inside each subset
	for element in elements:
		for subset in element.subsets:
			subsets[subset-1].elements.append(element.id);


# Print Information about Subsets and Elements to the console 
def information_print():

	global subsets
	global elements

	for subset in subsets:
		print "Subset #" + str(subset.id) + " with cost " + str(subset.cost) + " contains " + str(len(subset.elements)) + " Elements: " + str(subset.elements)

	for element in elements:
		print "Element #" + str(element.id) + " contained in " + str(len(element.subsets)) + " Subsets"


# First Heuristic to choose a set of subsets that composes all elements.
# The criteria is to select first the elements with lowest cost. 
def heuristic_1():

	global elements;
	global elements_in_subsets;
	global subsetsCosts;
	global subsets;
	missingElementsList = [];
	chosenElementsList = [];
	chosenSubsetsList = [];

	iteration = 1;

	# Costructs the list of elements still to choose
	for elementId, elementCost in enumerate(elements):
		missingElementsList.append(int(elementId+1))

	# Iterates until there is no element left
	while  missingElementsList:
		

		currentElement = missingElementsList.pop(0);
		chosenElementsList.append(int(currentElement));

		# print " -------------- ITERATION " + str(iteration) + " -------------- "
		# print "Iteration Element: " + str(currentElement)


		# Checks in which subsets the element can be found

		candidateSubsets = elements_in_subsets[currentElement-1];
		candidateSubsetsCosts = [];

		# print "Subsets in which Element is found:  " + str(candidateSubsets);


		# Selects the subset with the lowest cost 

		for subset in candidateSubsets:
			candidateSubsetsCosts.append(subsetsCosts[subset])

		# print "Cost of the Canidate Subsets found: " + str(candidateSubsetsCosts);


		# Gets the subset with the minimum cost
		val, idx = min((val, idx) for (idx, val) in enumerate(candidateSubsetsCosts))
		chosenSubset = int(candidateSubsets[idx]);

		# print "Selected Subset with Minimum Cost:  " + str(chosenSubset)


		# Adds the lowest cost subset to the list of chosen subsets
		chosenSubsetsList.append(chosenSubset);

		# Removes all elements contained in the chosen subset from the missing elements list (as they were already chosen)
		for element in subsets[chosenSubset]:
			if int(element) in missingElementsList:
				missingElementsList.remove(int(element));
				chosenElementsList.append(int(element));

			# pass

		# print subsets[chosenSubset];

		# print missingElementsList
		# print chosenElementsList

		# print "Number of Elements already chosen:  " + str(len(chosenElementsList));
		# print "Number of Elements still missing:   " + str(len(missingElementsList));

		
		iteration += 1;

	print " ============ HEURISTIC 1 ================ "	
	print "Number of Subsets chosen: " + str(len(chosenSubsetsList));

	print "Chosen Subsets: "
	chosenSubsetsListOrdered = [int(x) for x in chosenSubsetsList]
	chosenSubsetsListOrdered.sort()
	print chosenSubsetsListOrdered


	# Computes the Final Cost of the Heuristic
	heuristicCost = 0;

	for chosenSubset in chosenSubsetsList:
		heuristicCost += subsetsCosts[int(chosenSubset)]

	print "Cost: " + str(heuristicCost)

# Second Heuristic to choose a set of subsets that composes all elements.
# The criteria is to first select subsets that have unique elements. A second stage selects all the remainder 
# elements chosing first the element with the lowest cost. 
def heuristic_2():

	global elements;
	global elements_in_subsets;
	global subsetsCosts;
	global subsets;
	missingElementsList = [];
	chosenElementsList = [];
	chosenSubsetsList = [];


	# Costructs the list of elements still to choose
	for elementId, elementCost in enumerate(elements):
		missingElementsList.append(int(elementId+1))


	# Tests if there are elements that are only in one subset (and therefore must be chosen)
	for element, listSubsets in enumerate(elements_in_subsets):
		
		if len(listSubsets) == 1:

			subset = int(listSubsets[0])

			# print "Unique Element " + str(element+1) + " in Subset " + str(subset);

			chosenSubsetsList.append(subset);

			for el in subsets[subset]:
				if int(el) in missingElementsList:
					missingElementsList.remove(int(el));
					chosenElementsList.append(int(el));


	# print "Number of Elements already chosen:  " + str(len(chosenElementsList));
	# print "Number of Elements still missing:   " + str(len(missingElementsList));

	# print "Number of Subsets chosen: " + str(len(chosenSubsetsList));

	# print "Chosen Subsets: "
	chosenSubsetsListOrdered = [int(x) for x in chosenSubsetsList]
	chosenSubsetsListOrdered.sort()
	# print chosenSubsetsListOrdered


	iteration = 1;

	# Iterates until there is no element left
	while  missingElementsList:
		

		currentElement = missingElementsList.pop(0);
		chosenElementsList.append(int(currentElement));

		# print " -------------- ITERATION " + str(iteration) + " -------------- "
		# print "Iteration Element: " + str(currentElement)


		# Checks in which subsets the element can be found

		candidateSubsets = elements_in_subsets[currentElement-1];
		candidateSubsetsCosts = [];

		# print "Subsets in which Element is found:  " + str(candidateSubsets);


		# Selects the subset with the lowest cost 

		for subset in candidateSubsets:
			candidateSubsetsCosts.append(subsetsCosts[subset])

		# print "Cost of the Canidate Subsets found: " + str(candidateSubsetsCosts);


		# Gets the subset with the minimum cost
		val, idx = min((val, idx) for (idx, val) in enumerate(candidateSubsetsCosts))
		chosenSubset = int(candidateSubsets[idx]);

		# print "Selected Subset with Minimum Cost:  " + str(chosenSubset)


		# Adds the lowest cost subset to the list of chosen subsets
		chosenSubsetsList.append(chosenSubset);

		# Removes all elements contained in the chosen subset from the missing elements list (as they were already chosen)
		for element in subsets[chosenSubset]:
			if int(element) in missingElementsList:
				missingElementsList.remove(int(element));
				chosenElementsList.append(int(element));

			# pass

		# print subsets[chosenSubset];

		# print missingElementsList
		# print chosenElementsList

		# print "Number of Elements already chosen:  " + str(len(chosenElementsList));
		# print "Number of Elements still missing:   " + str(len(missingElementsList));

		
		iteration += 1;


	print " ============ HEURISTIC 2 ================ "	
	print "Number of Subsets chosen: " + str(len(chosenSubsetsList));

	print "Chosen Subsets: "
	chosenSubsetsListOrdered = [int(x) for x in chosenSubsetsList]
	chosenSubsetsListOrdered.sort()
	print chosenSubsetsListOrdered


	# Computes the Final Cost of the Heuristic
	heuristicCost = 0;

	for chosenSubset in chosenSubsetsList:
		heuristicCost += subsetsCosts[int(chosenSubset)]

	print "Cost: " + str(heuristicCost)

# Third Heuristic to choose a set of subsets that composes all elements.
def heuristic_3():
	pass

##########
## MAIN ##
##########

if __name__ == "__main__":

	directory = "SCP-Instances"
	file = "scp42.txt"

	print "###################################################################################"
	print "File: " + directory + "/" + file

	inputList = read_file(directory, file);

	list_analysis(inputList);

	information_print();

	# subsets_costs();

	# elements_in_subsets();

	# heuristic_1();

	# heuristic_2();

	# heuristic_3();

