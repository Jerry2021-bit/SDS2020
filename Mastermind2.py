from tkinter import *
import random

#https://pypi.org/project/tkmacosx/
#pip3 install tkmacosx
from tkmacosx import Button

currRow = []
Rows = []

PegColors = ['magenta2','cyan','purple2','teal','yellow','dark green']

Solution = []


def DrawRow(currRow, row):
    offset = 20
    size = 20
    spacing = 25

    # draw the current row
    col = 0
    for pc in currRow:
        canvas1.create_oval(spacing * col + offset,
                            spacing * row + offset,
                            spacing * col + size + offset ,
                            spacing * row + size + offset, fill=pc)
        col += 1
    pass


def DrawBoard(status):
  canvas1.delete(ALL)
  row = 0

  #draw the rows
  for r in Rows:
      DrawRow(r, row)
      row += 1

  DrawRow(currRow, row)

  #draw the solution... just for testing.
  DrawRow(Solution, 12)

  canvas1.create_text(80,380,text = status)
  pass


def Color(c):
  global currRow
  global Rows5
  if len(currRow) < 4:
    currRow.append(c)
  DrawBoard('keep choosing')
  pass


def Delete():
    pass


def Check():
    global currRow
    global Rows
    tempRow = currRow.copy()
    tempSol = Solution.copy()
    totalBlack = 0
    status = ''
    if len(currRow) == 4:
        # check to see if we win
        for i in range(len(Solution)):
            if currRow[i] == Solution[i]:
                currRow.append('black')
                totalBlack += 1
                tempSol[i] = 'X'
                tempRow[i] = 'X'

        for i in range(len(tempRow)):
            if tempRow[i] in tempSol and tempRow[i] != 'X':
                currRow.append('pink')
                tempSol.remove(tempRow[i])

        Rows.append(currRow.copy())
        currRow = []

        if totalBlack == 4:
            print('you win!')
            status = 'you win!'

    DrawBoard(status)
    #print(Rows)
    pass


root = Tk()
root.title("MasterMind")
root.configure(background = 'white')

frame1 = Frame(root, bg='sky blue', bd= 10)
frame1.pack(side=TOP)

canvas1 = Canvas(frame1, width = 250, height=400)
canvas1.pack()

frame2 = Frame(root )

c1 = Button(frame2, text=" ", borderless=1, bg=PegColors[0], command=lambda: Color(PegColors[0]))
c1.pack(side=LEFT)

c2 = Button(frame2, text=" ", borderless=1, bg=PegColors[1], command=lambda: Color(PegColors[1]))
c2.pack(side=LEFT)

c3 = Button(frame2, text=" ", borderless=1, bg=PegColors[2], command=lambda: Color(PegColors[2]))
c3.pack(side=LEFT)

c4 = Button(frame2, text=" ", borderless=1, bg=PegColors[3], command=lambda: Color(PegColors[3]))
c4.pack(side=LEFT)

c5 = Button(frame2, text=" ", borderless=1, bg=PegColors[4], command=lambda: Color(PegColors[4]))
c5.pack(side=LEFT)

c6 = Button(frame2, text=" ", borderless=1, bg=PegColors[5], command=lambda: Color(PegColors[5]))
c6.pack(side=LEFT)

b1 = Button(frame2, text="Delete", command=Delete)
b1.pack(side=RIGHT)

b2 = Button(frame2, text="Check", command=Check)
b2.pack(side=RIGHT)

frame2.pack(side=BOTTOM)

#generate a solution - randomly
for i in range(4):
    Solution.append(PegColors[random.randint(0,len(PegColors)-1)])
print(Solution)

DrawBoard('Choose a peg')

mainloop()