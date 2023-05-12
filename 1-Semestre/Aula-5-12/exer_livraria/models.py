class Author:
    def __init__(self, name, nickname, age):
        self.name = name
        self.nickname = nickname
        self.age = age

class Book:
    def __init__(self, isBn, name, Author):
        self.isBn = isBn
        self.name = name
        self.Author = Author