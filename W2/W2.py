#####################################
##                                 ##
##  Heuristics and Metaheuristics  ##
##        PDEEC 2016 / 2017        ##
##              Week 2             ##
##                                 ##
#####################################

######################
## GLOBAL VARIABLES ##
######################

elements = [];
subsets = [];
totalCost = 0;
subsetsCosts = [];
elements_in_subsets = [];
chosen_subsets = [];

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

	n_subsets = int(inputList.pop(0));
	n_elements = int(inputList.pop(0));

	print "Number of Subsets: " + str(n_subsets);
	print "Number of Elements: " + str(n_elements);


	# Cost of each Element:
	global elements

	for idx in xrange(0,n_elements):
		elements.append(inputList.pop(0))


	# Computes the Total Cost:
	global totalCost

	for cost in elements:
		totalCost += int(cost);


	# List of Subsets:
	global subsets

	while inputList :

		subset = []
		n_elementsInSubset = int(inputList.pop(0))
		
		for idx in xrange(0,n_elementsInSubset):
			subset.append(inputList.pop(0))
		
		subsets.append(subset)

# Computes the cost of each subset
def subsets_costs():

	global subsetsCosts;

	# Iterate each subset
	for subset in subsets:
		subsetCost = 0;

		for element in subset:
			
			subsetCost += int(elements[int(element)-1]);

		subsetsCosts.append(subsetCost);

	# # Print Information to the Screen
	# for idx, subsetCost in enumerate(subsetsCosts):
	# 	print "Cost of Subset " + str(idx) + ": " + str(subsetCost);

# Computes the subsets in which each element is found
def elements_in_subsets():

	global elements_in_subsets;

	# Constructs the elements_in_subsets with the appropriate size
	elements_in_subsets = [ [None] ] * len(elements);


	# Iterate each subset in search of elements 
	for idx, subset in enumerate(subsets):

		for element in subset:
		
			# Tests if the element has already been found in a subset
			if elements_in_subsets[int(element)-1] == [None]:
				elements_in_subsets[int(element)-1] = [idx];
		
			else:
				elements_in_subsets[int(element)-1].append(idx);

	# # Print Information to the Screen
	# for elemenet, listSubsets in enumerate(elements_in_subsets):
	# 	print "Element " + str(elemenet+1) + " appears in " + str(len(listSubsets)) + " subsets: " + str(listSubsets)


# First Heuristic to choose a set of subsets that composes all elements
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

		print " -------------- ITERATION " + str(iteration) + " -------------- "
		print "Iteration Element: " + str(currentElement)


		# Checks in which subsets the element can be found

		candidateSubsets = elements_in_subsets[currentElement-1];
		candidateSubsetsCosts = [];

		print "Subsets in which Element is found:  " + str(candidateSubsets);


		# Selects the subset with the lowest cost 

		for subset in candidateSubsets:
			candidateSubsetsCosts.append(subsetsCosts[subset])

		print "Cost of the Canidate Subsets found: " + str(candidateSubsetsCosts);


		# Gets the subset with the minimum cost
		val, idx = min((val, idx) for (idx, val) in enumerate(candidateSubsetsCosts))
		chosenSubset = int(candidateSubsets[idx]);

		print "Selected Subset with Minimum Cost:  " + str(chosenSubset)


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

		print "Number of Elements already chosen:  " + str(len(chosenElementsList));
		print "Number of Elements still missing:   " + str(len(missingElementsList));

		
		iteration += 1;

	print " ========================================= "
	print "Number of Subsets chosen: " + str(len(chosenSubsetsList));

	print "Chosen Subsets: "
	chosenSubsetsListOrdered = [int(x) for x in chosenSubsetsList]
	chosenSubsetsListOrdered.sort()
	print chosenSubsetsListOrdered


	# Computes the Final Cost of the Heuristic
	heuristicCost = 0;

	for chosenSubset in chosenSubsetsList:
		heuristicCost += subsetsCosts[int(chosenSubset)]

	print "Final Heuristic cost: " + str(heuristicCost-totalCost) + " ( " + str(heuristicCost) + " - " + str(totalCost) + " )"

# Second Heuristic to choose a set of subsets that composes all ements
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


	print "Number of Elements already chosen:  " + str(len(chosenElementsList));
	print "Number of Elements still missing:   " + str(len(missingElementsList));

	print "Number of Subsets chosen: " + str(len(chosenSubsetsList));

	print "Chosen Subsets: "
	chosenSubsetsListOrdered = [int(x) for x in chosenSubsetsList]
	chosenSubsetsListOrdered.sort()
	print chosenSubsetsListOrdered


	iteration = 1;

	# Iterates until there is no element left
	while  missingElementsList:
		

		currentElement = missingElementsList.pop(0);
		chosenElementsList.append(int(currentElement));

		print " -------------- ITERATION " + str(iteration) + " -------------- "
		print "Iteration Element: " + str(currentElement)


		# Checks in which subsets the element can be found

		candidateSubsets = elements_in_subsets[currentElement-1];
		candidateSubsetsCosts = [];

		print "Subsets in which Element is found:  " + str(candidateSubsets);


		# Selects the subset with the lowest cost 

		for subset in candidateSubsets:
			candidateSubsetsCosts.append(subsetsCosts[subset])

		print "Cost of the Canidate Subsets found: " + str(candidateSubsetsCosts);


		# Gets the subset with the minimum cost
		val, idx = min((val, idx) for (idx, val) in enumerate(candidateSubsetsCosts))
		chosenSubset = int(candidateSubsets[idx]);

		print "Selected Subset with Minimum Cost:  " + str(chosenSubset)


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

		print "Number of Elements already chosen:  " + str(len(chosenElementsList));
		print "Number of Elements still missing:   " + str(len(missingElementsList));

		
		iteration += 1;

	print " ========================================= "
	print "Number of Subsets chosen: " + str(len(chosenSubsetsList));

	print "Chosen Subsets: "
	chosenSubsetsListOrdered = [int(x) for x in chosenSubsetsList]
	chosenSubsetsListOrdered.sort()
	print chosenSubsetsListOrdered


	# Computes the Final Cost of the Heuristic
	heuristicCost = 0;

	for chosenSubset in chosenSubsetsList:
		heuristicCost += subsetsCosts[int(chosenSubset)]

	print "Final Heuristic cost: " + str(heuristicCost-totalCost) + " ( " + str(heuristicCost) + " - " + str(totalCost) + " )"


##########
## MAIN ##
##########

if __name__ == "__main__":

	directory = "SCP-Instances"
	file = "scp42.txt"

	inputList = read_file(directory, file);

	list_analysis(inputList);

	subsets_costs();

	elements_in_subsets();

	heuristic_1();

	# heuristic_2();

