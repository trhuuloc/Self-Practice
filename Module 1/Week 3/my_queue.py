class MyQueue:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__elements = []

    def is_empty(self):
        return len(self.__elements) == 0

    def is_full(self):
        return len(self.__elements) == self.__capacity

    def dequeue(self):
        if self.is_empty():
            print('Queue is empty')
            return None
        else:
            return self.__elements.pop(0)

    def enqueue(self, value):
        if self.is_full():
            print('Queue is full')
        else:
            self.__elements.append(value)

    def front(self):
        if self.is_empty():
            print('Queue is empty')
            return None
        else:
            return self.__elements[0]

# Example usage of MyQueue
queue1 = MyQueue(capacity=5)
queue1.enqueue(1)
queue1.enqueue(2)
print(queue1.is_full())  # False
print(queue1.front())    # 1
print(queue1.dequeue())  # 1
print(queue1.front())    # 2
print(queue1.dequeue())  # 2
print(queue1.is_empty()) # True
