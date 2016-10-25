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

import os
import csv
import sys
import copy
from Element import Element
from Subset import Subset
from Solution import Solution


######################
## GLOBAL VARIABLES ##
######################

subsets = [];
elements = [];


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
	subsets = []; # Make sure to delete subsets array.

	for i in xrange(0,n_subsets):
		subset = Subset(i+1, int(inputList.pop(0)));
		subsets.append(subset);

	# Construction of Element list:
	global elements
	elements = []; # Make sure to delete elements array.

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


# First Constructive Heuristic to build an initial solution.
# The procedure is to first select subsets with the lowest cost
def CH1():

	global elements;
	global subsets;
	missingElementsList = [];
	chosenElementsList = [];
	chosenSubsetsList = [];

	iteration = 1;

	# Costructs the list of elements still to choose
	for element in elements:
		missingElementsList.append(element.id)

	# Iterates until there is no element left
	while  missingElementsList:

		# 1. Choose the subset with the lowest cost
		
		chosenSubset = None
		candidateSubsetId = 1; # Initial Subset Candidate
		
		while chosenSubset is None:
			if candidateSubsetId not in chosenSubsetsList:
				chosenSubset = subsets[candidateSubsetId-1]
			else:
				candidateSubsetId += 1;

		# 2. Adds the lowest cost subset to the list of chosen subsets
		chosenSubsetsList.append(chosenSubset.id);

		# 3. Remove elements contained in the subset from a list of Missing Elements 
		for elementId in chosenSubset.elements:
			if elementId in missingElementsList:
				missingElementsList.remove(elementId);
				chosenElementsList.append(elementId);

		# print " -------------- ITERATION " + str(iteration) + " -------------- "
		# print "Iteration Subset: " + str(chosenSubset.id)

		# print "Subset Cost: " + str(chosenSubset.cost)
		# print "Elements Contained in the Subset:  " + str(chosenSubset.elements);

		# print missingElementsList
		# print chosenElementsList

		# print "Number of Elements already chosen:  " + str(len(chosenElementsList));
		# print "Number of Elements still missing:   " + str(len(missingElementsList));

		iteration += 1;

	print " ============ CONSTRUCTIVE HEURISTIC 1 ================ "	
	print "Number of Subsets chosen: " + str(len(chosenSubsetsList));

	# print "Chosen Subsets: "
	# chosenSubsetsListOrdered = [int(x) for x in chosenSubsetsList]
	# chosenSubsetsListOrdered.sort()
	# print chosenSubsetsListOrdered

	# Computes the Final Cost of the Heuristic
	heuristicCost = 0;

	for chosenSubset in chosenSubsetsList:
		heuristicCost += subsets[chosenSubset-1].cost

	print "Cost: " + str(heuristicCost)

	return heuristicCost


# Second Constructive Heuristic to build an initial solution.
# The procedure is to first select subsets with the lowest cost to number of elements weight
def CH2():

	global elements;
	global subsets;
	missingElementsList = [];
	orderedSubsets = [];
	chosenElementsList = [];
	chosenSubsetsList = [];

	iteration = 1;

	# Costructs the list of elements still to choose
	for element in elements:
		missingElementsList.append(element.id)

	# 1. Orders Subsets using the weight (cost / #elements) as a criteria
	orderedSubsets = sorted(subsets, key=lambda x: x.weight())

	# for subset in orderedSubsets:
	# 	print "Subset # " + str(subset.id) + " with Weight: " + str(subset.weight())

	# Iterates until there is no element left
	while  missingElementsList:

		# 2. Choose the subset with the lowest weight
		
		chosenSubset = orderedSubsets.pop(0);

		# 3. Adds the lowest cost subset to the list of chosen subsets
		chosenSubsetsList.append(chosenSubset.id);

		# 4. Remove elements contained in the subset from a list of Missing Elements 
		for elementId in chosenSubset.elements:
			if elementId in missingElementsList:
				missingElementsList.remove(elementId);
				chosenElementsList.append(elementId);

		# print " -------------- ITERATION " + str(iteration) + " -------------- "
		# print "Iteration Subset: " + str(chosenSubset.id)

		# print "Subset Cost: " + str(chosenSubset.cost)
		# print "Elements Contained in the Subset:  " + str(chosenSubset.elements);

		# print missingElementsList
		# print chosenElementsList

		# print "Number of Elements already chosen:  " + str(len(chosenElementsList));
		# print "Number of Elements still missing:   " + str(len(missingElementsList));

		iteration += 1;

	print " ============ CONSTRUCTIVE HEURISTIC 2 ================ "	
	print "Number of Subsets chosen: " + str(len(chosenSubsetsList));

	# print "Chosen Subsets: "
	# chosenSubsetsListOrdered = [int(x) for x in chosenSubsetsList]
	# chosenSubsetsListOrdered.sort()
	# print chosenSubsetsListOrdered

	# Computes the Final Cost of the Heuristic
	heuristicCost = 0;

	for chosenSubset in chosenSubsetsList:
		heuristicCost += subsets[chosenSubset-1].cost

	print "Cost: " + str(heuristicCost)

	return heuristicCost


# Third Constructive Heuristic to build an initial solution.
# The procedure is to iterate each element and select the subset with the lowest cost. 
def CH3():

	global elements;
	global subsets;
	missingElementsList = [];
	chosenElementsList = [];
	chosenSubsetsList = [];

	iteration = 1;

	# Costructs the list of elements still to choose
	for element in elements:
		missingElementsList.append(element.id)

	# Iterates until there is no element left
	while  missingElementsList:
		
		# currentElementNumber = missingElementsList.pop(0);
		currentElement = elements[missingElementsList.pop(0)-1]
		# chosenElementsList.append(currentElement.id);

		# 1. Checks in which subsets the element can be found, selects the subset with the lowest cost:

		candidateSubsets = currentElement.subsets
		chosenSubset = candidateSubsets[0];
		chosenSubsetCost = subsets[chosenSubset-1].cost

		# 2. Adds the lowest cost subset to the list of chosen subsets
		chosenSubsetsList.append(chosenSubset);

		# 3. Removes all elements contained in the chosen subset from the missing elements list (as they were already chosen)
		for elementId in subsets[chosenSubset-1].elements:
			# if elementId in missingElementsList:
			try:
				missingElementsList.remove(elementId);
			except Exception, e:
				pass
			chosenElementsList.append(elementId);

		# print " -------------- ITERATION " + str(iteration) + " -------------- "
		# print "Iteration Element: " + str(currentElement.id)

		# print "Subsets in which Element is found:  " + str(candidateSubsets);

		# print "Selected Subset with Minimum Cost:  " + str(chosenSubset) + " with cost " + str(chosenSubsetCost)

		# print missingElementsList
		# print chosenElementsList

		# print "Number of Elements already chosen:  " + str(len(chosenElementsList));
		# print "Number of Elements still missing:   " + str(len(missingElementsList));

		iteration += 1;

	print " ============ CONSTRUCTIVE HEURISTIC 3 ================ "	
	print "Number of Subsets chosen: " + str(len(chosenSubsetsList));

	# print "Chosen Subsets: "
	chosenSubsetsListOrdered = [int(x) for x in chosenSubsetsList]
	chosenSubsetsListOrdered.sort()
	# print chosenSubsetsListOrdered

	chosenElementsListOrdered = [int(x) for x in chosenElementsList]
	chosenElementsListOrdered.sort()

	# Computes the Final Cost of the Heuristic
	heuristicCost = 0;

	for chosenSubset in chosenSubsetsList:
		heuristicCost += subsets[chosenSubset-1].cost

	print "Cost: " + str(heuristicCost)

	# Solution Representation
	solution = Solution("SR3_0", "CH3", heuristicCost, chosenSubsetsListOrdered, chosenElementsListOrdered)

	return solution


# Fourth Constructive Heuristic to build an initial solution.
# The procedure is to iterate each element and select the subset with the best cost / #elements
def CH4():
	
	global elements;
	global subsets;
	missingElementsList = [];
	chosenElementsList = [];
	chosenSubsetsList = [];

	iteration = 1;

	# Costructs the list of elements still to choose
	for element in elements:
		missingElementsList.append(element.id)

	# Iterates until there is no element left
	while  missingElementsList:

		# 1. Select the Current Element
		currentElement = elements[missingElementsList.pop(0)-1]
		chosenElementsList.append(currentElement.id);


		# 2. Compute the cost / #elements ratio for each subset containing the element
		candidateSubsets = currentElement.subsets
		candidateSubsetsWeight = []

		for candidateSubset in candidateSubsets:
			weight = subsets[candidateSubset-1].weight()
			candidateSubsetsWeight.append(weight);


		# 3. Choose the subset with the lowest cost / #elements ratio
		
		# Gets the subset with the minimum weight
		val, idx = min((val, idx) for (idx, val) in enumerate(candidateSubsetsWeight))
		chosenSubset = int(candidateSubsets[idx]);
		chosenSubsetWeight = val


		# 4. Adds the lowest weight subset to the list of chosen subsets
		chosenSubsetsList.append(chosenSubset);

		# 5. Removes all elements contained in the chosen subset from the missing elements list (as they were already chosen)
		for elementId in subsets[chosenSubset-1].elements:
			if elementId in missingElementsList:
				missingElementsList.remove(elementId);
				chosenElementsList.append(elementId);

		# print " -------------- ITERATION " + str(iteration) + " -------------- "
		# print "Iteration Element: " + str(currentElement.id)

		# print "Subsets in which Element is found:  " + str(candidateSubsets);

		# print "Subsets Weights (cost / #elements): " + str(candidateSubsetsWeight)

		# print "Selected Subset with Min Weight:    " + str(chosenSubset) + " with cost " + str(chosenSubsetWeight)

		# # print missingElementsList
		# # print chosenElementsList

		# print "Number of Elements already chosen:  " + str(len(chosenElementsList));
		# print "Number of Elements still missing:   " + str(len(missingElementsList));

		iteration += 1;


	print " ============ CONSTRUCTIVE HEURISTIC 4 ================ "	
	print "Number of Subsets chosen: " + str(len(chosenSubsetsList));

	# print "Chosen Subsets: "
	# chosenSubsetsListOrdered = [int(x) for x in chosenSubsetsList]
	# chosenSubsetsListOrdered.sort()
	# print chosenSubsetsListOrdered

	# Computes the Final Cost of the Heuristic
	heuristicCost = 0;

	for chosenSubset in chosenSubsetsList:
		heuristicCost += subsets[chosenSubset-1].cost

	print "Cost: " + str(heuristicCost)

	return heuristicCost

# Redundancy elimination
def RE():
	return

# First Improvment: 
def FI(solution):
	
	FI_solution = Solution("FI_0", solution.CH, solution.cost, solution.subsets, solution.elements)

	print FI_solution.subsets

	for iteration in xrange(1,len(solution.subsets)+1):
		print " ===== Iteration " + str(iteration) + " ===== "

		actualSolutionCost = FI_solution.getCost(subsets);

		# Remove last subset from the list of chosen subsets
		removedSubset = FI_solution.subsets.pop(-iteration)

		# print "Removed Subset " + str(removedSubset)
		
		# Remove elements from the last subset from the list of chosen subsets
		for removedSubsetElements in subsets[removedSubset-1].elements:
			if removedSubsetElements in FI_solution.elements:
				FI_solution.elements.remove(removedSubsetElements);

		# Detects which elements are now missing
		missingElementsList = FI_solution.getElementsMissing(elements);
	
		# REDUDANCY DETECTION
		if len(missingElementsList) is 0:
			# print "Redudant Solution!"

			# Adds back subset and elements
			FI_solution.subsets.append(removedSubset)

			for element in subsets[removedSubset-1].elements:
				FI_solution.elements.append(element)

			continue 


		flg_improvedSolution = False;

		# Iterates list of missing elements and tries to construct another solution
		for missingElement in missingElementsList:

			if not flg_improvedSolution:

				# For each subset containing the Missing Element that is not the removed one and is not already in the list of chosen subsets, try to construct a solution
				for subset in elements[missingElement-1].subsets:
					if subset != removedSubset and subset not in FI_solution.subsets:
						
						FI_tentativeSolution = copy.deepcopy(FI_solution);

						for element in subsets[subset-1].elements:
							FI_tentativeSolution.elements.append(element)

						# Gets the list of Missing Elements in the Tentative Solution
						missingElementsList = FI_tentativeSolution.getElementsMissing(elements);

						# If it is a Potential Solution, computes the cost
						if len(missingElementsList) is 0:

							FI_tentativeSolution.subsets.append(subset)

							tentativeSolutionCost = FI_tentativeSolution.getCost(subsets)

							print "Potential Solution: Swap " + str(removedSubset) + " with " + str(subset) + " (COST " + str(tentativeSolutionCost) + ")"

							# If the cost is lower than the actual cost, the new solution is changed. If not, try again.
							if tentativeSolutionCost <= actualSolutionCost:
								print "New Solution! Swap " + str(removedSubset) + " with " + str(subset) + " (NEW COST: " + str(tentativeSolutionCost) + ") (COST IMPROVEMENT: " + str(actualSolutionCost-tentativeSolutionCost) + ")"

								FI_solution = copy.deepcopy(FI_tentativeSolution);

								flg_improvedSolution = True;

								break;

							# else:
								# print "No Improvement!"

						# If it is not a Potential Solution, try again

		# print FI_solution.subsets

		if not flg_improvedSolution:


			# Adds back subset and elements
			FI_solution.subsets.append(removedSubset)

			for element in subsets[removedSubset-1].elements:
				FI_solution.elements.append(element)

			# print "No New Solution... Adding back " + str(removedSubset) + " (COST:  " + str(FI_solution.getCost(subsets)) + ")"


	print FI_solution.subsets



##########
## MAIN ##
##########

if __name__ == "__main__":

	directory = "SCP-Instances"
	file = "scp42.txt"

	dataFile = "data.csv"

	f = open(dataFile, 'wt')

	writer = csv.writer(f)
	writer.writerow( ('SCP', 'CH1', 'CH2', 'CH3') )


	print "###################################################################################"
	print "File: " + directory + "/" + file

	inputList = read_file(directory, file);

	list_analysis(inputList);

	# information_print();

	# CH1()

	# CH2();

	CH3_solution = CH3();

	FI(CH3_solution);

	# CH4();

	# for subdir, dirs, files in os.walk(directory):
	# 	for file in files:

	# 		print "###################################################################################"
	# 		print "File: " + directory + "/" + file

	# 		inputList = read_file(directory, file);

	# 		list_analysis(inputList);

	# 		# information_print();

	# 		CH1_result = CH1();

	# 		# CH2_result = CH2();

	# 		CH3_result = CH3();

	# 		CH4_result = CH4();

	# 		writer.writerow( (file, CH1_result, CH3_result, CH4_result) );

	f.close()


	
