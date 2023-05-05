class Dog:
    total = 0    

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Dog.total += 1

    def details(self):
        return f"{self.name} is {self.age} years old"

    def bark(self, sound="Woof Woof"):
        return f"{self.name} barks {sound}"

    
