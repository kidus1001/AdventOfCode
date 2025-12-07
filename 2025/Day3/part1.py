with open("/Users/kidus1001/Desktop/Advent of Code/2025/Day3/input1.txt", "r") as file:
    input = [line.strip() for line in file]
total = 0
for line in input:
    print(line)
    firstNum = 0
    secondNum = 0
    length = len(line)
    for i in range(length):
        if line[i].isdigit():
            lineInt = int(line[i])
            if lineInt > firstNum and i != length-1:
                firstNum = lineInt
                secondNum = int(line[i+1])
            elif lineInt > secondNum:
                secondNum = lineInt
    # print(total)
    total += (10 * firstNum) + secondNum
print(total)