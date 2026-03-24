class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        next_val = self.next.value if self.next else None
        return f"value: {self.value}, next: {next_val}"