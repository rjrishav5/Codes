class queue:
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
    
    def enqueue(self,data):
        self.items.append(data)
        return "The data is added to the last element!"
    
    def dequeue(self):
        if self.isEmpty():
            return "The queue is empty"
        else:     
            return self.items.pop(0)
    def peek(self):
        if self.isEmpty():
            return "The queue is empty"
        else:
            return self.items[-1]
    def delete(self):
         self.items = None
custom = queue()
custom.enqueue(1)
custom.enqueue(2)
custom.enqueue(3)
custom.enqueue(4)
print(custom)
print(custom.peek())
print(custom.dequeue())
print(custom.dequeue())
print(custom)