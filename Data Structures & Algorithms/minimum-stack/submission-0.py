class MinStack:

    def __init__(self):
        self.stack =[]
        return None

    def push(self, val: int) -> None:
        self.stack.append(val)
        return self

    def pop(self) -> None:
        self.stack.pop()
        return self

    def top(self) -> int:
        return self.stack[-1]
    

    def getMin(self) -> int:
        return min(self.stack)
        
