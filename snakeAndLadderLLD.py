import random
from collections import deque

class Piece:
    
    def __init__(self,start,end):
        self.start=start
        self.end=end

    

class Board:
    
    def __init__(self,size,winningPosition):
        self.size=size
        self.winningPosition=winningPosition
        self.peiceMap={}
        
    def initialiseBoard(self):
        self.board=[i+1 for i in range(self.size)]
        
    def addPiece(self,piece):
        self.peiceMap[piece.start]=piece.end
        
    
class Dice:
    
    def __init__(self,size):
        self.size=size
        
    def roll(self):
        return random.randint(1,self.size)
    
    
class Player:
    
    def __init__(self,name,id,position):
        self.id=id
        self.name=name
        self.position=position
        
    def getPosition(self):
        return self.position
    
    def setNewPosition(self,pos):
        self.position=pos
        
        
    
class Game:
    
    player1=Player("sahil",1,0)
    player2=Player("Sumit",2,0)
    board=Board(100,100)
    board.initialiseBoard()
    snake1=Piece(11,1)
    board.addPiece(snake1)
    snake2=Piece(40,20)
    board.addPiece(snake2)
    ladder1=Piece(10,99)
    ladder2=Piece(55,97)
    board.addPiece(ladder1)
    board.addPiece(ladder2)
    queue=deque([player1,player2])
    dice=Dice(6)
    while queue:
        curplayer=queue.popleft()
        curPosition=curplayer.getPosition()
        roll=dice.roll()
        newPosition=curPosition+roll
        if newPosition in board.peiceMap:
            newPosition=board.peiceMap[newPosition]
            if newPosition<curPosition:
                print(curplayer.name+" is bitten by snake")
            if newPosition>curPosition:
                print(curplayer.name+" took a ladder")
            
            
        if newPosition>board.winningPosition:
            print("You need exact number to get to final position cannot make move")
            newPosition=curPosition
        if newPosition==board.winningPosition:
                print(curplayer.name+" have won the game")
                break
        curplayer.setNewPosition(newPosition)
        print(curplayer.name,newPosition)
        queue.append(curplayer)
            
        
    
    
    
        
