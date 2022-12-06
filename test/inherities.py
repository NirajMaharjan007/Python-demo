class Animal():
    def __init__(self, name):
        self.name = name
        print("Animal name: " + self.name)

    def walk(self):
        print(self.name + " walks")

    def eat(self):
        print(self.name + " eats")


class Dog(Animal):
    def bark(self):
        print(self.name + " bark")


class Cat(Animal):
    def meow(self):
        print(self.name + " meow")


dog = Dog("Doggy")

dog.bark()
dog.eat()

cat = Cat("Catty")
cat.meow()
cat.walk()
