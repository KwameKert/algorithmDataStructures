class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


    def insert(self, value):
        currentNode = self
        #loop through tree to find the node to insert
        while currentNode:
            #if currentNode left is none then insert a new node else assign currentNode left node to currentNode
            if value < currentNode.value:
                if currentNode.left is None:
                    currentNode.left = BST(value)
                    break
                else:
                    currentNode = currentNode.left
            else:
            #if currentNode right is none then insert a new node else assign currentNode right node to currentNode
                if currentNode.right is None:
                    currentNode.right = BST(value)
                    break
                else:
                    currentNode = currentNode.right
        return self

    def lookup(self, value):
        currentNode = self
        #loop through tree
        while currentNode:
            #if value less than current node then reassign currentNode to currentNode left node
            if value < currentNode.value:
                currentNode = currentNode.left
            #if value more than current node then reassign currentNode to currentNode right node
            elif value> currentNode.value:
                currentNode = currentNode.right
            else:
                return currentNode

        #if node not found return False
        return False


    def remove(self, value, parentNode = None):
        foundNode = self.lookup(value)
        if foundNode is False:
            return False
        currentNode = self

        while currentNode is not None:
            if value < currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.left

            elif value > currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.right

            else:
                # node found currentNode has two children
                if currentNode.left is not None and currentNode.right is not None:
                    currentNode.value = currentNode.right.getMinValue()
                    currentNode.right.remove(currentNode.value, currentNode)

                #if node to be removed is root
                elif parentNode is None:
                    #if node has only left children
                    if currentNode.left is not None:
                        currentNode.value = currentNode.left.value
                        currentNode.left = currentNode.left.left
                        currentNode.right = currentNode.left.right
                    #if node has only right children
                    elif currentNode.right is not None:
                        currentNode.value = currentNode.right.value
                        currentNode.left = currentNode.right.left
                        currentNode.right = currentNode.right.right
                    else:
                        #if no parent and has no child we can delete the root node
                        currentNode.value = None
                #if current node has only one child
                elif parentNode.left == currentNode:
                    parentNode.left = currentNode.left if currentNode.left is None else currentNode.right
                elif parentNode.right == currentNode:
                    parentNode.right = currentNode.right if currentNode.right is None else currentNode.left

                #found node to delete hence break from while loop
                break

    def getMinValue(self):
        currentNode = self
        while currentNode.left is not None:
            currentNode = currentNode.left
        return currentNode.value













