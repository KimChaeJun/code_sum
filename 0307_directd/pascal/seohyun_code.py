import sys
sys.stdin = open('input.txt', 'r')
#########################################
def findSide():
    sideList = []
    sumCntR = 0
    sumCntL = 1
    isSide = False
    for i in range(1, n + 1):
        sumCntR += i
        if isSide == True:
            sumCntL += i - 1
            sideList.append(sumCntL)
        sideList.append(sumCntR)
        isSide = True
    return sideList

def setListlength():
    listLength = 0
    for i in range(1, n + 1):
        listLength += i
        lineList.append(listLength)
    return listLength


def find_position(target):
    currentIdx = 0
    row = 0

    while True:
        row += 1
        currentIdx += row

        if currentIdx >= target:
            break
    rowPosition = target - (currentIdx - row)

    return row, rowPosition


def find_index(row, rowPosition):
    currentIdx = 0

    for i in range(1, row + 1):
        currentIdx += i

    index = currentIdx - (row - rowPosition)

    return index

def createT(n):
    sideList = findSide()
    listLength = setListlength()
    triangle = [0,]
    while listLength + 1 != len(triangle):
        current = len(triangle)
        line, row = find_position(current)
        left = find_index(line -1, row -1)
        right = find_index(line -1, row)
        for i in sideList:
            if i > current:
                triangle.append(triangle[left] + triangle[right])
                break

            if current == i:
                triangle.append(1)
                break

    triangle.pop(0)

    index = 0
    n = len(triangle)
    print(n)
    for i in range(1, n + 1):
        print(" ".join(map(str, triangle[index:index + i])))
        index += i


lineList = []
T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    n = int(input())
    print(f"#{tc}")
    createT(n)
