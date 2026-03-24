from .node import Node


class Queue:
    def __init__(self, value=None):
        self.first = None
        self.last = None
        self.length = 0
        if value is not None:
            new_node = Node(value)
            self.first = new_node
            self.last = new_node
            self.length = 1

    def __str__(self):
        values = []
        cur = self.first

        while cur is not None:
            values.append(str(cur.value))
            cur = cur.next

        return " -> ".join(values)

    def enqueue(self, value):
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node

        self.last = new_node

        self.length += 1

    def dequeue(self):
        if self.first is None:
            return None

        temp = self.first
        self.first = self.first.next
        self.length -= 1

        if self.first is None:
            self.last = None

        temp.next = None
        return temp.value

    def peek(self):
        if self.first:
            return self.first.value
        return None
