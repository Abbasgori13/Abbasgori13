import random
names = []

while len(names) < 4:
    name = input("Enter a user name: ")
    names.append(name)
print(random.choice(names))