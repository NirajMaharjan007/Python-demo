def largest(a, b, c):
    if (a > b) and (a > c):
        return str(a) + " is the largest"

    elif (b > a) and (b > c):
        return str(b) + " is the largest"

    elif (c > a) and (c > b):
        return str(c) + " is the largest"

    else:
        return "Maybe equal to each other"


def smallest(a, b, c):
    if (a < b) and (a < c):
        return str(a) + " is the smallest"

    elif (b < a) and (b < c):
        return str(b) + " is the smallest"

    elif (c < a) and (c < b):
        return str(c) + " is the smallest"

    else:
        return "Maybe equal to each other"


a = 8
b = 50
c = 6

print(largest(a, b, c))
print(smallest(a, b, c))
