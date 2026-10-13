class MinStack():

    def __init__(self):
        self.stack = []
        self.minStack = [float('inf')]

    def push(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.stack.append(value)
        if value <= self.minStack[-1]:
            self.minStack.append(value)

    

        

    def pop(self):
        """
        :rtype: None
        """
        if self.stack[-1] == self.minStack[-1]:
            self.minStack.pop()
        return self.stack.pop()


    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.minStack[-1]
    
        
