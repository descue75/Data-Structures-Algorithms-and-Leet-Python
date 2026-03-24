# Stack (Linked List Implementation)

## Definition

A stack is a linear data structure that follows the **LIFO (Last In, First Out)** principle.

- The last element added is the first one removed
- Think of a stack like a stack of plates

---

## Node Structure

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
```

---

## Structure

This implementation uses a singly linked list with:

- `top` → the top element of the stack
- `height` → number of elements

```python
class Stack:
    def __init__(self, value=None):
        self.top = None
        self.height = 0
```

---

## Visual Representation

```
Top
 ↓
[11] → [3] → [23] → [7] → None
```

- New elements are added at the **top**
- Elements are removed from the **top**

---

## Time Complexity

| Operation | Time Complexity |
| --------- | --------------- |
| Push      | O(1)            |
| Pop       | O(1)            |
| Peek      | O(1)            |

All operations are constant time because they only modify the top of the stack.

---

## Advantages

- Fast push and pop operations (O(1))
- Simple implementation
- No need for contiguous memory

---

## Disadvantages

- No random access
- Limited to LIFO access pattern

---

## Example Usage

```python
my_stack = Stack(7)

my_stack.push(23)
my_stack.push(3)
my_stack.push(11)

print(my_stack)        # 11 -> 3 -> 23 -> 7
print(my_stack.peek()) # 11

print(my_stack.pop())  # 11
print(my_stack)        # 3 -> 23 -> 7
```

---

## When to Use a Stack

Stacks are useful when:

- Reversing data
- Undo/redo operations
- Parsing expressions
- Backtracking algorithms (DFS, recursion)

---

## Implemented Methods

- [x] push
- [x] pop
- [x] peek

---

## Key Takeaways

- Stack follows **LIFO (Last In, First Out)**
- Best implemented using **linked list head operations**
- All primary operations run in **O(1) time**
- Common interview structure with many practical uses
