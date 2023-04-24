class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise Exception("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None

    def size(self):
        return len(self.stack)

def is_balanced(string):
    opening = "([{"
    closing = ")]}"
    stack = Stack()

    for char in string:
        if char in opening:
            stack.push(char)
        elif char in closing:
            if stack.is_empty():
                return "Несбалансированно"
            top_char = stack.pop()
            if opening.index(top_char) != closing.index(char):
                return "Несбалансированно"

    if stack.is_empty():
        return "Сбалансированно"
    else:
        return "Несбалансированно"

example1 = '(((([{}]))))'
print(is_balanced(example1))

example2 = '{{[(])]}}'
print(is_balanced(example2))