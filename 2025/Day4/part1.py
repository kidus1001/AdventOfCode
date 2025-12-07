with open("/Users/kidus1001/Desktop/Advent of Code/2025/Day4/input.txt", "r") as file:
    input = [line.strip() for line in file]
    
twoDArray = []
for line in input:
    twoDArray.append (list(line))
result = 0
directions = [
    (0, -1),
    (0, 1),
    (1, 0),
    (-1, 0),
    (-1,-1),
    (-1, 1),
    (1, -1),
    (1,1)
]
row = len(twoDArray)
col = len(twoDArray[0])

for i in range(row):
    for j in range (col):
        count = 0
        
        if twoDArray[i][j] != "@":
            continue

        for x, y in directions:
            ni = i+x
            nj = j+y
            
            if 0<= ni < row and 0<=nj<col and twoDArray[ni][nj] == "@":
                count+=1
        if count < 4:
            result+=1
print(result)