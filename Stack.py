class Stack():

    def __init__(self, size = 10):
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
                    raise ValueError("Stack is full can not push item" + " " + str(i))
                
        except ValueError as e:
            print(e)
        return self.data
    
    def pop(self):
        if self.ptr > 0:
            self.ptr -= 1
            removed = self.data[self.ptr]
            self.data[self.ptr] = 0
            return removed
        else:
            print("Stack is empty. Cannot pop.")
        return None

elements = [int(element) for element in input("Enter elements seperated by coma: ").split(",") if element.strip()]
stack = Stack(len(elements))

if len(elements) == 0:
    print("Empty Stack, can not push, try inserting some elements")
    elements = [int(element) for element in input().split(",") if element.strip()]
    print(stack.push(elements))
else:
    print(stack.push(elements))


print("Popped elements:", stack.pop())
print("Popped elements:", stack.pop())
print("Data after popping an element:", stack.data)
