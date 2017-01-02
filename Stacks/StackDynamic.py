# Stack implementation using builtin data structure List.
# List is in itself uses LIFO order.


class Stack:
    def __init__(self):
        self.stklist = []
        self.length = -1

    def push(self, data=None):
        self.stklist.append(data)
        self.length += 1

    def pop(self):
        if self.length < 0:
            raise ValueError("UnderFlow!")
        else:
            self.stklist.pop()
            self.length -= 1

    def peek(self):
        if self.length < 0:
            raise ValueError("Peeking Into Empty Stack!")
        else:
            return self.stklist[self.length]

    def stack_length(self):
        return self.length+1