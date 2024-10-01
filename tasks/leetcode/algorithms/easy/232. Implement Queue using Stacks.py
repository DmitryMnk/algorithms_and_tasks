from collections import deque

class MyQueue:

    def __init__(self):
        self.my_queue = deque()

    def push(self, x: int) -> None:
        self.my_queue.append(x)

    def pop(self) -> int:
        return self.my_queue.popleft()

    def peek(self) -> int:
        return self.my_queue[0]

    def empty(self) -> bool:
        return not any(self.my_queue)
