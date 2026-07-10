class MyCircularQueue:

    def __init__(self, k):
        self.q = [0] * k        # fixed-size array
        self.size = k
        self.front = -1
        self.rear = -1

    def enQueue(self, value):
        # Check if full
        if self.isFull():
            return False

        # If empty, initialize front
        if self.isEmpty():
            self.front = 0

        # Move rear circularly
        self.rear = (self.rear + 1) % self.size
        self.q[self.rear] = value

        return True

    def deQueue(self):
        # Check if empty
        if self.isEmpty():
            return False

        # If only one element
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            # Move front circularly
            self.front = (self.front + 1) % self.size

        return True

    def Front(self):
        if self.isEmpty():
            return -1
        return self.q[self.front]

    def Rear(self):
        if self.isEmpty():
            return -1
        return self.q[self.rear]

    def isEmpty(self):
        return self.front == -1

    def isFull(self):
        return (self.rear + 1) % self.size == self.front
