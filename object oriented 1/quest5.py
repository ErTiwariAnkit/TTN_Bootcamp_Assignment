class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self,head1):
        self.head=None
        for i in head1:
            newnode=Node(i)
            if self.head==None:
                self.head=newnode
            else:
                temp=self.head
                while temp.next!=None:
                    temp=temp.next
                temp.next=newnode
    def display_linkedlist(self):
        temp=self.head
        while temp.next!=None:
            print(f"{temp.data} is pointing to {temp.next.data}")
            temp=temp.next
        print(f"{temp.data} is pointing to {temp.next}")
    def __str__(self):
        temp=self.head
        while temp.next!=None:
            print(f"{temp.data} is pointing to {temp.next.data}")
            temp=temp.next
        print(f"{temp.data} is pointing to {temp.next}")
        exit()
list_1=Linkedlist([1,2,3,4])
print(list_1)
