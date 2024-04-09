class Duplicate():

    def __init__(self, array):
        self.array = array

    def containDuplicate(self):

        unique = set()

        for element in self.array:
            if element in unique:
                return f"This array has duplicate element"
            unique.add(element)
        return f"This array does not has duplicate element"
    
array = [int(element) for element in input("Eneter elements seperated by coma: ").split(",") if element.strip()]
duplicate = Duplicate(array)
print(duplicate.containDuplicate())