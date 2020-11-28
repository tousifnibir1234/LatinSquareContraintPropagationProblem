from __future__ import print_function
from fc import forwardChecking 
game=[]
gameSize=0
consistencyChecking=0
failNumber=0
def domain_getter(game,r,c):
    global gameSize
    temp=list(range(1,gameSize+1))
    #print(temp)
    dom =0 
    for i in range(gameSize):
        if game[r][i] in temp:
            temp.remove(game[r][i])
        if game[i][c] in temp:
            temp.remove(game[i][c])

    #temp.sort(reverse=True)
    #print(temp)
    return temp.__len__()

def empty_checker(game,l):
    global gameSize
    for r in range(gameSize):
        for c in range(gameSize):
            if game[r][c]==0:
                l[0]=r
                l[1]=c
                return True
    
    return False
def Brelazempty_checker(game,l):
        global gameSize
        tupleList=[]
        for r in range( gameSize):
            for c in range( gameSize):
                if(game[r][c]==0):
                    ls= [row[c] for row in game]
                    mxf= game[r].count(0)+ ls.count(0)-2
                    #print(mxf ,'for ',r,c)
                    domain= domain_getter(game,r,c)
                    tupleList.append( (domain,(r,c),mxf))

        tupleList.sort()
        #->print(tupleList)
        if(tupleList.__len__()==0):
            return False
        else:
            #->print(tupleList.__len__())
            
            #->print('the min is',l)
            lowest=tupleList[0][0]

            #print('\n',tupleList)

            #print(lowest)
            p=[item  for item in tupleList if item[0]==lowest  ]
            #print(p)

            p.sort(key=lambda  x: x[2],reverse=True)
            #print('after sorting  p ',p)
            l[0]=p[0][1][0]
            l[1]=p[0][1][1]

            return True   


def SDFempty_checker(game,l):
    global gameSize
    tupleList=[]
    for r in range( gameSize):
        for c in range( gameSize):
            if(game[r][c]==0):
                domain= domain_getter(game,r,c)
                tupleList.append( (domain,(r,c)))

    

    tupleList.sort()
    # print(tupleList)
    if(tupleList.__len__()==0):
        return False
    else:
        # print(tupleList.__len__())
        l[0]=tupleList[0][1][0]
        l[1]=tupleList[0][1][1]
        # print('the min is',l)
        return True   
           
    

def row_check(game,row,n):
    global gameSize
    for i in range( gameSize):
        if(game[row][i]== n):
            return True
    return False

def colum_check(game,colum,n):
    global gameSize
    for i in range( gameSize):
        if(game[i][colum]==n):
            return True
    return False

def isSafe(game,r,c,num):
    return not row_check(game,r,num) and   not colum_check(game,c,num)



def solveGame(game):
    global gameSize,consistencyChecking,failNumber
    consistencyChecking+=1
    print(consistencyChecking)

    l=[0,0]
    if not (empty_checker(game,l)):
        return True
    row = l[0]
    colum = l[1]
    for num in  range(1, gameSize +1 ):
        #print('num check for ',num , 'for position',l)
        if isSafe(game,row,colum,num):
            game[row][colum]= num

            if solveGame(game):
                return  True
           # printTheGame(game)
            game[row][colum]= 0
        
            
    
    failNumber+=1
    return False


def problemInput(file):
    file=open(file,"r")
    global gameSize
    gameSize= int( file.readline())
    for i in range(gameSize):
        line=file.readline()
        list = line.split(",")
        list[-1]= list[-1].rstrip() #rstrip  removes the \n from string
        list = [ int(j) for j in list]        
        game.append(list)


def printTheGame(g):
    global gameSize
    for i in range(gameSize):
        print(game[i])
    
    
def main():

    problemInput('test.txt')
    
    if not solveGame(game):
        print('not solvable')
    else:
        print('solved')
        print(f'Node Number is {consistencyChecking}')
        print(f'Backtrack is {failNumber}')

        printTheGame(game)

    # fcheck=forwardChecking(game,gameSize)
    

if __name__ == "__main__": 
    main()
