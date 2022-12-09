# Conversions

a = 1
b = 2.4

c = int(b)
d = float(a)

print(c)
print(type(c))

print(d)
print(type(d))


name = "Student"  # Last index never used
print(name[3:7])  # answer dent

quantity = 3
item = 567
price = 49.49

# Ordering according to index
order = "I want to {2} dollars for {0} pieces of item {1}"

print(order.format(quantity, item, price))
