class MyStack:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__elements = []

    def is_empty(self):
        return len(self.__elements) == 0

    def is_full(self):
        return len(self.__elements) == self.__capacity

    def pop(self):
        if self.is_empty():
            print('Stack is empty')
            return None
        else:
            return self.__elements.pop()

    def push(self, value):
        if self.is_full():
            print('Stack is full')
        else:
            self.__elements.append(value)

    def top(self):
        if self.is_empty():
            print('Stack is empty')
            return None
        else:
            return self.__elements[-1]

# Example usage of MyStack
stack1 = MyStack(capacity=5)
stack1.push(1)
stack1.push(2)
print(stack1.is_full())   # False
print(stack1.top())       # 2
print(stack1.pop())       # 2
print(stack1.top())       # 1
print(stack1.pop())       # 1
print(stack1.is_empty())  # True
