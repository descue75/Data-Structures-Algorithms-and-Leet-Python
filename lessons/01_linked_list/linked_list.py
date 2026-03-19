from .node import Node


class LinkedList:
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
        if index >= self.length:
            return None
        cur = self.head
        for _ in range(index):
            cur = cur.next
        return cur

    def set_value(self, index, value):
        node = self.get(index)
        if node:
            node.value = value
            return True
        return True

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1

    def prepend(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
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
        cur = self.head

        for _ in range(index - 1):
            cur = cur.next

        new_node.next = cur.next
        cur.next = new_node
        self.length += 1

        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None

        if index == 0:
            temp = self.head
            self.head = self.head.next

            if self.length == 1:
                self.tail = None
        else:
            cur = self.head
            for _ in range(index - 1):
                cur = cur.next
            temp = cur.next
            cur.next = cur.next.next
            if index == self.length - 1:
                self.tail = cur

        temp.next = None
        self.length -= 1
        return temp

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
            prev = cur
            cur = nxt

        self.head = prev

    def clear(self):
        self.head = None
        self.tail = None
        self.length = 0

    ################### leet questions #################

    # find middle node without using length
    def leet_find_middle(self):
        fast = self.head
        slow = self.head

        while fast and fast != self.tail:
            fast = fast.next.next
            slow = slow.next

        return slow

    # has loop
    def leet_has_loop(self):
        fast = self.head
        slow = self.head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False

    # Kth node from end
    def leet_kth_from_end(self, k):
        fast = self.head
        slow = self.head

        for _ in range(k):
            if fast is None:
                return None
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next

        return slow

    # remove duplicates without using a set
    def leet_remove_duplicates_no_set(self):
        cur = self.head

        while cur:
            runner = cur
            while runner.next:
                if runner.next.value == cur.value:
                    temp = runner.next
                    runner.next = temp.next

                    if runner.next == self.tail:
                        self.tail = runner

                    self.length -= 1
                else:
                    runner = runner.next
            cur = cur.next

    # remove duplicates using a set
    def leet_remove_duplicates_with_set(self):
        if not self.head:
            return

        cur = self.head
        seen = {cur.value}

        while cur.next:
            if cur.next.value in seen:
                temp = cur.next
                cur.next = temp.next

                if temp == self.tail:
                    self.tail = cur

                self.length -= 1
            else:
                seen.add(cur.next.value)
                cur = cur.next

    def leet_binary_to_decimal(self):
        total = 0
        cur = self.head
        while cur:
            total *= 2
            if cur.value == 1:
                total += 1
            cur = cur.next
        return total

    def leet_partition_list(self, value):
        if self.head is None:
            return False

        left = LinkedList()
        right = LinkedList()
        cur = self.head
        while cur:
            if cur.value < value:
                left.append(cur.value)
            else:
                right.append(cur.value)
            cur = cur.next

        if left.head is None:
            self.head = right.head
            self.tail = right.tail
        elif right.head is None:
            self.head = left.head
            self.tail = left.tail
        else:
            left.tail.next = right.head
            self.head = left.head
            self.tail = right.tail
        return True
    
    def leet_between_reverse(self, start_index, end_index):
        if not (0 <= start_index < end_index < self.length):
            return False       
        
        dummy = Node(-1)
        dummy.next = self.head
        prev = dummy
  
        for _ in range(start_index):
            prev = prev.next

        cur = prev.next

        for _ in range(end_index - start_index):
            to_move = cur.next  
            cur.next = to_move.next
            to_move.next = prev.next
            prev.next = to_move

            if end_index == self.length - 1:
                self.tail = cur

        self.head = dummy.next
        return True
    
    def leet_swap_pairs(self):
        if self.length < 2:
            return False
        left = self.head
        prev = None

        while left and left.next:
            right = left.next  

            temp = right.next
            right.next = left
            left.next = temp

            if left == self.head:
                self.head = right

            if right == self.tail:
                self.tail = left

            if prev:
                prev.next = right

            prev = left
            left = temp
        return True
        