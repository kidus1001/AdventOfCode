with open("/Users/kidus1001/Desktop/Advent of Code/2025/Day3/input1.txt", "r") as file:
    input = [line.strip() for line in file]


res = 0
for line in input:
    answer = []
    lineLen = len(line)
    for i in line:
        lineLen -= 1
        while (answer and int(answer[-1]) < int(i) and lineLen+len(answer) >= 12):
            answer.pop()
        if len(answer) < 12:
            answer.append(i)
    res += int("".join(str(x) for x in answer))
print(res)

    
# 987654321111111
# 811111111111119
# 234234234234278
# 818181911112111