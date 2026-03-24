# Doubly Linked List

## Definition

A doubly linked list is a linear data structure where each element (node) contains:

- a value
- a reference (pointer) to the next node
- a reference (pointer) to the previous node

Unlike arrays, elements are not stored contiguously in memory.

---

## Node Structure

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
```

---

## Visual Representation

```
None ← [10] ⇄ [20] ⇄ [30] → None
         ↑              ↑
        Head           Tail
```

Each node points **forward and backward**, allowing traversal in both directions.

---

## Time Complexity

| Operation        | Time Complexity |
| ---------------- | --------------- |
| Access           | O(n)            |
| Search           | O(n)            |
| Insert at Head   | O(1)            |
| Insert at Tail   | O(1)            |
| Insert in Middle | O(n)            |
| Delete at Head   | O(1)            |
| Delete at Tail   | O(1)            |
| Delete in Middle | O(n)            |
| Reverse          | O(n)            |

---

## Why Access Is O(n)

Like singly linked lists, doubly linked lists do not support direct indexing.

However, they improve traversal by allowing movement from **both ends**:

```
head → → → ← ← ← tail
```

This enables optimized access:

```python
if index < length // 2:
    # traverse from head
else:
    # traverse from tail
```

---

## Advantages

- Bidirectional traversal (forward and backward)
- More efficient deletions (no need to track previous node)
- Optimized traversal (can start from head or tail)
- Efficient insertions and deletions at both ends

---

## Disadvantages

- Extra memory usage (two pointers per node)
- More complex pointer management
- Slightly more overhead than singly linked lists

---

## Example Usage

```python
my_list = DoublyLinkedList(10)
my_list.append(20)
my_list.append(30)

print(my_list)  # 10 -> 20 -> 30
```

---

## When to Use a Doubly Linked List

Doubly linked lists are useful when:

- You need to traverse in both directions
- Frequent insertions and deletions occur at both ends
- You need efficient removal of arbitrary nodes
- You want faster average traversal than a singly linked list

---

## Implemented Methods

- [x] get (optimized from head/tail)
- [x] set_value
- [x] append
- [x] prepend
- [x] insert
- [x] remove
- [x] pop
- [x] pop_first
- [x] reverse
- [x] clear
- [x] palindrome checker
- [x] partition list
- [x] reverse sublist
- [x] swap pairs

---

## Key Takeaways

- Doubly linked lists improve upon singly linked lists by adding backward traversal
- They provide **better real-world performance** for many operations
- Trade-off: extra memory for improved flexibility
- Common interview topics:
  - reverse a doubly linked list
  - insert/remove at index
  - optimize traversal from head vs tail
