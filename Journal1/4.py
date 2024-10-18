class animal:
    def __init__(self,name,age):
        self.lenArms = 3.2
        self.lenLegs = 3.5
        self.numEyes = 2
        self.hasTail = True
        self.isFurry = False
    def print_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Length of Arms: {self.lenArms}")
        print(f"Length of Legs: {self.lenLegs}")
        print(f"Number of Eyes: {self.numEyes}")
        print(f"Has Tail: {self.hasTail}")
        print(f"Is Furry: {self.isFurry}")
    
def main():
    favoriteAnimal = animal()
    favoriteAnimal.print_info()
    
if __name__ == "__main__":
    main()