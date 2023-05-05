class Dog:
    total = 0    

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        Dog.total += 1

lully = Dog("Lully", 3)

print(lully.name)
print(Dog.total)