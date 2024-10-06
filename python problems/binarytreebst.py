class Node:
    def __init__(self,data):
     self.data=data
     self.left=None
     self.right=None
def maxvalue(node):
    if node is None:
        return 0
    leftmax=maxvalue(node.left)
    rightmax=maxvalue(node.right)
    value=0
    if leftmax>rightmax:
        value=leftmax
    else:
        value=rightmax
    if value <node.data:
        value=node.data
    return value
def minvalue(node):
    if node is None:
        return 1000000000
    leftmax=minvalue(node.left)
    rightmax=minvalue(node.right)
    value=0
    if leftmax<rightmax:
        value=leftmax
    else:
        value=rightmax
    if value>node.data:
        value=node.data
    return value
def isBST(node):
    if node is None:
        return True
    if(node.left!=None and maxvalue(node.left)>node.data):
        return False
    if(node.right!=None and minvalue(node.right)<node.data):
        return False
    if (isBST(node.left)is False or isBST(node.right)is False):
        return False
    return True
if __name__=="__main__":
    root= Node(4)
    root.left=Node(2)
    root.right=Node(5)
    root.left.left = Node(1)
    root.left.right = Node(3)
    if isBST(root) is True:
      print("Is BST")
    else:
      print("Not a BST")
                               