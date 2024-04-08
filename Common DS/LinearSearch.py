class LinearSearch():

    def __init__(self, array, target):
        self.array = array
        self.target = target

    def linearSearch(self):
        found = False
        for i in self.array:
            if i == self.target:
                print(f"Found {self.target} in the given array")
                found = True
                break
        if not found:
            print(f"{self.target} is not found in the given array")

array = [int(n) for n in input("Enter the elements of an array seperated by comma\n").split(",") if n.strip()]
target = int(input("Enter an element to search in an array\n"))
linearsearch = LinearSearch(array, target)
linearsearch.linearSearch()