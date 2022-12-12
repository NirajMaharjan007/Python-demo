# if else control flow

a = int(input("Enter a first number: "))
b = int(input("Enter a second number: "))

if a > b:
    print(str(a) + " is greater than " + str(b))

elif a < b:
    print(str(b) + " is greater than " + str(a))

else:
    print("Both numbers are equal")
