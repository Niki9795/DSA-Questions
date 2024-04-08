class Queue():

    def __init__(self, size):
        self.size = size
        self.data = [0] * size
        self.ptr = 0

    def push(self, elements):
        try:
            for i in elements:
                if self.ptr < len(self.data):
                    self.data[self.ptr] = i
                    self.ptr += 1
                else:
                    raise ValueError("Queue is full can not add item" + " " + str(i))
        except ValueError as e:
            print(e)
        return self.data
    
    def pop(self):
        removed = self.data[0] 

        for i in range(1,self.ptr):
            self.data[i - 1] = self.data[i]
            self.data[i] = 0
        self.ptr -= 1
        return removed
    
elements = [int(element) for element in input("Enter elements seperated by coma: ").split(",") if element.strip()]
queue = Queue(len(elements))

if len(elements) == 0:
    print("Empty Stack, can not push, try inserting some elements")
    elements = [int(element) for element in input().split(",") if element.strip()]
    print(queue.push(elements))
else:
    print(queue.push(elements))


print("Popped elements:", queue.pop())
print("Popped elements:", queue.pop())
print("Data after popping an element:", queue.data)
