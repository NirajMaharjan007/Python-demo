# class -> blue print and always nouns

class Person():
    # OOP operation
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        print("Person name: " + self.name + " age: " +
              str(self.age) + " gender: " + self.gender)

    # encapsulation
    # def get_age(self):
    #     return self.age


print()
person = Person("Niraj", 80, "M")
# print(person.get_age())
print(person.age)
print()


class Animal():
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name + " is Eating")


class Dog(Animal):
    # it override the parent class __init__ if we use init
    # def __init__(self, age, gender):
    #     self.age = age
    #     self.gender = gender
    #

    def bark(self):
        print(self.name+" is Barking")
        # print("Barking")


class Cat(Animal):
    def meow(self):
        print(self.name+" meow")


dog = Dog("Doggy")
dog.eat()
dog.bark()
print()
cat = Cat("Catty")
cat.eat()
cat.meow()

# cat.bark can not be used because in cat has no def bark but in dog
