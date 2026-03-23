from .node import Node


class DoublyLinkedList:
    def __init__(self, value=None):
        if value is None:
            self.head = None
            self.tail = None
            self.length = 0
        else:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
            self.length = 1

    def __str__(self):
        values = []
        cur = self.head

        while cur is not None:
            values.append(str(cur.value))
            cur = cur.next

        return " -> ".join(values)

    def __len__(self):
        return self.length

    def get(self, index):
        if index >= self.length or index < 0:
            return None
        if index < self.length // 2:
            cur = self.head
            for _ in range(index):
                cur = cur.next
            return cur
        else:
            cur = self.tail
            for _ in range(self.length - 1, index, -1):
                cur = cur.prev
            return cur

    def set_value(self, index, value):
        node = self.get(index)
        if node:
            node.value = value
            return True
        return False

    def append(self, value):
        new_node = Node(value)
        if (self.length == 0):
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False

        if index == 0:
            self.prepend(value)
            return True

        if index == self.length:
            self.append(value)
            return True

        new_node = Node(value)
        cur = self.get(index)
        prev_node = cur.prev

        prev_node.next = new_node
        new_node.prev = prev_node
        new_node.next = cur
        cur.prev = new_node

        self.length += 1
        return True
    
    def remove(self, index):
        if (index < 0 or index >= self.length):
            return False

        cur = self.get(index)
        prev_node = cur.prev
        next_node = cur.next
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            if prev_node:
                prev_node.next = next_node
            else:
                self.head = next_node
            if next_node:
                next_node.prev = prev_node
            else:
                self.tail = prev_node

        cur.next = None
        cur.prev = None

        self.length -= 1
        return cur
    
    def pop(self):
        return self.remove(self.length - 1)

    def pop_first(self):
        return self.remove(0)

    def reverse(self):
        cur = self.head
        prev = None
        self.tail = self.head

        while cur:
            nxt = cur.next
            cur.next = prev
            cur.prev = nxt
            prev = cur
            cur = nxt

        self.head = prev

    def clear(self):
        self.head = None
        self.tail = None
        self.length = 0
