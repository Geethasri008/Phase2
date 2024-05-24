#array to linkedlist creation

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None 
def createLinkedlist(arr):
    if not arr:
        return None
    
    head=Node(arr[0])
    curr=head 
    for i in arr[1:]:
        curr.next=Node(i)
        curr=curr.next
    return head 
def printlinkedlist(head):
    curr=head
    while curr:
        print(curr.data,end=" -> ") 
        curr=curr.next
    print("None")
def insertatend(head,data):
    curr=head
    while curr.next:
        curr=curr.next 
    curr.next=Node(data)
    return head
def insertatsttart(head,data):
    new_node=Node(data)
    new_node.next=head
    return new_node
def insertatspecific(head,v,r):
    curr=head 
    while curr.data !=v:
        curr=curr.next 
    if curr.data==v:
        temp=curr.next
        curr.next=Node(r)
        curr.next.next=temp
    return head 
def deleteatend(head):
    if head.next==None:
        return None 
    curr=head
    while curr.next.next :
        curr=curr.next 
    curr.next=None 
    return head 
def deleteatstart(head):
    if not head.next:
        return None
    temp=head.next
    head=temp
    return head
def deletespecific(head,value):
    curr=head
    while curr.next:
        if curr.next.data==value:
            curr.next=curr.next.next 
        curr=curr.next
    return head
arr=[21,23,24,25,26,27]
head=createLinkedlist(arr)

head=deletespecific(head,23)
printlinkedlist(head)
