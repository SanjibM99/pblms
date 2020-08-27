"""class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linked:
    def __init__(self):
        self.last=None

    def atempty(self,data):
        if (self.last!=None):
            return self.last
        temp=Node(data)
        self.last=temp
        self.last.next=self.last
        return self.last

    def atbeg(self,data):
        if (self.last==None):
            return self.atempty(data)
        temp=Node(data)
        temp.next=self.last.next
        self.last.next=temp
        return self.last

    def atlast(self,data):
        if self.last==None:
            return self.atempty(data)

        temp=Node(data)
        temp.next=self.last.next
        self.last.next=temp
        self.last=temp

        return self.last

    def atmiddle(self,data,item):
        if self.last==None:
            return None

        temp=Node(data)
        p=self.last.next
        while p:
            if(p.data==item):
                temp.next=p.next
                p.next=temp

                if(p==self.last):
                    self.last=temp
                    return self.last
                else:
                    return self.last

            p=p.next
            if p==self.last.next:
                print(item,'not present in list')
                break


    def traverse(self):
        if (self.last==None):
            print("list are empty")
            return 
        temp=self.last.next
        while temp:
            print(temp.data)
            temp=temp.next
            if temp==self.last.next:
                break

l=Linked()
l.atbeg(3)
l.atbeg(2)
l.atbeg(1)
l.atmiddle(4,2)
l.traverse()        """

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Cir:
    def __init__(self):
        self.last=None

    def atempty(self,data):
        if self.last!=None:
            return self.last
        newnode=Node(data)
        self.last=newnode
        self.last.next=self.last
        return self.last

    def atbeg(self,data):
        if self.last==None:
            return self.atempty(data)
        newnode=Node(data)
        newnode.next=self.last.next
        self.last.next=newnode
        return self.last
        
    def atend(self,data):
        if self.last==None:
            return self.atempty(data)

        newnode=Node(data)
        newnode.next=self.last.next
        self.last.next=newnode
        self.last=newnode
        return self.last

    def atmidd(self,data,item):
        if self.last==None:
            return None
        newnode=Node(data)
        p=self.last.next
        while p:
            if p.data==item:
                newnode.next=p.next
                p.next=newnode

                if p==self.last:
                    self.last=newnode
                    return self.last
                else:
                    return self.last

            p=p.next
            if (p == self.last.next): 
                print(item, "not present in the list") 
                break
        
            
    def traverse(self): 
        if (self.last == None): 
            print("List is empty") 
            return
  
        temp = self.last.next
        while temp: 
            print(temp.data) 
            temp = temp.next
            if temp == self.last.next: 
                break

ll=Cir()
ll.atbeg(3)
ll.atbeg(2)
ll.atbeg(1)
ll.atmidd('bich mein aa ya',1)
ll.traverse()