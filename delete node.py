"""class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class sing:
    def __init__(self):
        self.head=None

    

    def be(self,newda):
        newnode=Node(newda)
        newnode.next=self.head
        self.head=newnode

    def dd(self):
        val=self.head
        while val is not None:
            print(val.data)
            val=val.next
    
    def end(self,newdata):
        newnode=Node(newdata)
        if self.head is None:
            self.head=newnode
            return
        last=self.head
        while last.next:
            last=last.next
        last.next=newnode

ll=sing()
ll.be("3")
ll.be("2")
ll.be("1")
#ll.dell("2")
ll.end("last")

ll.dd()"""
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
    def pri(self):
        val=self.head
        while val is not None:
            print(val.data)
            val=val.next

    def dele(self,key):
        temp=self.head
        if temp is not None:
            if temp.data==key:
                self.head=temp.next
                temp=None
                return

        while temp is not None:
            if temp.data==key:
                break
            prev=temp
            temp=temp.next

        if temp ==None:
            return
        prev.next=temp.next
        temp=None

        
list=Sing()
list.beg(3)
list.beg(2)
list.beg(1)
list.dele(2)
list.pri()"""
 
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class delete:
    def __init__(self):
        self.head=None

    def beg(self,data):
        newnode=Node(data)
        newnode.next=self.head
        self.head=newnode


    def de(self,key):
        temp=self.head
        if temp is not None:
            if temp.data==key:
                self.head=temp.next
                temp=None
                return

        while temp is not None:
            if temp.data==key:
                break
            prev=temp
            temp=temp.next

        if temp==None:
            return

        prev.next=temp.next
        temp=None
        
    def trav(self):
        val=self.head
        while val is not None:
            print(val.data)
            val=val.next


ll=delete()
ll.beg(4)
ll.beg(3)
ll.beg(2)
ll.beg(1)
ll.trav()
print()
ll.de(2)
ll.trav()