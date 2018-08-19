class Stack:
    def __init__(self, MAX):
        self.stack = [None] * MAX
        self.MAX = MAX
        self.top = -1

    def push(self, item):
        if self.top == self.MAX-1:
            print("Stack overflow")
            return False

        self.top += 1
        self.stack[self.top] = item
        return True

    def pop(self):
        if self.top == -1:
            print("Stack underflow")
            return False

        self.stack[self.top]
        self.top -= 1
        return True


if __name__ == "__main__":
    stack = Stack(3)
    print(stack.push(1))
    print(stack.push(2))
    print(stack.push(3))
    print(stack.push(4))

    print(stack.stack)

    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
