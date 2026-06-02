from collections import deque

class MyStack:
    def __init__(self):
        self.q=deque()

    def push(self, x: int) -> None:
        s=len(self.q)
        self.q.append(x)
        for _ in range(s): #move elements imp
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        if self.empty():
            return None
        return self.q.popleft()

    def top(self) -> int:
        if self.empty():
            return None        
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q)==0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()