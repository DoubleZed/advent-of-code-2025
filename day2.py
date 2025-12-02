import os
day="2"

inputfile = "input_day" + day + ".txt"
inputPath = os.path.join(os.getcwd(),"input",inputfile)
inputarray = [x for x in open(inputPath).read().split(",")]

def part1 (inputarr):
    invalidcount = 0
    invalidsum = 0
    for idrange in inputarr:
        splitted = idrange.split("-")
        for id in range(int(splitted[0]),int(splitted[1])+1):
            if abs(id) < 100 or abs(id) > 999:
                halfid = str(id)
                leftid, rightid = halfid[:len(halfid)//2], halfid[len(halfid)//2:]
                if leftid == rightid:
                    invalidcount += 1
                    invalidsum = invalidsum + int(halfid)
    return (invalidsum)

print(part1(inputarray))              

