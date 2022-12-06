# try and catch in Python
try:
    num = int(input("Enter a number: "))
    if (num <= 0):
        raise Exception("The number is negative or zero!")  # Exception message

    elif (num % 2) == 0:
        print("The number is even!")

    else:
        print("The number is odd!")

except Exception as e:
    print("Error: " + str(e))
