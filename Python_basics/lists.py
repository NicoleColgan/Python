import random

list = ["2","1", "3"]
print(list[-1])
print(list[0:2])
print(list[:2])
print(list[:2])
#how many numbers to increase by each time
print(list[::2])
list.append("0")
print(list)
list.remove("3")
print(list)
list.pop()
print(list)
list.sort()
print(list)
#help(list)
list[0] = "7"
print(list)
list.insert(0,"11")
print(list)

for item in list:
    print(item)

# pick random number in this list
print(f"chosen at random={random.choice(list)}")