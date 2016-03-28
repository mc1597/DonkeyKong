#!/usr/bin/python 
import sys
import random
import gameboard
import pygame
import time
import classes
from pygame.locals import *

clock = pygame.time.Clock()
font = pygame.font.SysFont("comicsansms", 36)
font1 = pygame.font.SysFont("comicsansms", 76)
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,125,0)
BLUE = (0,0,255)

def moveInput(player,donkey,instgame):
		pressed_a = False
		pressed_d = False
		cnt = 0
		cntf = 0
		cntb = 0
		fireballs = []
		
		while True:
			keys = pygame.key.get_pressed()
    			for event in pygame.event.get():
			        if event.type == QUIT:
			            pygame.quit()
			            sys.exit()
				elif keys[K_SPACE] and keys[K_d]:
					player.Jump(1,instgame)			#jump right
					pressed_a = False
					pressed_d = False
				elif keys[K_SPACE] and keys[K_a]:
					player.Jump(0,instgame)			#jump left	
					pressed_a = False
					pressed_d = False
			        elif event.type == KEYDOWN:
			            if event.key == K_a:
			                pressed_a = True
			            elif event.key == K_d:
			                pressed_d = True    
			            elif event.key == K_w:
			                player.MoveUp(instgame)
			            elif event.key == K_s:
			                player.MoveDown(instgame)
			            elif event.key == K_q:
			            	pygame.quit()
			            	sys.exit()
			        elif event.type == KEYUP:
			            if event.key == K_a:
  			            	pressed_a = False
 			            elif event.key == K_d:
 			            	pressed_d = False
			
			if player._posx == 1:
				break
			if player._won is True:
				break
			if player.retLives() == 0:
				instgame.Lost = True
				break
			if pressed_a:					
		        	player.MoveLeft(instgame)				#cont movement of player on holding down key
			if pressed_d:
		        	player.MoveRight(instgame)
			clock.tick(15)
			cnt = cnt + 1
			if cnt%7 == 0:
				donkey.moveDonkey(instgame)
			if cntb%4 == 0:
				for ball in fireballs:
					if ball._dead is True:
						fireballs.remove(ball)
					else:
						ball.movefb(player,instgame)	
			if cntf%240 == 0:
				fireballs.append(classes.Fireball(donkey,player))
			cntf = cntf + 1
			cntb = cntb + 1
			instgame.printGame()
			player.printScore()
			player.printLives()
