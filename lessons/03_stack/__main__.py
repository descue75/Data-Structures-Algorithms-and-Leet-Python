from .stack import Stack

# =========================
# BASIC OPERATIONS
# =========================

# Initialize stack with one element
my_stack = Stack(7)

# Push items on stack
my_stack.push(23)
my_stack.push(3)
my_stack.push(11)
print(my_stack)

# Peek at top value
print(f"top = {my_stack.peek()}")

# Pop items off stack
print(my_stack.pop())
print(my_stack)
print(my_stack.pop())
print(my_stack)
print(my_stack.pop())
print(my_stack)
print(my_stack.pop())
print(my_stack)

# Pop item off of empty stack - return None
print(my_stack.pop())
print(my_stack)
