from .queue import Queue

# =========================
# BASIC OPERATIONS
# =========================

# Initialize empty queue
my_queue = Queue()
print(my_queue)

# Put item into empty queue
my_queue.enqueue(7)
print(my_queue)

# Put items in non-empty queue
my_queue.enqueue(23)
my_queue.enqueue(3)
my_queue.enqueue(11)
print(my_queue)
print(f"first = {my_queue.first.value}, last = {my_queue.last.value}")

# Peek at top value
print(f"front = {my_queue.peek()}")

# Dequeue from first of queue
print(my_queue.dequeue())
print(my_queue)
print(my_queue.dequeue())
print(my_queue)
print(my_queue.dequeue())
print(my_queue)
print(my_queue.dequeue())
print(my_queue)

# Dequeue off of empty queue - return None
print(my_queue.dequeue())
print(my_queue)
