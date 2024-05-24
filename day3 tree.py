
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None 
        self.right=None 
def inordertraversal(root): #left root right
    if root==None:
        return None 
    inordertraversal(root.left)
    print(root.data,end="->")
    inordertraversal(root.right)
def preorder(root): # root left right
    if root==None:
        return None 
    print(root.data,end="->")
    preorder(root.left)
    preorder(root.right)
def postorder(root): # left right root
    if root==None:
        return None 
    
    postorder(root.left)
    postorder(root.right)
    print(root.data,end="->")
def levelorderTraversal(root):
    if root ==None:
        return None 
    result=[]
    Q=[root]
    while len(Q)>0:
        n=len(Q)
        subResult=[]
        for i in range(n):
            currentNode=Q.pop(0)
            subResult.append(currentNode.data)
            if currentNode.left !=None:
                Q.append(currentNode.left)
            if currentNode.right !=None:
                Q.append(currentNode.right)
        result.append(subResult)
    print(result)
def zigzagorder(root):
    if root==None:
        return None 
    result=[]
    Q=[root]
    level=0
    while len(Q)>0:
        n=len(Q)
        subResult=[]
        level+=1
        for i in range(n):
            currentNode=Q.pop(0)
            subResult.append(currentNode.data)
            if currentNode.left !=None:
                Q.append(currentNode.left)
            if currentNode.right !=None:
                Q.append(currentNode.right)
        if (level%2==0):
            subResult=subResult[::-1]
        result.append(subResult)
        
    print(result)

def findLeftview(root):
    if root ==None :
        return []
    result=[]
    Q=[root]
    while Q:
        n=len(Q)
        for i in range(n):
            curr=Q.pop(0)
            if i==0:
                result.append(curr.data)
            if curr.left != None:
                Q.append(curr.left)
            if curr.right !=None :
                Q.append(curr.right)
    print(result)

def topViewHelper(root, store, hd, level):
    if root == None:
        return 
 
    if hd not in store or store[hd][0] > level:
        store[hd] = [level, root.data]
 
    topViewHelper(root.left, store, hd - 1, level + 1)
    topViewHelper(root.right, store, hd + 1, level + 1)
 
def findTopView(root):
    result = []
    if root == None:
        print(result)
 
    store = {}
    topViewHelper(root, store, 0, 0)
    sortedKeys = sorted(store.keys())
    for key in sortedKeys:
        result.append(store[key][1])
    print(result)

def bottomViewHelper(root, store, hd, level):
    if root == None:
        return 
 
    if hd not in store or store[hd][0] < level:
        store[hd] = [level, root.data]
 
    bottomViewHelper(root.left, store, hd - 1, level + 1)
    bottomViewHelper(root.right, store, hd + 1, level + 1)
 
def findBottomView(root):
    result = []
    if root == None:
        return result
 
    store = {}
    bottomViewHelper(root, store, 0, 0)
    sortedKeys = sorted(store.keys())
    for key in sortedKeys:
        result.append(store[key][1])
    print(result)
obj1=Node(1)
obj2=Node(2)
obj3=Node(3)
obj4=Node(4)
obj5=Node(5)
obj6=Node(6)
obj7=Node(7)
obj8=Node(8)
obj9=Node(9)
obj10=Node(10)
obj11=Node(11)
obj12=Node(12)
obj13=Node(13)
obj1.left=obj2
obj1.right=obj3
obj2.left=obj4
obj2.right=obj5
obj3.left=obj6 
obj3.right=obj7
obj4.left=obj8
obj4.right=obj9
obj5.left=obj10 
obj5.right=obj11
obj6.left=obj12 
obj6.right=obj13
inordertraversal(obj1)
print()
preorder(obj1)
print()
postorder(obj1)
print()
levelorderTraversal(obj1)
print()
zigzagorder(obj1)
print()
findLeftview(obj1)
print()
findTopView(obj1)
print()
findBottomView(obj1)
print()