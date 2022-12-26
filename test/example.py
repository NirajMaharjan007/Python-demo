def function(a, b):
    '''
        def name is function setting two parameter
        Parameter=> two parameters
        Return=> None / Void
        if a or b is equal exam it breaks
    '''
    # while (a != "exam" or b != "exam"): => we can also do this too
    while (True):
        if a != "exam" and b != "exam":
            print("Learning Python")

        if (a == "exam") or (b == "exam"):
            print("Forgetting Everything")
            break


a = input("Enter a first name: ")
b = input("Enter a second name: ")

function(a, b)
