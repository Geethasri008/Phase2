
class Tree:
    def __init__(self,key):
        self.val=key
        self.left=None 
        self.right=None 
def bstinsertion(root,key):
    if not root:
        return Tree(key)
    else:
        if root.val==key:
            return Tree(key)
        
        elif root.val>key:
            root.left=bstinsertion(root.left,key)
        else:
            root.right=bstinsertion(root.right,key)
    return root 

def inorder(root,result):
    if not root:
        return None 
    
    inorder(root.left,result)
    result+=[root.val]
    inorder(root.right,result)
    return (result)

def klargest(result,largest):
    l=len(result)
    if largest>l:
        print()
    print("The {} largest element is {} ".format(largest,result[-largest]))
def kthsmallest(result,smallest):
    print("The {} smallest element is {}".format(smallest,result[smallest-1]))

  
largest=int(input())
smallest=int(input())
result=[]
r=Tree(10)
r=bstinsertion(r,8)

r=bstinsertion(r,15)
r=bstinsertion(r,22)
r=bstinsertion(r,28)
r=bstinsertion(r,-5)    
r=bstinsertion(r,6)
r=bstinsertion(r,7)
r=(inorder(r,result))
print(r)
klargest(result,largest)
kthsmallest(result,smallest)
'''
# Python program to demonstrate
# insert operation in binary search tree


# A utility class that represents
# an individual node in a BST
class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key


# A utility function to insert
# a new node with the given key
def insert(root, key):
	if root is None:
		return Node(key)
	else:
		if root.val == key:
			return root
		elif root.val < key:
			root.right = insert(root.right, key)
		else:
			root.left = insert(root.left, key)
	return root


# A utility function to do inorder tree traversal
def inorder(root):
	if root:
		inorder(root.left)
		print(root.val, end=" ")
		inorder(root.right)


# Driver program to test the above functions
if __name__ == '__main__':

	# Let us create the following BST
	# 50
	# /	 \
	# 30	 70
	# / \ / \
	# 20 40 60 80

	r = Node(50)
	r = insert(r, 30)
	r = insert(r, 20)
	r = insert(r, 40)
	r = insert(r, 70)
	r = insert(r, 60)
	r = insert(r, 80)

	# Print inorder traversal of the BST
	inorder(r)
'''