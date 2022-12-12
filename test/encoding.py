# for encrpting using pip install cryptography
# imported
from cryptography.fernet import Fernet

print("encoding")

# Opening from file
f = open("test/file.txt")

r = f.read()

print("---------------------------Not Encoded---------------------------")
print(r)
print("--------------------------------------------------------------\n")

# Assigning the values
key = Fernet.generate_key()
fernet = Fernet(key)

# used encoding procesing
encMessage = fernet.encrypt(r.encode())
print("\n---------------------------Encoded---------------------------")
print(encMessage)
print("--------------------------------------------------------------\n")
