#!/usr/bin/python

import gameboard
import classes
import pygame
import sys
import control

from pygame.locals import *
BLUE = (0,0,255)
BLACK = (0,0,0)
font = pygame.font.SysFont("comicsansms", 36)

def func(level,score):
	fl = 0
	MyBoard = gameboard.Board()
	if level:
		MyBoard.array[32][1] = "P"
		MyBoard.array[4][1] = "D"
		MyPlayer = classes.Player(32,1,score,level)
		MyDonkey = classes.Donkey(4,1,0,level)
	while True:
		bg = pygame.image.load("dk.jpg")
		bgrect = bg.get_rect()
		sc = "Press P to Play"
		sc1 = "Press Q to Quit" 
 		text = font.render(sc, True, BLUE)
	 	text1 = font.render(sc1, True, BLUE)
		gameboard.screen.blit(bg,bgrect)
      		gameboard.screen.blit(text,(1080,325))
	      	gameboard.screen.blit(text1,(1085,425))
		pygame.display.flip()
	    	for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
		
			elif event.type == KEYDOWN:
				if event.key == K_p:
					fl = 1
					break
				elif event.key == K_q:
					pygame.quit()
					sys.exit()
		if fl == 1:
			fl = 0
			break
	
	gameboard.screen.fill(BLACK)	               
	while MyBoard.Lost == False:
		MyBoard.printGame()
		MyPlayer.printScore()
		MyPlayer.printLevel()
		MyPlayer.printLives()
		MyPlayer.printInstructions()
		control.moveInput(MyPlayer,MyDonkey,MyBoard)
		#MyDonkey.moveDonkey(MyBoard)
		if MyPlayer._posx == 1:
			MyPlayer.levelUp()
			level = level + 1
			score = MyPlayer.retScore()
			break
	
	if MyBoard.Lost:
		level = 1
		score = 0		
	MyPlayer._won = False
	MyPlayer._Lost = True
	func(level,score)

def main():
	func(1,0)

if __name__ == "__main__":
	main()
