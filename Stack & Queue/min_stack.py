# Leetcode no.155 - Min Stack

class MinStack(object):
    def __init__(self):
        self.stack = []
        
    def push(self, val):
        if len(self.stack) == 0:
            self.stack.append([val, val])
        else:
            mini = min(self.stack[-1][1], val)
            self.stack.append([val, mini])
               
    def pop(self):
        if self.stack:
            self.stack.pop()
        
    def top(self):
        if not self.stack:
            return None
        return self.stack[-1][0]
        
    def getMin(self):
        if not self.stack:
            return None
        return self.stack[-1][1]
    
# Example usage
if __name__ == "__main__":
    obj = MinStack()
    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)

    print(f"getMin(): {obj.getMin()}")  # -3
    obj.pop()
    print(f"top(): {obj.top()}")        # 0
    print(f"getMin(): {obj.getMin()}")  # -2
    
        