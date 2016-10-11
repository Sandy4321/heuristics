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
subsetsCosts = [];
elements_in_subsets = [];

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

	for idx, subsetCost in enumerate(subsetsCosts):
		print "Cost of Subset " + str(idx) + ": " + str(subsetCost);

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

	# Print Information to the Screen
	for idx, element_in_subset in enumerate(elements_in_subsets):
		print "Element " + str(idx+1) + " appears in " + str(len(element_in_subset)) + " subsets: " + str(element_in_subset)


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
