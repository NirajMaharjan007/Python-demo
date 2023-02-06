# class inherite

class Animal:
    def walk(self):
        print("walking")


class Dog(Animal):
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(self.name+"barking")


class Cat(Animal):
    def __init__(self, name):
        self.name = name

    def meow(self):
        print(self.name+" meow")


cat = Cat("Catty")
dog = Dog("Doggy")

cat.walk()
dog.walk()

cat.meow()
dog.bark()
