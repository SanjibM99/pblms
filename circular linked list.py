"""class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Cir:
    def __init__(self):
        self.head=None

    def beg(self,data):
        newnode=Node(data)
        temp=self.head
        newnode.next=self.head
        if self.head is not None:
            while temp.next!=self.head:
                temp=temp.next
            temp.next=newnode

        else:
            newnode.next=newnode
        self.head=newnode
        

    def pr(self):
        val=self.head
        if self.head is not None:
            while (True):
                print(val.data)
                val=val.next
                if val ==self.head:
                    break

        
ll=Cir()
ll.beg(0)
ll.beg(1)
ll.beg(2)
ll.pr()"""

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Cir:
    def __init__(self):
        self.head=None

    def beg(self,data):
        newnode=Node(data)
        temp=self.head
        newnode.next=self.head
        if self.head is not None:
            while temp.next!=self.head:
                temp=temp.next
            temp.next=newnode
            
        else:
            newnode.next=newnode
        self.head=newnode

    def dis(self):
        val=self.head
        if self.head is not None:
            while (True):
                print(val.data,end=" ")
                val=val.next
                if val==self.head:
                    break

ll=Cir()
ll.beg("majhi")
ll.beg('Kumar')
ll.beg('Sanjib')
ll.dis()