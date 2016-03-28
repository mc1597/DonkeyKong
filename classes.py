#!/usr/bin/python 
import sys
import random
import gameboard
import pygame
import time
from pygame.locals import *

clock = pygame.time.Clock()
font = pygame.font.SysFont("comicsansms", 36)
font1 = pygame.font.SysFont("comicsansms", 76)
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,125,0)
BLUE = (0,0,255)
class Person():
	def __init__(self,x,y,score,level):
		self._posx = x
		self._posy = y
		self.__score = score
		self.__lives = 3
		self.__level = level
		self._won = 0
	
	def retScore(self):
		sc = self.__score
		return sc

	def retLives(self):
		sc = self.__lives
		return sc

	#def checkCoin(self,instgame):
	#	return "C" in instgame.array[self._posx][self._posy]

	def collectCoin(self,instgame):
		soundObj = pygame.mixer.Sound('coin.wav')
		soundObj.play()
		self.__score = self.__score + 5*(self.__level)

	def levelUp(self):	
		self.__score = self.__score + 50
		self._won = 1
		soundObj = pygame.mixer.Sound('level.wav')
		soundObj.play()
		gameboard.screen.fill(BLACK)
		sc = "LEVEL PASSED!"
		sc1 = "Your score is: " + str(self.__score)
 	        text = font1.render(sc, True, BLUE)
 	        text1 = font.render(sc1, True, BLUE)
      	        gameboard.screen.blit(text,(500,325))
      	        gameboard.screen.blit(text1,(505,425))
		pygame.display.flip()
		time.sleep(5)
		#pygame.quit()
	        #sys.exit()

	def savePrincess(self):			                        # need to load next level; EDIT: DONE
		if self._posx == 1 and self._won == 0:
			self.__score = self.__score + 50
			self._won = 1
			self.levelUp()

	def printScore(self):
		sc = "Score: "
 	        text = font.render(sc+str(self.__score), True, BLUE)
		gameboard.screen.fill(BLACK,(1100,200,200,200))
      	        gameboard.screen.blit(text,(1100,200))
		pygame.display.flip()
	
	def printLevel(self):
		sc = "Level: "
 	        text = font.render(sc+str(self.__level), True, BLUE)
		gameboard.screen.fill(BLACK,(1100,100,200,100))
      	        gameboard.screen.blit(text,(1100,100))
		pygame.display.flip()

	def printInstructions(self):
		inst = "Rules:"
		left = "a -> left"
		right = "d -> right"
		up = "w -> up"
		down = "s -> down"
		jr = "space+d -> jump right"
		jl = "space+a -> jump left"
 	        text = font.render(inst, True, GREEN)
 	        text1 = font.render(left, True, GREEN)
 	        text2 = font.render(right, True, GREEN)
 	        text3 = font.render(up, True, GREEN)
 	        text4 = font.render(down, True, GREEN)
 	        text5 = font.render(jr, True, GREEN)
 	        text6 = font.render(jl, True, GREEN)
		#gameboard.screen.fill(BLACK,(1050,400,200,300))
      	        gameboard.screen.blit(text,(1050,400))
      	        gameboard.screen.blit(text1,(1050,420))
      	        gameboard.screen.blit(text2,(1050,440))
      	        gameboard.screen.blit(text3,(1050,460))
      	        gameboard.screen.blit(text4,(1050,480))
      	        gameboard.screen.blit(text5,(1050,500))
      	        gameboard.screen.blit(text6,(1050,520))
		pygame.display.flip()
	
	def takemebacktothestart(self):
		self._posx = 32
		self._posy = 1

	def gameOver(self):	
		gameboard.screen.fill(BLACK)
		soundObj = pygame.mixer.Sound('dead.wav')
		soundObj.play()
		sc = "GAME OVER!!!"
		sc1 = "Your score is: " + str(self.__score)
 	        text = font1.render(sc, True, RED)
 	        text1 = font.render(sc1, True, BLUE)
      	        gameboard.screen.blit(text,(500,325))
      	        gameboard.screen.blit(text1,(505,425))
		pygame.display.flip()
		time.sleep(3)
		#pygame.quit()
	        #sys.exit()

	def printLives(self):
		sc = "Lives: "
 	        text = font.render(sc+str(self.__lives), True, RED)
		gameboard.screen.fill(BLACK,(1100,300,200,100))
      	        gameboard.screen.blit(text,(1100,300))
		pygame.display.flip()
		if self.__lives == 0:
			self.gameOver()			

	def declives(self):
		self.__lives = self.__lives - 1
		
	def decscore(self):
		 self.__score = self.__score - 25*(self.__level)

	def incscore(self):
		 self.__score = self.__score + 5*(self.__level)

	def checkCollision(self,direction,instgame):
		if direction == 2:
			return False
		else:
			soundObj = pygame.mixer.Sound('mariofireball.wav')
			soundObj.play()
			instgame.array[self._posx][self._posy] = " "
			self._posx = 32
			self._posy = 1	
			#self.__score = self.__score - 25*(self.__level)
			#self.__lives = self.__lives - 1
			self.decscore()
			self.declives()
			instgame.array[self._posx][self._posy] = "P"


	def FallDown(self,instgame,direction):
		if direction == 2:
			return False
		else:
			soundObj = pygame.mixer.Sound('fall.wav')
			soundObj.play()
			if self._onLadder is False:
				instgame.array[self._posx][self._posy] = " "
			else:
				instgame.array[self._posx][self._posy] = "H"
				self._onLadder = False
		
			if direction == 0:
				instgame.array[self._posx+4][self._posy-1] = "P"		
				self._posy = self._posy - 1
			elif direction == 1:
				instgame.array[self._posx+4][self._posy+1] = "P"		
				self._posy = self._posy + 1
	
			self._posx = self._posx + 4
	                                         
	def checkWall(self,x,y,direction,instgame):
		if "X" in instgame.array[x][y]:
			return False
  
	def CanMoveHere(self,posx,posy,instgame,direction):			
		if posy < 1 or posy > 79 or posx < 1 or posx > 32:
			return False
		if " " in instgame.array[posx+1][posy]:
			rows = [4,8,12,16,20,24,28]
			if posx in rows:
				self.FallDown(instgame,direction)
			return False
		if "O" in instgame.array[posx][posy]:
			self.checkCollision(direction,instgame)
			return False
		if "D" in instgame.array[posx][posy]:
			return False
		if "P" in instgame.array[posx][posy]:
			return False
		if "X" in instgame.array[posx][posy]:
			self.checkWall(posx,posy,direction,instgame)
			return False
		if "C" in instgame.array[posx][posy]:
			if direction != 2:
				self.collectCoin(instgame)
			return True
		#if posx == 1:
		#	self.savePrincess()
		#	return True
		return True

	def coord(self):
		x = self._posx
		y = self._posy
		return x,y


class Player(Person):
	def __init__(self,posx,posy,score,level):
		Person.__init__(self,posx,posy,score,level)
		self._onLadder = False

	def CanMoveUp(self,posx,posy,instgame):
		if self._onLadder is True:
			return True
		return False
		
	def CanMoveDown(self,posx,posy,instgame):
		if "H" in instgame.array[posx][posy]:
			return True		
		return False

	def MoveLeft(self,instgame):
		direction = 0
		if self.CanMoveHere(self._posx,self._posy-1,instgame,direction):
			new = instgame.array[self._posx][self._posy-1]
			if self._onLadder is True:
				instgame.array[self._posx][self._posy] = "H"
			else:
				instgame.array[self._posx][self._posy] = " "
			instgame.array[self._posx][self._posy-1] = "P"
			self._posx = self._posx
			self._posy = self._posy - 1
			if new == "H":
				self._onLadder = True
			else:
				self._onLadder = False
			

	def MoveRight(self,instgame):
		direction = 1
		if self.CanMoveHere(self._posx,self._posy+1,instgame,direction):
			new = instgame.array[self._posx][self._posy+1]
			if self._onLadder is True:
				instgame.array[self._posx][self._posy] = "H"
			else:
				instgame.array[self._posx][self._posy] = " "
			instgame.array[self._posx][self._posy+1] = "P"
			self._posx = self._posx
			self._posy = self._posy + 1
			if new == "H":
				self._onLadder = True
			else:
				self._onLadder = False

	def MoveUp(self,instgame):
		if self.CanMoveUp(self._posx-1,self._posy,instgame):
			new = instgame.array[self._posx-1][self._posy]
			if self._onLadder is True:
				instgame.array[self._posx][self._posy] = "H"
			else:
				instgame.array[self._posx][self._posy] = " "
			instgame.array[self._posx-1][self._posy] = "P"
			self._posx = self._posx - 1
			self._posy = self._posy 
			if new == "H":
				self._onLadder = True
			else:
				self._onLadder = False
			

	def MoveDown(self,instgame):
		if self.CanMoveDown(self._posx+1,self._posy,instgame):
			new = instgame.array[self._posx+1][self._posy]
			if self._onLadder is True:
				instgame.array[self._posx][self._posy] = "H"
			else:
				instgame.array[self._posx][self._posy] = " "
			instgame.array[self._posx+1][self._posy] = "P"
			self._posx = self._posx + 1
			self._posy = self._posy 
			if new == "H":
				self._onLadder = True
			else:
				self._onLadder = False

	def northeast(self,instgame):
		new = instgame.array[self._posx - 1][self._posy + 1]
		if self._onLadder is False:
			instgame.array[self._posx][self._posy] = " "
		else:
			instgame.array[self._posx][self._posy] = "H"
		instgame.array[self._posx - 1][self._posy + 1] = "P"
		self._posx = self._posx - 1
		self._posy = self._posy + 1
		if new == "H":
			self._onLadder = True
		else:
			self._onLadder = False
		return		

	def northwest(self,instgame):
		new = instgame.array[self._posx - 1][self._posy - 1]
		if self._onLadder is False:
			instgame.array[self._posx][self._posy] = " "
		else:
			instgame.array[self._posx][self._posy] = "H"
		instgame.array[self._posx -1][self._posy - 1] = "P"
		self._posx = self._posx - 1
		self._posy = self._posy - 1
		if new == "H":
			self._onLadder = True
		else:
			self._onLadder = False
		return

	def southeast(self,instgame):
		new = instgame.array[self._posx + 1][self._posy + 1]
		if self._onLadder is False:
			instgame.array[self._posx][self._posy] = " "
		else:
			instgame.array[self._posx][self._posy] = "H"
		if "O" in instgame.array[self._posx + 1][self._posy + 1]:
			self.checkCollision(1,instgame)
		else:
			if "C" in instgame.array[self._posx + 1][self._posy + 1]:
				#self.__score = self.__score + 5
				#self.incscore()
				self.collectCoin(instgame)
			instgame.array[self._posx + 1][self._posy + 1] = "P"
			self._posx = self._posx + 1
			self._posy = self._posy + 1
			if new == "H":
				self._onLadder = True
			else:
				self._onLadder = False
		return

	def southwest(self,instgame):
		new = instgame.array[self._posx + 1][self._posy - 1]
		if self._onLadder is False:
			instgame.array[self._posx][self._posy] = " "
		else:
			instgame.array[self._posx][self._posy] = "H"
		if "O" in instgame.array[self._posx + 1][self._posy - 1]:
			self.checkCollision(0,instgame)
		else:
			if "C" in instgame.array[self._posx + 1][self._posy - 1]:
				#self.__score = self.__score + 5
				#self.incscore()
				self.collectCoin(instgame)
			instgame.array[self._posx + 1][self._posy - 1] = "P"
			self._posx = self._posx + 1
			self._posy = self._posy - 1
			if new == "H":
				self._onLadder = True
			else:
				self._onLadder = False
		return

	def CanJumpHere(self,posx,posy,side,instgame):
		if side == 0 and posy < 1:
			return False
		if side == 0 and instgame.array[posx-2][posy+2] == "X":			#Note: here posx and posy are coord after jump
			return False
		if side == 1 and posy > 78:
			return False
		if side == 1 and instgame.array[posx-2][posy-2] == "X":
			return False
		if instgame.array[posx + 1][posy] is "X":
			return True
		return False

	def Jump(self,side,instgame):
		if side == 1:
			if self.CanJumpHere(self._posx,self._posy+4,side,instgame):
				
				soundObj = pygame.mixer.Sound('jump.wav')
				soundObj.play()
				self.northeast(instgame)
				instgame.printGame()
				self.printScore()
				self.printLevel()
				self.printLives()
				self.printInstructions()
				self.northeast(instgame)
				instgame.printGame()
				self.printScore()
				self.printLevel()
				self.printLives()
				self.printInstructions()
				self.southeast(instgame)
				instgame.printGame()
				self.printScore()
				self.printLevel()
				self.printLives()
				self.printInstructions()
				self.southeast(instgame)
				instgame.printGame()
				self.printScore()
				self.printLevel()
				self.printLives()
				self.printInstructions()
		elif side == 0:	
			if self.CanJumpHere(self._posx,self._posy-4,side,instgame):		
				
				soundObj = pygame.mixer.Sound('jump.wav')
				soundObj.play()
				self.northwest(instgame)
				instgame.printGame()
				self.printScore()
				self.printLevel()
				self.printLives()
				self.printInstructions()
				self.northwest(instgame)
				instgame.printGame()
				self.printScore()
				self.printLevel()
				self.printLives()
				self.printInstructions()
				self.southwest(instgame)
				instgame.printGame()
				self.printScore()
				self.printLevel()
				self.printLives()
				self.printInstructions()
				self.southwest(instgame)
				instgame.printGame()
				self.printScore()
				self.printLevel()
				self.printLives()
				self.printInstructions()

class Donkey(Person):
	def __init__(self,posx,posy,score,level):
		Person.__init__(self,posx,posy,score,level)
		self._onLadder = False
		self._onCoin = False
		self._posx = 4
		self._posy = 1

	def moveDonkey(self,instgame):
		lr = random.randint(0,1)
		if lr == 0:
			if self.CanMoveHere(self._posx,self._posy-1,instgame,2):
				new = instgame.array[self._posx][self._posy-1]
				new1 = instgame.array[self._posx-1][self._posy-1]
				if self._onLadder is True:
					instgame.array[self._posx][self._posy] = "H"
				if self._onCoin is True:
					instgame.array[self._posx][self._posy] = "C"
				else:
					instgame.array[self._posx][self._posy] = " "
				instgame.array[self._posx][self._posy-1]="D"
				self._posx = self._posx
				self._posy = self._posy-1
				if new == "H" or new1 == "H":
					self._onLadder = True
				else:
					self._onLadder = False
				if new == "C":
					self._onCoin = True
				else:
					self._onCoin = False
				
			else:
				lr = 1

		if lr == 1:
			if self.CanMoveHere(self._posx,self._posy+1,instgame,2):
				new = instgame.array[self._posx][self._posy+1]
				if self._onLadder is True:
					instgame.array[self._posx][self._posy] = "H"
				if self._onCoin is True:
					instgame.array[self._posx][self._posy] = "C"
				else:
					instgame.array[self._posx][self._posy] = " "
				instgame.array[self._posx][self._posy+1]="D"
				self._posx = self._posx
				self._posy = self._posy+1
				if new == "H":
					self._onLadder = True
				else:
					self._onLadder = False
				if new == "C":
					self._onCoin = True
				else:
					self._onCoin = False
		

class Fireball():		
	def __init__(self,donkey,player):
		self._movement = 1 
		fbcoord = donkey.coord()
		self._posx = fbcoord[0]
		self._posy = fbcoord[1] + 1
		self._onCoin = False
		self._onLadder = False
		self._dead = False
	
	def FallDown(self,player,direction,instgame):
		if self._onLadder is False:
			instgame.array[self._posx][self._posy] = " "
		else:
			instgame.array[self._posx][self._posy] = "H"
		if direction == 0:
			instgame.array[self._posx+4][self._posy-1] = "O"		
			self._posy = self._posy - 1
		elif direction == 1:
			instgame.array[self._posx+4][self._posy+1] = "O"		
			self._posy = self._posy + 1
		self._onLadder = False
		self._posx = self._posx + 4
		lr = random.randint(0,1)
		#lr = 0
		if lr == 0:
			self.MoveLeft(player,instgame)
		else:
			self.MoveRight(player,instgame)
		
	def Dropdown(self,player,instgame):
		var = instgame.array[self._posx-1][self._posy]
		if var is not "H":
			self._onLadder = False
		if self._onLadder is False:
			instgame.array[self._posx][self._posy] = " "
			self._onLadder = True
		else:
			instgame.array[self._posx][self._posy] = "H"
		
		if "P" in instgame.array[self._posx + 1][self._posy]:
			self.checkCollision(self._posx + 1,self._posy,player,instgame)
		instgame.array[self._posx + 1][self._posy] = "O"
		self._posx = self._posx+1
		self._posy = self._posy
			
		if var is not "X":	
			while instgame.array[self._posx+1][self._posy] is not "X":
				if self._onLadder is False:
					instgame.array[self._posx][self._posy] = " "
				else:
					instgame.array[self._posx][self._posy] = "H"
				if "P" in instgame.array[self._posx + 1][self._posy]:
					self.checkCollision(self._posx,self._posy,player,instgame)
				instgame.array[self._posx + 1][self._posy] = "O"
				self._posx = self._posx+1
				self._posy = self._posy
			#instgame.array[self.posx][self.posy] = "O"
			lr = random.randint(0,1)
			#lr = 0
			self._onLadder = True
			if lr == 0:
				self.MoveLeft(player,instgame)
			else:
				self.MoveRight(player,instgame)
		else:
			return True

	def destroy(self,instgame):
		instgame.array[self._posx][self._posy] = " "
		self._dead = True
		
	def checkCollision(self,x,y,player,instgame):
		if player._onLadder is True:
			var = "H"
		else:
			var = " "
		soundObj = pygame.mixer.Sound('mariofireball.wav')
		soundObj.play()
		instgame.array[x][y] = var
		instgame.array[32][1] = "P"
		#player.takemebacktothestart()
		player._posx = 32
		player._posy = 1
		player.declives()
		player.decscore()
		player._onLadder = False

	def CanMoveHere(self,posx,posy,instgame,player,direction):
		if posy < 1 or posy > 79 or posx < 1 or posx > 32:
			return False
		elif " " in instgame.array[posx+1][posy]:
			self.FallDown(player,direction,instgame)
			return False
		elif "X" in instgame.array[posx][posy]:
			return False
		elif "P" in instgame.array[posx][posy]:
			self.checkCollision(posx,posy,player,instgame)
			return False
		elif posx == 32 and posy == 1:
			self.destroy(instgame)
			return False	
		return True

	def MoveLeft(self,player,instgame):
		direction = 0
		self._movement = direction
		drop = instgame.array[self._posx+1][self._posy]
		if self._posx < 32:
			drop1 = instgame.array[self._posx+2][self._posy]
		else:
			drop1 = drop
		wall = instgame.array[self._posx][self._posy-1]
		if drop == "H" or drop1 == "H":
			self.Dropdown(player,instgame)
		elif wall == "X":
			self.MoveRight(player,instgame)
		elif self.CanMoveHere(self._posx,self._posy-1,instgame,player,direction):
			new = instgame.array[self._posx][self._posy-1]
			if self._onLadder is True:
				instgame.array[self._posx][self._posy] = "H"
			elif self._onCoin is True:
				instgame.array[self._posx][self._posy] = "C"
			else:
				instgame.array[self._posx][self._posy] = " "
			instgame.array[self._posx][self._posy-1] = "O"
			self._posx = self._posx
			self._posy = self._posy - 1
			if new == "H":
				self._onLadder = True
			else:
				self._onLadder = False
			if new == "C":
				self._onCoin = True
			else:
				self._onCoin = False
		direction = 0
			

	def MoveRight(self,player,instgame):
		direction = 1
		self._movement = direction
		drop = instgame.array[self._posx+1][self._posy]
		if self._posx < 32:
			drop1 = instgame.array[self._posx+2][self._posy]
		else:
			drop1 = drop
		wall = instgame.array[self._posx][self._posy+1]
		if drop == "H" or drop1 == "H":
			self.Dropdown(player,instgame)
		elif wall == "X":
			self.MoveLeft(player,instgame)
		elif self.CanMoveHere(self._posx,self._posy+1,instgame,player,direction):
			new = instgame.array[self._posx][self._posy+1]
			if self._onLadder is True:
				instgame.array[self._posx][self._posy] = "H"
			elif self._onCoin is True:
				instgame.array[self._posx][self._posy] = "C"
			else:
				instgame.array[self._posx][self._posy] = " "
			instgame.array[self._posx][self._posy+1] = "O"
			self._posx = self._posx
			self._posy = self._posy + 1
			if new == "H":
				self._onLadder = True
			else:
				self._onLadder = False
			if new == "C":
				self._onCoin = True
			else:
				self._onCoin = False
		direction = 1
	
	def movefb(self,player,instgame):
		if self._movement == 0:
			self.MoveLeft(player,instgame)
		elif self._movement == 1:
			self.MoveRight(player,instgame)
				
