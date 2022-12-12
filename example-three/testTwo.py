a = 6
b = 4


print(a) if a > b else print(b)

# For loop

for i in range(2, 4):
    print(i, end=" ")

print()

for i in (2, 4):
    print(i, end=" ")

print()

for i in range(7):
    if i < 6:
        x = "6 is lesser"
    else:
        x = "6 is greater"

    print(x)

print()


def looper(a, b):
    for i in range(a, b, -1):
        print(i, end=" ")


looper(7, 1)

print()

a = [5, 6, 8, 9, 2]

a.sort()
j = len(a)-1

for i in a:
    while j >= 0:
        print(a[j], end=" ")
        j -= 1

b = [9, 8, 2, 1, 6, 5]

length = len(b)

print()
# Bubble sort
for i in range(length-1):
    for j in range(length-1):
        if (b[j+1] > b[j]):
            temp = b[j]
            b[j] = b[j+1]
            b[j+1] = temp

print(b)
