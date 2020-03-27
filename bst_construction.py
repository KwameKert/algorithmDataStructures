class BST:

	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None



#Average Time O(log(n)) ||  Space O(1)
#Worst Time O(n) || Space O(1)
	def insert(self,value):

		currentNode = self
		while True:

			if value < currentNode.value:
				if currentNode.left is None:
					currentNode.left = BST(value)
					break
				else:
					currentNode = currentNode.left
			else:
				if currentNode.right is None:
					currentNode.right = BST(value)
					break
				else:
					currentNode = currentNode.right
		return self;
		


#Average Time O(log(n)) ||  Space O(1)
#Worst Time O(n) || Space O(1)
	def contains(self,value):
		
		currentNode = self

		while currentNode is not None:
			if value < currentNode.value:
				currentNode = currentNode.left;

			elif value > currentNode.value:
				currentNode = currentNode.right

			else:
				return True
		return False;



	def remove(self,value):
	
		currentNode = self

		while currentNode is not True:

			if value < currentNode.value:

				parentNode = currentNode
				currentNode = currentNode.left;

			elif value > currentNode.value:

				parentNode	= currentNode
				currentNode = currentNode.right;

			else:

				if currentNode.left is not None and currentNode.right is not None:

					currentNode.value = currentNode.right.getMinValue()
					currentNode.right.remove(currentNode.value, currentNode)

				elif currentNode.parent is None:

					if currentNode.left is not None:
						currentNode.value =  currentNode.left.value
						currentNode.right = currentNode.left.right;
						currentNode.left  = currentNode.left.left;

					elif currentNode.right is not None:
						
						currentNode.value = currentNode.right.value
						currentNode.right = currentNode.right.right
						currentNode.left = currentNode.right.left	

					else:

						currentNode.value = None


				elif parentNode.left = currentNode:

					parentNode.left = currentNode.left if currentNode.left is not None else currentNode.right

				elif parentNode.right = currentNode:

					parentNode.right = currentNode.right if currentNode.right is not None else currentNode.left
					break;

		return self;						

	def getMinValue(self):
		
		currentNode = self;
		
		while currentNode.left is not None:

			currentNode = currentNode.left;

		return currentNode.value;			
		




		