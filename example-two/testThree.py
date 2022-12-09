li = ["p", 1, "Hello world!"]
print(li)

li.append(9.5)


li2 = li.copy()  # does not change value
li.append("hello")
li3 = li

print(li2)
print(li3)

print(li.pop())

name = "name"
print(name[::-1])  # whole index with one gap with last

li.reverse()
print(li)
