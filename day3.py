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

def part2 (inputarr):
    resultsum = 0
    for bank in inputarr:
        result = []
        battsleft = 12
        i = 0
        while battsleft > 0:
            end = len(bank) - battsleft + 1
            largest = max(bank[i:end])
            pos = bank.index(largest, i, end)
            result.append(largest)
            battsleft -= 1
            i = pos + 1
        bankresult = int(''.join(map(str, result)))
        resultsum += bankresult
    return resultsum

print(part1(inputarray))
print(part2(inputarray))
