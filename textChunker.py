#splits text into divisable chunks

def splitChunks(divisions : int, filepath : str):
    file = open(filepath, "r")
    data = file.read()
    file.close()
    linecount = 0
    
    for line in data.splitlines():
        linecount = linecount + 1
    
    divisionCount = division
    print(divisionCount)

    currentLineCount = 0

    for i in range(currentLineCount, divisionCount):
        currentLineCount += 1
    



splitChunks(4, "a.txt")