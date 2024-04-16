import random
import tkinter as TK
import math
import json

# var || cons

startmatrics = []

leng = 0

matrics = []
lastmatrics = []
ccount = 1
sleep = 0

commands = ["random", "load"]

WIDTH=600
HEIGHT=600

cellsset = set()

with open('life.json') as f:
    life = json.load(f)

# main func

def _main() -> None:
    global lastmatrics
    global matrics
    global root
    global ccount
    global sleep
    global canvas
    global leng

    # settings

    leng = input("len: ")

    if leng.isdigit():
        leng = int(leng)
    else:
        return 1
    
    command = input("type: ")

    if commands.__contains__(command):
        pass
    else:
        return 2

    if command == "random":
        startmatrics = getRandom(leng)
    elif command == "load":
        command = input("name: ")

        if life[command]:
            pass
        else:
            return 2
        
        startmatrics = getEmphyMatrics(leng)
        startmatrics = loadLife(startmatrics, life[command], leng)

    sleep = input("speed: ")

    if sleep.isdigit():
        sleep = int(sleep)
    else:
        return 1

    lastmatrics = startmatrics

    # creating window

    root = TK.Tk()
    root.title("game of life")
    root.geometry(str(WIDTH)+"x"+str(HEIGHT))
    root.resizable(False, False)

    canvas = TK.Canvas(root, width=WIDTH,height=HEIGHT)
    canvas.pack(fill="both")

    root.after(sleep, loop)
    root.mainloop()

# inf loop

def loop():
    global lastmatrics
    global matrics
    global root
    global ccount
    global sleep

    matrics = []

    # testing tiles

    cellsset = getCellsSet(leng, lastmatrics)
    matrics = getEmphyMatrics(leng)
    j = range(len(cellsset))

    for i in j:
        b = cellsset.pop()
        if lastmatrics[b] == 1:
            if getCellsNum(b, leng) == 2 or getCellsNum(b, leng) == 3:
                matrics[b] = 1
            else:
                matrics[b] = 0
        else:
            if getCellsNum(b, leng) == 3:
                matrics[b] = 1
            else:
                matrics[b] = 0
    
    # testing for end
    
    if matrics == lastmatrics or not (1 in matrics):
        drawLife()
        print(matrics, leng)
        print("life went extint. Your simulation survived "+str(ccount)+" iterations.")
        root.destroy()
    else:
        drawLife()
        lastmatrics = matrics
        ccount += 1

        # call itself

        root.after(sleep, loop)

# get number of life cells arround

def getCellsNum(point:int, leng):
    cells = 0
    j = 0
    cCell = []

    if isOnEndOrStart(point, leng) == "end":
        cCell =[point - leng - 1,
                point - leng,
                point - leng + 1 - leng,
                point - 1,
                point + 1 - leng,
                point + leng - 1,
                point + leng,
                point + leng + 1 - leng]
    elif isOnEndOrStart(point, leng) == "start":
        cCell =[point - leng - 1 + leng,
                point - leng,
                point - leng + 1,
                point - 1 + leng,
                point + 1,
                point + leng - 1 + leng,
                point + leng,
                point + leng + 1]
    else:
        cCell =[point - leng - 1,
                point - leng,
                point - leng + 1,
                point - 1,
                point + 1,
                point + leng - 1,
                point + leng,
                point + leng + 1]

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

# prints array of life

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

# draw life

def drawLife():
    canvas.delete("all")
    x=0
    y=0
    j=0
    wh=WIDTH/leng

    canvas.create_rectangle(0,0,WIDTH,HEIGHT, outline="#000000", fill="#000000")

    for i in range(len(matrics)):
        if matrics[i] == 1:
            j=i
            while j>leng-1:
                j-=leng
            x=j*wh
            y=math.floor(i/leng)*wh
            canvas.create_rectangle(x,y,x+wh,y+wh, outline="#FFFFFF", fill="#FFFFFF")

# create random cells

def getRandom(len):
    i=0
    startmatrics = []
    for j in range(len*len):
        i=random.randint(1,5)
        if i == 1:
            startmatrics.append(1)
        else:
            startmatrics.append(0)
    return startmatrics

# getting a cells to check

def getCellsSet(leng, lastmatrics):
    cellsset = set()
    for i in range(len(lastmatrics)):
        if lastmatrics[i] == 1:
            j = []

            if isOnEndOrStart(i, leng) == "end":
                j =[i - leng - 1,
                        i - leng,
                        i - leng + 1 - leng,
                        i - 1,
                        i + 1 - leng,
                        i + leng - 1,
                        i + leng,
                        i + leng + 1 - leng]
            elif isOnEndOrStart(i, leng) == "start":
                j =[i - leng - 1 + leng,
                        i - leng,
                        i - leng + 1,
                        i - 1 + leng,
                        i + 1,
                        i + leng - 1 + leng,
                        i + leng,
                        i + leng + 1]
            else:
                j =[i - leng - 1,
                        i - leng,
                        i - leng + 1,
                        i - 1,
                        i + 1,
                        i + leng - 1,
                        i + leng,
                        i + leng + 1]

            for k in range(len(j)):
                if j[k] < 0:
                    j[k] = j[k] + (leng*leng)
                elif j[k] > (leng*leng)-1:
                    j[k] = j[k] - (leng*leng)
            for k in j:
                cellsset.add(k)
    return cellsset

# getting emphy matrics

def getEmphyMatrics(leng):
    matrics = []
    for i in range(leng*leng):
        matrics.append(0)
    return matrics

# pasting life

def loadLife(startmatrics, to_past, leng):
    pos = to_past["pos"][0] + to_past["pos"][1]*leng
    j = 0
    k = 0
    for i in range(len(to_past["map"])):
        startmatrics[pos+k+(j*leng)] = to_past["map"][i]
        if (i+1)%to_past["leng"] == 0:
            j+=1
            k=0
        else:
            k+=1
    return startmatrics


# end or start?

def isOnEndOrStart(pointer, leng):
    if (pointer+1)%leng == 0:
        return "end"
    elif (pointer+1)%leng == 1:
        return "start"
    return None


# calling main

if __name__=="__main__":
    _main()