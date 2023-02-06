def sub(num1, num2):
    '''
        Parameter num1 and num2
        Return num1 - num2
    '''
    return num1-num2


writer = open("./example-six/revise/doc_string.txt", 'w')
print(sub.__doc__)
writer.write(sub.__doc__)
print(sub(4, 6))
