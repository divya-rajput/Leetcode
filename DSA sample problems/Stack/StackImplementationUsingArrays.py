class Stack(object):
    def __init__(self,limit = 10):
        self.stk = []
        self.limit = limit
    #Checking if the stack is empty
    def isEmpty(self):
        return len(self.stk) <= 0
    #Insertion operation
    def push(self,item):
        if len(self.stk) >= self.limit:
            print("Stack Overflow!!")
            return
        else:
            self.stk.append(item)
            print("Pushed Item-", item)

    #Deletion operation
    def pop(self):
        if len(self.stk) <= 0:
            print("Stack Underflow!!!")
            return
        else:
            return self.stk.pop()

    #Peek operation
    def peek(self):
        if len(self.stk) <= 0:
            print("Stack Underflow!!!")
            return
        else:
            return self.stk[-1]

if __name__ == "__main__":
    print("********Stack Implementation*********")
    ourStack = Stack(5)
    ourStack.push("10")
    ourStack.push("13")
    ourStack.push("15")
    print("Popped Item =", ourStack.pop())
    print("Last Item in stack =", ourStack.peek())
    print("Popped Item =", ourStack.pop())
    print("Last Item in stack =", ourStack.peek())
