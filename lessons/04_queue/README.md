# Queue (Linked List Implementation)

## Definition

A queue is a linear data structure that follows the **FIFO (First In, First Out)** principle.

- The first element added is the first one removed
- Think of a queue like a line of people waiting

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

- `first` → the front of the queue
- `last` → the end of the queue
- `length` → number of elements

```python
class Queue:
    def __init__(self, value=None):
        self.first = None
        self.last = None
        self.length = 0
```

---

## Visual Representation

```
First              Last
 ↓                   ↓
[7] → [23] → [3] → [11] → None
```

- Elements are added at the **end (enqueue)**
- Elements are removed from the **front (dequeue)**

---

## Time Complexity

| Operation | Time Complexity |
|----------|----------------|
| Enqueue  | O(1)           |
| Dequeue  | O(1)           |
| Peek     | O(1)           |

All operations are constant time because they only modify the ends of the list.

---

## Advantages

- Fast enqueue and dequeue operations (O(1))
- Simple implementation
- No need for contiguous memory

---

## Disadvantages

- No random access
- Limited to FIFO access pattern

---

## Example Usage

```python
my_queue = Queue()

my_queue.enqueue(7)
my_queue.enqueue(23)
my_queue.enqueue(3)
my_queue.enqueue(11)

print(my_queue)         # 7 -> 23 -> 3 -> 11
print(my_queue.peek())  # 7

print(my_queue.dequeue())  # 7
print(my_queue)            # 23 -> 3 -> 11
```

---

## When to Use a Queue

Queues are useful when:

- Processing tasks in order
- Breadth-first search (BFS)
- Scheduling systems
- Handling asynchronous data (buffers)

---

## Implemented Methods

- [x] enqueue
- [x] dequeue
- [x] peek

---

## Key Takeaways

- Queue follows **FIFO (First In, First Out)**
- Requires both **head and tail pointers** for O(1) operations
- Efficient for ordered processing of data
- Common in real-world systems and algorithms