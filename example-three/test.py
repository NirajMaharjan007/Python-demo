def evaluate(name, a):
    if a > 80:
        return (name + " has got distinction with marks:" + str(a))

    elif a > 60:
        return (name + " has got 1st division with marks:" + str(a))

    elif a > 40:
        return (name + " has got 2nd division with marks:" + str(a))

    elif a < 41 and a > 30:
        return (name + " has got 3rd division with marks:" + str(a))

    else:
        return (name + " has Failed with: " + str(a))


name = input("Name: ")
a = int(input("Enter a total marks:"))

print(evaluate(name, a))
