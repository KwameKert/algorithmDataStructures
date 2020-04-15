

def findClosestValueInBst(tree, target):

	return findClosestValueInBstHelper(tree, target, float("inf"))


def findClosestValueInBstHelper(tree , target, closest):
	
	currentNode = tree

	while currentNode is not None:

		if abs(target - closest) > abs(target - currentNode.value):

			closest = currentNode.value

		if target < currentNode.value:
			
			currentNode = currentNode.left;

		elif target > currentNode.value:
			
			currentNode  = currentNode.right;

		else:
		
			break;

	return closest;
	

#i traverse the tree and search for the closest value 
#to the target by comparing the absolute different of 
#target to closest and target to current node value



