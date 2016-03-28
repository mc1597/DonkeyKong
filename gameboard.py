#!/usr/bin/python

import random
import pygame
import time
from pygame.locals import *

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED = (255,0,34)
GREEN = (0,255,0)
BLUE = (0,0,255)
LTBLUE = (15,110,145)
LTGREEN = (102,191,13)
YELLOW = (205,157,0)
BROWN = (100,0,0)
PINK = (205,0,96)
PALEPINK = (255,102,102)
PURPLE = (102,0,51)
WIDTH = 13
HEIGHT = 18
MARGIN = 0

pygame.init()

screen = pygame.display.set_mode((1300, 715))
pygame.display.set_caption('DonkeyKong')

clock = pygame.time.Clock()

font = pygame.font.SysFont("comicsansms", 26)


class Board():

	def __init__(self):
		self.Lost = False
		self.createMatrix()
		self.buildWalls()
		self.generateCoins()

	def createMatrix(self):
		self.array = []
		for i in xrange(34):
    			self.array.append([])
		        for j in xrange(80):
                		self.array[i].append(" ")

	
	def buildWalls(self):
		s = "X"
		t = " "
		u = 81
		v = 81
		fl = 0
		for k in xrange(80):
		        self.array[0][k] = "X"
			

		self.array[1][0] = "X"
		p = random.randint(15,45)
		self.array[1][p] = "X"
		self.array[1][p+5] = "Q"
		self.array[1][p+9] = "X"
		self.array[1][79] = "X"

		self.array[2][0] = "X"
		for b in range(p,p+7):
		        self.array[2][b] = "X"
		self.array[2][p+7] = "H"
		a = p+7
		self.array[2][p+8] = "X"
		self.array[2][p+9] = "X"
		self.array[2][79] = "X"
		self.array[3][0] = "X"
		self.array[3][p+7] = "H"
		self.array[3][79] = "X"
		self.array[4][0] = "X"
		self.array[4][p+7] = "H"
		self.array[4][79] = "X"

		
		
		for i in range(28):
	
	
			if i%4!=0:
				if i < 1:
					#print "X"+t*78+"X"             			# X 78 spaces X
					for k in xrange(80):
						self.array[i+5][k] = "X"
				else:							# a is the value of the top of staircase 
					#print "X"+t*(a-1) + "H" + t*(78-a)+"X"  	#X spaces till H i.e (a-1) spaces then H then remaining spaces X
					self.array[i+5][0] = "X"
					self.array[i+5][a] = "H"
					self.array[i+5][79] = "X"			


			else:
				if fl == 0:						# walls starting from left side
					u = random.randint(2,77)			# max num of walls = 80 -2X -H =77
		
					if a <= u:					# walls should be beneath i.e, to the right of prev. staircase
						v = random.randint(0,77 - u)		
					
					else:						#So if new staircase is left of old one there must be enough X's to
									#be on or on right of prev staircase
						if a >= 77: 
							v = 77-u         
						else:
							v = random.randint(a - u,77 - u)   #Problem when a-u = 77/78 - u why?? condition has been put to avoid 
											   # prob but not working CHECK!!! EDIT: FIXED	
					
					#print s*u + "H" + s*v + t*(78-u-v)+"X"          #XXXXXHXXXX      X
					for m in xrange(u):
						self.array[i+5][m] = "X"
					self.array[i+5][u] = "H"
					for m in range(u+1,u+1+v):
						self.array[i+5][m] = "X"
					self.array[i+5][79]="X"	
			
					fl = 1
				else:
					if a != 0 and a!=1:						#walls starting from right side
						u1 = random.randint(1,a-1)		        #spaces are left of prev. staircase
					elif a== 0:
						u1 = 1
					u = random.randint(0,77-u1-1)			#X+spaces+walls+H+X = 80
					#print "X"+t*u1+s*u+"H"+s*(78-u-u1)              #X   XXXXHXXXXX
					self.array[i+5][0] = "X"
					for m in range(u1+1,u1+1+u):
						self.array[i+5][m] = "X"
					self.array[i+5][u1+1+u] = "H"
					for m in range(u1+u+2,80):
        		                        self.array[i+5][m] = "X"
                        		u = u+u1+1                                      #position of new staircase
              			        fl = 0
		        a = u                                                           #saving current/new staircase position                                  

		#print s*80                     
		for m in xrange(80):
        		self.array[33][m] = "X"



	def generateCoins(self):
		for i in range(2,33):
        		c = 1
		        for j in range(2,79):
                		x = random.randint(5,11)
   		                if self.array[i+1][j] == "X" and j%x == 1 and self.array[i][j] != "H" and c <= 5:
		                        self.array[i][j] = "C"
                		        c = c+1
	
	def printGame(self):
	#	for k in xrange(33):
	#	        print ''.join(self.array[k])
    		for i in range(34):
		        for j in range(80):
		            pygame.draw.rect(screen,BLACK,[ (MARGIN + WIDTH)*j + MARGIN,(MARGIN + HEIGHT)*i + MARGIN,WIDTH,HEIGHT] )
			    if self.array[i][j] == "C":	
 		           	 text = font.render(self.array[i][j], True, YELLOW)
			    elif self.array[i][j] == "H":	
 		           	 text = font.render(self.array[i][j], True, BROWN)
			    elif self.array[i][j] == "D":	
 		           	 text = font.render(self.array[i][j], True, LTBLUE)
			    elif self.array[i][j] == "P":	
 		           	 text = font.render(self.array[i][j], True, PALEPINK)
			    elif self.array[i][j] == "O":	
 		           	 text = font.render(self.array[i][j], True, RED)
			    elif self.array[i][j] == "Q":	
 		           	 text = font.render(self.array[i][j], True, LTGREEN)
			    elif self.array[i][j] == "X":	
 		           	 text = font.render(self.array[i][j], True, PURPLE)
			    else:	
 		           	 text = font.render(self.array[i][j], True, WHITE)
        		    screen.blit(text,( (MARGIN + WIDTH)*j + MARGIN + WIDTH/50, (MARGIN + HEIGHT)*i + MARGIN + HEIGHT/50))
	
		pygame.display.flip()		

	def PlayerStart(self):
		posx = 32
		posy = 1
		self.array[posx][posy] = "P"
		return posx,posy

	def DonkeyStart(self):
		posx = 4
		posy = 1
		self.array[posx][posy] = "D"
		return posx,posy





