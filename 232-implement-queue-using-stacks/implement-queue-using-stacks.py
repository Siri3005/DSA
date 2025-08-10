class MyQueue(object):

    def __init__(self):
        self.stack=[]

    def push(self, x):
        self.stack.append(x)
        

    def pop(self):
        ele=self.stack.pop(0)
        return ele
        

    def peek(self):
        return self.stack[0]
        

    def empty(self):
        return len(self.stack)==0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()