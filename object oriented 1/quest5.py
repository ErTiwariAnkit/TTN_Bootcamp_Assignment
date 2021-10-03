class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self,head):
        self.head=None
        for i in head:
            newnode=Node(i)
            if self.head==None:
                self.head=newnode
            else:
                temp=self.head
                while temp.next!=None:
                    temp=temp.next
                temp.next=newnode
list_1=Linkedlist([1,2,3,4])
print(list_1)
