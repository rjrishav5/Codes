class stack:
    def __init__(self):
        self.items = []
    
    def __str__(self):
        values = [str(x) for x in self.items]
        return " ".join(values)

    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False
    def peek(self):
        if self.isEmpty():
            return "The stack is empty"
        else:
            return self.items[0]
    def push(self,data):
        self.items.append(data)
    
    def pop(self):
        if self.isEmpty():
            return "The stack is empty"
        else:
            return self.items.pop()
    def delete(self):
        self.items = None
custom = stack()

custom.push(1)
custom.push(2)
custom.push(3)
custom.push(4)

print(custom)
print(custom.peek())
print(custom.pop())
print(custom)