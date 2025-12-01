import os

### Part one ###
inputPath = os.path.join(os.getcwd(),"input","input_day1.txt")

inputarray = [line.rstrip() for line in open(inputPath,"r")]

current = 50
password = 0

for line in inputarray:
    if line[0] == "L":
        current=(current - int(line[1:])) % 100
    else:
        current=(current + int(line[1:])) % 100
    if current == 0:
            password +=1

print (password)


