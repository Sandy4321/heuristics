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


##########
## MAIN ##
##########

if __name__ == "__main__":

	directory = "SCP-Instances"
	file = "scp42.txt"

	inputList = read_file(directory, file);

	list_analysis(inputList);


