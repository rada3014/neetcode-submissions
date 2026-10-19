import math
class MinStack:

    def __init__(self):
        self.stack =[]
        self.smallstack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.smallstack:
            self.smallstack.append(val)
        else:
            if val<=self.smallstack[-1]:
                self.smallstack.append(val)
        
        return None

    def pop(self) -> None:

        if self.smallstack[-1] == self.stack[-1]:
            self.smallstack.pop()

        self.stack.pop()
        return None

    def top(self) -> int:
        return self.stack[-1]
    
    def getMin(self) -> int:
        return self.smallstack[-1]
        
