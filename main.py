import random
import tkinter as TK
import math

# var || cons

startmatrics = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
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
ccount = 1
sleep = 0

WIDTH=600
HEIGHT=600

# main func

def _main() -> None:
    global lastmatrics
    global matrics
    global root
    global ccount
    global sleep
    global canvas

    # settings

    command = input("type: ")
    if command == "random":
        genRandom(leng)
    sleep = int(input("speed: "))

    lastmatrics = startmatrics

    # creating window

    root = TK.Tk()
    root.title("game of life")
    root.geometry(str(WIDTH)+"x"+str(HEIGHT))

    canvas = TK.Canvas(root, width=WIDTH,height=HEIGHT)
    canvas.pack(side="left")

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

    print()

    # testing tiles

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
    
    # testing for end
    
    if matrics == lastmatrics or not (1 in matrics):
        print_array(matrics, leng)
        drawLife()
        print("life went extint. Your simulation survived "+str(ccount)+" iterations.")
        root.destroy()
    else:
        print_array(matrics, leng)
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

    canvas.create_rectangle(0,0,600,600, outline="#000000", fill="#000000")

    for i in range(len(matrics)):
        if matrics[i] == 1:
            j=i
            while j>leng-1:
                j-=leng
            x=j*30
            y=math.floor(i/leng)*30
            canvas.create_rectangle(x,y,x+30,y+30, outline="#FFFFFF", fill="#FFFFFF")


# create random cells

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

# calling main

if __name__=="__main__":
    _main()