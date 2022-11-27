class Fruit():
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def sort_priority(self):
        return self.price

#create list of objects
L = [Fruit("Cherry", 10), Fruit("Apple", 5), Fruit("Blueberry", 20)]

print("-----sorted by price, referencing a class method-----")
for f in sorted(L, key=Fruit.sort_priority):
    print(f.name)

print("\n---- do the same thing using a lambda-----")
for f in sorted(L, key=lambda x: x.sort_priority()):
    print(f.name)
