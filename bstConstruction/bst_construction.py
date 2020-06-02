class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


    def insert(value):
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

    def lookup(value):
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
