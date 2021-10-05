class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Cyclic_Linkedlist:
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
        temp = self.head
        while temp.next != None:
            temp = temp.next
        temp.next=self.head.next
    def display_linkedlist(self):
        temp=self.head
        while temp.next!=None:
            print(f"{temp.data} is pointing to {temp.next.data}")
            temp=temp.next
        print(f"{temp.data} is pointing to {temp.next}")
    def is_cyclic(self):
        hash_map={}
        temp=self.head
        while temp.next!=None:
            if temp.next not in hash_map:
                hash_map[temp.next]=temp.data
                temp=temp.next
            else:
                print("linkedlist is cyclic")
                break
        else:
            print("linkedlist not in cyclic")
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
    def is_cyclic(self):
        hash_map={}
        temp=self.head
        while temp.next!=None:
            if temp.next not in hash_map:
                hash_map[temp.next]=temp.data
                temp=temp.next
            else:
                print("linkedlist is cyclic")
                break
        else:
            print("linkedlist not in cyclic")
list1=Cyclic_Linkedlist([23,78,67,57])
list12=Linkedlist([56,33,66,87])
list1.is_cyclic()
list12.is_cyclic()

