# class Exam:
#     '''
#         Class name is Exam
#         init or Passing two variable
#     '''

#     def __init__(self, a, b):
#         self.a = a
#         self.b = b

#     def set_exam(self):
#         '''
#             def name is set_exam
#             return => void
#             two input is given
#         '''

#         exam_one = input("Enter a exam for " + self.a + ": ")
#         exam_two = input("Enter a exam for " + self.b + ": ")

#         if exam_one == "exam":
#             print(self.a + " has forgotten")

#         if exam_two == "exam":
#             print(self.b + " has forgotten")

#         if exam_one != "exam":
#             print(self.a + " has not forgotten")

#         if exam_two != "exam":
#             print(self.b + " has not forgotten")

#         else:
#             print("not found")


# a = input("Enter a first name: ")
# b = input("Enter a second name: ")

# c = Exam(a, b)
# c.set_exam()

# Another method


class A:
    '''
        Class name A
        Parameter passed String variable "a"
        Methods:
            check_exam()
                Check if variable 'a' has forgotten Python or not
    '''

    def __init__(self, name):
        self.name = name

    def check_exam(self):
        '''
            Check if variable 'a' has forgotten Python or not
            Parameter => no parameter 
            Return => void
        '''
        exam = input("Checking for Exam... for " + self.name + ": ")

        if exam == "exam":
            print(self.name + " has forgotten a Python")

        else:
            print(self.name + " has not forgotten a Python")


# a = input("Enter a name: ")
# b = input("Enter another name: ")

object_one = A("Niraj")
object_two = A("Maharjan")

# object_one.check_exam()
# object_two.check_exam()

print(object_one.__doc__)
print(object_one.check_exam.__doc__)

# Here \ after object_one.__doc__ + means enter
doc_string = "For class: " + object_one.__doc__ + \
    "\nFor method: " + object_one.check_exam.__doc__

# file_create = open("docstring.txt", "x")  # => new file created

file_write = open("docstring.txt", "a")
file_write.write(doc_string)
