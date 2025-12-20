class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    

def create(tree, i=0):
    newNode = Node(tree[i])
    if (2*i+1)<len(tree):
        if tree[2*i+1] is not None:
            newNode.left = create(tree, 2*i+1)
    if (2*i+2)<len(tree):
        if tree[2*i+2] is not None:
            newNode.right = create(tree, 2*i+2)
    return newNode

def print_tree(root):
    if root is None:
        return
    if root.left and root.right:
        print(root.left.val + "--" + root.val +"--" + root.right.val )
    elif root.left is not None and root.right is None:
        print(root.left.val + "--" + root.val + "--"  )
    elif root.left is None and root.right:
        print("--" + root.val + "--" + root.right.val )
    print_tree(root.left)
    print_tree(root.right)
    


tree = ['a', 'b', 'c', None, 'd', 'e', None ,'f', 'g', 'h']
root = create(tree)    
print_tree(root)   