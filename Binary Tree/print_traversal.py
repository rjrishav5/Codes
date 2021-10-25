class Node:
    def __init__(self,data):
        self.data = data 
        self.left = None
        self.right = None

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.data,end=' ')
        inorder_traversal(root.right)


def preorder_traversal(root):
    if root:
        print(root.data,end=' ')
        preorder_traversal(root.left)
        preorder_traversal(root.right)

def PostOrder_traversal(root):
    if root:
        PostOrder_traversal(root.left)
        PostOrder_traversal(root.right)
        print(root.data,end=' ')

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print("InOrder traversal of binart tree is :",end=' ')
inorder_traversal(root)
print("\n")
print("PreOrder traversal of binary tree is :",end=" ")
preorder_traversal(root)
print("\n")
print("PostOrder traversal of binary tree is :",end=' ')
PostOrder_traversal(root)