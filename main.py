import time
import random

startmatrics = [
    0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
leng = 20
matrics = []
lastmatrics = []

def _main() -> None:
    global lastmatrics
    global matrics

    command = input("type: ")
    if command == "random":
        genRandom(leng)
    sleep = float(input("speed: "))

    run = True
    lastmatrics = startmatrics
    count = 1

    while run:
        matrics = []

        print()

        for i in range(len(lastmatrics)):
            if lastmatrics[i] == 1:
                if getCellsNum(i) == 2 or getCellsNum(i) == 3:
                    matrics.append(1)
                else:
                    matrics.append(0)
            else:
                if getCellsNum(i) == 3:
                    matrics.append(1)
                else:
                    matrics.append(0)
        
        if matrics == lastmatrics or not (1 in matrics):
            print_array(matrics, leng)
            run = False
            print("life went extint. Your simulation survived "+str(count)+" iterations")
        else:
            print_array(matrics, leng)
            lastmatrics = matrics
            count += 1
        time.sleep(sleep)
                
def getCellsNum(point:int):
    cells = 0
    j = 0
    cCell = [
        point - leng - 1,
        point - leng,
        point - leng + 1,
        point - 1,
        point + 1,
        point + leng - 1,
        point + leng,
        point + leng + 1,
    ]

    for i in cCell:
        if i < 0:
            j = i + (leng*leng)
        elif i > leng*leng-1:
            j = i - (leng*leng)
        else:
            j = i

        if lastmatrics[j] == 1:
            cells += 1
    
    return cells

def print_array(array, leng):
    counter = 1
    for i in range(len(array)):
        if counter == leng:
            if array[i] == 1:
                print("■")
            else:
                print("□")
            counter = 1
        else:
            if array[i] == 1:
                print("■", end=" ")
            else:
                print("□", end=" ")
            counter += 1

def genRandom(len):
    i=0
    global startmatrics
    startmatrics = []
    for j in range(len*len):
        i=random.randint(1,3)
        if i == 1:
            startmatrics.append(1)
        else:
            startmatrics.append(0)


if __name__=="__main__":
    _main()
