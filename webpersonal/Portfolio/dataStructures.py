class Node:
    def __init__(self) -> None:
        self.value = None
        self.next = None
        self.left = None
        self.rigth = None
        self.before = None
        self.visited = False
        self.adjacentes = {}

    def addNeighbor(self,node):
        if node not in self.adjacentes.values():
            self.adjacentes[node.value] = node
        return
    
class Stack:
    def __init__(self) -> None:
        self.top = None
        self.size = 0

    def isEmpty(self):
        return self.top == None
    
    def peek(self):
        if self.isEmpty():return
        return self.top
    
    def push(self,node:Node):
        if self.isEmpty():
            self.top = node
        else:
            node.next = self.top
            self.top = node
        self.size += 1
        return self.peek()
    
    def pop(self):
        if self.isEmpty():return
        else:
            popped = self.top
            self.top = self.top.next
            self.size -= 1
            return popped
        
    def Size(self):
        return self.size
        
    def __str__(self) -> str:
        string = '['
        current = self.top 
        while current != None:
            string += str(current.value)
            if current.next != None:
                string += (',')
            current = current.next
        string +=']'
        return f'{string} -> {self.Size()}'
    
class Queue:
    def __init__(self) -> None:
        self.first = None
        self.last = None
        self.size = 0
    
    def isEmpty(self):
        return self.first == None
    
    def peek(self):
        if self.isEmpty():return
        return self.first()
    
    def push(self,node:Node):
        if self.isEmpty():
            self.first = self.last = node
        else:
            self.last.next = node
            self.last = node
        self.size += 1
        return self.peek()
    
    def remove(self):
        pass



if __name__=='__main__':
    node1 = Node()
    node2 = Node()
    node3 = Node()
    node4 = Node()
    node5 = Node()
    node6 = Node()
    node7 = Node()
    node8 = Node()
    node1.value = 1
    node2.value = 2
    node3.value = 3
    node4.value = 4
    node5.value = 5
    node6.value = 6
    node7.value = 7
    node8.value = 8
    lista = [node1,node2,node3,node4,node5,node6,node7,node8]





