import random
import tkinter as TK
import math

# var || cons

startmatrics = []

leng = 0

matrics = []
lastmatrics = []
ccount = 1
sleep = 0

WIDTH=600
HEIGHT=600

cellsset = set()

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

    leng = int(input("len: "))
    command = input("type: ")
    if command == "random":
        genRandom(leng)
    sleep = int(input("speed: "))

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

    getCellsSet()
    getEmphyMatrics()
    j = range(len(cellsset))

    for i in j:
        b = cellsset.pop()
        if lastmatrics[b] == 1:
            if getCellsNum(b) == 2 or getCellsNum(b) == 3:
                matrics[b] = 1
            else:
                matrics[b] = 0
        else:
            if getCellsNum(b) == 3:
                matrics[b] = 1
            else:
                matrics[b] = 0
    
    # testing for end
    
    if matrics == lastmatrics or not (1 in matrics):
        drawLife()
        print("life went extint. Your simulation survived "+str(ccount)+" iterations.")
        root.destroy()
    else:
        drawLife()
        lastmatrics = matrics
        ccount += 1

        # call itself

        root.after(sleep, loop)

# get number of life cells arround

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
    global root
    global canvas

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

def genRandom(len):
    i=0
    global startmatrics
    startmatrics = []
    for j in range(len*len):
        i=random.randint(1,4)
        if i == 1:
            startmatrics.append(1)
        else:
            startmatrics.append(0)

# getting a cells to check

def getCellsSet():
    global cellsset
    cellsset = set()
    for i in range(len(lastmatrics)):
        if lastmatrics[i] == 1:
            j = [
                i - leng - 1,
                i - leng,
                i - leng + 1,
                i - 1,
                i,
                i + 1,
                i + leng - 1,
                i + leng,
                i + leng + 1,
            ]
            for k in range(len(j)):
                if j[k] < 0:
                    j[k] = j[k] + (leng*leng)
                elif j[k] > (leng*leng)-1:
                    j[k] = j[k] - (leng*leng)
            for k in j:
                cellsset.add(k)

# getting emphy matrics

def getEmphyMatrics():
    global matrics
    matrics = []
    for i in range(leng*leng):
        matrics.append(0)

# calling main

if __name__=="__main__":
    _main()