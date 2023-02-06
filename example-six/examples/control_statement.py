age = int(input("Enter a age:"))

if (age >= 18 and age < 50):
    print("Yes, you can vote")
elif age >= 50:
    print("Yes, you can vote but you are too old")
else:
    print("No, you can't vote")
