#codingal = open("Martinez.txt","x")
with open("victors.txt", "w") as example:
    example.write("Today's lesson is on operations on a file ")
    example.close()
with open("victors.txt", "r") as example:
    print(example.read())


import os
# os.remove("Martinez.txt")

# codingal = open("saturday.txt", "x")
os.remove("saturday.txt")