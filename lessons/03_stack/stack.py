from .node import Node


class Stack:
    def __init__(self, value=None):
        self.top = None
        self.height = 0
        if value is not None:
            new_node = Node(value)
            self.top = new_node
            self.height = 1

    def __str__(self):
        values = []
        cur = self.top

        while cur is not None:
            values.append(str(cur.value))
            cur = cur.next

        return " -> ".join(values)

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.height += 1

    def pop(self):
        if self.height == 0:
            return None

        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1

        return temp.value
    
    def peek(self):
        if self.top:
            return self.top.value
        return None
