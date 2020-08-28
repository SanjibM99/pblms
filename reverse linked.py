
"""class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
class Sing:
    def __init__(self):
        self.head=None

    def beg(self,newdata):
        newnode=Node(newdata)
        newnode.next=self.head
        self.head=newnode

    def de(self):
        prev=None
        current=self.head
        while current is not None:
            next=current.next
            current.next=prev
            prev=current
            current=next
        self.head=prev

    def dis(self):
        val=self.head
        while val is not None:
            print(val.data)
            val=val.next
ll=Sing()
ll.beg(3)
ll.beg(2)
ll.beg(1)
ll.de()
ll.dis()
"""
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Rev:
    def __init__(self):
        self.head=None

    def beg(self,data):
        newnode=Node(data)
        newnode.next=self.head
        self.head=newnode

    def reverse(self):
        prev=None
        current=self.head
        while current is not None:
            next=current.next
            current.next=prev
            prev=current
            current=next
        self.head=prev

    def trav(self):
        val=self.head
        while val is not None:
            print(val.data)
            val=val.next

ll=Rev()
ll.beg(1)        
ll.beg(2)
ll.beg(3)
ll.trav()
ll.reverse()
ll.trav()