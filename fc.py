import copy


class forwardChecking:
    def __init__(self,game,gameSize):
        self.game=game[:]
        self.gameSize=gameSize
        self.varDomain={}
        self.initialList()
        self.failNumber = 0
        self.nodeCount=0


        self.solveGame(self.game,self.varDomain)
        self.printTheGame(self.game)
        print('node count',self.nodeCount)

        

    
    def initialList(self):
        for r in range(self.gameSize):
            for c in range(self.gameSize):
                if self.game[r][c]==0:
                    self.varDomain[(r,c)]=self.domain_getter(self.game,r,c)

        self.printVarDomain(self.varDomain)



    def domain_getter(self,game,r,c):
    
        temp=list(range(1,self.gameSize+1))
        #print(temp)
        dom =0 
        for i in range(self.gameSize):
            if game[r][i] in temp:
                temp.remove(game[r][i])
            if game[i][c] in temp:
                temp.remove(game[i][c])

        #temp.sort(reverse=True)
        #print(temp)
        return temp

    def empty_checker(self,game,l):
        for r in range(self.gameSize):
            for c in range(self.gameSize):
                if game[r][c]==0:
                    l[0]=r
                    l[1]=c
                    return True
        return False

    def row_check(self,game,row,n):
        for i in range( self.gameSize):
            if(game[row][i]== n):
                return True
        return False
    
    def colum_check(self,game,colum,n):
        for i in range( self.gameSize):
            if(game[i][colum]==n):
                return True
        return False

    def printTheGame(self,game):
        for i in range(self.gameSize):
            print(game[i])

    def isSafe(self,game,r,c,num):
        return not self.row_check(game,r,num) and   not self.colum_check(game,c,num)
    
    def  printVarDomain(self,var):
        for k,v in var.items():
            print( k,v)

    def solveGame(self,game,varDomain):
        self.nodeCount+=1
        l=[0,0]
        if not (self.empty_checker(game,l)):
            print('return of empty chek')
            return True
        row = l[0]
        colum = l[1]

        print('\n\ncoming for ',l)
        dictinput=copy.deepcopy(varDomain)

        temp=varDomain.get((row,colum))
        checkerForDomain=-1000
        for num in temp:
            #for num in  range(1, self.gameSize +1 ):

            #print('num check for ',num , 'for position',l)
            game[row][colum]=num
            p={(row,colum):varDomain.get((row,colum))}

            print('\npoop  is  the starting state ' ,p)
            print('before removing and popping')
            self.printVarDomain(varDomain)
            print('popping of ',row,colum,'with number ',num)
            for k in varDomain.keys():
                if  k[0]==row and k[1] != colum:
                    print('     following ',k)

                    if num in varDomain.get(k):
                        print('     found instance in',k)
                        varDomain.get(k).remove(num)

                if k[1]==colum and k[0]!= row:
                    print('     following ',k)
                    if num in varDomain.get(k):
                        print('     found instance in',k)
                        varDomain.get(k).remove(num)

            varDomain.pop((row,colum))
            print('after the popof ownself')
            self.printVarDomain(varDomain)
            print ('        now the game is ')
            self.printTheGame(game)

            for v in varDomain.values():
                if v.__len__()== 0:
                    print('empty is found')

                    varDomain = copy.deepcopy(dictinput)            
                    print('returning from inner loop')
                    checkerForDomain=1
                    game[row][colum]= 0
                    break
                    #return false will be added here
            if checkerForDomain == 1:
                print('continuing for next')
                checkerForDomain=-1000
                continue
            if self.solveGame(game,varDomain):
                return  True

            print('for backtracking current is ' , row, colum)
            varDomain = copy.deepcopy(dictinput)            
            self.printVarDomain(varDomain)
            print (         'finishing gotcha temp is ',temp)
            # printTheGame(game)
            
            self.failNumber+=1
            game[row][colum]= 0
            
        #pura khali hoye gese. tai abar ager moto kore deyar lagbe
        print("returned with false")       
        return False








