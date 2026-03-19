# Linked List

## Definition

A linked list is a linear data structure where each element (node) contains:

- a value
- a reference (pointer) to the next node in the sequence

Unlike arrays, elements are not stored contiguously in memory.

---

## Node Structure

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
```

---

## Visual Representation

```
Head
 ↓
[10 | •] → [20 | •] → [30 | •] → None
                       ↑
                      Tail
```

Each node points to the next node in the sequence.

---

## Time Complexity

| Operation        | Time Complexity |
| ---------------- | --------------- |
| Access           | O(n)            |
| Search           | O(n)            |
| Insert at Head   | O(1)            |
| Insert at Tail   | O(1)\*          |
| Insert in Middle | O(n)            |
| Delete at Head   | O(1)            |
| Delete in Middle | O(n)            |
| Reverse          | O(n)            |

> _O(1) for tail insertion assumes a tail pointer is maintained._

---

## Why Access Is O(n)

Unlike arrays, linked lists cannot directly access an index.

To reach a specific position, you must traverse from the head node step-by-step:

```
index 0 → index 1 → index 2 → ...
```

---

## Advantages

- Dynamic size (no fixed capacity)
- Efficient insertions and deletions (especially at the head)
- No need for contiguous memory allocation

---

## Disadvantages

- No random access (must traverse sequentially)
- Extra memory overhead for pointers
- More complex than arrays for many operations

---

## Example Usage

```python
my_list = LinkedList(10)
my_list.append(20)
my_list.append(30)

print(my_list.head.value)  # Output: 10
```

---

## When to Use a Linked List

Linked lists are a good choice when:

- Frequent insertions and deletions are required
- The size of the data structure is unknown or dynamic
- Sequential access is acceptable

---

## Implemented Methods

- [x] append
- [x] prepend
- [x] insert
- [x] remove
- [x] reverse
- [x] find middle
- [x] detect loop
- [x] kth from end
- [x] remove duplicates (with and without set)
- [x] binary to decimal
- [x] partition list
- [x] reverse sublist
- [x] swap pairs

---

## Key Takeaways

- Linked lists trade **fast access** for **fast modification**
- Best used when structure changes frequently
- Common interview topics:
  - reversing a list
  - detecting cycles
  - finding the middle node
  - removing duplicates
