from collections import deque


class MyStack:

    def __init__(self):
        self.stack = deque()

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        for i in range(len(self.stack) - 1):
            self.push(self.stack.popleft())
        return self.stack.popleft()

    def top(self) -> int:
        number = self.stack[-1]
        return number

    def empty(self) -> bool:
        return not any(self.stack)

stack = MyStack()
stack.push(1)
stack.push(2)
print(stack.top())
print(stack.pop())
print(stack.empty())