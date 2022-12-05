def sum(a, b):
    '''
    Addition of two numbers
    Parameters:
        a(int):value to add
        b(int):value to add
    Returns:
        int : Sum of two values
    '''
    return a+b


s = sum(5, 4)
print(s)


def name():
    '''
    Input from user and returns name from the user
    Parameter:
        None
    Return:
        printed name
    '''
    name = input('Enter your name:')
    return ("Your name is: " + name)


string = name()
print(string)
print(type(string))
