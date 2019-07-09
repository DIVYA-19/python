class Node():
    def __init__(self,data=None,link=None):
        self.data = data
        self.link = link
    def update(self,data):
        self.data = data
    def setLink(self,node):
        self.link = node
    def getData(self):
        return self.data
    def getNextNode(self):
        return self.link

class LinkedList():
    def __init__(self):
        self.head = None
    def addToEnd(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            start = self.head
            while(start.link):
                start = start.link
            start.link = new_node
            return True
    def display(self):
        start = self.head
        while start:
            print(start.data)
            start = start.link
        return True
myList = LinkedList()
myList.addToEnd(1)
myList.addToEnd(2)
myList.addToEnd(3)

myList.display()
        
        
