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
            target = currentPositon + magnitude
            zeros = (target // 100) - (currentPositon // 100)
            numberOfZero += zeros
            currentPositon = target % 100
        elif direction == 'L':
            target = currentPositon - magnitude
            zeros = ((currentPositon - 1) // 100) - ((target - 1) // 100)
            numberOfZero += zeros
            currentPositon = target % 100
            
    return numberOfZero



print(countNumberOfZeros('day01.txt'))