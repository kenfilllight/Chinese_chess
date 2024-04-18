
from math import fabs
from pickle import FALSE, TRUE
from re import T
from tkinter.font import ITALIC
import pygame
import os
##tcp
from re import A
import sys
import socket
import struct
import binascii
import threading
PORT = 6666
backlog = 5
BUF_SIZE = 1024	


FPS=60
BLUE=(0,255,255)
BLACK=(0,0,0)
WHITE=(255,255,255)
GREEN=(196, 255, 14)
RED=(255,0,0)
YELLOW=(255,255,0)
CHESSSIZE=(80,70)
WIDTH=900
HEIGHT=1000
GEEN=(0,255,0)

radius=35
global boardleft
boardleft=17
global boardtop
boardtop=25
global boarddown
boarddown=907
global boardright
boardright=801
global oneblock
oneblock=98
all_whitebox=[]
all_redbox=[]
all_blackbox=[]
all_chessbox=[]
peacebox=[]

global blackriver
blackriver=515
global redriver
redriver=417
global start
start=False

send_move=[]
global count
count=[]
global caneat
caneat=[]
client=0

pygame.init()
screen=pygame.display.set_mode((WIDTH, HEIGHT))#長寬
pygame.display.set_caption("first game")#視窗標頭
clock=pygame.time.Clock()#畫面更新率

#載入圖片#########################################
second_background_img=pygame.image.load(os.path.join("image1","broad.png")).convert() #載入圖片
second_background_img=pygame.transform.scale(second_background_img,(WIDTH,HEIGHT))
first_background_img=pygame.image.load(os.path.join("image1","background.png")).convert()
first_background_img=pygame.transform.scale(first_background_img,(WIDTH,HEIGHT))
white_img=pygame.image.load(os.path.join("image1","white.png")).convert()
dott_img=pygame.image.load(os.path.join("image1","dott.png")).convert()
redwin_img=pygame.image.load(os.path.join("image1","redwin.png")).convert()
blackwin_img=pygame.image.load(os.path.join("image1","blackwin.png")).convert()
peace_img=pygame.image.load(os.path.join("image1","peace.png")).convert()
peace__img=pygame.image.load(os.path.join("image1","peace.png")).convert()
peace_yes_img=pygame.image.load(os.path.join("image1","peace_yes.png")).convert()
peace_no_img=pygame.image.load(os.path.join("image1","peace_no.png")).convert()
peaceend_img=pygame.image.load(os.path.join("image1","peace_end.png")).convert()


black_bomb_img=pygame.image.load(os.path.join("image1","black_bomb.png")).convert()
red_bomb_img=pygame.image.load(os.path.join("image1","red_bomb.png")).convert()
black_elephant_img=pygame.image.load(os.path.join("image1","black_elephant.png")).convert()
red_elephant_img=pygame.image.load(os.path.join("image1","red_elephant.png")).convert()
black_horse_img=pygame.image.load(os.path.join("image1","black_horse.png")).convert()
red_horse_img=pygame.image.load(os.path.join("image1","red_horse.png")).convert()
black_king_img=pygame.image.load(os.path.join("image1","black_king.png")).convert()
red_king_img=pygame.image.load(os.path.join("image1","red_king.png")).convert()
black_knight_img=pygame.image.load(os.path.join("image1","black_knight.png")).convert()
red_knight_img=pygame.image.load(os.path.join("image1","red_knight.png")).convert()
black_soldier_img=pygame.image.load(os.path.join("image1","black_soldier.png")).convert()
red_soldier_img=pygame.image.load(os.path.join("image1","red_soldier.png")).convert()
black_car_img=pygame.image.load(os.path.join("image1","black_car.png")).convert()
red_car_img=pygame.image.load(os.path.join("image1","red_car.png")).convert()

black_f_bomb_img=pygame.image.load(os.path.join("image1","black_bomb1.png")).convert()
red_f_bomb_img=pygame.image.load(os.path.join("image1","red_bomb1.png")).convert()
black_f_elephant_img=pygame.image.load(os.path.join("image1","black_elephant1.png")).convert()
red_f_elephant_img=pygame.image.load(os.path.join("image1","red_elephant1.png")).convert()
black_f_horse_img=pygame.image.load(os.path.join("image1","black_horse1.png")).convert()
red_f_horse_img=pygame.image.load(os.path.join("image1","red_horse1.png")).convert()
black_f_king_img=pygame.image.load(os.path.join("image1","black_king1.png")).convert()
red_f_king_img=pygame.image.load(os.path.join("image1","red_king1.png")).convert()
black_f_knight_img=pygame.image.load(os.path.join("image1","black_knight1.png")).convert()
red_f_knight_img=pygame.image.load(os.path.join("image1","red_knight1.png")).convert()
black_f_soldier_img=pygame.image.load(os.path.join("image1","black_soldier1.png")).convert()
red_f_soldier_img=pygame.image.load(os.path.join("image1","red_soldier1.png")).convert()
black_f_car_img=pygame.image.load(os.path.join("image1","black_car1.png")).convert()
red_f_car_img=pygame.image.load(os.path.join("image1","red_car1.png")).convert()

blackturn_img=pygame.image.load(os.path.join("image1","black_turn.png")).convert()
redturn_img=pygame.image.load(os.path.join("image1","red_turn.png")).convert()
###################################################





###################################################

pygame.font.init()
font_name=os.path.join("font.ttf")#選擇文字

#顯示文字(遊戲分數)

def draw_text(surf,text,size,x,y,color):
	font=pygame.font.Font(font_name,size)
	text_surface=font.render(text,True,color)  
	text_rect=text_surface.get_rect()
	text_rect.centerx =x
	text_rect.top=y
	surf.blit(text_surface,text_rect)
	
def draw_init():
	screen.blit(first_background_img,(0,0))
	draw_text(screen,'象棋',150,WIDTH/2,HEIGHT/4,GEEN)
	draw_text(screen,'按一下滑鼠開始遊戲!',50,WIDTH/2,HEIGHT*3/4,WHITE)
 
  
#導入棋子圖片的物件加動畫###################################################

class Bomb(pygame.sprite.Sprite):
		def __init__(self,id,x,y):
			pygame.sprite.Sprite.__init__(self)
			self.id=id
			self.type='Bomb'
			self.beeat=False
			
			if self.id == 'b1' or self.id == 'b2':
				self.image=pygame.transform.scale(black_bomb_img,CHESSSIZE)#重新定義圖片大小
				self.image.set_colorkey(WHITE)#把黑色變透明
				self.rect=self.image.get_rect()#定位圖片
				self.type_color='black'
					
			if self.id == 'r1' or self.id == 'r2':
				self.image=pygame.transform.scale(red_bomb_img,CHESSSIZE)#重新定義圖片大小
				self.image.set_colorkey(WHITE)#把黑色變透明
				self.rect=self.image.get_rect()#定位圖片
				self.type_color='red'
					
			self.rect.left=x#0
			self.rect.bottom=y#1000
   
			if self.id == 'b1' or self.id == 'r1':
				self.speedx=5
				self.speedy=10
			if self.id == 'b2'or self.id == 'r2':
				self.speedx=45
				self.speedy=10
			self.chessbox = pygame.Rect(self.rect.x,self.rect.y,self.rect.width,self.rect.height)
			self.stopupdate=False
			self.arrivedx=False
			self.arrivedy=False
   
		def move(self,x,y):
			if self.id == 'b1' or self.id == 'b2':
				self.chessbox.move_ip(x-self.rect.x,y-self.rect.y)
				self.rect.x=x
				self.rect.y=y

			elif self.id == 'r1' or self.id == 'r2':
				self.chessbox.move_ip(x-self.rect.x,y-self.rect.y)
				self.rect.x=x
				self.rect.y=y
		def change_to_frame(self):
			if self.id == 'b1' or self.id == 'b2':
				self.image = pygame.transform.scale(black_f_bomb_img,CHESSSIZE)
				self.image.set_colorkey(WHITE)
				self.beeat=True
			if self.id == 'r1' or self.id == 'r2':
				self.image = pygame.transform.scale(red_f_bomb_img,CHESSSIZE)
				self.image.set_colorkey(WHITE)
				self.beeat=True
		def change_to_noframe(self):
			if self.id == 'b1' or self.id == 'b2':
				self.image = pygame.transform.scale(black_bomb_img,CHESSSIZE)
				self.image.set_colorkey(WHITE)
				self.beeat=False
			if self.id == 'r1' or self.id == 'r2':
				self.image = pygame.transform.scale(red_bomb_img,CHESSSIZE)
				self.image.set_colorkey(WHITE)
				self.beeat=False
		def update(self):
			if self.id == 'b1' and self.stopupdate==False:
				if self.rect.x!=115:
					self.rect.x+=self.speedx
					if self.rect.x>=115:
						self.rect.x=115
						self.arrivedx=True                       
				if self.rect.y!=boarddown-oneblock*2:   
					self.rect.y-=self.speedy
					if self.rect.y<=boarddown-oneblock*2:
						self.rect.y=boarddown-oneblock*2
						self.arrivedy=True
				if self.arrivedx==True and self.arrivedy==True:
						self.stopupdate=True  
				if self.stopupdate==True:
					self.chessbox = pygame.Rect(self.rect.x,self.rect.y,self.rect.width,self.rect.height)        
			if self.id == 'b2'and self.stopupdate==False:
				if self.rect.x!=703:
					self.rect.x+=self.speedx 
					if self.rect.x>=703:
						self.rect.x=703
						self.arrivedx=True
				if self.rect.y!=boarddown-oneblock*2:   
					self.rect.y-=self.speedy
					if self.rect.y<=boarddown-oneblock*2:
						self.rect.y=boarddown-oneblock*2 
						self.arrivedy=True  
				if self.arrivedx==True and self.arrivedy==True:
					self.stopupdate=True
				if self.stopupdate==True:
					self.chessbox = pygame.Rect(self.rect.x,self.rect.y,self.rect.width,self.rect.height)  
			if self.id == 'r1'and self.stopupdate==False:
				if self.rect.x!=115:
					self.rect.x+=self.speedx
					if self.rect.x>=115:
						self.rect.x=115
						self.arrivedx=True
				if self.rect.y!=boardtop+oneblock*2:   
					self.rect.y+=self.speedy
					if self.rect.y>=boardtop+oneblock*2:
						self.rect.y=boardtop+oneblock*2
						self.arrivedy=True
				if self.arrivedx==True and self.arrivedy==True:
					self.stopupdate=True
				if self.stopupdate==True:
					self.chessbox = pygame.Rect(self.rect.x,self.rect.y,self.rect.width,self.rect.height) 
			if self.id == 'r2'and self.stopupdate==False: 
				if self.rect.x!=703:
					self.rect.x+=self.speedx 
					if self.rect.x>=703:
						self.rect.x=703
						self.arrivedx=True
				if self.rect.y!=boardtop+oneblock*2:   
					self.rect.y+=self.speedy
					if self.rect.y>=boardtop+oneblock*2:
						self.rect.y=boardtop+oneblock*2
						self.arrivedy=True
				if self.arrivedx==True and self.arrivedy==True:
					self.stopupdate=True 
				if self.stopupdate==True:
					self.chessbox = pygame.Rect(self.rect.x,self.rect.y,self.rect.width,self.rect.height) 		
       
class Elephant(pygame.sprite.Sprite):
		def __init__(self,id,x,y):
			pygame.sprite.Sprite.__init__(self)
			self.id=id
			self.type='Elephant'
			self.beeat=False
			if self.id == 'b1' or self.id == 'b2':
				self.image=pygame.transform.scale(black_elephant_img,CHESSSIZE)#重新定義圖片大小
				self.image.set_colorkey(WHITE)#把黑色變透明
				self.rect=self.image.get_rect()#定位圖片 
				self.type_color='black'
				
			if self.id == 'r1' or self.id == 'r2':
				self.image=pygame.transform.scale(red_elephant_img,CHESSSIZE)#重新定義圖片大小
				self.image.set_colorkey(WHITE)#把黑色變透明
				self.rect=self.image.get_rect()#定位圖片
				self.type_color='red'
				
			self.rect.left=x#0
			self.rect.bottom=y#1000
			if self.id == 'b1' or self.id == 'r1':
				self.speedx=15
				self.speedy=7
			if self.id == 'b2'or self.id == 'r2':
				self.speedx=45
				self.speedy=7
			self.chessbox = pygame.Rect(self.rect.x,self.rect.y,self.rect.width,self.rect.height)
			self.stopupdate=False
			self.arrivedx=False
			self.arrivedy=False
		def move(self,x,y):
			if self.id == 'b1' or self.id == 'b2':
				self.chessbox.move_ip(x-self.rect.x,y-self.rect.y)
				self.rect.x=x
				self.rect.y=y

			elif self.id == 'r1' or self.id == 'r2':
				self.chessbox.move_ip(x-self.rect.x,y-self.rect.y)
				self.rect.x=x
				self.rect.y=y
		def change_to_frame(self):
			if self.id == 'b1' or self.id == 'b2':
				self.image = pygame.transform.scale(black_f_elephant_img,CHESSSIZE)
				self.image.set_colorkey(WHITE)
				self.beeat=True
			if self.id == 'r1' or self.id == 'r2':
				self.image = pygame.transform.scale(red_f_elephant_img,CHESSSIZE)
				self.image.set_colorkey(WHITE)
				self.beeat=True
		def change_to_noframe(self):
			if self.id == 'b1' or self.id == 'b2':
				self.image = pygame.transform.scale(black_elephant_img,CHESSSIZE)
				self.image.set_colorkey(WHITE)
				self.beeat=False
			if self.id == 'r1' or self.id == 'r2':
				self.image = pygame.transform.scale(red_elephant_img,CHESSSIZE)
				self.image.set_colorkey(WHITE)
				self.beeat=False
		def update(self):
			if self.id == 'b1' and self.stopupdate==False:
				if self.rect.x!=213:
					self.rect.x+=self.speedx
					if self.rect.x>=213:
						self.rect.x=213
						self.arrivedx=True                       
				if self.rect.y!=boarddown:   
					self.rect.y-=self.speedy
					if self.rect.y<=boarddown:
						self.rect.y=boarddown 
						self.arrivedy=True
				if self.arrivedx==True and self.arrivedy==True:
					self.stopupdate=True   
				if self.stopupdate==True:
					self.chessbox = pygame.Rect(self.rect.x,self.rect.y,self.rect.width,self.rect.height)       
			if self.id == 'b2'and self.stopupdate==False:
				if self.rect.x!=605:
					self.rect.x+=self.speedx 
					if self.rect.x>=605:
						self.rect.x=605
						self.arrivedx=True
				if self.rect.y!=boarddown:   
					self.rect.y-=self.speedy
					if self.rect.y<=boarddown:
						self.rect.y=boarddown 
						self.arrivedy=True  
				if self.arrivedx==True and self.arrivedy==True:
					self.stopupdate=True 
				if self.stopupdate==True:
					self.chessbox = pygame.Rect(self.rect.x,self.rect.y,self.rect.width,self.rect.height) 
			if self.id == 'r1'and self.stopupdate==False:
				if self.rect.x!=213:
					self.rect.x+=self.speedx
					if self.rect.x>=213:
						self.rect.x=213
						self.arrivedx=True
				if self.rect.y!=boardtop:   
					self.rect.y+=self.speedy
					if self.rect.y>=boardtop:
						self.rect.y=boardtop
						self.arrivedy=True
				if self.arrivedx==True and self.arrivedy==True:
					self.stopupdate=True
				if self.stopupdate==True:
					self.chessbox = pygame.Rect(self.rect.x,self.rect.y,self.rect.width,self.rect.height) 
			if self.id == 'r2'and self.stopupdate==False: 
				if self.rect.x!=605:
					self.rect.x+=self.speedx 
					if self.rect.x>=605:
						self.rect.x=605
						self.arrivedx=True
				if self.rect.y!=boardtop:   
					self.rect.y+=self.speedy
					if self.rect.y>=boardtop:
						self.rect.y=boardtop
						self.arrivedy=True
				if self.arrivedx==True and self.arrivedy==True:
					self.stopupdate=True              
				if self.stopupdate==True:
					self.chessbox = pygame.Rect(self.rect.x,self.rect.y,self.rect.width,self.rect.height) 

class Horse(pygame.sprite.Sprite):
		def __init__(self,id,x,y):
			pygame.sprite.Sprite.__init__(self)
			self.id=id
			self.type='Horse'
			self.beeat=False
			if self.id == 'b1' or self.id == 'b2':
				self.image=pygame.transform.scale(black_horse_img,CHESSSIZE)#重新定義圖片大小
				self.image.set_colorkey(WHITE)#把黑色變透明
				self.rect=self.image.get_rect()#定位圖片 
				self.type_color='black'
				
			if self.id == 'r1' or self.id == 'r2':
				self.image=pygame.transform.scale(red_horse_img,CHESSSIZE)#重新定義圖片大小
				self.image.set_colorkey(WHITE)#把黑色變透明
				self.rect=self.image.get_rect()#定位圖片
				self.type_color='red'
				
			self.rect.left=x#0
			self.rect.bottom=y#1000
			if self.id == 'b1' or self.id == 'r1':
				self.speedx=15
				self.speedy=7
			if self.id == 'b2'or self.id == 'r2':
				self.speedx=45
				self.speedy=7
			self.chessbox = pygame.Rect(self.rect.x,self.rect.y,self.rect.width,self.rect.height)
			self.stopupdate=False
			self.arrivedx=False
			self.arrivedy=False
		def move(self,x,y):
			if self.id == 'b1' or self.id == 'b2':
				self.chessbox.move_ip(x-self.rect.x,y-self.rect.y)
				self.rect.x=x
				self.rect.y=y

			elif self.id == 'r1' or self.id == 'r2':
				self.chessbox.move_ip(x-self.rect.x,y-self.rect.y)
				self.rect.x=x
				self.rect.y=y
		def change_to_frame(self):
			if self.id == 'b1' or self.id == 'b2':
				self.image = pygame.transform.scale(black_f_horse_img,CHESSSIZE)
				self.image.set_colorkey(WHITE)
				self.beeat=True
			if self.id == 'r1' or self.id == 'r2':
				self.image = pygame.transform.scale(red_f_horse_img,CHESSSIZE)
				self.image.set_colorkey(WHITE)
				self.beeat=True
		def change_to_noframe(self):
			if self.id == 'b1' or self.id == 'b2':
				self.image = pygame.transform.scale(black_horse_img,CHESSSIZE)
				self.image.set_colorkey(WHITE)
				self.beeat=False
			if self.id == 'r1' or self.id == 'r2':
				self.image = pygame.transform.scale(red_horse_img,CHESSSIZE)
				self.image.set_colorkey(WHITE)
				self.beeat=False
		def update(self):
			if self.id == 'b1' and self.stopupdate==False:
				if self.rect.x!=115:
					self.rect.x+=self.speedx
					if self.rect.x>=115:
						self.rect.x=115
						self.arrivedx=True                       
				if self.rect.y!=boarddown:   
					self.rect.y-=self.speedy
					if self.rect.y<=boarddown:
						self.rect.y=boarddown 
						self.arrivedy=True
				if self.arrivedx==True and self.arrivedy==True:
					self.stopupdate=True  
				if self.stopupdate==True:
					self.chessbox = pygame.Rect(self.rect.x,self.rect.y,self.rect.width,self.rect.height)        
			if self.id == 'b2'and self.stopupdate==False:
				if self.rect.x!=703:
					self.rect.x+=self.speedx 
					if self.rect.x>=703:
						self.rect.x=703
						self.arrivedx=True
				if self.rect.y!=boarddown:   
					self.rect.y-=self.speedy
					if self.rect.y<=boarddown:
						self.rect.y=boarddown 
						self.arrivedy=True  
				if self.arrivedx==True and self.arrivedy==True:
					self.stopupdate=True 
				if self.stopupdate==True:
					self.chessbox = pygame.Rect(self.rect.x,self.rect.y,self.rect.width,self.rect.height) 
			if self.id == 'r1'and self.stopupdate==False:
				if self.rect.centerx!=115:
					self.rect.x+=self.speedx
					if self.rect.x>=115:
						self.rect.x=115
						self.arrivedx=True
				if self.rect.y!=boardtop:   
					self.rect.y+=self.speedy
					if self.rect.y>=boardtop:
						self.rect.y=boardtop
						self.arrivedy=True
				if self.arrivedx==True and self.arrivedy==True:
					self.stopupdate=True
				if self.stopupdate==True:
					self.chessbox = pygame.Rect(self.rect.x,self.rect.y,self.rect.width,self.rect.height) 
			if self.id == 'r2'and self.stopupdate==False: 
				if self.rect.x!=703:
					self.rect.x+=self.speedx 
					if self.rect.x>=703:
						self.rect.x=703
						self.arrivedx=True
				if self.rect.y!=boardtop:   
					self.rect.y+=self.speedy
					if self.rect.y>=boardtop:
						self.rect.y=boardtop
						self.arrivedy=True
				if self.arrivedx==True and self.arrivedy==True:
					self.stopupdate=True   
				if self.stopupdate==True:
					self.chessbox = pygame.Rect(self.rect.x,self.rect.y,self.rect.width,self.rect.height) 

class kING(pygame.sprite.Sprite):
		def __init__(self,id,x,y):
			pygame.sprite.Sprite.__init__(self)
			self.id=id
			self.type='kING'
			self.beeat=False
			if self.id == 'b1':
				self.image=pygame.transform.scale(black_king_img,CHESSSIZE)#重新定義圖片大小
				self.image.set_colorkey(WHITE)#把黑色變透明
				self.rect=self.image.get_rect()#定位圖片 
				self.type_color='black'
				
			if self.id == 'r1' :
				self.image=pygame.transform.scale(red_king_img,CHESSSIZE)#重新定義圖片大小
				self.image.set_colorkey(WHITE)#把黑色變透明
				self.rect=self.image.get_rect()#定位圖片
				self.type_color='red'
				
			self.rect.left=x#0
			self.rect.bottom=y#1000
			self.speedx=25
			self.speedy=5
			self.chessbox = pygame.Rect(self.rect.x,self.rect.y,self.rect.width,self.rect.height)
			self.stopupdate=False
			self.arrivedx=False
			self.arrivedy=False
   
		def move(self,x,y):
			if self.id == 'b1' :
				self.chessbox.move_ip(x-self.rect.x,y-self.rect.y)
				self.rect.x=x
				self.rect.y=y

			elif self.id == 'r1':
				self.chessbox.move_ip(x-self.rect.x,y-self.rect.y)
				self.rect.x=x
				self.rect.y=y
		def change_to_frame(self):
			if self.id == 'b1':
				self.image = pygame.transform.scale(black_f_king_img,CHESSSIZE)
				self.image.set_colorkey(WHITE)
				self.beeat=True
			if self.id == 'r1':
				self.image = pygame.transform.scale(red_f_king_img,CHESSSIZE)
				self.image.set_colorkey(WHITE)
				self.beeat=True
		def change_to_noframe(self):
			if self.id == 'b1':
				self.image = pygame.transform.scale(black_king_img,CHESSSIZE)
				self.image.set_colorkey(WHITE)
				self.beeat=False
			if self.id == 'r1':
				self.image = pygame.transform.scale(red_king_img,CHESSSIZE)
				self.image.set_colorkey(WHITE)	
				self.beeat=False
		def update(self):
			if self.id == 'b1' and self.stopupdate==False:
				if self.rect.x!=409:
					self.rect.x+=self.speedx
					if self.rect.x>=409:
						self.rect.x=409
						self.arrivedx=True                       
				if self.rect.y!=boarddown:   
					self.rect.y-=self.speedy
					if self.rect.y<=boarddown:
						self.rect.y=boarddown
						self.arrivedy=True
				if self.arrivedx==True and self.arrivedy==True:
					self.stopupdate=True 
				if self.stopupdate==True:
					self.chessbox = pygame.Rect(self.rect.x,self.rect.y,self.rect.width,self.rect.height)        
			if self.id == 'r1'and self.stopupdate==False:
				if self.rect.x!=409:
					self.rect.x+=self.speedx
					if self.rect.x>=409:
						self.rect.x=409
						self.arrivedx=True
				if self.rect.y!=boardtop:   
					self.rect.y+=self.speedy
					if self.rect.y>=boardtop:
						self.rect.y=boardtop
						self.arrivedy=True
				if self.arrivedx==True and self.arrivedy==True:
					self.stopupdate=True  
				if self.stopupdate==True:
					self.chessbox = pygame.Rect(self.rect.x,self.rect.y,self.rect.width,self.rect.height)
    					 
class Knight(pygame.sprite.Sprite):
		def __init__(self,id,x,y):
			pygame.sprite.Sprite.__init__(self)
			self.id=id
			self.type='Knight'
			self.beeat=False
			if self.id == 'b1' or self.id == 'b2':
				self.image=pygame.transform.scale(black_knight_img,CHESSSIZE)#重新定義圖片大小
				self.image.set_colorkey(WHITE)#把黑色變透明
				self.rect=self.image.get_rect()#定位圖片  
				self.type_color='black'
				
			if self.id == 'r1' or self.id == 'r2':
				self.image=pygame.transform.scale(red_knight_img,CHESSSIZE)#重新定義圖片大小
				self.image.set_colorkey(WHITE)#把黑色變透明
				self.rect=self.image.get_rect()#定位圖片
				self.type_color='red'
				
			self.rect.left=x#0
			self.rect.bottom=y#1000
			self.speedx=25
			self.speedy=5
			self.chessbox = pygame.Rect(self.rect.x,self.rect.y,self.rect.width,self.rect.height)
			self.stopupdate=False
			self.arrivedx=False
			self.arrivedy=False

		def move(self,x,y):
			if self.id == 'b1' or self.id == 'b2':
				self.chessbox.move_ip(x-self.rect.x,y-self.rect.y)
				self.rect.x=x
				self.rect.y=y

			elif self.id == 'r1' or self.id == 'r2':
				self.chessbox.move_ip(x-self.rect.x,y-self.rect.y)
				self.rect.x=x
				self.rect.y=y
		def change_to_frame(self):
			if self.id == 'b1' or self.id == 'b2':
				self.image = pygame.transform.scale(black_f_knight_img,CHESSSIZE)
				self.image.set_colorkey(WHITE)
				self.beeat=True
			if self.id == 'r1' or self.id == 'r2':
				self.image = pygame.transform.scale(red_f_knight_img,CHESSSIZE)
				self.image.set_colorkey(WHITE)
				self.beeat=True
		def change_to_noframe(self):
			if self.id == 'b1' or self.id == 'b2':
				self.image = pygame.transform.scale(black_knight_img,CHESSSIZE)
				self.image.set_colorkey(WHITE)
				self.beeat=False
			if self.id == 'r1' or self.id == 'r2':
				self.image = pygame.transform.scale(red_knight_img,CHESSSIZE)
				self.image.set_colorkey(WHITE)
				self.beeat=False
		def update(self):
			if self.id == 'b1' and self.stopupdate==False:
				if self.rect.x!=311:
					self.rect.x+=self.speedx
					if self.rect.x>=311:
						self.rect.x=311
						self.arrivedx=True                     
				if self.rect.y!=boarddown:   
					self.rect.y-=self.speedy
					if self.rect.y<=boarddown:
						self.rect.y=boarddown
						self.arrivedy=True
				if self.arrivedx==True and self.arrivedy==True:
					self.stopupdate=True   
				if self.stopupdate==True:
					self.chessbox = pygame.Rect(self.rect.x,self.rect.y,self.rect.width,self.rect.height)
			if self.id == 'b2'and self.stopupdate==False:
				if self.rect.x!=507:
					self.rect.x+=self.speedx 
					if self.rect.x>=507:
						self.rect.x=507
						self.arrivedx=True
				if self.rect.y!=boarddown:   
					self.rect.y-=self.speedy
					if self.rect.y<=boarddown:
						self.rect.y=boarddown
						self.arrivedy=True
				if self.arrivedx==True and self.arrivedy==True:
					self.stopupdate=True 
				if self.stopupdate==True:
					self.chessbox = pygame.Rect(self.rect.x,self.rect.y,self.rect.width,self.rect.height)
			if self.id == 'r1'and self.stopupdate==False:
				if self.rect.x!=311:
					self.rect.x+=self.speedx
					if self.rect.x>=311:
						self.rect.x=311
						self.arrivedx=True
				if self.rect.y!=boardtop:   
					self.rect.y+=self.speedy
					if self.rect.y>=boardtop:
						self.rect.y=boardtop
						self.arrivedy=True
				if self.arrivedx==True and self.arrivedy==True:
					
					self.stopupdate=True
				if self.stopupdate==True:
					self.chessbox = pygame.Rect(self.rect.x,self.rect.y,self.rect.width,self.rect.height)
			if self.id == 'r2'and self.stopupdate==False: 
				if self.rect.x!=507:
					self.rect.x+=self.speedx 
					if self.rect.x>=507:
						self.rect.x=507
						self.arrivedx=True
				if self.rect.y!=boardtop:   
					self.rect.y+=self.speedy
					if self.rect.y>=boardtop:
						self.rect.y=boardtop
						self.arrivedy=True
				if self.arrivedx==True and self.arrivedy==True:
					self.stopupdate=True   
				if self.stopupdate==True:
					self.chessbox = pygame.Rect(self.rect.x,self.rect.y,self.rect.width,self.rect.height)
				
     	   
class Car(pygame.sprite.Sprite):
		def __init__(self,id,x,y):
			pygame.sprite.Sprite.__init__(self)
			self.id=id
			self.type='Car'
			self.beeat=False
			if self.id == 'b1' or self.id == 'b2':
				self.image=pygame.transform.scale(black_car_img,CHESSSIZE)#重新定義圖片大小
				self.image.set_colorkey(WHITE)#把黑色變透明
				self.rect=self.image.get_rect()#定位圖片
				self.type_color='black'
				
			if self.id == 'r1' or self.id == 'r2':
				self.image=pygame.transform.scale(red_car_img,CHESSSIZE)#重新定義圖片大小
				self.image.set_colorkey(WHITE)#把黑色變透明
				self.rect=self.image.get_rect()#定位圖片
				self.type_color='red'
				
			self.rect.left=x#0
			self.rect.bottom=y#1000
			if self.id == 'b1' or self.id == 'r1':
				self.speedx=25
				self.speedy=5
			if self.id == 'b2'or self.id == 'r2':
				self.speedx=45
				self.speedy=5
			self.chessbox = pygame.Rect(self.rect.x,self.rect.y,self.rect.width,self.rect.height)
			self.stopupdate=False
			self.arrivedx=False
			self.arrivedy=False

		def move(self,x,y):
			if self.id == 'b1' or self.id == 'b2':
				self.chessbox.move_ip(x-self.rect.x,y-self.rect.y)
				self.rect.x=x
				self.rect.y=y

			elif self.id == 'r1' or self.id == 'r2':
				self.chessbox.move_ip(x-self.rect.x,y-self.rect.y)
				self.rect.x=x
				self.rect.y=y
		def change_to_frame(self):
			if self.id == 'b1' or self.id == 'b2':
				self.image = pygame.transform.scale(black_f_car_img,CHESSSIZE)
				self.image.set_colorkey(WHITE)
				self.beeat=True
			if self.id == 'r1' or self.id == 'r2':
				self.image = pygame.transform.scale(red_f_car_img,CHESSSIZE)
				self.image.set_colorkey(WHITE)
				self.beeat=True
		def change_to_noframe(self):
			if self.id == 'b1' or self.id == 'b2':
				self.image = pygame.transform.scale(black_car_img,CHESSSIZE)
				self.image.set_colorkey(WHITE)
				self.beeat=False
			if self.id == 'r1' or self.id == 'r2':
				self.image = pygame.transform.scale(red_car_img,CHESSSIZE)
				self.image.set_colorkey(WHITE)
				self.beeat=False
 
		def update(self):
			if self.id == 'b1' and self.stopupdate==False:
				if self.rect.x!=17:
					self.rect.x+=self.speedx
					if self.rect.x>=17:
						self.rect.x=17
						self.arrivedx=True                       
				if self.rect.y!=boarddown:   
					self.rect.y-=self.speedy
					if self.rect.y<=boarddown:
						self.rect.y=boarddown 
						self.arrivedy=True
				if self.arrivedx==True and self.arrivedy==True:
					self.stopupdate=True    
				if self.stopupdate==True:
					self.chessbox = pygame.Rect(self.rect.x,self.rect.y,self.rect.width,self.rect.height)     
			if self.id == 'b2'and self.stopupdate==False:
				if self.rect.x!=801:
					self.rect.x+=self.speedx 
					if self.rect.x>=801:
						self.rect.x=801
						self.arrivedx=True
				if self.rect.y!=boarddown:   
					self.rect.y-=self.speedy
					if self.rect.y<=boarddown:
						self.rect.y=boarddown 
						self.arrivedy=True  
				if self.arrivedx==True and self.arrivedy==True:
					self.stopupdate=True 
				if self.stopupdate==True:
					self.chessbox = pygame.Rect(self.rect.x,self.rect.y,self.rect.width,self.rect.height)
			if self.id == 'r1'and self.stopupdate==False:
				if self.rect.x!=17:
					self.rect.centerx+=self.speedx
					if self.rect.x>=17:
						self.rect.x=17
						self.arrivedx=True
				if self.rect.y!=boardtop:   
					self.rect.y+=self.speedy
					if self.rect.y>=boardtop:
						self.rect.y=boardtop
						self.arrivedy=True
				if self.arrivedx==True and self.arrivedy==True:
					self.stopupdate=True
				if self.stopupdate==True:
					self.chessbox = pygame.Rect(self.rect.x,self.rect.y,self.rect.width,self.rect.height)
			if self.id == 'r2'and self.stopupdate==False: 
				if self.rect.x!=801:
					self.rect.x+=self.speedx 
					if self.rect.x>=801:
						self.rect.x=801
						self.arrivedx=True
				if self.rect.y!=boardtop:   
					self.rect.y+=self.speedy
					if self.rect.y>=boardtop:
						self.rect.y=boardtop
						self.arrivedy=True
				if self.arrivedx==True and self.arrivedy==True:
					self.stopupdate=True   
				if self.stopupdate==True:
					self.chessbox = pygame.Rect(self.rect.x,self.rect.y,self.rect.width,self.rect.height)
			
class Soldier(pygame.sprite.Sprite):
		def __init__(self,id,x,y):
			pygame.sprite.Sprite.__init__(self)
			self.id=id
			self.type='Soldier'
			self.beeat=False
			if self.id == 'b1' or self.id == 'b2'or self.id == 'b3' or self.id == 'b4'or self.id == 'b5':
				self.image=pygame.transform.scale(black_soldier_img,CHESSSIZE)#重新定義圖片大小
				self.image.set_colorkey(WHITE)#把黑色變透明
				self.rect=self.image.get_rect()#定位圖片 
				self.type_color='black'
				
			if self.id == 'r1' or self.id == 'r2'or self.id == 'r3' or self.id == 'r4'or self.id == 'r5':
				self.image=pygame.transform.scale(red_soldier_img,CHESSSIZE)#重新定義圖片大小
				self.image.set_colorkey(WHITE)#把黑色變透明
				self.rect=self.image.get_rect()#定位圖片
				self.type_color='red'
				
			self.rect.left=x#0
			self.rect.bottom=y#1000
			if self.id == 'b1' or self.id == 'r1':
				self.speedx=8
				self.speedy=15
			if self.id == 'b2'or self.id == 'r2':
				self.speedx=16
				self.speedy=15
			if self.id == 'b3'or self.id == 'r3':
				self.speedx=24
				self.speedy=15
			if self.id == 'b4'or self.id == 'r4':
				self.speedx=32
				self.speedy=15
			if self.id == 'b5'or self.id == 'r5':
				self.speedx=40
				self.speedy=15
			self.chessbox = pygame.Rect(self.rect.x,self.rect.y,self.rect.width,self.rect.height)
			self.stopupdate=False
			self.arrivedx=False
			self.arrivedy=False

		def move(self,x,y):
			if self.id == 'b1' or self.id == 'b2'or self.id == 'b3' or self.id == 'b4' or self.id == 'b5':
				self.chessbox.move_ip(x-self.rect.x,y-self.rect.y)
				self.rect.x=x
				self.rect.y=y

			elif self.id == 'r1' or self.id == 'r2'or self.id == 'r3' or self.id == 'r4' or self.id == 'r5':
				self.chessbox.move_ip(x-self.rect.x,y-self.rect.y)
				self.rect.x=x
				self.rect.y=y
		def change_to_frame(self):
			if self.id == 'b1' or self.id == 'b2'or self.id == 'b3' or self.id == 'b4'or self.id == 'b5':
				self.image = pygame.transform.scale(black_f_soldier_img,CHESSSIZE)
				self.image.set_colorkey(WHITE)
				self.beeat=True
			if self.id == 'r1' or self.id == 'r2'or self.id == 'r3' or self.id == 'r4' or self.id == 'r5':
				self.image = pygame.transform.scale(red_f_soldier_img,CHESSSIZE)
				self.image.set_colorkey(WHITE)	
				self.beeat=True
		def change_to_noframe(self):
			if self.id == 'b1' or self.id == 'b2'or self.id == 'b3' or self.id == 'b4'or self.id == 'b5':
				self.image = pygame.transform.scale(black_soldier_img,CHESSSIZE)
				self.image.set_colorkey(WHITE)
				self.beeat=False
			if self.id == 'r1' or self.id == 'r2'or self.id == 'r3' or self.id == 'r4' or self.id == 'r5':
				self.image = pygame.transform.scale(red_soldier_img,CHESSSIZE)
				self.image.set_colorkey(WHITE)
				self.beeat=False
		def update(self):
			if self.id == 'b1' and self.stopupdate==False:
				if self.rect.x!=17:
					self.rect.x+=self.speedx
					if self.rect.x>=17:
						self.rect.x=17
						self.arrivedx=True                           
				if self.rect.y!=boarddown-oneblock*3:   
					self.rect.y-=self.speedy
					if self.rect.y<=boarddown-oneblock*3:
						self.rect.y=boarddown-oneblock*3 
						self.arrivedy=True						
				if self.arrivedx==True and self.arrivedy==True:
					self.stopupdate=True
				if self.stopupdate==True:
					self.chessbox = pygame.Rect(self.rect.x,self.rect.y,self.rect.width,self.rect.height)
			if self.id == 'b2'and self.stopupdate==False:
				if self.rect.x!=213:
					self.rect.x+=self.speedx 
					if self.rect.x>=213:
						self.rect.x=213
						self.arrivedx=True
				if self.rect.y!=boarddown-oneblock*3:   
					self.rect.y-=self.speedy
					if self.rect.y<=boarddown-oneblock*3:
						self.rect.y=boarddown-oneblock*3 
						self.arrivedy=True  
				if self.arrivedx==True and self.arrivedy==True:
					self.stopupdate=True
				if self.stopupdate==True:
					self.chessbox = pygame.Rect(self.rect.x,self.rect.y,self.rect.width,self.rect.height)     
			if self.id == 'b3' and self.stopupdate==False:
				if self.rect.x!=409:
					self.rect.x+=self.speedx
					if self.rect.x>=409:
						self.rect.x=409
						self.arrivedx=True   
                          
				if self.rect.y!=boarddown-oneblock*3:   
					self.rect.y-=self.speedy
					if self.rect.y<=boarddown-oneblock*3:
						self.rect.y=boarddown-oneblock*3
						self.arrivedy=True
				if self.arrivedx==True and self.arrivedy==True:
					self.stopupdate=True
				if self.stopupdate==True:
					self.chessbox = pygame.Rect(self.rect.x,self.rect.y,self.rect.width,self.rect.height)
			if self.id == 'b4' and self.stopupdate==False:
				if self.rect.x!=605:
					self.rect.x+=self.speedx
					if self.rect.x>=605:
						self.rect.x=605
						self.arrivedx=True                       
				if self.rect.y!=boarddown-oneblock*3:   
					self.rect.y-=self.speedy
					if self.rect.y<=boarddown-oneblock*3:
						self.rect.y=boarddown-oneblock*3
						self.arrivedy=True
				if self.arrivedx==True and self.arrivedy==True:
					self.stopupdate=True
				if self.stopupdate==True:
					self.chessbox = pygame.Rect(self.rect.x,self.rect.y,self.rect.width,self.rect.height)     
			if self.id == 'b5' and self.stopupdate==False:
				if self.rect.x!=801:
					self.rect.x+=self.speedx
					if self.rect.x>=801:
						self.rect.x=801
						self.arrivedx=True                       
				if self.rect.y!=boarddown-oneblock*3:   
					self.rect.y-=self.speedy
					if self.rect.y<=boarddown-oneblock*3:
						self.rect.y=boarddown-oneblock*3 
						self.arrivedy=True
				if self.arrivedx==True and self.arrivedy==True:
					self.stopupdate=True 
				if self.stopupdate==True:
					self.chessbox = pygame.Rect(self.rect.x,self.rect.y,self.rect.width,self.rect.height)     
			if self.id == 'r1'and self.stopupdate==False:
				if self.rect.x!=17:
					self.rect.x+=self.speedx
					if self.rect.x>=17:
						self.rect.x=17
						self.arrivedx=True
				if self.rect.y!=boardtop+oneblock*3:   
					self.rect.y+=self.speedy
					if self.rect.y>=boardtop+oneblock*3:
						self.rect.y=boardtop+oneblock*3
						self.arrivedy=True
				if self.arrivedx==True and self.arrivedy==True:
					self.stopupdate=True
				if self.stopupdate==True:
					self.chessbox = pygame.Rect(self.rect.x,self.rect.y,self.rect.width,self.rect.height)     
			if self.id == 'r2'and self.stopupdate==False: 
				if self.rect.x!=213:
					self.rect.x+=self.speedx 
					if self.rect.x>=213:
						self.rect.x=213
						self.arrivedx=True
				if self.rect.y!=boardtop+oneblock*3:   
					self.rect.y+=self.speedy
					if self.rect.y>=boardtop+oneblock*3:
						self.rect.y=boardtop+oneblock*3
						self.arrivedy=True
				if self.arrivedx==True and self.arrivedy==True:
					self.stopupdate=True
				if self.stopupdate==True:
					self.chessbox = pygame.Rect(self.rect.x,self.rect.y,self.rect.width,self.rect.height)
			if self.id == 'r3'and self.stopupdate==False:
				if self.rect.x!=409:
					self.rect.x+=self.speedx
					if self.rect.x>=409:
						self.rect.x=409
						self.arrivedx=True
				if self.rect.y!=boardtop+oneblock*3:   
					self.rect.y+=self.speedy
					if self.rect.y>=boardtop+oneblock*3:
						self.rect.y=boardtop+oneblock*3
						self.arrivedy=True
				if self.arrivedx==True and self.arrivedy==True:
					self.stopupdate=True
				if self.stopupdate==True:
					self.chessbox = pygame.Rect(self.rect.x,self.rect.y,self.rect.width,self.rect.height)     
			if self.id == 'r4'and self.stopupdate==False: 
				if self.rect.x!=605:
					self.rect.x+=self.speedx 
					if self.rect.x>=605:
						self.rect.x=605
						self.arrivedx=True
				if self.rect.y!=boardtop+oneblock*3:   
					self.rect.y+=self.speedy
					if self.rect.y>=boardtop+oneblock*3:
						self.rect.y=boardtop+oneblock*3
						self.arrivedy=True
				if self.arrivedx==True and self.arrivedy==True:
					self.stopupdate=True
				if self.stopupdate==True:
					self.chessbox = pygame.Rect(self.rect.x,self.rect.y,self.rect.width,self.rect.height) 
			if self.id == 'r5'and self.stopupdate==False:
				if self.rect.x!=801:
					self.rect.x+=self.speedx
					if self.rect.x>=801:
						self.rect.x=801
						self.arrivedx=True
				if self.rect.y!=boardtop+oneblock*3:   
					self.rect.y+=self.speedy
					if self.rect.y>=boardtop+oneblock*3:
						self.rect.y=boardtop+oneblock*3
						self.arrivedy=True
				if self.arrivedx==True and self.arrivedy==True:
					self.stopupdate=True
				if self.stopupdate==True:
					self.chessbox = pygame.Rect(self.rect.x,self.rect.y,self.rect.width,self.rect.height) 

class space(pygame.sprite.Sprite):
    
	def __init__(self,x,y):
		self.type='space'
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.transform.scale(white_img,CHESSSIZE)
		self.image.set_colorkey(WHITE)
		self.rect=self.image.get_rect()
		self.rect.x=x
		self.rect.y=y
		self.active=False
		self.chessbox = pygame.Rect(self.rect.x,self.rect.y,self.rect.width,self.rect.height)
	def switch_on(self):
		self.image = pygame.transform.scale(dott_img,CHESSSIZE)
		self.image.set_colorkey(WHITE)
		self.active=True
		
	def switch_off(self):	
		self.image = pygame.transform.scale(white_img,CHESSSIZE)
		self.image.set_colorkey(WHITE)
		self.active=False

class peace_butt(pygame.sprite.Sprite):   
	def __init__(self,x,y):
		self.type='peace'
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.transform.scale(peace_img,(68,68))
		self.image.set_colorkey(WHITE)
		self.rect=self.image.get_rect()
		self.rect.x=x
		self.rect.y=y
		self.active=False
		self.chessbox = pygame.Rect(self.rect.x,self.rect.y,self.rect.width,self.rect.height)
	def switch_on(self):
		self.image = pygame.transform.scale(peace_yes_img,(68,68))
		self.image.set_colorkey(WHITE)
		self.active=True
		
	def switch_off(self):	
		self.image = pygame.transform.scale(peace_no_img,(68,68))
		self.image.set_colorkey(WHITE)
		self.active=False
###############################################################   
			
all_sprites=pygame.sprite.Group()

###################################################################
##棋子演算
def convert_to_hc(inner_x,inner_y):
	if inner_y<=907 and inner_y>=25 and inner_x>=17 and inner_x<=801:
		if inner_y==25:
			x=0
		if inner_y==123:
			x=1
		if inner_y==221:
			x=2
		if inner_y==319:
			x=3
		if inner_y==417:
			x=4
		if inner_y==515:
			x=5
		if inner_y==613:
			x=6	
		if inner_y==711:
			x=7
		if inner_y==809:
			x=8
		if inner_y==907:
			x=9
		if inner_x==17:
			y=0
		if inner_x==115:
			y=1  
		if inner_x==213:
			y=2
		if inner_x==311:
			y=3
		if inner_x==409:
			y=4
		if inner_x==507:
			y=5
		if inner_x==605:
			y=6
		if inner_x==703: 
			y=7
		if inner_x==801:
			y=8
	return x,y

def check(n,i):
	y=int()
	x=int()
	j=0

	x,y=convert_to_hc(i.chessbox.x,i.chessbox.y)
#Soldier
	if n==1:
			count.clear()
			if HAVECHESS[x][y]==1 and i.type=='Soldier':
					print(i.id,"chess_x,chess_y:",i.chessbox.x,i.chessbox.y,"havechess_x,havechess_y:",x,y)
					while(True):
						current_x=i.chessbox.x
						current_y=i.chessbox.y
						cx=x
						cy=y
						finish_1=0
						finish_2=0
						finish_3=0
						if i.id == 'b1' or i.id == 'b2'or i.id == 'b3' or i.id == 'b4'or i.id == 'b5':
							if current_y>=blackriver:	##黑兵未過河
								##黑兵上一格是否有棋
								#print('-------------top--------------')
								current_y -=oneblock
								cx-=1
								while(1):
									if current_y<25:
										print("over top range")
										finish_1=1
										finish_2=1
										finish_3=1
										break
									if HAVECHESS[cx][cy]==1:											
										#print("top have chess") 
										finish_1=1
										finish_2=1
										finish_3=1
										for j in all_redbox:
											if j.chessbox.y==current_y and j.chessbox.x==current_x:
												caneat.append(current_x)
												caneat.append(current_y)
										break
									if HAVECHESS[cx][cy]==0:
										print(cx,cy,current_x,current_y)
										count.append(current_x)
										count.append(current_y)
										finish_1=1
										finish_2=1
										finish_3=1
										break
							else:##黑兵過河	
								current_x=i.chessbox.x
								current_y=i.chessbox.y
								cx=x
								cy=y
								finish_1=0
								##黑兵上一格是否有棋
								#print('-------------top--------------')
								current_y -=oneblock
								cx-=1
								while(1):
									if current_y<25:
										#print("over top range")
										finish_1=1
										break
									if HAVECHESS[cx][cy]==1:											
										#print("top have chess")
										for j in all_redbox:
											if j.chessbox.y==current_y and j.chessbox.x==current_x:
												caneat.append(current_x)
												caneat.append(current_y)
										finish_1=1
										break
									if HAVECHESS[cx][cy]==0:
										#print(cx,cy,current_x,current_y)
										count.append(current_x)
										count.append(current_y)
										finish_1=1
										break

								##黑兵左一格是否有棋
								current_x=i.chessbox.x
								current_y=i.chessbox.y
								cx=x
								cy=y
								finish_2=0
								#print('-------------left--------------')
								current_x -=oneblock
								cy-=1
								while(1):
									if current_x<17:
										#print("over left range")
										finish_2=1
										break
									if HAVECHESS[cx][cy]==1:											
										#print("left have chess")
										for j in all_redbox:
											if j.chessbox.y==current_y and j.chessbox.x==current_x:
												caneat.append(current_x)
												caneat.append(current_y)
										finish_2=1
										break
									if HAVECHESS[cx][cy]==0:
										#(cx,cy,current_x,current_y)
										count.append(current_x)
										count.append(current_y)
										finish_2=1
										break
								##黑兵右一格是否有棋
								current_x=i.chessbox.x
								current_y=i.chessbox.y
								cx=x
								cy=y
								finish_3=0
								#print('-------------right--------------')
								current_x +=oneblock
								cy+=1
								while(1):
									if current_x>801:
										#print("over right range")
										finish_3=1
										break
									if HAVECHESS[cx][cy]==1:											
										#print("right have chess")
										for j in all_redbox:
											if j.chessbox.y==current_y and j.chessbox.x==current_x:
												caneat.append(current_x)
												caneat.append(current_y)
										finish_3=1
										break
									if HAVECHESS[cx][cy]==0:
										#print(cx,cy,current_x,current_y)
										count.append(current_x)
										count.append(current_y)
										finish_3=1
										break	
							if(finish_1==1 and finish_2==1 and finish_3==1 ):
								break					
						if i.id == 'r1' or i.id == 'r2'or i.id == 'r3' or i.id == 'r4'or i.id == 'r5':
							if current_y<=redriver:	##紅兵未過河
								##紅兵上一格是否有棋
								#('-------------top--------------')
								current_y +=oneblock
								cx+=1
								while(1):
									if current_y>907:
										#print("over top range")
										finish_1=1
										finish_2=1
										finish_3=1
										break
									if HAVECHESS[cx][cy]==1:											
										#print("top have chess") 
										finish_1=1
										finish_2=1
										finish_3=1
										for j in all_blackbox:
											if j.chessbox.y==current_y and j.chessbox.x==current_x:
												caneat.append(current_x)
												caneat.append(current_y)
										break
									if HAVECHESS[cx][cy]==0:
										#(cx,cy,current_x,current_y)
										count.append(current_x)
										count.append(current_y)
										finish_1=1
										finish_2=1
										finish_3=1
										break
							else:##紅兵過河	
								current_x=i.chessbox.x
								current_y=i.chessbox.y
								cx=x
								cy=y
								finish_1=0
								##紅兵下一格是否有棋
								#print('-------------top--------------')
								current_y +=oneblock
								cx+=1
								while(1):
									if current_y>907:
										#print("over top range")
										finish_1=1
										break
									if HAVECHESS[cx][cy]==1:											
										#print("top have chess")
										for j in all_blackbox:
											if j.chessbox.y==current_y and j.chessbox.x==current_x:
												caneat.append(current_x)
												caneat.append(current_y)
										finish_1=1
										break
									if HAVECHESS[cx][cy]==0:
										#print(cx,cy,current_x,current_y)
										count.append(current_x)
										count.append(current_y)
										finish_1=1
										break
									
								##紅兵左一格是否有棋
								current_x=i.chessbox.x
								current_y=i.chessbox.y
								cx=x
								cy=y
								finish_2=0
								#print('-------------left--------------')
								current_x -=oneblock
								cy-=1
								while(1):
									if current_x<17:
										#print("over left range")
										finish_2=1
										break
									if HAVECHESS[cx][cy]==1:											
										#print("left have chess")
										for j in all_blackbox:
											if j.chessbox.y==current_y and j.chessbox.x==current_x:
												caneat.append(current_x)
												caneat.append(current_y)
										finish_2=1
										break
									if HAVECHESS[cx][cy]==0:
										#print(cx,cy,current_x,current_y)
										count.append(current_x)
										count.append(current_y)
										finish_2=1
										break
								##紅兵右一格是否有棋
								current_x=i.chessbox.x
								current_y=i.chessbox.y
								cx=x
								cy=y
								finish_3=0
								#print('-------------right--------------')
								current_x +=oneblock
								cy+=1
								while(1):
									if current_x>801:
										#print("over right range")
										finish_3=1
										break
									if HAVECHESS[cx][cy]==1:											
										#print("right have chess")
										for j in all_blackbox:
											if j.chessbox.y==current_y and j.chessbox.x==current_x:
												caneat.append(current_x)
												caneat.append(current_y)
										finish_3=1
										break
									if HAVECHESS[cx][cy]==0:
										#print(cx,cy,current_x,current_y)
										count.append(current_x)
										count.append(current_y)
										finish_3=1
										break	
							if(finish_1==1 and finish_2==1 and finish_3==1 ):
								break
#car
	if n==2:
		count.clear()
		if HAVECHESS[x][y]==1 and i.type=='Car':
			print(i.type,"chess_x,chess_y:",i.chessbox.x,i.chessbox.y,"havechess_x,havechess_y:",x,y)
			current_x=i.chessbox.x
			current_y=i.chessbox.y
			cx=x
			cy=y
			finish_1=0
			finish_2=0
			finish_3=0
			finish_4=0
			if i.id == 'b1' or i.id == 'b2':
				while(True):					
					#('-------------top--------------')##車上面可走格數
					while(1):
						current_y-=oneblock
						cx-=1
						if current_y<25:
							#print("over top range")
							finish_1=1
							break
						if cx>=0:
							if(HAVECHESS[cx][cy]==1):
								#print("next top have chess")
								for j in all_redbox:
									if j==r2_kn:
										print(j.chessbox.x,j.chessbox.y,current_x,current_y)
									if j.chessbox.y==current_y and j.chessbox.x==current_x:		
										caneat.append(current_x)
										caneat.append(current_y)
								finish_1=1
								break
						else:
							finish_1=1
							break
						#print(cx,cy,current_x,current_y)
						count.append(current_x)
						count.append(current_y)
					current_x=i.chessbox.x
					current_y=i.chessbox.y
					cx=x
					cy=y
					finish_2=0
					#print('-------------down--------------')##車下面可走格數
					while(1):
						current_y+=oneblock
						cx+=1
						if current_y>907:
							#print("over down range")
							finish_2=1
							break
						if cx<=9:
							if(HAVECHESS[cx][cy]==1):
								#print("next down have chess")
								for j in all_redbox:
									if j.chessbox.y==current_y and j.chessbox.x==current_x:
										#print(j)
										caneat.append(current_x)
										caneat.append(current_y)				
								finish_2=1
								break
						else:
							finish_2=1
							break
						#print(cx,cy,current_x,current_y)
						count.append(current_x)
						count.append(current_y)
					current_x=i.chessbox.x
					current_y=i.chessbox.y
					cx=x
					cy=y
					finish_3=0
					#print('-------------left--------------')##車左面可走格數
					while(1):
						current_x -=oneblock
						cy-=1
						if current_x<17:
							#print("over left range")
							finish_3=1
							break
						if cy>=0:
							if(HAVECHESS[cx][cy]==1):
								#print("next left have chess")
								for j in all_redbox:
									if j.chessbox.y==current_y and j.chessbox.x==current_x:
										#print(j)
										caneat.append(current_x)
										caneat.append(current_y)
								finish_3=1
								break  
						else:
							finish_3=1
							break 
						#print(cx,cy,current_x,current_y)
						count.append(current_x)
						count.append(current_y)
					current_x=i.chessbox.x
					current_y=i.chessbox.y
					cx=x
					cy=y
					finish_4=0
					#print('-------------right--------------')##車右面可走格數
					while(1):
						current_x +=oneblock
						cy+=1
						if current_x>801:
							#print("over right range")
							finish_4=1
							break
						if cy<=8:
							if(HAVECHESS[cx][cy]==1):
								#print("next right have chess")
								for j in all_redbox:
									if j.chessbox.y==current_y and j.chessbox.x==current_x:
										#print(j)
										caneat.append(current_x)
										caneat.append(current_y)
								finish_4=1
								break
						else:
							finish_4=1
							break
						#print(cx,cy,current_x,current_y)
						count.append(current_x)
						count.append(current_y)
					if(finish_1==1 and finish_2==1 and finish_3==1 and finish_4==1):
						break	
			if i.id == 'r1' or i.id == 'r2':
				while(True):				
					#print('-------------top--------------')##車上面可走格數
					while(1):
						current_y-=oneblock
						cx-=1
						if current_y<25:
							#print("over top range")
							finish_1=1
							break
						if cx>=0:
							if(HAVECHESS[cx][cy]==1):
								#print("next top have chess")
								for j in all_blackbox:
									if j.chessbox.y==current_y and j.chessbox.x==current_x:		
										caneat.append(current_x)
										caneat.append(current_y)
								finish_1=1
								break
						else:
							finish_1=1
							break
						#print(cx,cy,current_x,current_y)
						count.append(current_x)
						count.append(current_y)
					current_x=i.chessbox.x
					current_y=i.chessbox.y
					cx=x
					cy=y
					finish_2=0
					#print('-------------down--------------')##車下面可走格數
					while(1):
						current_y+=oneblock
						cx+=1
						if current_y>907:
							#print("over down range")
							finish_2=1
							break
						if cx<=9:
							if(HAVECHESS[cx][cy]==1):
								#print("next down have chess")
								for j in all_blackbox:
									if j.chessbox.y==current_y and j.chessbox.x==current_x:
										#print(j)
										caneat.append(current_x)
										caneat.append(current_y)				
								finish_2=1
								break
						else:
							finish_2=1
							break
						#print(cx,cy,current_x,current_y)
						count.append(current_x)
						count.append(current_y)
					current_x=i.chessbox.x
					current_y=i.chessbox.y
					cx=x
					cy=y
					finish_3=0
					#print('-------------left--------------')##車左面可走格數
					while(1):
						current_x -=oneblock
						cy-=1
						if current_x<17:
							#print("over left range")
							finish_3=1
							break
						if cy>=0:
							if(HAVECHESS[cx][cy]==1):
								#print("next left have chess")
								for j in all_blackbox:
									if j.chessbox.y==current_y and j.chessbox.x==current_x:
										#print(j)
										caneat.append(current_x)
										caneat.append(current_y)
								finish_3=1
								break  
						else:
							finish_3=1
							break 
						#print(cx,cy,current_x,current_y)
						count.append(current_x)
						count.append(current_y)
					current_x=i.chessbox.x
					current_y=i.chessbox.y
					cx=x
					cy=y
					finish_4=0
					#print('-------------right--------------')##車右面可走格數
					while(1):
						current_x +=oneblock
						cy+=1
						if current_x>801:
							#print("over right range")
							finish_4=1
							break
						if cy<=8:
							if(HAVECHESS[cx][cy]==1):
								#print("next right have chess")
								for j in all_blackbox:
									if j.chessbox.y==current_y and j.chessbox.x==current_x:
										#print(j)
										caneat.append(current_x)
										caneat.append(current_y)
								finish_4=1
								break
						else:
							finish_4=1
							break
						#print(cx,cy,current_x,current_y)
						count.append(current_x)
						count.append(current_y)
					if(finish_1==1 and finish_2==1 and finish_3==1 and finish_4==1):
						break
#bomb
	elif n==3:
		count.clear()
		if HAVECHESS[x][y]==1 and i.type=='Bomb':
			#print(i.type,"chess_x,chess_y:",i.chessbox.x,i.chessbox.y,"havechess_x,havechess_y:",x,y)
			current_x=i.chessbox.x
			current_y=i.chessbox.y
			cx=x
			cy=y
			finish_1=0
			finish_2=0
			finish_3=0
			finish_4=0
		if i.id == 'b1' or i.id == 'b2':    
			while(True):				
				#print('-------------top--------------')##炮上面可走格數
				while(1):
					current_y-=oneblock
					cx-=1
					if current_y<25:
						#print("over top range")
						finish_1=1
						break
					if cx>=0:
						if(HAVECHESS[cx][cy]==1):
							#print("next top have chess",cx,cy)
							while(1):
								current_y-=oneblock
								cx-=1
								if cx>=0:	
									if(HAVECHESS[cx][cy]==1):
										#print("next next top have chess")
										for j in all_redbox:
											if j.chessbox.y==current_y and j.chessbox.x==current_x:
												caneat.append(current_x)
												caneat.append(current_y)
										break
								else:	
									#print("next next down have notthing")
									break
							finish_1=1
							break
					else:
						finish_1=1
						break
					#print(cx,cy,current_x,current_y)
					count.append(current_x)
					count.append(current_y)
				current_x=i.chessbox.x
				current_y=i.chessbox.y
				cx=x
				cy=y
				#print('-------------down--------------')##炮下面可走格數
				while(1):
					current_y+=oneblock
					cx+=1
					if current_y>907:
						#print("over down range")
						finish_2=1
						break
					if cx<=9:
						if(HAVECHESS[cx][cy]==1):
							#print("next down have chess")
							while(1):
								current_y+=oneblock
								cx+=1
								if cx<=9:	
									if(HAVECHESS[cx][cy]==1):
										#print("next next down have chess")
										for j in all_redbox:
											if j.chessbox.y==current_y and j.chessbox.x==current_x:
												caneat.append(current_x)
												caneat.append(current_y)
										break
								else:
									#print("next next down have notthing")
									break
							finish_2=1
							break
					else:
						finish_2=1
						break
					#print(cx,cy,current_x,current_y)
					count.append(current_x)
					count.append(current_y)
				current_x=i.chessbox.x
				current_y=i.chessbox.y
				cx=x
				cy=y
				#print('-------------left--------------')##炮左面可走格數
				while(1):
					current_x -=oneblock
					cy-=1
					if current_x<17:
						print("over left range")
						finish_3=1
						break
					if cy>=0:
						if(HAVECHESS[cx][cy]==1):
							#print("next left have chess")
							while(1):
								current_x-=oneblock
								cy-=1
								if cy>=0:	
									if(HAVECHESS[cx][cy]==1):
										#print("next next left have chess")
										for j in all_redbox:
											if j.chessbox.y==current_y and j.chessbox.x==current_x:
												caneat.append(current_x)
												caneat.append(current_y)
										break
								else:
									#print("next next left have notthing")
									break
							finish_3=1
							break
					else:
						finish_3=1
						break
					#print(cx,cy,current_x,current_y)
					count.append(current_x)
					count.append(current_y)
				current_x=i.chessbox.x
				current_y=i.chessbox.y
				cx=x
				cy=y
				#print('-------------right--------------')##炮右面可走格數
				while(1):
					current_x +=oneblock
					cy+=1
					if current_x>801:
						#print("over right range")
						finish_4=1
						break
					if cy<=8:
						if(HAVECHESS[cx][cy]==1):
							#print("next right have chess")
							while(1):
								current_x+=oneblock
								cy+=1
								if cy<=8:	
									if(HAVECHESS[cx][cy]==1):
										#print("next next right have chess")
										for j in all_redbox:
											if j.chessbox.y==current_y and j.chessbox.x==current_x:
												caneat.append(current_x)
												caneat.append(current_y)
										break
								else:
									#print("next next right have notthing")
									break
							finish_4=1
							break 
					else:
						finish_4=1
						break					  
					#print(cx,cy,current_x,current_y)
					count.append(current_x)
					count.append(current_y)
				if(finish_1==1 and finish_2==1 and finish_3==1 and finish_4==1):
					break
		if i.id == 'r1' or i.id == 'r2':				
			while(True):
				#print('-------------top--------------')##炮上面可走格數
				while(1):
					current_y-=oneblock
					cx-=1
					if current_y<25:
						#print("over top range")
						finish_1=1
						break
					if cx>=0:
						if(HAVECHESS[cx][cy]==1):
							#print("next top have chess",cx,cy)
							while(1):
								current_y-=oneblock
								cx-=1
								if cx>=0:	
									if(HAVECHESS[cx][cy]==1):
										#print("next next top have chess")
										for j in all_blackbox:
											if j.chessbox.y==current_y and j.chessbox.x==current_x:
												caneat.append(current_x)
												caneat.append(current_y)
										break
								else:	
									#print("next next down have notthing")
									break
							finish_1=1
							break
					else:
						finish_1=1
						break
					#print(cx,cy,current_x,current_y)
					count.append(current_x)
					count.append(current_y)
				current_x=i.chessbox.x
				current_y=i.chessbox.y
				cx=x
				cy=y
				#print('-------------down--------------')##炮下面可走格數
				while(1):
					current_y+=oneblock
					cx+=1
					if current_y>907:
						#print("over down range")
						finish_2=1
						break
					if cx<=9:
						if(HAVECHESS[cx][cy]==1):
							#print("next down have chess")
							while(1):
								current_y+=oneblock
								cx+=1
								if cx<=9:	
									if(HAVECHESS[cx][cy]==1):
										#print("next next down have chess")
										for j in all_blackbox:
											if j.chessbox.y==current_y and j.chessbox.x==current_x:
												caneat.append(current_x)
												caneat.append(current_y)
										break
								else:
									#print("next next down have notthing")
									break
							finish_2=1
							break
					else:
						finish_2=1
						break
					#print(cx,cy,current_x,current_y)
					count.append(current_x)
					count.append(current_y)
				current_x=i.chessbox.x
				current_y=i.chessbox.y
				cx=x
				cy=y
				#print('-------------left--------------')##炮左面可走格數
				while(1):
					current_x -=oneblock
					cy-=1
					if current_x<17:
						#print("over left range")
						finish_3=1
						break
					if cy>=0:
						if(HAVECHESS[cx][cy]==1):
							#print("next left have chess")
							while(1):
								current_x-=oneblock
								cy-=1
								if cy>=0:	
									if(HAVECHESS[cx][cy]==1):
										#print("next next left have chess")
										for j in all_blackbox:
											if j.chessbox.y==current_y and j.chessbox.x==current_x:
												caneat.append(current_x)
												caneat.append(current_y)
										break
								else:
									#print("next next left have notthing")
									break
							finish_3=1
							break 
					else:
						finish_3=1
						break 
					#print(cx,cy,current_x,current_y)
					count.append(current_x)
					count.append(current_y)
				current_x=i.chessbox.x
				current_y=i.chessbox.y
				cx=x
				cy=y
				#print('-------------right--------------')##炮右面可走格數
				while(1):
					current_x +=oneblock
					cy+=1
					if current_x>801:
						#print("over right range")
						finish_4=1
						break
					if cy<=8:
						
						if(HAVECHESS[cx][cy]==1):
							#print("next right have chess")
							while(1):
								current_x+=oneblock
								cy+=1
								if cy<=8:	
									if(HAVECHESS[cx][cy]==1):
										#print("next next right have chess")
										for j in all_blackbox:
											if j.chessbox.y==current_y and j.chessbox.x==current_x:
												caneat.append(current_x)
												caneat.append(current_y)
										break
								else:
									#print("next next right have notthing")
									break
							finish_4=1
							break 
					else:
						finish_4=1
						break 
					#print(cx,cy,current_x,current_y)
					count.append(current_x)
					count.append(current_y)
				if(finish_1==1 and finish_2==1 and finish_3==1 and finish_4==1):
					break		
#horse
	elif n==4:			
		count.clear()
		if HAVECHESS[x][y]==1 and i.type=='Horse':
			print(i.type,"chess_x,chess_y:",i.chessbox.x,i.chessbox.y,"havechess_x,havechess_y:",x,y)	
			current_x=i.chessbox.x
			current_y=i.chessbox.y
			cx=x
			cy=y
			horsestep_1=0
			horsestep_2=0
			horsestep_3=0
			horsestep_4=0
			horsestep_5=0
			horsestep_6=0
			horsestep_7=0
			horsestep_8=0
			finish_1=0
			finish_2=0
			finish_3=0
			finish_4=0
			finish_5=0
			finish_6=0
			finish_7=0
			finish_8=0
			if i.id == 'b1' or i.id == 'b2':
				while(1):
					##超過邊線的判定
					if cx-1<0:
						#print("top is bound")
						horsestep_1=1
						horsestep_2=1
						horsestep_7=1
						horsestep_8=1
						finish_1=1
						finish_2=1
						finish_7=1
						finish_8=1
					if cx+1>9:
						#print("down is bound")
						horsestep_3=1
						horsestep_4=1
						horsestep_5=1
						horsestep_6=1
						finish_3=1
						finish_4=1
						finish_5=1
						finish_6=1
					if cy-1<0:
						#print("left is bound")
						horsestep_5=1
						horsestep_6=1
						horsestep_7=1
						horsestep_8=1
						finish_5=1
						finish_6=1
						finish_7=1
						finish_8=1
					if cy+1>8:
						#print("right is bound")
						horsestep_1=1
						horsestep_2=1
						horsestep_3=1
						horsestep_4=1
						finish_1=1
						finish_2=1
						finish_3=1
						finish_4=1

					if cx-1>=0: 
						if  HAVECHESS[cx-1][cy]==1:##馬上一格
							#print("top have chess")
							horsestep_1=1
							horsestep_8=1
							finish_1=1
							finish_8=1
					if cy+1<=8:
						if HAVECHESS[cx][cy+1]==1:##馬右一格
							#print("right have chess")
							horsestep_2=1
							horsestep_3=1
							finish_2=1
							finish_3=1
					if cx+1<=9:
						if HAVECHESS[cx+1][cy]==1:##馬下一格
							#print("down have chess")
							horsestep_4=1
							horsestep_5=1
							finish_4=1
							finish_5=1
					if cy-1>=0:
						if HAVECHESS[cx][cy-1]==1:##馬左一格
							#print("left have chess")
							horsestep_6=1
							horsestep_7=1
							finish_6=1
							finish_7=1

					current_x=i.chessbox.x
					current_y=i.chessbox.y
					cx=x
					cy=y
					if horsestep_1==0:##上右可走
						current_x +=oneblock
						cy+=1
						current_y -=oneblock*2
						cx-=2
						if cx<=9 and cy>=0:
							if(HAVECHESS[cx][cy]==1):
								#print("horsestep_1 have chess")
								for j in all_redbox:
									if j.chessbox.y==current_y and j.chessbox.x==current_x:
										caneat.append(current_x)
										caneat.append(current_y)
								finish_1=1
							else:
								#print(cx,cy,current_x,current_y)
								count.append(current_x)
								count.append(current_y)
								finish_1=1
						else:
							finish_1=1

					current_x=i.chessbox.x
					current_y=i.chessbox.y
					cx=x
					cy=y
					if horsestep_2==0:##右上可走
						current_x +=oneblock*2
						cy+=2
						current_y -=oneblock
						cx-=1
						if cx>=0 and cy<=8:
							if(HAVECHESS[cx][cy]==1):
								#print("horsestep_2 have chess")
								for j in all_redbox:
									if j.chessbox.y==current_y and j.chessbox.x==current_x:
										caneat.append(current_x)
										caneat.append(current_y)
								finish_2=1
							else:
								#print(cx,cy,current_x,current_y)
								count.append(current_x)
								count.append(current_y)
								finish_2=1
						else:
							finish_2=1
					current_x=i.chessbox.x
					current_y=i.chessbox.y
					cx=x
					cy=y
					if horsestep_3==0:##右下可走
						current_x +=oneblock*2
						cy+=2
						current_y +=oneblock
						cx+=1
						if cx<=9 and cy<=8:
							if(HAVECHESS[cx][cy]==1):
								#print("horsestep_3 have chess")
								for j in all_redbox:
									if j.chessbox.y==current_y and j.chessbox.x==current_x:
										caneat.append(current_x)
										caneat.append(current_y)
								finish_3=1
							else:
								#print(cx,cy,current_x,current_y)
								count.append(current_x)
								count.append(current_y)
								finish_3=1
						else:
							finish_3=1
					current_x=i.chessbox.x
					current_y=i.chessbox.y
					cx=x
					cy=y
					if horsestep_4==0:##下右可走
						current_x +=oneblock
						cy+=1
						current_y +=oneblock*2
						cx+=2
						if cx<=9 and cy<=8:
							if(HAVECHESS[cx][cy]==1):
								#print("horsestep_4 have chess")
								for j in all_redbox:
									if j.chessbox.y==current_y and j.chessbox.x==current_x:
										caneat.append(current_x)
										caneat.append(current_y)
								finish_4=1
							else:
								#print(cx,cy,current_x,current_y)
								count.append(current_x)
								count.append(current_y)
								finish_4=1
						else:
							finish_4=1
					current_x=i.chessbox.x
					current_y=i.chessbox.y
					cx=x
					cy=y
					if horsestep_8==0:##上左可走
						current_x -=oneblock
						cy-=1
						current_y -=oneblock*2
						cx-=2
						if cx>=0 and cy>=0:
							if(HAVECHESS[cx][cy]==1):
								#print("horsestep_8 have chess")
								for j in all_redbox:
									if j.chessbox.y==current_y and j.chessbox.x==current_x:
										caneat.append(current_x)
										caneat.append(current_y)
								finish_8=1
							else:
								#print(cx,cy,current_x,current_y)
								count.append(current_x)
								count.append(current_y)
								finish_8=1
						else:
							finish_8=1
					current_x=i.chessbox.x
					current_y=i.chessbox.y
					cx=x
					cy=y
					if horsestep_7==0:##左上可走
						current_x -=oneblock*2
						cy-=2
						current_y -=oneblock
						cx-=1
						if cx>=0 and cy>=0:
							if(HAVECHESS[cx][cy]==1):
								#print("horsestep_7 have chess")
								for j in all_redbox:
									if j.chessbox.y==current_y and j.chessbox.x==current_x:
										caneat.append(current_x)
										caneat.append(current_y)
								finish_7=1
							else:
								#print(cx,cy,current_x,current_y)
								count.append(current_x)
								count.append(current_y)
								finish_7=1
						else:
							finish_7=1
					current_x=i.chessbox.x
					current_y=i.chessbox.y
					cx=x
					cy=y
					if horsestep_6==0:##左下可走
						current_x -=oneblock*2
						cy-=2
						current_y +=oneblock
						cx+=1
						if cx<=9 and cy>=0 :
							if(HAVECHESS[cx][cy]==1):
								#print("horsestep_6 have chess")
								for j in all_redbox:
									if j.chessbox.y==current_y and j.chessbox.x==current_x:
										caneat.append(current_x)
										caneat.append(current_y)
								finish_6=1
							else:
								#print(cx,cy,current_x,current_y)
								count.append(current_x)
								count.append(current_y)
								finish_6=1
						else:
							finish_6=1
					current_x=i.chessbox.x
					current_y=i.chessbox.y
					cx=x
					cy=y
					if horsestep_5==0:##下左可走
						current_x -=oneblock
						cy-=1
						current_y +=oneblock*2
						cx+=2
						if cx<=9 and cy>=0:
							if(HAVECHESS[cx][cy]==1):
								#print("horsestep_5 have chess")
								for j in all_redbox:
									if j.chessbox.y==current_y and j.chessbox.x==current_x:
										caneat.append(current_x)
										caneat.append(current_y)
								finish_5=1
							else:
								#print(cx,cy,current_x,current_y)
								count.append(current_x)
								count.append(current_y)
								finish_5=1
						else:
							finish_5=1

					if finish_1==1 and finish_2==1 and finish_3==1 and finish_4==1 and finish_5==1 and finish_6==1 and finish_7==1 and finish_8==1 :
						break
			if i.id == 'r1' or i.id == 'r2':
				while(1):
					##超過邊線的判定
					if cx-1<0:
						#print("top is bound")
						horsestep_1=1
						horsestep_2=1
						horsestep_7=1
						horsestep_8=1
						finish_1=1
						finish_2=1
						finish_7=1
						finish_8=1
					if cx+1>9:
						#print("down is bound")
						horsestep_3=1
						horsestep_4=1
						horsestep_5=1
						horsestep_6=1
						finish_3=1
						finish_4=1
						finish_5=1
						finish_6=1
					if cy-1<0:
						#print("left is bound")
						horsestep_5=1
						horsestep_6=1
						horsestep_7=1
						horsestep_8=1
						finish_5=1
						finish_6=1
						finish_7=1
						finish_8=1
					if cy+1>8:
						#print("right is bound")
						horsestep_1=1
						horsestep_2=1
						horsestep_3=1
						horsestep_4=1
						finish_1=1
						finish_2=1
						finish_3=1
						finish_4=1
	
					if cx-1>=0: 
						if  HAVECHESS[cx-1][cy]==1:##馬上一格
							#print("top have chess")
							horsestep_1=1
							horsestep_8=1
							finish_1=1
							finish_8=1
					if cy+1<=8:
						if HAVECHESS[cx][cy+1]==1:##馬右一格
							#print("right have chess")
							horsestep_2=1
							horsestep_3=1
							finish_2=1
							finish_3=1
					if cx+1<=9:
						if HAVECHESS[cx+1][cy]==1:##馬下一格
							#print("down have chess")
							horsestep_4=1
							horsestep_5=1
							finish_4=1
							finish_5=1
					if cy-1>=0:
						if HAVECHESS[cx][cy-1]==1:##馬左一格
							#print("left have chess")
							horsestep_6=1
							horsestep_7=1
							finish_6=1
							finish_7=1
	
					current_x=i.chessbox.x
					current_y=i.chessbox.y
					cx=x
					cy=y
					if horsestep_1==0:##上右可走
						current_x +=oneblock
						cy+=1
						current_y -=oneblock*2
						cx-=2
						if cx<=9 and cy>=0:
							if(HAVECHESS[cx][cy]==1):
								#print("horsestep_1 have chess")
								for j in all_blackbox:
									if j.chessbox.y==current_y and j.chessbox.x==current_x:
										caneat.append(current_x)
										caneat.append(current_y)
								finish_1=1
							else:
								#print(cx,cy,current_x,current_y)
								count.append(current_x)
								count.append(current_y)
								finish_1=1
						else:
							finish_1=1
	
					current_x=i.chessbox.x
					current_y=i.chessbox.y
					cx=x
					cy=y
					if horsestep_2==0:##右上可走
						current_x +=oneblock*2
						cy+=2
						current_y -=oneblock
						cx-=1
						if cx>=0 and cy<=8:
							if(HAVECHESS[cx][cy]==1):
								#print("horsestep_2 have chess")
								for j in all_blackbox:
									if j.chessbox.y==current_y and j.chessbox.x==current_x:
										caneat.append(current_x)
										caneat.append(current_y)
								finish_2=1
							else:
								#print(cx,cy,current_x,current_y)
								count.append(current_x)
								count.append(current_y)
								finish_2=1
						else:
							finish_2=1
					current_x=i.chessbox.x
					current_y=i.chessbox.y
					cx=x
					cy=y
					if horsestep_3==0:##右下可走
						current_x +=oneblock*2
						cy+=2
						current_y +=oneblock
						cx+=1
						if cx<=9 and cy<=8:
							if(HAVECHESS[cx][cy]==1):
								#print("horsestep_3 have chess")
								for j in all_blackbox:
									if j.chessbox.y==current_y and j.chessbox.x==current_x:
										caneat.append(current_x)
										caneat.append(current_y)
								finish_3=1
							else:
								#print(cx,cy,current_x,current_y)
								count.append(current_x)
								count.append(current_y)
								finish_3=1
						else:
							finish_3=1
					current_x=i.chessbox.x
					current_y=i.chessbox.y
					cx=x
					cy=y
					if horsestep_4==0:##下右可走
						current_x +=oneblock
						cy+=1
						current_y +=oneblock*2
						cx+=2
						if cx<=9 and cy<=8:
							if(HAVECHESS[cx][cy]==1):
								#print("horsestep_4 have chess")
								for j in all_blackbox:
									if j.chessbox.y==current_y and j.chessbox.x==current_x:
										caneat.append(current_x)
										caneat.append(current_y)
								finish_4=1
							else:
								#print(cx,cy,current_x,current_y)
								count.append(current_x)
								count.append(current_y)
								finish_4=1
						else:
							finish_4=1
					current_x=i.chessbox.x
					current_y=i.chessbox.y
					cx=x
					cy=y
					if horsestep_8==0:##上左可走
						current_x -=oneblock
						cy-=1
						current_y -=oneblock*2
						cx-=2
						if cx>=0 and cy>=0:
							if(HAVECHESS[cx][cy]==1):
								#print("horsestep_8 have chess")
								for j in all_blackbox:
									if j.chessbox.y==current_y and j.chessbox.x==current_x:
										caneat.append(current_x)
										caneat.append(current_y)
								finish_8=1
							else:
								#print(cx,cy,current_x,current_y)
								count.append(current_x)
								count.append(current_y)
								finish_8=1
						else:
							finish_8=1
					current_x=i.chessbox.x
					current_y=i.chessbox.y
					cx=x
					cy=y
					if horsestep_7==0:##左上可走
						current_x -=oneblock*2
						cy-=2
						current_y -=oneblock
						cx-=1
						if cx>=0 and cy>=0:
							if(HAVECHESS[cx][cy]==1):
								#print("horsestep_7 have chess")
								for j in all_blackbox:
									if j.chessbox.y==current_y and j.chessbox.x==current_x:
										caneat.append(current_x)
										caneat.append(current_y)
								finish_7=1
							else:
								#print(cx,cy,current_x,current_y)
								count.append(current_x)
								count.append(current_y)
								finish_7=1
						else:
							finish_7=1
					current_x=i.chessbox.x
					current_y=i.chessbox.y
					cx=x
					cy=y
					if horsestep_6==0:##左下可走
						current_x -=oneblock*2
						cy-=2
						current_y +=oneblock
						cx+=1
						if cx<=9 and cy>=0 :
							if(HAVECHESS[cx][cy]==1):
								#print("horsestep_6 have chess")
								for j in all_blackbox:
									if j.chessbox.y==current_y and j.chessbox.x==current_x:
										caneat.append(current_x)
										caneat.append(current_y)
								finish_6=1
							else:
								#print(cx,cy,current_x,current_y)
								count.append(current_x)
								count.append(current_y)
								finish_6=1
						else:
							finish_6=1
					current_x=i.chessbox.x
					current_y=i.chessbox.y
					cx=x
					cy=y
					if horsestep_5==0:##下左可走
						current_x -=oneblock
						cy-=1
						current_y +=oneblock*2
						cx+=2
						if cx<=9 and cy>=0:
							if(HAVECHESS[cx][cy]==1):
								#print("horsestep_5 have chess")
								for j in all_blackbox:
									if j.chessbox.y==current_y and j.chessbox.x==current_x:
										caneat.append(current_x)
										caneat.append(current_y)
								finish_5=1
							else:
								#print(cx,cy,current_x,current_y)
								count.append(current_x)
								count.append(current_y)
								finish_5=1
						else:
							finish_5=1
						
					if finish_1==1 and finish_2==1 and finish_3==1 and finish_4==1 and finish_5==1 and finish_6==1 and finish_7==1 and finish_8==1 :
						break
#Elephant
	elif n==5:			
		count.clear()
		if HAVECHESS[x][y]==1 and i.type=='Elephant':
			print(i.type,"chess_x,chess_y:",i.chessbox.x,i.chessbox.y,"havechess_x,havechess_y:",x,y)	
			current_x=i.chessbox.x
			current_y=i.chessbox.y
			cx=x
			cy=y
			elephantstep_1=0
			elephantstep_2=0
			elephantstep_3=0
			elephantstep_4=0
			finish_1=0
			finish_2=0
			finish_3=0
			finish_4=0

			while(1):
				##超過邊線的判定
				if i.id == 'b1' or i.id == 'b2':
					if cx-1<5:
						#print("top is bound")
						elephantstep_1=1
						elephantstep_4=1
						finish_1=1
						finish_4=1
					if cx+1>9:
						#print("down is bound")
						elephantstep_2=1
						elephantstep_3=1
						finish_2=1
						finish_3=1
					if cy-1<0:
						#print("left is bound")
						elephantstep_3=1
						elephantstep_4=1
						finish_3=1
						finish_4=1
					if cy+1>8:
						#print("right is bound")
						elephantstep_1=1
						elephantstep_2=1
						finish_1=1
						finish_2=1
					if cx-1>=0 and cy+1<=8: 
						if  HAVECHESS[cx-1][cy+1]==1:##象右上一格
							#print("topright have chess")
							elephantstep_1=1
							finish_1=1
					if cx+1<=9 and cy+1<=8:
						if HAVECHESS[cx+1][cy+1]==1:##象右下一格
							#print("downright have chess")
							elephantstep_2=1
							finish_2=1
					if cx+1<=9 and cy-1>=0:
						if HAVECHESS[cx+1][cy-1]==1:##象左下一格
							#print("downleft have chess")
							elephantstep_3=1
							finish_3=1
					if cx-1>=0 and cy-1>=0:
						if HAVECHESS[cx-1][cy-1]==1:##象左上一格
							#print("topleft have chess")
							elephantstep_4=1
							finish_4=1


					current_x=i.chessbox.x
					current_y=i.chessbox.y
					cx=x
					cy=y
					if elephantstep_1==0:##右上可走
						current_x +=oneblock*2
						cy+=2
						current_y -=oneblock*2
						cx-=2
						if cx>=0 and cy <=8:
							if(HAVECHESS[cx][cy]==1):
								#print("elephantstep_1 have chess")
								for j in all_redbox:
									if j.chessbox.y==current_y and j.chessbox.x==current_x:
										caneat.append(current_x)
										caneat.append(current_y)
								finish_1=1
							else:
								#print(cx,cy,current_x,current_y)
								count.append(current_x)
								count.append(current_y)
								finish_1=1
						else:
							finish_1=1
					current_x=i.chessbox.x
					current_y=i.chessbox.y
					cx=x
					cy=y
					if elephantstep_2==0:##右下可走
						current_x +=oneblock*2
						cy+=2
						current_y +=oneblock*2
						cx+=2
						if cx<=9 and cy<=8:
							if(HAVECHESS[cx][cy]==1):
								#print("elephantstep_2 have chess")
								for j in all_redbox:
									if j.chessbox.y==current_y and j.chessbox.x==current_x:
										caneat.append(current_x)
										caneat.append(current_y)
								finish_2=1
							else:
								#print(cx,cy,current_x,current_y)
								count.append(current_x)
								count.append(current_y)
								finish_2=1
						else:
							finish_2=1
					current_x=i.chessbox.x
					current_y=i.chessbox.y
					cx=x
					cy=y
					if elephantstep_3==0:##左上可走
						current_x -=oneblock*2
						cy-=2
						current_y +=oneblock*2
						cx+=2
						if cx<=9 and cy>=0:
							if(HAVECHESS[cx][cy]==1):
								#print("elephantstep_3 have chess")
								for j in all_redbox:
									if j.chessbox.y==current_y and j.chessbox.x==current_x:
										caneat.append(current_x)
										caneat.append(current_y)
								finish_3=1
							else:
								#print(cx,cy,current_x,current_y)
								count.append(current_x)
								count.append(current_y)
								finish_3=1
						else:
							finish_3=1
					current_x=i.chessbox.x
					current_y=i.chessbox.y
					cx=x
					cy=y
					if elephantstep_4==0:##左下可走
						current_x -=oneblock*2
						cy-=2
						current_y -=oneblock*2
						cx-=2
						if cx>=0 and cy>=0:
							if(HAVECHESS[cx][cy]==1):
								#print("horsestep_4 have chess")
								for j in all_redbox:
									if j.chessbox.y==current_y and j.chessbox.x==current_x:
										caneat.append(current_x)
										caneat.append(current_y)
								finish_4=1
							else:
								#print(cx,cy,current_x,current_y)
								count.append(current_x)
								count.append(current_y)
								finish_4=1
						else:
							finish_4=1

					if finish_1==1 and finish_2==1 and finish_3==1 and finish_4==1:
						break
				if i.id == 'r1' or i.id == 'r2':
					if cx-1<0:
						#print("top is bound")
						elephantstep_1=1
						elephantstep_4=1
						finish_1=1
						finish_4=1	
					if cx+1>4:
						#print("down is bound")
						elephantstep_2=1
						elephantstep_3=1
						finish_2=1
						finish_3=1
					if cy-1<0:
						#print("left is bound")
						elephantstep_3=1
						elephantstep_4=1
						finish_3=1
						finish_4=1
					if cy+1>8:
						#print("right is bound")
						elephantstep_1=1
						elephantstep_2=1
						finish_1=1
						finish_2=1
					if cx-1>=0 and cy+1<=8: 
						if  HAVECHESS[cx-1][cy+1]==1:##象右上一格
							#print("topright have chess")
							elephantstep_1=1
							finish_1=1
					if cx+1<=9 and cy+1<=8:
						if HAVECHESS[cx+1][cy+1]==1:##象右下一格
							#print("downright have chess")
							elephantstep_2=1
							finish_2=1
					if cx+1<=9 and cy-1>=0:
						if HAVECHESS[cx+1][cy-1]==1:##象左下一格
							#print("downleft have chess")
							elephantstep_3=1
							finish_3=1
					if cx-1>=0 and cy-1>=0:
						if HAVECHESS[cx-1][cy-1]==1:##象左上一格
							#print("topleft have chess")
							elephantstep_4=1
							finish_4=1


					current_x=i.chessbox.x
					current_y=i.chessbox.y
					cx=x
					cy=y
					if elephantstep_1==0:##右上可走
						current_x +=oneblock*2
						cy+=2
						current_y -=oneblock*2
						cx-=2
						if cx>=0 and cy <=8:
							if(HAVECHESS[cx][cy]==1):
								#print("elephantstep_1 have chess")
								for j in all_redbox:
									if j.chessbox.y==current_y and j.chessbox.x==current_x:
										caneat.append(current_x)
										caneat.append(current_y)
								finish_1=1
							else:
								#print(cx,cy,current_x,current_y)
								count.append(current_x)
								count.append(current_y)
								finish_1=1
						else:
							finish_1=1
					current_x=i.chessbox.x
					current_y=i.chessbox.y
					cx=x
					cy=y
					if elephantstep_2==0:##右下可走
						current_x +=oneblock*2
						cy+=2
						current_y +=oneblock*2
						cx+=2
						if cx<=9 and cy<=8:
							if(HAVECHESS[cx][cy]==1):
								#print("elephantstep_2 have chess")
								for j in all_redbox:
									if j.chessbox.y==current_y and j.chessbox.x==current_x:
										caneat.append(current_x)
										caneat.append(current_y)
								finish_2=1
							else:
								#print(cx,cy,current_x,current_y)
								count.append(current_x)
								count.append(current_y)
								finish_2=1
						else:
							finish_2=1
					current_x=i.chessbox.x
					current_y=i.chessbox.y
					cx=x
					cy=y
					if elephantstep_3==0:##左上可走
						current_x -=oneblock*2
						cy-=2
						current_y +=oneblock*2
						cx+=2
						if cx<=9 and cy>=0:
							if(HAVECHESS[cx][cy]==1):
								#print("elephantstep_3 have chess")
								for j in all_redbox:
									if j.chessbox.y==current_y and j.chessbox.x==current_x:
										caneat.append(current_x)
										caneat.append(current_y)
								finish_3=1
							else:
								#print(cx,cy,current_x,current_y)
								count.append(current_x)
								count.append(current_y)
								finish_3=1
						else:
							finish_3=1
					current_x=i.chessbox.x
					current_y=i.chessbox.y
					cx=x
					cy=y
					if elephantstep_4==0:##左下可走
						current_x -=oneblock*2
						cy-=2
						current_y -=oneblock*2
						cx-=2
						if cx>=0 and cy>=0:
							if(HAVECHESS[cx][cy]==1):
								#print("horsestep_4 have chess")
								for j in all_redbox:
									if j.chessbox.y==current_y and j.chessbox.x==current_x:
										caneat.append(current_x)
										caneat.append(current_y)
								finish_4=1
							else:
								#print(cx,cy,current_x,current_y)
								count.append(current_x)
								count.append(current_y)
								finish_4=1
						else:
							finish_4=1

					if finish_1==1 and finish_2==1 and finish_3==1 and finish_4==1:
						break
#knight
	elif n==6:
		count.clear()
		if HAVECHESS[x][y]==1 and i.type=='Knight':	
			print(i.type,"chess_x,chess_y:",i.chessbox.x,i.chessbox.y,"havechess_x,havechess_y:",x,y)
			cx=x
			cy=y	
			current_x=i.chessbox.x
			current_y=i.chessbox.y
			top=0
			down=0
			left=0
			right=0
			finish_1=0
			finish_2=0
			finish_3=0
			finish_4=0
		if i.id == 'b1' or i.id == 'b2':
			while(1):
				##辨別位置
				if current_x-oneblock<311:
					#print('left bound')
					left=1
				if current_x+oneblock>507:
					#print('right bound')
					right=1
				if current_y-oneblock<711:
					#print('top bound')
					top=1
				if current_y+oneblock>907:
					#print('down bound')
					down=1

				if left==0 and top==0 and down==0 and right==0:##士在中間
					#print("middle")	
					##右上可不可以走
					cx=x
					cy=y	
					current_x=i.chessbox.x
					current_y=i.chessbox.y
					if cx-1>=0 and cy+1<=8:
						if HAVECHESS[cx-1][cy+1]==1:
							#print('topright have chess')
							
							for j in all_redbox:
								if j.chessbox.y==current_y-oneblock and j.chessbox.x==current_x+oneblock:
									caneat.append(current_x+oneblock)
									caneat.append(current_y-oneblock)
							finish_1=1
						else:
							current_x=i.chessbox.x+oneblock
							cy+=1	
							current_y=i.chessbox.y-oneblock
							cx-=1						
							#print(cx,cy,current_x,current_y)
							count.append(current_x)
							count.append(current_y)
							finish_1=1
					else:
						finish_1=1
					##右下可不可以走
					cx=x
					cy=y	
					current_x=i.chessbox.x
					current_y=i.chessbox.y
					if cx+1<=9 and cy+1<=8:
						if HAVECHESS[cx+1][cy+1]==1:
							#print('downright have chess')
							for j in all_redbox:
								if j.chessbox.y==current_y+oneblock and j.chessbox.x==current_x+oneblock:
									caneat.append(current_x+oneblock)
									caneat.append(current_y+oneblock)
							finish_2=1
						else:
							current_x=i.chessbox.x+oneblock
							cy+=1	
							current_y=i.chessbox.y+oneblock
							cx+=1	
							#print(cx,cy,current_x,current_y)
							count.append(current_x)
							count.append(current_y)
							finish_2=1
					else:
						finish_2=1
					##左下可不可以走
					cx=x
					cy=y	
					current_x=i.chessbox.x
					current_y=i.chessbox.y
					if cx+1<=9 and cy-1>=0:
						if HAVECHESS[cx+1][cy-1]==1:
							#print('downleft have chess')
							for j in all_redbox:
								if j.chessbox.y==current_y+oneblock and j.chessbox.x==current_x-oneblock:
									caneat.append(current_x-oneblock)
									caneat.append(current_y+oneblock)
							finish_3=1
						else:
							current_x=i.chessbox.x-oneblock
							cy-=1	
							current_y=i.chessbox.y+oneblock
							cx+=1	
							#print(cx,cy,current_x,current_y)
							count.append(current_x)
							count.append(current_y)
							finish_3=1
					else:
						finish_3=1
					##左上可不可以走
					cx=x
					cy=y	
					current_x=i.chessbox.x
					current_y=i.chessbox.y
					if cx-1>=0 and cy-1>=0:
						if HAVECHESS[cx-1][cy-1]==1:
							#print('topleft have chess')
							#print(current_x,current_y)
							for j in all_redbox:
								if j.chessbox.y==current_y-oneblock and j.chessbox.x==current_x-oneblock:
									caneat.append(current_x-oneblock)
									caneat.append(current_y-oneblock)
							finish_4=1
						else:
							current_x=i.chessbox.x-oneblock
							cy-=1	
							current_y=i.chessbox.y-oneblock
							cx-=1	
							#print(cx,cy,current_x,current_y)
							count.append(current_x)
							count.append(current_y)
							finish_4=1
					else:
						finish_4=1

				if left==1 and top==1:##士在左上
					#print("topleft")
					current_x=i.chessbox.x+oneblock
					current_y=i.chessbox.y+oneblock
					cx+=1
					cy+=1
					if cx<=9 and cy<=8:
						if HAVECHESS[cx][cy]==1:
							#print('have chess')
							for j in all_redbox:
								if j.chessbox.y==current_y and j.chessbox.x==current_x:
									caneat.append(current_x)
									caneat.append(current_y)
							finish_1=1
							finish_2=1
							finish_3=1
							finish_4=1
						else:
							#print(cx,cy,current_x,current_y)
							count.append(current_x)
							count.append(current_y)
							finish_1=1
							finish_2=1
							finish_3=1
							finish_4=1
					else:
						finish_1=1
						finish_2=1
						finish_3=1
						finish_4=1
				if right==1 and top==1:##士在右上
					#print("topright")
					current_x=i.chessbox.x-oneblock
					current_y=i.chessbox.y+oneblock
					cx+=1
					cy-=1
					if cx<=9 and cy>=0:
						if HAVECHESS[cx][cy]==1:
							#print('have chess')
							for j in all_redbox:
								if j.chessbox.y==current_y and j.chessbox.x==current_x:
									caneat.append(current_x)
									caneat.append(current_y)
							finish_1=1
							finish_2=1
							finish_3=1
							finish_4=1
						else:
							#print(cx,cy,current_x,current_y)
							count.append(current_x)
							count.append(current_y)
							finish_1=1
							finish_2=1
							finish_3=1
							finish_4=1
					else:
						finish_1=1
						finish_2=1
						finish_3=1
						finish_4=1
				if right==1 and down==1:##士在右下
					#print("downright")
					current_x=i.chessbox.x-oneblock
					current_y=i.chessbox.y-oneblock
					cx-=1
					cy-=1
					if cx>=0 and cy>=0:
						if HAVECHESS[cx][cy]==1:
							#print('have chess')
							for j in all_redbox:
								if j.chessbox.y==current_y and j.chessbox.x==current_x:
									caneat.append(current_x)
									caneat.append(current_y)
							finish_1=1
							finish_2=1
							finish_3=1
							finish_4=1
						else:
							#print(cx,cy,current_x,current_y)
							count.append(current_x)
							count.append(current_y)
							finish_1=1
							finish_2=1
							finish_3=1
							finish_4=1
					else:
						finish_1=1
						finish_2=1
						finish_3=1
						finish_4=1
				if left==1 and down==1:##士在左下
					#print("downleft")
					current_x=i.chessbox.x+oneblock
					current_y=i.chessbox.y-oneblock
					cx-=1
					cy+=1
					if cx>=0 and cy<=8:
						if HAVECHESS[cx][cy]==1:
							##print('have chess')
							for j in all_redbox:
								if j.chessbox.y==current_y and j.chessbox.x==current_x:
									caneat.append(current_x)
									caneat.append(current_y)
							finish_1=1
							finish_2=1
							finish_3=1
							finish_4=1
						else:
							#print(cx,cy,current_x,current_y)
							count.append(current_x)
							count.append(current_y)
							finish_1=1
							finish_2=1
							finish_3=1
							finish_4=1
					else:
						finish_1=1
						finish_2=1
						finish_3=1
						finish_4=1
				if finish_1==1 and  finish_2==1 and  finish_3==1 and  finish_4==1:
					break	
##############################################################
		if i.id == 'r1' or i.id == 'r2':
			while(1):
				##辨別位置
				if current_x-oneblock<311:
					#print('left bound')
					left=1
				if current_x+oneblock>507:
					#print('right bound')
					right=1
				if current_y-oneblock<25:
					#print('top bound')
					top=1
				if current_y+oneblock>221:
					#print('down bound')
					down=1

				if left==0 and top==0 and down==0 and right==0:##士在中間
					#print("middle")	
					##右上可不可以走
					cx=x
					cy=y	
					current_x=i.chessbox.x
					current_y=i.chessbox.y
					if cx-1>=0 and cy+1<=8:
						if HAVECHESS[cx-1][cy+1]==1:
							#print('topright have chess')
							for j in all_blackbox:
								if j.chessbox.y==current_y-oneblock and j.chessbox.x==current_x+oneblock:
									caneat.append(current_x+oneblock)
									caneat.append(current_y-oneblock)
							finish_1=1
						else:
							current_x=i.chessbox.x+oneblock
							cy+=1	
							current_y=i.chessbox.y-oneblock
							cx-=1						
							#print(cx,cy,current_x,current_y)
							count.append(current_x)
							count.append(current_y)
							finish_1=1
					else:
						finish_1=1
					##右下可不可以走
					cx=x
					cy=y	
					current_x=i.chessbox.x
					current_y=i.chessbox.y
					if cx+1<=9 and cy+1<=8:
						if HAVECHESS[cx+1][cy+1]==1:
							#print('downright have chess')
							for j in all_blackbox:
								if j.chessbox.y==current_y+oneblock and j.chessbox.x==current_x+oneblock:
									caneat.append(current_x+oneblock)
									caneat.append(current_y+oneblock)
							finish_2=1
						else:
							current_x=i.chessbox.x+oneblock
							cy+=1	
							current_y=i.chessbox.y+oneblock
							cx+=1	
							#print(cx,cy,current_x,current_y)
							count.append(current_x)
							count.append(current_y)
							finish_2=1
					else:
						finish_2=1
					##左下可不可以走
					cx=x
					cy=y	
					current_x=i.chessbox.x
					current_y=i.chessbox.y
					if cx+1<=9 and cy-1>=0:
						if HAVECHESS[cx+1][cy-1]==1:
							#print('downleft have chess')
							for j in all_blackbox:
								if j.chessbox.y==current_y+oneblock and j.chessbox.x==current_x-oneblock:
									caneat.append(current_x-oneblock)
									caneat.append(current_y+oneblock)
							finish_3=1
						else:
							current_x=i.chessbox.x-oneblock
							cy-=1	
							current_y=i.chessbox.y+oneblock
							cx+=1	
							#print(cx,cy,current_x,current_y)
							count.append(current_x)
							count.append(current_y)
							finish_3=1
					else:
						finish_3=1
					##左上可不可以走
					cx=x
					cy=y	
					current_x=i.chessbox.x
					current_y=i.chessbox.y
					if cx-1>=0 and cy-1>=0:
						if HAVECHESS[cx-1][cy-1]==1:
							#print('topleft have chess')
							for j in all_blackbox:
								if j.chessbox.y==current_y-oneblock and j.chessbox.x==current_x-oneblock:
									caneat.append(current_x-oneblock)
									caneat.append(current_y-oneblock)
							finish_4=1
						else:
							current_x=i.chessbox.x-oneblock
							cy-=1	
							current_y=i.chessbox.y-oneblock
							cx-=1	
							#print(cx,cy,current_x,current_y)
							count.append(current_x)
							count.append(current_y)
							finish_4=1
					else:
						finish_4=1

				if left==1 and top==1:##士在左上
					#print("topleft")
					current_x=i.chessbox.x+oneblock
					current_y=i.chessbox.y+oneblock
					cx+=1
					cy+=1
					if cx<=9 and cy<=8:
						if HAVECHESS[cx][cy]==1:
							#print('have chess')
							for j in all_blackbox:
								if j.chessbox.y==current_y and j.chessbox.x==current_x:
									caneat.append(current_x)
									caneat.append(current_y)
							finish_1=1
							finish_2=1
							finish_3=1
							finish_4=1
						else:
							#print(cx,cy,current_x,current_y)
							count.append(current_x)
							count.append(current_y)
							finish_1=1
							finish_2=1
							finish_3=1
							finish_4=1
					else:
						finish_1=1
						finish_2=1
						finish_3=1
						finish_4=1
				if right==1 and top==1:##士在右上
					#print("topright")
					current_x=i.chessbox.x-oneblock
					current_y=i.chessbox.y+oneblock
					cx+=1
					cy-=1
					if cx<=9 and cy>=0:
						if HAVECHESS[cx][cy]==1:
							#print('have chess')
							for j in all_blackbox:
								if j.chessbox.y==current_y and j.chessbox.x==current_x:
									caneat.append(current_x)
									caneat.append(current_y)
							finish_1=1
							finish_2=1
							finish_3=1
							finish_4=1
						else:
							#print(cx,cy,current_x,current_y)
							count.append(current_x)
							count.append(current_y)
							finish_1=1
							finish_2=1
							finish_3=1
							finish_4=1
					else:
						finish_1=1
						finish_2=1
						finish_3=1
						finish_4=1
				if right==1 and down==1:##士在右下
					#print("downright")
					current_x=i.chessbox.x-oneblock
					current_y=i.chessbox.y-oneblock
					cx-=1
					cy-=1
					if cx>=0 and cy>=0:
						if HAVECHESS[cx][cy]==1:
							#print('have chess')
							for j in all_blackbox:
								if j.chessbox.y==current_y and j.chessbox.x==current_x:
									caneat.append(current_x)
									caneat.append(current_y)
							finish_1=1
							finish_2=1
							finish_3=1
							finish_4=1
						else:
							#print(cx,cy,current_x,current_y)
							count.append(current_x)
							count.append(current_y)
							finish_1=1
							finish_2=1
							finish_3=1
							finish_4=1
					else:
						finish_1=1
						finish_2=1
						finish_3=1
						finish_4=1
				if left==1 and down==1:##士在左下
					#print("downleft")
					current_x=i.chessbox.x+oneblock
					current_y=i.chessbox.y-oneblock
					cx-=1
					cy+=1
					if cx>=0 and cy<=8:
						if HAVECHESS[cx][cy]==1:
							#print('have chess')
							for j in all_blackbox:
								if j.chessbox.y==current_y and j.chessbox.x==current_x:
									caneat.append(current_x)
									caneat.append(current_y)
							finish_1=1
							finish_2=1
							finish_3=1
							finish_4=1
						else:
							#print(cx,cy,current_x,current_y)
							count.append(current_x)
							count.append(current_y)
							finish_1=1
							finish_2=1
							finish_3=1
							finish_4=1
					else:
						finish_1=1
						finish_2=1
						finish_3=1
						finish_4=1
				if finish_1==1 and  finish_2==1 and  finish_3==1 and  finish_4==1:
					break						
#king
	elif n==7:
		count.clear()
		if HAVECHESS[x][y]==1 and i.type=='kING':
			print(i.id,"chess_x,chess_y:",i.chessbox.x,i.chessbox.y,"havechess_x,havechess_y:",x,y)
			if i.id == 'b1':
				while(1):
					current_x=i.chessbox.x
					current_y=i.chessbox.y
					cx=x
					cy=y
					finish_1=0
					finish_2=0
					finish_3=0
					finish_4=0
   					##黑將上一格是否有棋
					#print('-------------top--------------')
					current_y -=oneblock
					cx-=1
					if cx>=0:
						while(1):	
							if current_y<711:
								#print("over top range")
								is_break=0
								while  current_y>=25:
									for j in all_chessbox:
										if j.chessbox.y==current_y and j.chessbox.x==current_x and j==r_kg:
											#print('1')
											caneat.append(current_x)
											caneat.append(current_y)
											break					
										elif j.chessbox.y==current_y and j.chessbox.x==current_x and j!=r_kg:
											is_break=1
											break
									current_y -=oneblock
									if is_break==1:
										break
								finish_1=1
								break
							if HAVECHESS[cx][cy]==1:											
								#print("top have chess")
								for j in all_redbox:
									if j.chessbox.y==current_y and j.chessbox.x==current_x :
										caneat.append(current_x)
										caneat.append(current_y)
								finish_1=1
								break
							if HAVECHESS[cx][cy]==0:
								is_break=0
								while  current_y>=25:
									for j in all_chessbox:
										if j.chessbox.y==current_y and j.chessbox.x==current_x and j==r_kg:

											caneat.append(current_x)
											caneat.append(current_y)
											break					
										elif j.chessbox.y==current_y and j.chessbox.x==current_x and j!=r_kg:
											is_break=1
											break
									current_y -=oneblock
									if is_break==1:
										break
						
								current_y=i.chessbox.y
								cx=x
								current_y -=oneblock
								cx-=1
								#print(cx,cy,current_x,current_y)
								count.append(current_x)
								count.append(current_y)
								finish_1=1
								break
					else:
						finish_1=1
					##黑將下一格是否有棋
					current_x=i.chessbox.x
					current_y=i.chessbox.y
					cx=x
					cy=y
					finish_2=0
					#print('-------------down--------------')
					current_y +=oneblock
					cx+=1
					if cx<=9:
						while(1):
							if current_y>907:
								#print("over down range")
								finish_2=1
								break
							if HAVECHESS[cx][cy]==1:											
								#print("down have chess")
								for j in all_redbox:
										if j.chessbox.y==current_y and j.chessbox.x==current_x:
											caneat.append(current_x)
											caneat.append(current_y)
								finish_2=1
								break
							if HAVECHESS[cx][cy]==0:
								#print(cx,cy,current_x,current_y)
								count.append(current_x)
								count.append(current_y)
								finish_2=1
								break
					else:
						finish_2=1
					##黑將左一格是否有棋
					current_x=i.chessbox.x
					current_y=i.chessbox.y
					cx=x
					cy=y
					finish_3=0
					#print('-------------left--------------')
					current_x -=oneblock
					cy-=1
					if cy>=0:
						while(1):
							if current_x<311:
								#print("over left range")
								finish_3=1
								break
							if HAVECHESS[cx][cy]==1:											
								#print("left have chess")
								for j in all_redbox:
										if j.chessbox.y==current_y and j.chessbox.x==current_x:
											caneat.append(current_x)
											caneat.append(current_y)
								finish_3=1
								break
							if HAVECHESS[cx][cy]==0:
								#print(cx,cy,current_x,current_y)
								count.append(current_x)
								count.append(current_y)
								finish_3=1
								break
					else:
						finish_3=1
					##黑將右一格是否有棋
					current_x=i.chessbox.x
					current_y=i.chessbox.y
					cx=x
					cy=y
					finish_4=0
					#print('-------------right--------------')
					current_x +=oneblock
					cy+=1
					if cy<=8:
						while(1):
							if current_x>507:
								#print("over right range")
								finish_4=1
								break
							if HAVECHESS[cx][cy]==1:											
								#print("right have chess")
								for j in all_redbox:
										if j.chessbox.y==current_y and j.chessbox.x==current_x:
											caneat.append(current_x)
											caneat.append(current_y)
								finish_4=1
								break
							if HAVECHESS[cx][cy]==0:
								#print(cx,cy,current_x,current_y)
								count.append(current_x)
								count.append(current_y)
								finish_4=1
								break
					else:
						finish_4=1
					if(finish_1==1 and finish_2==1 and finish_3==1 and finish_4==1):				
						break
			if i.id == 'r1' :
				while(1):
					current_x=i.chessbox.x
					current_y=i.chessbox.y
					cx=x
					cy=y
					finish_1=0
					finish_2=0
					finish_3=0
					finish_4=0

   					##紅將上一格是否有棋
					#print('-------------top--------------')
					current_y -=oneblock
					cx-=1
					if cx>=0:
						while(1):
							if current_y<25:
								#print("over top range")
								finish_1=1
								break
							if HAVECHESS[cx][cy]==1:											
								#print("top have chess")
								for j in all_blackbox:
										if j.chessbox.y==current_y and j.chessbox.x==current_x:
											caneat.append(current_x)
											caneat.append(current_y)
								finish_1=1
								break
							if HAVECHESS[cx][cy]==0:
								#print(cx,cy,current_x,current_y)
								count.append(current_x)
								count.append(current_y)
								finish_1=1
								break
					else:
						finish_1=1

					##紅將下一格是否有棋
					current_x=i.chessbox.x
					current_y=i.chessbox.y
					cx=x
					cy=y
					finish_2=0
					#print('-------------down--------------')
					current_y +=oneblock
					cx+=1
					if cx<=9:
						while(1):
							if current_y>221:
								is_break=0
								
								while  current_y<=907:	
									for j in all_chessbox:
										if j.chessbox.y==current_y and j.chessbox.x==current_x and j==b_kg:
											caneat.append(current_x)
											caneat.append(current_y)
											break					
										elif j.chessbox.y==current_y and j.chessbox.x==current_x and j!=b_kg:
											is_break=1
											break
									current_y +=oneblock	
									if is_break==1:
										break
								#print("over down range")
								finish_2=1
								break
							if HAVECHESS[cx][cy]==1:											
								#print("down have chess")
								for j in all_blackbox:
										if j.chessbox.y==current_y and j.chessbox.x==current_x:
											caneat.append(current_x)
											caneat.append(current_y)
								finish_2=1
								break
							if HAVECHESS[cx][cy]==0:
								is_break=0
								
								while  current_y<=907:	
									for j in all_chessbox:
										if j.chessbox.y==current_y and j.chessbox.x==current_x and j==b_kg:
											caneat.append(current_x)
											caneat.append(current_y)
											break					
										elif j.chessbox.y==current_y and j.chessbox.x==current_x and j!=b_kg:
											is_break=1
											break
									current_y +=oneblock	
									if is_break==1:
										break
								current_y=i.chessbox.y
								cx=x
								current_y +=oneblock
								cx+=1	
								#print(cx,cy,current_x,current_y)
								count.append(current_x)
								count.append(current_y)
								finish_2=1
								break
					else:
						finish_2=1
					##紅將左一格是否有棋
					current_x=i.chessbox.x
					current_y=i.chessbox.y
					cx=x
					cy=y
					finish_3=0
					#print('-------------left--------------')
					current_x -=oneblock
					cy-=1
					if cy>=0:
						while(1):
							if current_x<311:
								#print("over left range")
								finish_3=1
								break
							if HAVECHESS[cx][cy]==1:											
								#print("left have chess")
								for j in all_blackbox:
										if j.chessbox.y==current_y and j.chessbox.x==current_x:
											caneat.append(current_x)
											caneat.append(current_y)
								finish_3=1
								break
							if HAVECHESS[cx][cy]==0:
							#	print(cx,cy,current_x,current_y)
								count.append(current_x)
								count.append(current_y)
								finish_3=1
								break
					else:
						finish_3=1
					##紅將右一格是否有棋
					current_x=i.chessbox.x
					current_y=i.chessbox.y
					cx=x
					cy=y
					finish_4=0
					#print('-------------right--------------')
					current_x +=oneblock
					cy+=1
					if cy<=8:
						while(1):
							if current_x>507:
								#print("over right range")
								finish_4=1
								break
							if HAVECHESS[cx][cy]==1:											
								#print("right have chess")
								for j in all_blackbox:
										if j.chessbox.y==current_y and j.chessbox.x==current_x:
											caneat.append(current_x)
											caneat.append(current_y)
								finish_4=1
								break
							if HAVECHESS[cx][cy]==0:
								print(cx,cy,current_x,current_y)
								count.append(current_x)
								count.append(current_y)
								finish_4=1
								break	
					else:
						finish_4=1
					if(finish_1==1 and finish_2==1 and finish_3==1 and finish_4==1):				
						break


##連線tcp
	
def tcp_link():   
	global IS_MENU
	global IS_PLAY
	global show_PLAY_init
	global client
	global BLACKWIN
	global REDWIN
	global TIE
	val=[]
	global break_flag
	break_flag=0
	global link_flag
	global show_MAIN_init
	global srvSocket
	global peace_2
	peace_2=0
	global player_turn
	player_turn=0
	srvSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	srvSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	srvSocket.bind(('', PORT))	
	srvSocket.listen(backlog)
	print("waiting...")
	client, (rip, rport) = srvSocket.accept()
	player_turn=1
	while True:
		client_msg = client.recv(BUF_SIZE)	
		try:
			s = struct.Struct('!' + 'IIII')				
			unpacked_data = s.unpack(client_msg)	
			print('receive: Integer= %d' %(unpacked_data[0]))
			if unpacked_data[1]==1:			
				peace_2=1
				if peace_2==1 and peace_1==1:
					IS_PLAY = 0
					TIE = 1
					srvSocket.close()
					client.close()
					break_flag=1
					link_flag=True
					show_MAIN_init=True
					break
			else:
				peace_2=0

			if unpacked_data[0]==1:			
				val=(1,2,3,4)
				packed_data = s.pack(*val)
				client.send(packed_data)
				print('@@1')
				player_turn=1
				IS_MENU = 0
				IS_PLAY = 1
				show_PLAY_init=True
			elif unpacked_data[1]!=1 and unpacked_data[1]!=2:
				player_turn=1
				for i in all_redbox: 
					if i.chessbox.x==unpacked_data[0] and i.chessbox.y==unpacked_data[1]:
						for j in all_blackbox:
							if j.chessbox.x==unpacked_data[2] and j.chessbox.y==unpacked_data[3]:
								convert_a,convert_b=convert_to_hc(unpacked_data[0],unpacked_data[1])
								convert_x,convert_y=convert_to_hc(unpacked_data[2],unpacked_data[3])
								i.move(unpacked_data[2],unpacked_data[3])
								j.move(-100,-100)
								HAVECHESS[convert_x][convert_y]=1
								HAVECHESS[convert_a][convert_b]=0
								j.kill()
								if all_sprites.has(r_kg)==False:
									IS_PLAY = 0
									BLACKWIN = 1
									srvSocket.close()
									client.close()
									break_flag=1
									link_flag=True
									show_MAIN_init=True
									break
								if all_sprites.has(b_kg)==False:
									IS_PLAY = 0
									REDWIN = 1
									srvSocket.close()
									client.close()
									break_flag=1
									link_flag=True
									show_MAIN_init=True
									break
							else:
								i.move(unpacked_data[2],unpacked_data[3])
								convert_a,convert_b=convert_to_hc(unpacked_data[0],unpacked_data[1])
								convert_x,convert_y=convert_to_hc(unpacked_data[2],unpacked_data[3])
								HAVECHESS[convert_x][convert_y]=1
								HAVECHESS[convert_a][convert_b]=0
								print('before_move_x:',unpacked_data[0],'before_move_y:',unpacked_data[1],'after_move_x:',unpacked_data[2],'after_move_y:',unpacked_data[3])
					if break_flag==1:
						break
			if break_flag==1:
				break		
		except socket.error as e:
				break
		except Exception as e:
				break


###################################################################
tmp=[]
y=int()
x=int()
j=0
k=0
running =True
#遊戲迴圈
show_MAIN_init=True
show_PLAY_init=True
IS_MENU = 1
IS_PLAY = 0
BLACKWIN = 0
REDWIN = 0
TIE=0
move_i=0
link_flag=True
peace_1=0
while running:
	
	clock.tick(FPS)#1秒最多執行10次
	for event in pygame.event.get():#關閉視窗
		
		if event.type==pygame.QUIT:
			running=False 
		elif event.type==pygame.MOUSEBUTTONDOWN and IS_MENU == 1 and link_flag==True:
				link_start = threading.Thread(target=tcp_link)
				link_start.setDaemon(True)
				link_start.start()
				link_flag=False
   
		elif event.type==pygame.MOUSEBUTTONDOWN and IS_PLAY == 1: 
			finish_move=0
			#和局按鈕
			for i in peacebox:
				s = struct.Struct('!' + 'IIII')	
				if i.chessbox.collidepoint(event.pos) and i.active==False:
					i.switch_on()
					val=(0,1,0,0)
					packed_data = s.pack(*val)
					client.send(packed_data)
					print('@@2')
					peace_1=1
					if peace_2==1 and peace_1==1:
						IS_PLAY = 0
						TIE = 1
						srvSocket.close()
						client.close()
						break_flag=1
						link_flag=True
						show_MAIN_init=True
						break
					i.active==True
				elif i.chessbox.collidepoint(event.pos):
					i.switch_off()
					val=(0,2,0,0)
					packed_data = s.pack(*val)
					client.send(packed_data)
					print('@@3')
					peace_1=0
					i.active==False
							
			##移動	
			for i in all_whitebox:  
				if i.chessbox.collidepoint(event.pos) and i.active==True:
					before_move_x=0
					before_move_y=0
					after_move_x=0
					after_move_y=0
					convert_a,convert_b=convert_to_hc(move_i.chessbox.x,move_i.chessbox.y)
					convert_x,convert_y=convert_to_hc(i.chessbox.x,i.chessbox.y)
					print(move_i.rect.x,move_i.rect.y)
					before_move_x=move_i.rect.x
					before_move_y=move_i.rect.y
					move_i.move(i.chessbox.x,i.chessbox.y)	
					print(move_i.rect.x,move_i.rect.y)
					after_move_x=move_i.rect.x
					after_move_y=move_i.rect.y
					HAVECHESS[convert_x][convert_y]=1
					HAVECHESS[convert_a][convert_b]=0
					s = struct.Struct('!' + 'IIII')	
					send_move=(before_move_x,before_move_y,after_move_x,after_move_y)
					packed_data = s.pack(*send_move)
					client.send(packed_data)
					print('@@4')
					player_turn=0
					finish_move=1
			#吃牌
			for i in all_redbox:  
				if i.chessbox.collidepoint(event.pos) and i.beeat==True:
					before_move_x=0
					before_move_y=0
					after_move_x=0
					after_move_y=0
					convert_a,convert_b=convert_to_hc(move_i.chessbox.x,move_i.chessbox.y)
					convert_x,convert_y=convert_to_hc(i.chessbox.x,i.chessbox.y)				
					before_move_x=move_i.rect.x
					before_move_y=move_i.rect.y
					move_i.move(i.chessbox.x,i.chessbox.y)
					after_move_x=move_i.rect.x
					after_move_y=move_i.rect.y
					i.move(-100,-100)
					HAVECHESS[convert_x][convert_y]=1
					HAVECHESS[convert_a][convert_b]=0
					s = struct.Struct('!' + 'IIII')	
					send_move=(before_move_x,before_move_y,after_move_x,after_move_y)
					packed_data = s.pack(*send_move)
					client.send(packed_data)
					print('@@5')
					player_turn=0
					#print(all_sprites.has(i))
					i.kill()
					#print(all_sprites.has(i))
					finish_move=1
					if all_sprites.has(r_kg)==False:
						IS_PLAY = 0
						BLACKWIN = 1
						srvSocket.close()
						client.close()
						break_flag=1
						link_flag=True
						show_MAIN_init=True
						break
					if all_sprites.has(b_kg)==False:
						IS_PLAY = 0
						REDWIN = 1
						srvSocket.close()
						client.close()
						break_flag=1
						link_flag=True
						show_MAIN_init=True
						break
			for i in all_blackbox: 
				if i.chessbox.collidepoint(event.pos) and i.beeat==True:
					convert_a,convert_b=convert_to_hc(move_i.chessbox.x,move_i.chessbox.y)
					convert_x,convert_y=convert_to_hc(i.chessbox.x,i.chessbox.y)				
					move_i.move(i.chessbox.x,i.chessbox.y)
					i.move(-100,-100)
					HAVECHESS[convert_x][convert_y]=1
					HAVECHESS[convert_a][convert_b]=0
					#print(all_sprites.has(i))
					i.kill()
					#print(all_sprites.has(i))
					finish_move=1
			##清空面板綠點
			k=0
			for k in all_whitebox:
				k.switch_off()
			k=0
			for k in all_redbox:
				k.change_to_noframe()
			k=0
			for k in all_blackbox:
				k.change_to_noframe()
			##點擊的黑色棋種可進行的操作演算
			for i in all_blackbox:				
				if i.chessbox.collidepoint(event.pos) and finish_move==0 and player_turn==1:
					caneat.clear()
					move_i=i
					if i==b1_s or i==b2_s or i==b3_s or i==b4_s or i==b5_s:
						check(1,i)
					if i==b1_c or i==b2_c:
						check(2,i)						
					if i==b1_b or i==b2_b:
						check(3,i)								
					if i==b1_h or i==b2_h:
						check(4,i)
					if i==b1_elep or i==b2_elep:
						check(5,i)
					if i==b1_kn or i==b2_kn:
						check(6,i)
					if i==b_kg :
						check(7,i)
					caneat_len=len(caneat)
					count_len=len(count)
					j=0
					while(j!=count_len):
						curr_x=0
						curr_y=0
						curr_x=count[j]
						curr_y=count[j+1]
						for u in all_whitebox:
							if(u.chessbox.x==curr_x and u.chessbox.y==curr_y):
								u.switch_on()								
						j+=2
					l=0
					while(l!=caneat_len):
						curr_x=0
						curr_y=0
						curr_x=caneat[l]
						curr_y=caneat[l+1]
						for u in all_redbox:
							if(u.chessbox.x==curr_x and u.chessbox.y==curr_y):
								u.change_to_frame()								
						l+=2

		elif event.type==pygame.MOUSEBUTTONDOWN and BLACKWIN == 1:
			BLACKWIN = 0
			IS_MENU = 1
			print(link_flag)
		elif event.type==pygame.MOUSEBUTTONDOWN and REDWIN == 1:
			REDWIN = 0
			IS_MENU = 1
			print(link_flag)
		elif event.type==pygame.MOUSEBUTTONDOWN and TIE == 1:
			TIE = 0
			IS_MENU = 1
	if IS_MENU == 1:
		if show_MAIN_init:
			#draw_init()
			peace_1=0
			peace_2=0
			player_turn=0
			link_flag=True
			show_MAIN_init=False
		
		screen.blit(first_background_img,(0,0))
		draw_text(screen,'象棋',150,WIDTH/2,HEIGHT/4,GEEN)
		draw_text(screen,'按一下滑鼠開始遊戲!',50,WIDTH/2,HEIGHT*3/4,WHITE)
	if BLACKWIN == 1:
		blackwin_img=pygame.transform.scale(blackwin_img,(WIDTH,HEIGHT))
		screen.blit(blackwin_img,(0,0))
		draw_text(screen,'按一下滑鼠回到主畫面!',50,WIDTH/2,HEIGHT*3/4,BLACK)
	if REDWIN == 1:
		redwin_img=pygame.transform.scale(redwin_img,(WIDTH,HEIGHT))
		screen.blit(redwin_img,(0,0))
		draw_text(screen,'按一下滑鼠回到主畫面!',50,WIDTH/2,HEIGHT*3/4,BLACK)
	if TIE == 1:
		peaceend_img=pygame.transform.scale(peaceend_img,(WIDTH,HEIGHT))
		screen.blit(peaceend_img,(0,0))
		draw_text(screen,'按一下滑鼠回到主畫面!',50,WIDTH/2,HEIGHT*3/4,BLACK)	
	if IS_PLAY == 1:
		if show_PLAY_init:	
			all_whitebox=[]
			all_redbox=[]
			all_blackbox=[]	
			all_chessbox=[]
			peacebox=[]	
			all_sprites=pygame.sprite.Group()
			#紅方空格
			r1_s1=space(17,123)
			r1_s2=space(115,123)
			r1_s3=space(213,123)
			r1_s4=space(311,123)
			r1_s5=space(409,123)
			r1_s6=space(507,123)
			r1_s7=space(605,123)
			r1_s8=space(703,123)
			r1_s9=space(801,123)
			r1_s10=space(17,221)
			r1_s11=space(213,221)
			r1_s12=space(311,221)
			r1_s13=space(409,221)
			r1_s14=space(507,221)
			r1_s15=space(605,221)
			r1_s16=space(801,221)
			r1_s17=space(115,319)
			r1_s18=space(311,319)
			r1_s19=space(507,319)
			r1_s20=space(703,319)
			r1_s21=space(17,417)
			r1_s22=space(115,417)
			r1_s23=space(213,417)
			r1_s24=space(311,417)
			r1_s25=space(409,417)
			r1_s26=space(507,417)
			r1_s27=space(605,417)
			r1_s28=space(703,417)
			r1_s29=space(801,417)
			#紅方旗子
			r1_s30=space(17,25)
			r1_s31=space(115,25)
			r1_s32=space(213,25)
			r1_s33=space(311,25)
			r1_s34=space(409,25)
			r1_s35=space(507,25)
			r1_s36=space(605,25)
			r1_s37=space(703,25)
			r1_s38=space(801,25)
			r1_s39=space(115,221)
			r1_s40=space(703,221)
			r1_s41=space(17,319)
			r1_s42=space(213,319)
			r1_s43=space(409,319)
			r1_s44=space(605,319)
			r1_s45=space(801,319)
			#黑方空格
			b1_s1=space(17,809)
			b1_s2=space(115,809)
			b1_s3=space(213,809)
			b1_s4=space(311,809)
			b1_s5=space(409,809)
			b1_s6=space(507,809)
			b1_s7=space(605,809)
			b1_s8=space(703,809)
			b1_s9=space(801,809)
			b1_s10=space(17,711)
			b1_s11=space(213,711)
			b1_s12=space(311,711)
			b1_s13=space(409,711)
			b1_s14=space(507,711)
			b1_s15=space(605,711)
			b1_s16=space(801,711)
			b1_s17=space(115,613)
			b1_s18=space(311,613)
			b1_s19=space(507,613)
			b1_s20=space(703,613)
			b1_s21=space(17,515)
			b1_s22=space(115,515)
			b1_s23=space(213,515)
			b1_s24=space(311,515)
			b1_s25=space(409,515)
			b1_s26=space(507,515)
			b1_s27=space(605,515)
			b1_s28=space(703,515)
			b1_s29=space(801,515)
			#黑方旗子
			b1_s30=space(17,907)
			b1_s31=space(115,907)
			b1_s32=space(213,907)
			b1_s33=space(311,907)
			b1_s34=space(409,907)
			b1_s35=space(507,907)
			b1_s36=space(605,907)
			b1_s37=space(703,907)
			b1_s38=space(801,907)
			b1_s39=space(115,711)
			b1_s40=space(703,711)
			b1_s41=space(17,613)
			b1_s42=space(213,613)
			b1_s43=space(409,613)
			b1_s44=space(605,613)
			b1_s45=space(801,613)

			peace_b=peace_butt(760,470)

			b1_b=Bomb('b1',155,1000)
			b2_b=Bomb('b2',743,1000)
			r1_b=Bomb('r1',155,0)
			r2_b=Bomb('r2',743,0)

			b1_elep=Elephant('b1',253,1000)
			b2_elep=Elephant('b2',645,1000)
			r1_elep=Elephant('r1',253,0)
			r2_elep=Elephant('r2',645,0)

			b1_h=Horse('b1',155,1000)
			b2_h=Horse('b2',743,1000)
			r1_h=Horse('r1',155,0)
			r2_h=Horse('r2',743,0)

			b1_c=Car('b1',57,1000)
			b2_c=Car('b2',841,1000)
			r1_c=Car('r1',57,0)
			r2_c=Car('r2',841,0)

			b1_kn=Knight('b1',351,1000)
			b2_kn=Knight('b2',547,1000)
			r1_kn=Knight('r1',351,0)
			r2_kn=Knight('r2',547,0)

			b_kg=kING('b1',449,1000)
			r_kg=kING('r1',449,0)

			b1_s=Soldier('b1',57,1000)
			b2_s=Soldier('b2',253,1000)
			b3_s=Soldier('b3',449,1000)
			b4_s=Soldier('b4',645,1000)
			b5_s=Soldier('b5',841,1000)
			r1_s=Soldier('r1',57,0)
			r2_s=Soldier('r2',253,0)
			r3_s=Soldier('r3',449,0)
			r4_s=Soldier('r4',645,0)
			r5_s=Soldier('r5',841,0)

			all_chessbox.append(b1_b)
			all_chessbox.append(b2_b)
			all_chessbox.append(b1_elep)
			all_chessbox.append(b2_elep)
			all_chessbox.append(b1_h)
			all_chessbox.append(b2_h)
			all_chessbox.append(b_kg)
			all_chessbox.append(b1_kn)
			all_chessbox.append(b2_kn)
			all_chessbox.append(b1_c)
			all_chessbox.append(b2_c)
			all_chessbox.append(b1_s)
			all_chessbox.append(b2_s)
			all_chessbox.append(b3_s)
			all_chessbox.append(b4_s)
			all_chessbox.append(b5_s)
			all_chessbox.append(r1_b)
			all_chessbox.append(r2_b)
			all_chessbox.append(r1_elep)
			all_chessbox.append(r2_elep)
			all_chessbox.append(r1_h)
			all_chessbox.append(r2_h)
			all_chessbox.append(r_kg)
			all_chessbox.append(r1_kn)
			all_chessbox.append(r2_kn)
			all_chessbox.append(r1_c)
			all_chessbox.append(r2_c)
			all_chessbox.append(r1_s)
			all_chessbox.append(r2_s)
			all_chessbox.append(r3_s)
			all_chessbox.append(r4_s)
			all_chessbox.append(r5_s)
			##黑棋的集合
			all_blackbox.append(b1_b)
			all_blackbox.append(b2_b)
			all_blackbox.append(b1_elep)
			all_blackbox.append(b2_elep)
			all_blackbox.append(b1_h)
			all_blackbox.append(b2_h)
			all_blackbox.append(b_kg)
			all_blackbox.append(b1_kn)
			all_blackbox.append(b2_kn)
			all_blackbox.append(b1_c)
			all_blackbox.append(b2_c)
			all_blackbox.append(b1_s)
			all_blackbox.append(b2_s)
			all_blackbox.append(b3_s)
			all_blackbox.append(b4_s)
			all_blackbox.append(b5_s)
			##紅棋的集合
			all_redbox.append(r1_b)
			all_redbox.append(r2_b)
			all_redbox.append(r1_elep)
			all_redbox.append(r2_elep)
			all_redbox.append(r1_h)
			all_redbox.append(r2_h)
			all_redbox.append(r_kg)
			all_redbox.append(r1_kn)
			all_redbox.append(r2_kn)
			all_redbox.append(r1_c)
			all_redbox.append(r2_c)
			all_redbox.append(r1_s)
			all_redbox.append(r2_s)
			all_redbox.append(r3_s)
			all_redbox.append(r4_s)
			all_redbox.append(r5_s)

			all_whitebox.append(b1_s1)
			all_whitebox.append(b1_s2)
			all_whitebox.append(b1_s3)
			all_whitebox.append(b1_s4) 
			all_whitebox.append(b1_s5)
			all_whitebox.append(b1_s6)
			all_whitebox.append(b1_s7)
			all_whitebox.append(b1_s8)
			all_whitebox.append(b1_s9)
			all_whitebox.append(b1_s10)
			all_whitebox.append(b1_s11)
			all_whitebox.append(b1_s12)
			all_whitebox.append(b1_s13)
			all_whitebox.append(b1_s14)
			all_whitebox.append(b1_s15)
			all_whitebox.append(b1_s16)
			all_whitebox.append(b1_s17)
			all_whitebox.append(b1_s18)
			all_whitebox.append(b1_s19)
			all_whitebox.append(b1_s20)
			all_whitebox.append(b1_s21)
			all_whitebox.append(b1_s22)
			all_whitebox.append(b1_s23)
			all_whitebox.append(b1_s24)
			all_whitebox.append(b1_s25)
			all_whitebox.append(b1_s26)
			all_whitebox.append(b1_s27)
			all_whitebox.append(b1_s28)
			all_whitebox.append(b1_s29)
			all_whitebox.append(b1_s30)
			all_whitebox.append(b1_s31)
			all_whitebox.append(b1_s32)
			all_whitebox.append(b1_s33) 
			all_whitebox.append(b1_s34)
			all_whitebox.append(b1_s35)
			all_whitebox.append(b1_s36)
			all_whitebox.append(b1_s37)
			all_whitebox.append(b1_s38)
			all_whitebox.append(b1_s39)
			all_whitebox.append(b1_s40)
			all_whitebox.append(b1_s41)
			all_whitebox.append(b1_s42)
			all_whitebox.append(b1_s43)
			all_whitebox.append(b1_s44)
			all_whitebox.append(b1_s45)

			all_whitebox.append(r1_s1)
			all_whitebox.append(r1_s2)
			all_whitebox.append(r1_s3)
			all_whitebox.append(r1_s4)
			all_whitebox.append(r1_s5)
			all_whitebox.append(r1_s6)
			all_whitebox.append(r1_s7)
			all_whitebox.append(r1_s8)
			all_whitebox.append(r1_s9)
			all_whitebox.append(r1_s10)
			all_whitebox.append(r1_s11)
			all_whitebox.append(r1_s12)
			all_whitebox.append(r1_s13)
			all_whitebox.append(r1_s14)
			all_whitebox.append(r1_s15)
			all_whitebox.append(r1_s16)
			all_whitebox.append(r1_s17)
			all_whitebox.append(r1_s18)
			all_whitebox.append(r1_s19)
			all_whitebox.append(r1_s20)
			all_whitebox.append(r1_s21)
			all_whitebox.append(r1_s22)
			all_whitebox.append(r1_s23)
			all_whitebox.append(r1_s24)
			all_whitebox.append(r1_s25)
			all_whitebox.append(r1_s26)
			all_whitebox.append(r1_s27)
			all_whitebox.append(r1_s28)
			all_whitebox.append(r1_s29)
			all_whitebox.append(r1_s30)
			all_whitebox.append(r1_s31)
			all_whitebox.append(r1_s32)
			all_whitebox.append(r1_s33) 
			all_whitebox.append(r1_s34)
			all_whitebox.append(r1_s35)
			all_whitebox.append(r1_s36)
			all_whitebox.append(r1_s37)
			all_whitebox.append(r1_s38)
			all_whitebox.append(r1_s39)
			all_whitebox.append(r1_s40)
			all_whitebox.append(r1_s41)
			all_whitebox.append(r1_s42)
			all_whitebox.append(r1_s43)
			all_whitebox.append(r1_s44)
			all_whitebox.append(r1_s45)

			peacebox.append(peace_b)


			all_sprites.add(b1_b)
			all_sprites.add(b2_b)
			all_sprites.add(r1_b)
			all_sprites.add(r2_b)
			all_sprites.add(b1_elep)
			all_sprites.add(b2_elep)
			all_sprites.add(r1_elep)
			all_sprites.add(r2_elep)
			all_sprites.add(b1_h)
			all_sprites.add(b2_h)
			all_sprites.add(r1_h)
			all_sprites.add(r2_h)
			all_sprites.add(b_kg)
			all_sprites.add(r_kg)
			all_sprites.add(b1_kn)
			all_sprites.add(b2_kn)
			all_sprites.add(r1_kn)
			all_sprites.add(r2_kn)
			all_sprites.add(b1_c)
			all_sprites.add(b2_c)
			all_sprites.add(r1_c)
			all_sprites.add(r2_c)
			all_sprites.add(b1_s)
			all_sprites.add(b2_s)
			all_sprites.add(b3_s)
			all_sprites.add(b4_s)
			all_sprites.add(b5_s)
			all_sprites.add(r1_s)
			all_sprites.add(r2_s)
			all_sprites.add(r3_s)
			all_sprites.add(r4_s)
			all_sprites.add(r5_s)


			all_sprites.add(b1_s1)
			all_sprites.add(b1_s2)
			all_sprites.add(b1_s3)
			all_sprites.add(b1_s4)
			all_sprites.add(b1_s5)
			all_sprites.add(b1_s6)
			all_sprites.add(b1_s7)
			all_sprites.add(b1_s8)
			all_sprites.add(b1_s9)
			all_sprites.add(b1_s10)
			all_sprites.add(b1_s11)
			all_sprites.add(b1_s12)
			all_sprites.add(b1_s13)
			all_sprites.add(b1_s14)
			all_sprites.add(b1_s15)
			all_sprites.add(b1_s16)
			all_sprites.add(b1_s17)
			all_sprites.add(b1_s18)
			all_sprites.add(b1_s19)
			all_sprites.add(b1_s20)
			all_sprites.add(b1_s21)
			all_sprites.add(b1_s22)
			all_sprites.add(b1_s23)
			all_sprites.add(b1_s24)
			all_sprites.add(b1_s25)
			all_sprites.add(b1_s26)
			all_sprites.add(b1_s27)
			all_sprites.add(b1_s28)
			all_sprites.add(b1_s29)
			all_sprites.add(b1_s30)
			all_sprites.add(b1_s31)
			all_sprites.add(b1_s32)
			all_sprites.add(b1_s33) 
			all_sprites.add(b1_s34)
			all_sprites.add(b1_s35)
			all_sprites.add(b1_s36)
			all_sprites.add(b1_s37)
			all_sprites.add(b1_s38)
			all_sprites.add(b1_s39)
			all_sprites.add(b1_s40)
			all_sprites.add(b1_s41)
			all_sprites.add(b1_s42)
			all_sprites.add(b1_s43)
			all_sprites.add(b1_s44)
			all_sprites.add(b1_s45)

			all_sprites.add(r1_s1)
			all_sprites.add(r1_s2)
			all_sprites.add(r1_s3)
			all_sprites.add(r1_s4)
			all_sprites.add(r1_s5)
			all_sprites.add(r1_s6)
			all_sprites.add(r1_s7)
			all_sprites.add(r1_s8)
			all_sprites.add(r1_s9)
			all_sprites.add(r1_s10)
			all_sprites.add(r1_s11)
			all_sprites.add(r1_s12)
			all_sprites.add(r1_s13)
			all_sprites.add(r1_s14)
			all_sprites.add(r1_s15)
			all_sprites.add(r1_s16)
			all_sprites.add(r1_s17)
			all_sprites.add(r1_s18)
			all_sprites.add(r1_s19)
			all_sprites.add(r1_s20)
			all_sprites.add(r1_s21)
			all_sprites.add(r1_s22)
			all_sprites.add(r1_s23)
			all_sprites.add(r1_s24)
			all_sprites.add(r1_s25)
			all_sprites.add(r1_s26)
			all_sprites.add(r1_s27)
			all_sprites.add(r1_s28)
			all_sprites.add(r1_s29)
			all_sprites.add(r1_s30)
			all_sprites.add(r1_s31)
			all_sprites.add(r1_s32)
			all_sprites.add(r1_s33) 
			all_sprites.add(r1_s34)
			all_sprites.add(r1_s35)
			all_sprites.add(r1_s36)
			all_sprites.add(r1_s37)
			all_sprites.add(r1_s38)
			all_sprites.add(r1_s39)
			all_sprites.add(r1_s40)
			all_sprites.add(r1_s41)
			all_sprites.add(r1_s42)
			all_sprites.add(r1_s43)
			all_sprites.add(r1_s44)
			all_sprites.add(r1_s45)
   
			all_sprites.add(peace_b)
			HAVECHESS=[[1,1,1,1,1,1,1,1,1],
			[0,0,0,0,0,0,0,0,0],
			[0,1,0,0,0,0,0,1,0],
			[1,0,1,0,1,0,1,0,1],
			[0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0],
			[1,0,1,0,1,0,1,0,1],
			[0,1,0,0,0,0,0,1,0],
			[0,0,0,0,0,0,0,0,0],
			[1,1,1,1,1,1,1,1,1]]
			show_PLAY_init=False				 
	   #更新遊戲
		all_sprites.update()
	   #顯示畫面
		screen.fill(WHITE)#改變底色
		screen.blit(second_background_img,(0,0))
		if player_turn==1:
			blackturn_img.set_colorkey(GREEN)#把黑色變透明
			blackturn_img=pygame.transform.scale(blackturn_img,(68,68))
			screen.blit(blackturn_img,(60,470))
		else:
			redturn_img.set_colorkey(GREEN)#把黑色變透明
			redturn_img=pygame.transform.scale(redturn_img,(68,68))
			screen.blit(redturn_img,(60,470))
		all_sprites.draw(screen)
	pygame.display.update()
			      
pygame.QUIT

