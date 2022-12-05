def calculation():
    print("Given number is: " + str(a) + " and " + str(b))
    print("------------------------------------------")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("------------------------------------------")

    c = int(input("enter a choice: "))

    if c == 1:
        print("Addition:", a+b)

    # elif can do
    if c == 2:
        print("Subtraction:", a-b)

    if c == 3:
        print("Multiplication:", a*b)

    if c == 4:
        print("Division:", float(a)/float(b))


a = int(input("enter a first number: "))
b = int(input("enter a second number: "))

calculation()
