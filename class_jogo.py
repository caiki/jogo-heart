import pygame,sys
from pygame.locals import *

class Proyectil(pygame.sprite.Sprite):
	"""docstring for Proyectil"""
	def __init__(self, posx, posy):
		pygame.sprite.Sprite.__init__(self)
		self.imageProyectil = pygame.image.load('flecha.png')
		self.rect = self.imageProyectil.get_rect()
		self.velocidadDisparo = 50
		self.rect.top = posy
		self.rect.left = posx

	def trayectoria(self):
		self.rect.left = self.rect.left - self.velocidadDisparo		

	def dibujar(self, superficie):
		superficie.blit(self.imageProyectil,self.rect)

class Coracao(pygame.sprite.Sprite):
	"""classe para Coracao"""
	def __init__(self, posx, posy):
		pygame.sprite.Sprite.__init__(self)
		self.My_heart = pygame.image.load("heart.png")
		self.rect = self.My_heart.get_rect()
		self.velocidad = 10
		self.rect.top = posy
		self.rect.left = posx

		self.hr_value=50
		self.Fuente = pygame.font.SysFont("Arial",20)	

	def dibujar(self, superficie):
		superficie.blit(self.My_heart,self.rect)

	def animacao(self,image):
		self.My_heart = pygame.image.load(image)
	# variacao dos batimentos cardiacos	
	def variacao(self,polar,aux,superficie):
		hr = polar.readHR()
		print "[%.2f]"%(hr[0]), hr[1]
		if hr[1] > self.hr_value:
			self.rect.top -= self.velocidad
			self.hr_value = hr[1]
		elif hr[1] < self.hr_value:
			self.rect.top += self.velocidad
			self.hr_value = hr[1]

		# Display Time
		Tiempo = pygame.time.get_ticks()/1000
		if aux == Tiempo:
			aux+=1
			print Tiempo
		contador = self.Fuente.render("Tempo: "+str(Tiempo)+"-F.C.:"+str(hr[1]) ,0,(120,70,0))
		superficie.blit(contador,(superficie.get_width()/2-15,25))

	#DemoProyectil = Proyectil(ancho/2, alto-30)