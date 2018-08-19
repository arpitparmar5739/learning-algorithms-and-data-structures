class Stack:
    def __init__(self, MAX):
        self.stack = [None] * MAX
        self.MAX = MAX
        self.top = -1

    def push(self, item):
        if self.top == self.MAX-1:
            return False

        self.top += 1
        self.stack[self.top] = item
        return True

    def pop(self):
        if self.top == -1:
            return False

        self.stack[self.top]
        self.top -= 1
        return True

    def isEmpty(self):
        if self.top == -1:
            return True
        return False


def test_stack():
    stack = Stack(3)
    print(True) if stack.push(1) else print("Stack Overflow")
    print(True) if stack.push(2) else print("Stack Overflow")
    print(True) if stack.push(3) else print("Stack Overflow")
    print(True) if stack.push(4) else print("Stack Overflow")

    print(stack.stack)

    print(True) if stack.pop() else print("Stack Underflow")
    print(True) if stack.pop() else print("Stack Underflow")
    print(True) if stack.pop() else print("Stack Underflow")
    print(True) if stack.pop() else print("Stack Underflow")


if __name__ == "__main__":
    test_stack()
