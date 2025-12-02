import os
day="2"

inputfile = "input_day" + day + ".txt"
inputPath = os.path.join(os.getcwd(),"input",inputfile)
inputarray = [x for x in open(inputPath).read().split(",")]

def part1 (inputarr):
    invalidsum = 0
    for idrange in inputarr:
        splitted = idrange.split("-")
        for id in range(int(splitted[0]),int(splitted[1])+1):
            if abs(id) < 100 or abs(id) > 999:
                halfid = str(id)
                leftid, rightid = halfid[:len(halfid)//2], halfid[len(halfid)//2:]
                if leftid == rightid:
                    invalidsum =+ int(halfid)
    return (invalidsum)

#print(part1(inputarray))              

def part2 (inputarr):
    invalidsum = 0
    for idrange in inputarr:
        splitted = idrange.split("-")
        for id in range(int(splitted[0]),int(splitted[1])+1):
            id = str(id)
            for i in range (1,len(id)):
                candidate = id[:i]
                repeated = ""
                while len(repeated) < len(id):
                    repeated += candidate              
                if repeated == id:
                    match = True # Need to only count once in cases where all digits are the same (11111,888888)
                    if match:
                        invalidsum += int(repeated)
                    break
            
    return (invalidsum)

print(part2(inputarray))   