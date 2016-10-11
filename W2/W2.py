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


# Heuristic to choose a set of subsets that composes all elements
def heuristic():

	global chosen_subsets;
	global elements_in_subsets;
	global subsetsCosts;
	global subsets;
	global totalCost;
	chosen_elements = []
	missing_elements = []

	# Tests if there are elements that are only in one subset (and therefore must be chosen)
	for elemenet, listSubsets in enumerate(elements_in_subsets):
		if len(listSubsets) == 1:
			# print "Subset " + str(listSubsets[0]) + " must be chosen"
			chosen_subsets.append(listSubsets[0]);


	# Adds elements to the list of chosen elements
	for chosenSubset in chosen_subsets:

		for element in subsets[int(chosenSubset)]:

			if (int(element)+1) not in chosen_elements:
				chosen_elements.append(int(element)+1)


	# Constructs the list of elements which were not chosen:
	for element, listSubsets in enumerate(elements_in_subsets):

		if (element+1) not in chosen_elements:
			missing_elements.append(int(element)+1);

	# Print information to the console
	print " == HEURISTIC 1 == "
	print str(len(chosen_subsets)) + " Subsets must be chosen because they are the only ones with a given element."
	print "Initial Chosen Elements: " + str(len(chosen_elements))
	print "Initial Missing Elements: " + str(len(missing_elements))

	# Computes the Cost of the Heuristic
	heuristicCost = 0;

	for chosenSubset in chosen_subsets:
		heuristicCost += subsetsCosts[int(chosenSubset)]

	print "Initial Heuristic cost: " + str(heuristicCost) + " (" + str(totalCost) + "): " + str(heuristicCost-totalCost)

	# print missing_elements

	iteration = 1;

	# Iterates over the list of elements which were not chosen:
	while missing_elements:

		currentElement = missing_elements.pop(0);
		subsetCosts = [];

		print " -- ITERATION " + str(iteration) + " -- "
		print "Current Element: " + str(currentElement);

		print "Subsets in which Element is found: " + str(elements_in_subsets[currentElement]);

		for i in elements_in_subsets[currentElement]:
			subsetCosts.append(subsetsCosts[i])

		print "Subsets Costs " + str(subsetCosts) 

		# Gets the subset with the minimum cost
		val, idx = min((val, idx) for (idx, val) in enumerate(subsetCosts))
		chosenSubset = int(elements_in_subsets[currentElement][idx])

		print "Minimum Cost: " + str(val) + " corresponding to Subset " + str(chosenSubset)

		# Add minimum cost subset to the list of chosen subsets.
		chosen_subsets.append(chosenSubset)

		print chosen_subsets

		# Remove elements from the chosen subset from the missing elements list.

		# Add elements from the chosen subset to the list of chosen elements. 

		# Increment the number of iterations
		iteration += 1;




	# Computes the Final Cost of the Heuristic
	heuristicCost = 0;

	for chosenSubset in chosen_subsets:
		heuristicCost += subsetsCosts[int(chosenSubset)]

	print "Final Heuristic cost: " + str(heuristicCost) + " (" + str(totalCost) + "): " + str(heuristicCost-totalCost)






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

	heuristic();
