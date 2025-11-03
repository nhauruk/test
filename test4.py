class Node:
    def __init__(self, value):
        self.value = value   
        self.next = None  

class Stack:
    def __init__(self):
        self.top = None     
        self.size = 0      

    def is_empty(self):
        return self.top is None

    def push(self, value):
        new_node = Node(value)   
        new_node.next = self.top 
        self.top = new_node
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Стек пустой")
        popped_value = self.top.value
        self.top = self.top.next 
        self.size -= 1
        return popped_value

    def peek(self):
        if self.is_empty():
            raise IndexError("Стек пустой")
        return self.top.value



