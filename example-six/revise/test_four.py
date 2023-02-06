class Person:
    __name = "Niraj"

    def name(self, name):
        self.__name = name

    def birth_date(self, date):
        print(self.__name + "'s birth date => " + date)

    def walk(self):
        print(self.__name+" is walking")


person = Person()
person.birth_date("2002-2-2")
person.walk()

person_2 = Person()
person_2.name("Sijian")
person.birth_date("2002-2-2")
person.walk()
