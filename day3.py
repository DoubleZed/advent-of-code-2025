import os
day="3"

inputfile = "input_day" + day + ".txt"
inputPath = os.path.join(os.getcwd(),"input",inputfile)
inputarray = [line.rstrip() for line in open(inputPath,"r")]

def part1 (inputarr):
    pairsum = 0
    for bank in inputarr:
        largepair = 0
        for i in range(len(bank)):
            for j in range (i+1,len(bank)):
                pair = int(str(bank[i])+str(bank[j]))
                if pair > largepair:
                    largepair = pair
        pairsum += largepair
    return pairsum

print(part1(inputarray))
