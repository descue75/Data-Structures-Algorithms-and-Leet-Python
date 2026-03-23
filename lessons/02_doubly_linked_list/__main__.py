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