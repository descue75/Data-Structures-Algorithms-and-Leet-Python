from .doubly_linked_list import DoublyLinkedList

# =========================
# BASIC OPERATIONS
# =========================

# Initialize list with one element
my_linked_list = DoublyLinkedList(1)
print(my_linked_list)

# Append adds to the end (O(1))
my_linked_list.append(2)
print(my_linked_list)

# Prepend adds to the beginning (O(1))
my_linked_list.prepend(0)
print(my_linked_list)

# =========================
# INSERT OPERATIONS
# =========================

# Insert at beginning (behaves like prepend)
my_linked_list.insert(0, 10)
print(my_linked_list)

# Insert at end (behaves like append)
my_linked_list.insert(4, 11)
print(my_linked_list)

# Insert in the middle (requires traversal O(n/2) = O(n))
my_linked_list.insert(1, 12)
print(my_linked_list)

# =========================
# REMOVE OPERATIONS
# =========================

# Remove from a single-element list
my_one_element_linked_list = DoublyLinkedList(1)
print(my_one_element_linked_list)
print(my_one_element_linked_list.remove(0))

# Remove with invalid index (should return None)
print(my_linked_list.remove(-1))
print(my_linked_list.remove(100))

# Remove head (O(1))
print(my_linked_list.remove(0))
print(my_linked_list)

# Remove tail (O(1))
print(my_linked_list.remove(my_linked_list.length - 1))
print(my_linked_list)

# Remove from middle (O(n))
print(my_linked_list.remove(1))
print(my_linked_list)

# =========================
# REVERSE LIST
# =========================

# Reverse entire list in-place (O(n), O(1) space)
print(my_linked_list)
my_linked_list.reverse()
print(f"reversed = {my_linked_list}")


# =========================
# GET / SET OPERATIONS
# =========================

# Get node by index (O(n))
print(my_linked_list.get(3))
print(my_linked_list.get(my_linked_list.length - 1))
print(my_linked_list.get(0))

# Set value at index (O(n))
my_linked_list.set_value(0, 100)
print(my_linked_list)

# =========================
# LEET QUESTION 1 - PALINDROME CHECKER
# =========================
palindrome_list = DoublyLinkedList(1)
palindrome_list.append(2)
palindrome_list.append(4)
palindrome_list.append(2)
palindrome_list.append(1)
print(palindrome_list)
print(palindrome_list.leet_is_palindrome())

palindrome_list.remove(2)
print(palindrome_list)
print(palindrome_list.leet_is_palindrome())

palindrome_list.set_value(2, 100)
print(palindrome_list)
print(palindrome_list.leet_is_palindrome())

# =========================
# LEET QUESTION 2 - PARTITION LIST
# =========================
# Split into < value and >= value (O(n), O(n) space)
linked_list_partition = DoublyLinkedList(3)
linked_list_partition.append(8)
linked_list_partition.append(5)
linked_list_partition.append(10)
linked_list_partition.append(2)
linked_list_partition.append(1)

print(linked_list_partition)
linked_list_partition.leet_partition_list(5)
print(linked_list_partition)

# =========================
# LEET QUESTION 3 - REVERSE SUBLIST
# =========================
# Reverse nodes between indices (O(n), O(1))
linked_list_between_reverse = DoublyLinkedList(1)
linked_list_between_reverse.append(2)
linked_list_between_reverse.append(3)
linked_list_between_reverse.append(4)
linked_list_between_reverse.append(5)

print(linked_list_between_reverse)
linked_list_between_reverse.leet_between_reverse(1, 3)
print(linked_list_between_reverse)

# =========================
# LEET QUESTION 4 - SWAP PAIRS
# =========================
# Swap adjacent nodes (O(n), O(1))
linked_list_swap = DoublyLinkedList(1)
linked_list_swap.append(2)
linked_list_swap.append(3)
linked_list_swap.append(4)
linked_list_swap.append(5)
linked_list_swap.append(6)
linked_list_swap.append(7)

print(linked_list_swap)
linked_list_swap.leet_swap_pairs()
print(linked_list_swap)
