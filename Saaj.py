import sys
import os
import math
import random


# Create a stack for tracking path
stack = []
fringe=[]

# Tile Structure
class WorldCellState:
    breeze = False;
    stench = False;
    wumpus = False;
    pit    = False;
    gold   = False;
    glitter= False;
    bump=False;
    wall=False;
    safe=False;
    goldCollected=False;
    visited=False;
    #currentPosition=[]

class AgentCellState:

    agentSafe=False;
    goldCollected=False;
    visited=False;
    mayPit=False;
    mayWumpus=False;
    score=0;
    agentCurrentPosition=[]

colDimension = 4
rowDimension = 4

board = [[WorldCellState() for j in range(colDimension)] for i in range(rowDimension)]

agentBoard = [[AgentCellState() for j in range(colDimension)] for i in range(rowDimension)]



def printBoard():

    for r in range (rowDimension):
        cellInfo=""
        for c in range (colDimension):
            cellInfo+= "\t"+str(r) +", "+ str(c) +" : "

            if(r==0 and c==0):
                cellInfo+=" agent "

            if board[r][c].stench:
                cellInfo+=" stench"

            if board[r][c].wumpus:
                cellInfo+=" wumpus"

            if board[r][c].pit:
                cellInfo+=" pit"

            if board[r][c].breeze:
                cellInfo+=" breeze"

            if board[r][c].gold:
                cellInfo+=" gold"

            if board[r][c].glitter:
                cellInfo+=" glitter"

            #else:
            #cellInfo+="empty"

        print(cellInfo)

        print("\n")

def getAdjCellList(cell):

    r=cell[0]
    c=cell[1]

    listAdj=[]
    if r==0 and c==0:
        listAdj.append([r,c+1])
        listAdj.append([r+1,c])

    elif r==0 and c==9:
        listAdj.append([r,c-1])
        listAdj.append([r+1,c])

    elif r==9 and c==0:
        listAdj.append([r,c+1])
        listAdj.append([r-1,c])

    elif r==9 and c==9:
        listAdj.append([r-1,c])
        listAdj.append([r,c-1])

    elif r==0:
        listAdj.append([r,c+1])
        listAdj.append([r,c-1])
        listAdj.append([r+1,c])

    elif r==9:
        listAdj.append([r,c+1])
        listAdj.append([r,c-1])
        listAdj.append([r-1,c])

    elif c==0:
        listAdj.append([r-1,c])
        listAdj.append([r,c+1])
        listAdj.append([r+1,c])

    elif c==9:
        listAdj.append([r-1,c])
        listAdj.append([r+1,c])
        listAdj.append([r,c-1])

    else:
        listAdj.append([r,c+1])
        listAdj.append([r,c-1])
        listAdj.append([r-1,c])
        listAdj.append([r+1,c])

    return listAdj



def boundCheck(r,c):
    if(c>=0 and r>=0 and c<colDimension and r<rowDimension):
        return True

def addBreeze(r,c):
    if(boundCheck(r,c)):
        board[r][c].breeze=True

def addStench(r,c):
    if(boundCheck(r,c)):
        board[r][c].stench=True

def addGold(r,c):
    #print("ashchiiii")
    if(boundCheck(r,c)):
        board[r][c].gold=True
        board[r][c].glitter=True
        #print("*************"+ str(c)+ "     "+str(r))

def addPit(r,c):
    if(boundCheck(r,c)):
        board[r][c].pit=True
        addBreeze(r+1,c)
        addBreeze(r-1,c)
        addBreeze(r,c+1)
        addBreeze(r,c-1)

def addWumpus(r,c):
    if(boundCheck(r,c)):
        board[r][c].wumpus=True
        addStench(r+1,c)
        addStench(r-1,c)
        addStench(r,c+1)
        addStench(r,c-1)

def generateDefinedBoard():
    pitList=[[0,2], [0,3], [1,0], [3,0]]
    wumpusList=[3,2]
    goldList=[3,2]

    for p in range (len(pitList)):
        pitRow=pitList[p][0]
        pitCol=pitList[p][1]
        addPit(pitRow, pitCol)

    wumpusRow=wumpusList[0]
    wumpusCol=wumpusList[1]
    addWumpus(wumpusRow, wumpusCol)

    goldRow=goldList[0]
    goldCol=goldList[1]
    addGold(goldRow, goldCol)

def addFeaturesRandomly ( ):
        # Generate pits
        for r in range (rowDimension):
            for c in range (colDimension):
                if (c != 0 or r != 0) and random.randrange(10) < 3: #etaaaaaaki
                    addPit ( r, c )

        # Generate wumpus
        wummpusC = 0
        wumpusR = 0

        while wummpusC == 0 and wumpusR == 0:
            wumpusC = random.randrange(colDimension)
            wumpusR = random.randrange(rowDimension)

        addWumpus ( wumpusR, wumpusC );

        # Generate gold
        goldC = 0
        goldR = 0

        while goldC == 0 and goldR == 0:
            goldC = random.randrange(colDimension)
            goldR = random.randrange(rowDimension)


        addGold ( goldR, goldC )


def checkStench(r,c):
    if board[r][c].stench:

        print("Stench found in cell, wumpus around")
        if r==0 and c==0:
            agentBoard[r][c+1].mayWumpus=True
            agentBoard[r+1][c].mayWumpus=True
            agentBoard[r][c+1].score-=3
            agentBoard[r+1][c].score-=3

        elif r==0 and c==9:
            agentBoard[r][c-1].mayWumpus=True
            agentBoard[r+1][c].mayWumpus=True
            agentBoard[r][c-1].score-=3
            agentBoard[r+1][c].score-=3

        elif r==9 and c==0:
            agentBoard[r][c+1].mayWumpus=True
            agentBoard[r-1][c].mayWumpus=True
            agentBoard[r][c+1].score-=3
            agentBoard[r-1][c].score-=3

        elif r==9 and c==9:
            agentBoard[r-1][c].mayWumpus=True
            agentBoard[r][c-1].mayWumpus=True
            agentBoard[r-1][c].score-=3
            agentBoard[r][c-1].score-=3

        elif r==0:

            agentBoard[r][c+1].mayWumpus=True
            agentBoard[r][c-1].mayWumpus=True
            agentBoard[r+1][c].mayWumpus=True

            agentBoard[r][c+1].score-=3
            agentBoard[r][c-1].score-=3
            agentBoard[r+1][c].score-=3

        elif r==9:

            agentBoard[r][c+1].mayWumpus=True
            agentBoard[r][c-1].mayWumpus=True
            agentBoard[r-1][c].mayWumpus=True

            agentBoard[r][c+1].score-=3
            agentBoard[r][c-1].score-=3
            agentBoard[r-1][c].score-=3

        elif c==0:

            agentBoard[r-1][c].mayWumpus=True
            agentBoard[r][c+1].mayWumpus=True
            agentBoard[r+1][c].mayWumpus=True

            agentBoard[r-1][c].score-=3
            agentBoard[r][c+1].score-=3
            agentBoard[r+1][c].score-=3


        elif c==9:
            agentBoard[r-1][c].mayWumpus=True
            agentBoard[r+1][c].mayWumpus=True
            agentBoard[r][c-1].mayWumpus=True

            agentBoard[r-1][c].score-=3
            agentBoard[r+1][c].score-=3
            agentBoard[r][c-1].score-=3

        else:

            agentBoard[r][c+1].mayWumpus=True
            agentBoard[r][c-1].mayWumpus=True
            agentBoard[r+1][c].mayWumpus=True
            agentBoard[r-1][c].mayWumpus=True

            agentBoard[r][c+1].score-=3
            agentBoard[r][c-1].score-=3
            agentBoard[r+1][c].score-=3
            agentBoard[r-1][c].score-=3

def checkWumpus(r,c):
    if board[r][c].wumpus==True:
        print("Wumpus Eats You! You lose! Game Over!!!")
        return True

def checkPit(r,c):
    if board[r][c].pit==True:
        print("You fell into a pit. Game over")
        return True

def checkBreeze(r,c):
    if board[r][c].breeze:
        print("Breeze found in cell, pit around")
        if r==0 and c==0:
            agentBoard[r][c+1].mayPit=True
            agentBoard[r+1][c].mayPit=True
            agentBoard[r][c+1].score-=3
            agentBoard[r+1][c].score-=3

        elif r==0 and c==9:
            agentBoard[r][c-1].mayPit=True
            agentBoard[r+1][c].mayPit=True
            agentBoard[r][c-1].score-=3
            agentBoard[r+1][c].score-=3

        elif r==9 and c==0:
            agentBoard[r][c+1].mayPit=True
            agentBoard[r-1][c].mayPit=True
            agentBoard[r][c+1].score-=3
            agentBoard[r-1][c].score-=3

        elif r==9 and c==9:
            agentBoard[r-1][c].mayPit=True
            agentBoard[r][c-1].mayPit=True
            agentBoard[r-1][c].score-=3
            agentBoard[r][c-1].score-=3

        elif r==0:

            agentBoard[r][c+1].mayPit=True
            agentBoard[r][c-1].mayPit=True
            agentBoard[r+1][c].mayPit=True

            agentBoard[r][c+1].score-=3
            agentBoard[r][c-1].score-=3
            agentBoard[r+1][c].score-=3

        elif r==9:

            agentBoard[r][c+1].mayPit=True
            agentBoard[r][c-1].mayPit=True
            agentBoard[r-1][c].mayPit=True

            agentBoard[r][c+1].score-=3
            agentBoard[r][c-1].score-=3
            agentBoard[r-1][c].score-=3

        elif c==0:

            agentBoard[r-1][c].mayPit=True
            agentBoard[r][c+1].mayPit=True
            agentBoard[r+1][c].mayPit=True

            agentBoard[r-1][c].score-=3
            agentBoard[r][c+1].score-=3
            agentBoard[r+1][c].score-=3


        elif c==9:
            agentBoard[r-1][c].mayPit=True
            agentBoard[r+1][c].mayPit=True
            agentBoard[r][c-1].mayPit=True

            agentBoard[r-1][c].score-=3
            agentBoard[r+1][c].score-=3
            agentBoard[r][c-1].score-=3

        else:

            agentBoard[r][c+1].mayPit=True
            agentBoard[r][c-1].mayPit=True
            agentBoard[r+1][c].mayPit=True
            agentBoard[r-1][c].mayPit=True

            agentBoard[r][c+1].score-=3
            agentBoard[r][c-1].score-=3
            agentBoard[r+1][c].score-=3
            agentBoard[r-1][c].score-=3

def checkGlitter(r,c):
    if board[r][c].glitter==True:
        board[r][c].goldCollected=True
        print("Gold collected! Game won!")
        return True

threatInfo=""


def checkThreat(r,c):
    checkStench(r,c)
    w=checkWumpus(r,c)
    p=checkPit(r,c)
    checkBreeze(r,c)
    g=checkGlitter(r,c)

    if w==False and p==False:
        board[r][c].safe=True
        return 1
    if w==True or p==True or g==True:
        return -1


def enterCell(cell):

    print("CELLLLLL")
    print(cell)
    r=cell[0]
    c=cell[1]
    print("Agent is in cell: "+str(r)+" , "+str(c))
    agentBoard[r][c].currentPosition=[r,c]
    print("Printing current position")
    print(agentBoard[r][c].currentPosition)
    returnThreat=checkThreat(r,c)
    agentBoard[r][c].visited=True
    return returnThreat

    #checkThreat
    #more gele more jabe game shesh
    #na morle ashepashe moron  ase kina check korbe
    #tarpor value set korbe struct e

def getMaxCell(fringe):

    print("Fringeeeeeeeeeeeeeee")
    print(fringe)

    highestList=[]

    HighestScore=-99999999

    for fr in fringe:
        r=fr[0]
        c=fr[1]

        print("************")
        print(agentBoard[r][c].score)
        print(HighestScore)
        if agentBoard[r][c].score>HighestScore or agentBoard[r][c].score==HighestScore :
            HighestScore=agentBoard[r][c].score


    #highestscore pailam

    for fr in fringe:
        r=fr[0]
        c=fr[1]
        if agentBoard[r][c].score==HighestScore:
            highestList.append(agentBoard[r][c])

    #check if shbgular score same

    print("HighestListttttttttttttttttttt")
    print(highestList)


    if len(highestList)==len(fringe):
        return 11, highestList

    #check if ektai highest

    if len(highestList)==1:
        return 22, highestList

    #check if koyekta highest but shb na

    if len(highestList)>1 and len(highestList)<len(fringe):
        return 33, highestList

def popFuncForOne(cell):

    print("eijonnoooo 469")

    backtrack=stack.pop()
    print("Stack popeeeeeeeeeeeeeeed")
    print(backtrack)

    if(backtrack==cell):
        loop(backtrack)

    if(backtrack==agentBoard[0][0]): #stack ekhn faka

        difR=cell[0]
        difC=cell[1]

        for fr in range(difR):
            for fc in range(difC):
                print("going through cell "+str(fr)+", "+str(fc))

        enterCell(cell)


def sortList(cell,highestList): #nearestcell dey sort kore near---far
    return highestList



def loop(cell):

    print("492")
    print(cell)

    print("stackkkkkkkkkkkkkkkkkkkkkk")
    print(stack)

    stack.append(cell)
    retEnterCell=enterCell(cell)

    if(retEnterCell==-1):
        print("game over")

    print("498")
    print(cell)
    returnedListAdj=getAdjCellList(cell)


    print("Returned Adj List")
    print(returnedListAdj)

    for element in returnedListAdj:
        fringe.append(element)



    print("Fringeeeeeeeeeeeeeeeeeeeeeeeee 527")
    print(fringe)


    #list thke randomly choose kora lagbe ekta
    #cell return korle stack erakha lagbe
    #dekhtesi fringe er koi jabo

    returnMax, highestList=getMaxCell(fringe)

    if(returnMax==22): #ektai max
        #pop kore kore 0 te jabo
        #0 thke target tay jabo highest tay
        #popStack()


        print("eijonnoooo 532")

        popFuncForOne(highestList[0])

        backtrack=stack.pop()

        loop(highestList[0])

    if returnMax==11:

        print("eijonnoooo 542")

        #shbgula same
        #jeine asi oikhan thkei loop **

        print("returnedListAdj[0]")

        print(returnedListAdj[0])

        loop(returnedListAdj[0])

    if returnMax==33:

        print("eijonnoooo 550")

        #koyekta same koyekta highest

        retSortedSet=sortList(cell,highestList)
        #retSortedSet=highestList.sort()
        #sortedgulay ekta ekta kore jabo

        print("Ret    ")

        print(retSortedSet)
        for sortedSet in retSortedSet:
            retSortedSet.remove(sortedSet)

            #pop
            popFuncForOne(sortedSet)

            loop(sortedSet)




def startGame():
    print("Game started")

    # Mark the source node as
    # visited and keep it in stack
    #stack.append([0,0])
    #stackCell=[0,0]

    retEnterCell=enterCell([0,0])

    if(retEnterCell==-1):
        print("game over")

    loop([0,0])


def main():


    #board = [[cellState() for j in range(colDimension)] for i in range(rowDimension)]
    #addFeatures()

    print("Want to play in a random world or predefined world?")
    inp=input("Enter 1 for random world, 2 for predefined world")
    print(inp)

    inp=int(inp)

    if inp==1:
        print("Showing board for random world")
        print("\n")
        addFeaturesRandomly()

    if(inp==2):
        generateDefinedBoard()
        print("Showing board for user defined world")

    #printBoard
    #initiate board for agent
    #score=0, visited=false, agentSafe=false, mayPit=false, mayWumpus=false

    printBoard()
    startGame()

main()


    #startgame 0,0
    #0,0 visited true agentsafe true

    #stage 1: get directions from current position , keep them on map with score struct ei ase, randomly choose , change agentCurrentPosition
    #put it on stack , perceive, change struct variables, map this node/cell with point,
    #check map fringe, jei cell er point shb cheye beshi oitay jawa lagbe ekhn,
        #shb point same hoile jekhane asi shekhan thke abar stage 1, loop,

        #jodi shb point same na hoy tahole jekhane asi shekhan thke pop
        # korte korte back korte thakbo ar current position check korte thakbo konta shbcheye beshi score,1 ta highest er khetre

            #jodi current position target position er sathe match kore tahole oitai current position, oikahn thke abar stage 1 loop

            #nahoy jodi current position 0,0 hoy , tokhon oikhan thke dekha lagbe j target position er (row kotocolumn koto)
                #row 4 hoile row=0 er sathe 4 plus kore 4 ghor agano lagbe for loop
                #column 3 hoile col=0 er sathe 3 ghor jog kore agano lagbe
                #oi ghore shesh mesh giye pouchailam
                #stage 1 loop


        #onekgula same highest score thakle?
            #pop korte korte 0,0 te, ashar pothe jodi
                # current position target position er sathe match kore tahole oitai current position, oikahn thke abar stage 1 loop
            #nearest tay jabo age jetar row col kom
                #ekta func set of cell thke nearest ta ber kore sorted set return korbe
                #sorted gulay ekta ekta kore jabo ar set thke shorabo
                #tokhon oikhan thke dekha lagbe j target position er (row kotocolumn koto)
                #row 4 hoile row=0 er sathe 4 plus kore 4 ghor agano lagbe for loop
                #column 3 hoile col=0 er sathe 3 ghor jog kore agano lagbe
                #oi ghore shesh mesh giye pouchailam
                #stage 1 loop


    #
