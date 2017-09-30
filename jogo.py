import pygame,sys
from pygame.locals import * 
from random import randint
import threading
from importbluepy import *
from class_jogo import *

class jogo:
	def __init__(self):
		pygame.init() #Es preciso siempre utilizarlo
		self.x_size=800
		self.y_size=600
		self.janela = pygame.display.set_mode((self.x_size,self.y_size))
		pygame.display.set_caption("Hola Mundo")

		self.My_flecha = pygame.image.load("flecha.png")
		self.posX_f=650
		self.posY_f=400

		self.My_heart = pygame.image.load("heart.png")
		self.rect = self.My_heart.get_rect()
		self.posX_h=25
		self.posY_h=self.y_size/2
		self.rect.top = 0
		self.rect.left = 0
		self.velocidad = 10 
		self.Fondo = (255,255,255)

		self.hr_value=50	

		self.ImagenFondo = pygame.image.load('fondo.png')
		self.Fuente = pygame.font.SysFont("Arial",20)
	
	def variacao(self,polar,aux):
		hr = polar.readHR()
		print "[%.2f]"%(hr[0]), hr[1]
		if hr[1] > self.hr_value:
			self.posY_h -= self.velocidad
			self.hr_value = hr[1]
		elif hr[1] < self.hr_value:
			self.posY_h += self.velocidad
			self.hr_value = hr[1]

		Tiempo = pygame.time.get_ticks()/1000
		if aux == Tiempo:
			aux+=1
			print Tiempo
		contador = self.Fuente.render("Tempo: "+str(Tiempo)+"-F.C.:"+str(hr[1]) ,0,(120,70,0))
		self.janela.blit(contador,(self.x_size/2-15,25))

	def jog(self,polar):
		aux = 1
		DemoProyectil = Proyectil(self.x_size-30, self.y_size/2)
		DemoCoracao = Coracao(25,self.y_size/2)
		while True:
			self.janela.blit(self.ImagenFondo,(0,0))
			#self.janela.blit(self.My_heart,(self.posX_h,self.posY_h))
			#self.janela.blit(self.My_flecha,(self.posX_f,self.posY_f))
			DemoCoracao.dibujar(self.janela)
			DemoProyectil.dibujar(self.janela)
			DemoProyectil.trayectoria()

			if(DemoProyectil.rect.colliderect(DemoCoracao.rect)):
				DemoCoracao.animacao("heart-broken.png")
				DemoProyectil.velocidadDisparo = 0 
				final_message = self.Fuente.render("Voce Perdeu",0,(120,100,40))
				self.janela.blit(final_message,(self.x_size/2,self.y_size/2))

			DemoCoracao.variacao(polar,aux,self.janela)
			for evento in pygame.event.get():
				if evento.type == QUIT:
					pygame.quit()
					sys.exit()
			pygame.display.update()

if __name__ == '__main__':
	mac = '00:22:D0:B8:61:CA'
	polar = HRMonitor(mac)
	j=jogo()
	#j.jog()
	j.jog(polar)
	polar.finish()	

"""
	def contar():
	    '''Contar hasta cien'''
	    contador = 0
	    while contador<10:
	        contador+=1
	        print('Hilo:', 
	              threading.current_thread().getName(), 
	              'con identificador:', 
	              threading.current_thread().ident,
	              'Contador:', contador)
		hilo1 = threading.Thread(target=contar)
		hilo2 = threading.Thread(target=contar)
		hilo1.start()
		hilo2.start()
"""