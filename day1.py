import os

inputPath = os.path.join(os.getcwd(),"input","input_day1.txt")
inputarray = [line.rstrip() for line in open(inputPath,"r")]

current = 50
password = 0

### Part one ###

# for line in inputarray:
#     if line[0] == "L":
#         current=(current - int(line[1:])) % 100
#     else:
#         current=(current + int(line[1:])) % 100
#     if current == 0:
#         password +=1

# print (password)

### Part two ###

for line in inputarray:
    steps = int(line[1:])
    for i in range(steps):
        if line[0] == "L": 
            current = (current - 1) % 100
        else:
            current = (current + 1) % 100
        if current == 0:
            password += 1

print (password)

