class Node:

    def __init__(self, value):
        self.value = value
        self.leftChild = None
        self.rightChild = None

class BST:

    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.insertNode(self.root, value)

    def insertNode(self, currentNode, value):
        if value < currentNode.value:
            if currentNode.leftChild:
                self.insertNode(currentNode.leftChild, value)
            else:
                currentNode.leftChild = Node(value)
        else:
            if currentNode.rightChild:
                self.insertNode(currentNode.rightChild, value)
            else:
                currentNode.rightChild = Node(value)

    def printTree(self, currentNode=None):
        if currentNode is None:
            self.printTree(self.root)
        else:
            if currentNode.leftChild:
                self.printTree(currentNode.leftChild)
            print(currentNode.value)
            if currentNode.rightChild:
                self.printTree(currentNode.rightChild)


list = [7,1,4,2,6,8,3,9,5,0]
bst = BST()
for item in list:
    print(item)
    bst.insert(item)

bst.printTree()
