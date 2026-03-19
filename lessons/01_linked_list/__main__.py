from .linked_list import LinkedList

# =========================
# BASIC OPERATIONS
# =========================

# Initialize list with one element
my_linked_list = LinkedList(1)
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

# Insert at beginning (index 0 → behaves like prepend)
my_linked_list.insert(0, 10)
print(my_linked_list)

# Insert at or beyond end (behaves like append)
my_linked_list.insert(100, 11)
print(my_linked_list)

# Insert in the middle (requires traversal O(n))
my_linked_list.insert(1, 12)
print(my_linked_list)


# =========================
# REMOVE OPERATIONS
# =========================

# Remove from a single-element list
my_one_element_linked_list = LinkedList(1)
print(my_one_element_linked_list)
print(my_one_element_linked_list.remove(0))

# Remove with invalid index (should return None)
print(my_linked_list.remove(-1))
print(my_linked_list.remove(100))

# Remove head (O(1))
print(my_linked_list.remove(0))

# Remove tail (O(n))
print(my_linked_list)
print(len(my_linked_list))
print(my_linked_list.remove(4))

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
print(my_linked_list.get(2))
print(my_linked_list.get(0))

# Set value at index (O(n))
my_linked_list.set_value(0, 100)
print(my_linked_list)


# =========================
# LEET QUESTION 1 - FIND MIDDLE
# =========================
# Uses fast/slow pointer (O(n), O(1))
print(my_linked_list.leet_find_middle())
my_linked_list.append(10)
print(my_linked_list)
print(my_linked_list.leet_find_middle())


# =========================
# LEET QUESTION 2 - DETECT LOOP
# =========================
# Floyd’s cycle detection (O(n), O(1))
print(my_linked_list.leet_has_loop())

# Create a loop manually for testing
my_linked_list.tail.next = my_linked_list.head.next
print(my_linked_list.leet_has_loop())

# Remove loop
my_linked_list.tail.next = None


# =========================
# LEET QUESTION 3 - KTH FROM END
# =========================
# Two-pointer technique (O(n), O(1))
print(my_linked_list)
print(my_linked_list.leet_kth_from_end(3))


# =========================
# LEET QUESTION 4 - REMOVE DUPLICATES
# =========================

# Part 1: Without extra space (O(n^2))
linked_list_duplicates = LinkedList(1)
linked_list_duplicates.append(2)
linked_list_duplicates.append(3)
linked_list_duplicates.append(1)
linked_list_duplicates.append(4)
linked_list_duplicates.append(2)
linked_list_duplicates.append(5)

print(linked_list_duplicates)
linked_list_duplicates.leet_remove_duplicates_no_set()
print(linked_list_duplicates)

# Part 2: Using set (O(n) time, O(n) space)
linked_list_duplicates = LinkedList(1)
linked_list_duplicates.append(2)
linked_list_duplicates.append(3)
linked_list_duplicates.append(1)
linked_list_duplicates.append(4)
linked_list_duplicates.append(2)
linked_list_duplicates.append(5)

print(linked_list_duplicates)
linked_list_duplicates.leet_remove_duplicates_with_set()
print(linked_list_duplicates)


# =========================
# LEET QUESTION 5 - BINARY TO DECIMAL
# =========================
# Treat linked list as binary number (O(n))
linked_list_binary = LinkedList(0)
linked_list_binary.append(1)
linked_list_binary.append(1)
linked_list_binary.append(0)

print(linked_list_binary)
print(linked_list_binary.leet_binary_to_decimal())


# =========================
# LEET QUESTION 6 - PARTITION LIST
# =========================
# Split into < value and >= value (O(n), O(n) space)
linked_list_partition = LinkedList(3)
linked_list_partition.append(8)
linked_list_partition.append(5)
linked_list_partition.append(10)
linked_list_partition.append(2)
linked_list_partition.append(1)

print(linked_list_partition)
linked_list_partition.leet_partition_list(5)
print(linked_list_partition)


# =========================
# LEET QUESTION 7 - REVERSE SUBLIST
# =========================
# Reverse nodes between indices (O(n), O(1))
linked_list_between_reverse = LinkedList(1)
linked_list_between_reverse.append(2)
linked_list_between_reverse.append(3)
linked_list_between_reverse.append(4)
linked_list_between_reverse.append(5)

print(linked_list_between_reverse)
linked_list_between_reverse.leet_between_reverse(1, 3)
print(linked_list_between_reverse)


# =========================
# LEET QUESTION 8 - SWAP PAIRS
# =========================
# Swap adjacent nodes (O(n), O(1))
linked_list_swap = LinkedList(1)
linked_list_swap.append(2)
linked_list_swap.append(3)
linked_list_swap.append(4)
linked_list_swap.append(5)
linked_list_swap.append(6)
linked_list_swap.append(7)

print(linked_list_swap)
linked_list_swap.leet_swap_pairs()
print(linked_list_swap)