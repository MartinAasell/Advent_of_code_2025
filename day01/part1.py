def readTxtFile(filePath):
    with open(filePath, 'r') as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

def countNumberOfZeros(file_path: str):
    currentPositon = 50
    numberOfZero = 0
    lines = readTxtFile(file_path)
    for i in range(len(lines)):
        direction = lines[i][0]
        magnitude = int(lines[i][1:])
        if direction == 'R':
            currentPositon += magnitude
            while currentPositon > 100:
                currentPositon = currentPositon - 100
        elif direction == 'L':
            currentPositon -= magnitude
            while currentPositon < 0:
                currentPositon = 100 + currentPositon
        if currentPositon == 100:
            currentPositon = 0
        if currentPositon == 0:
            numberOfZero += 1
    return numberOfZero



print(countNumberOfZeros('day01.txt'))