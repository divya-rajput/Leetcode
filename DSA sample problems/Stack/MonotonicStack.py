class MonotonicStack:
    #initializing the stack
    def __init__(self):
        self.stack = []
        self.min = []
    
    #defining the stack push operation
    def stackPush(self,element):
        self.stack.append(element)
        if not self.min or element <= self.stackMin():
            self.min.append(element)
        else:
            self.min.append(self.min[-1])
    
    #defining the pop operation in stack

    def stackPop(self):
        element = self.stack.pop()
        self.min.pop()
        return element

    #returning the top element in stack

    def stackMin(self):
        return self.min[-1]

#Main method
if __name__ == "__main__":
    monoStack = MonotonicStack()
    monoStack.stackPush("5")
    monoStack.stackPush("6")
    monoStack.stackPush("3")
    monoStack.stackPush("7")
    monoStack.stackPush("1")
    
    print(monoStack.stackMin())


