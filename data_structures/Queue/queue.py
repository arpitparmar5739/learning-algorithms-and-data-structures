class Queue:
    def __init__(self, n):
        self.n = n
        self.q = [None] * n
        self.rear = 0
        self.front = 0

    def enqueue(self, item):
        if self.front == (self.rear+1) % self.n:
            print("Q is full")
            return False
        else:
            self.rear = (self.rear+1) % self.n
            self.q[self.rear] = item
            return True

    def dequeue(self):
        if self.front == self.rear:
            print("Q is empty")
            return False
        else:
            self.front = (self.front+1) % self.n
            item = self.q[self.front]
            return (True, item)


def test_queue():
    q = Queue(5)
    print(q.q)

    print(q.enqueue(1))
    print(q.enqueue(2))
    print(q.enqueue(3))
    print(q.enqueue(4))
    print(q.enqueue(5))

    print(q.q)

    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())

    print(q.q)


if __name__ == "__main__":
    test_queue()