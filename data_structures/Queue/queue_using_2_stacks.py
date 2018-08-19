from data_structures.Stack.stack import Stack


class QueueUsingTwoStacks:
    def __init__(self, n):
        self.S1 = Stack(n)
        self.S2 = Stack(n)

    def insert(self, stack, item):
        if stack.push(item):
            return True
        return False

    def delete(self, stack):
        if stack.pop():
            return True
        return False

    def enqueue(self, item):
        if self.insert(self.S1, item):
            return True

        return False

    def dequeue(self):
        if self.S2.isEmpty():
            if self.S1.isEmpty():
                return False
            else:
                while not self.S1.isEmpty():
                    x = self.S1.pop()
                    self.S2.push(x)

        self.delete(self.S2)
        return True


def main():
    q = QueueUsingTwoStacks(4)

    print(True) if q.enqueue(1) else print("Q is full")
    print(True) if q.enqueue(2) else print("Q is full")
    print(True) if q.enqueue(3) else print("Q is full")
    print(True) if q.enqueue(4) else print("Q is full")
    print(True) if q.enqueue(5) else print("Q is full")

    print(True) if q.dequeue() else print("Q is empty")
    print(True) if q.dequeue() else print("Q is empty")
    print(True) if q.dequeue() else print("Q is empty")
    print(True) if q.dequeue() else print("Q is empty")
    print(True) if q.dequeue() else print("Q is empty")


def test_queue_using_2_stacks():
    main()
