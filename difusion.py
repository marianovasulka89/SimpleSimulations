import random

import numpy as np

import matplotlib.pyplot as plt

import os

import cv2

def crear_recipiente(n_filas, m_columnas):

	'''
	Esta escrita de forma tal que las posiciones las piense de 1nfila a mcol
	arreglando automaticamente las margenes con -1
	(para pensar facil las coordenadas validas)
	'''

	instancia = np.zeros((n_filas+2,m_columnas+2), np.int16)
	
	instancia[:,0] = -1#todas las filas  de la columna 0
	
	instancia[:,instancia.shape[1]-1] = -1#todas las filas de la ultima columna
	
	instancia[0,:] = -1#todas las columnas de la fila 0
	
	instancia[instancia.shape[0]-1,:] = -1#todas las columnas de la ultima fila
	
	return instancia

#print(crear_recipiente(3,3))

def visualizar_recipiente(recipiente):
	plt.figure()
	cmap = plt.cm.Blues # inicializar mapa de colores azules
	cmap.set_under("black") # darle color negro a las posiciones con valor menor a vmin
	plt.imshow(recipiente, cmap=cmap, vmin=0) # graficar el heatmap usando vmin = 0
	plt.colorbar() # graficar la barra de escala de colores
	plt.show()

#visualizar_recipiente(crear_recipiente(5,5))

#para guardar figuras en formato deseado(yo l oqueiro usar en .png)

def guardar_recipiente(recipiente , nombre):
	plt.figure()
	cmap = plt.cm.Blues # inicializar mapa de colores azules
	cmap.set_under("black") # darle color negro a las posiciones con valor menor a vmin
	plt.imshow(recipiente, cmap=cmap, vmin=0) # graficar el heatmap usando vmin = 0
	plt.colorbar() # graficar la barra de escala de colores
	#plt.show()
	plt.savefig(nombre)

def agregar_particulas(recipiente, posicion, cantidad):

	'''
	asume que estamos poniendo particulas en posiciones
	validas, es decir NO en los bordes.
	
	recipiente dado, posicion es una tupla: (fila,columna),
	cantidad de particulas a agregar al recipiente
	en la posicion dada.
	'''
	
	recipiente[posicion] = recipiente[posicion]+cantidad
	
	return (recipiente)

#visualizar_recipiente(agregar_particulas(crear_recipiente(5,5) , (4,3) , 8))

def es_borde(recipiente, posicion):

	'''
	devuelve true si la posicion es borde
	'''

	return(posicion[0] == 0 or posicion[0] == recipiente.shape[0]-1 or posicion[1] == 0 or posicion[1] == recipiente.shape[1]-1)

#print(es_borde(crear_recipiente(5,5),(0,0)))
#print(es_borde(crear_recipiente(5,5),(0,3)))
#print(es_borde(crear_recipiente(5,5),(0,6)))
#print(es_borde(crear_recipiente(5,5),(4,6)))
#print(es_borde(crear_recipiente(5,5),(6,6)))
#print(es_borde(crear_recipiente(5,5),(3,4)))

def vecinos(recipiente, posicion):

	'''
	devuelve lista de posiciones vecinas
	estas son arriba,abajo,der,e,izq.
	si es borde, no aparece.
	'''
	
	arriba = (posicion[0]+1,posicion[1])
	
	abajo = (posicion[0]-1,posicion[1])
	
	derecha = (posicion[0],posicion[1]+1)
	
	izquierda = (posicion[0],posicion[1]-1)
	
	lista = [arriba,abajo,derecha,izquierda]
	
	res = []
	
	for i in lista:
		
		if(not es_borde(recipiente,i)):
			
			res.append(i)
	
	return res

#print(vecinos(crear_recipiente(5,5),(3,3)))

def mover_particula(recipiente, posicion):

	'''
	mueve una particula a una posicion vecina (valida) al azar
	'''
	
	if(recipiente[posicion]>=1):
		
		l = vecinos(recipiente, posicion)
		
		nueva_pos = l[random.randint(0 , len(l)-1)]
		
		recipiente[posicion] = recipiente[posicion]-1
		
		recipiente[nueva_pos] = recipiente[nueva_pos]+1
	
	return recipiente

#print(mover_particula(agregar_particulas(crear_recipiente(9,9) , (4,3) , 8) , (4,3)))
####hasta aca va perfecto
def mover_muchas_particulas(recipiente, posicion, cantidad):
	
	'''
	mueve cantidad de particulas al azar en posiciones validas al rededor
	
	'''
	contador = 0
	
	while(contador < cantidad):
		
		recipiente = mover_particula(recipiente , posicion)
		
		contador += 1
	
	return(recipiente)

#print(mover_muchas_particulas(agregar_particulas(crear_recipiente(9,9) , (4,3) , 8) , (4,3) , 5))
#####hassta aca viene bien
def mover_particulas_recipiente(recipiente, recipiente_original):

	'''
	realizar movimientos de a una vez por cada posicion
	del recipiente original
	modificando en recipiente
	(mapea en recipiente_original, y modifica en recipiente)
	esto define un lapso de tiempo
	'''
	
	#copia = np.copy(recipiente_original)
	
	for fila in range(1 , recipiente_original.shape[0]-1):
		
		for columna in range(1 , recipiente_original.shape[1]-1):
		
			#copia = np.copy(recipiente_original)
			
			#recipiente = copia
			
			pos = (fila , columna)
			
			if(recipiente_original[pos]>=1):
			
				recipiente = mover_particula(recipiente , pos)
	
	return recipiente

#rr = agregar_particulas(crear_recipiente(9,9) , (5,5) , 8)

#rr_r = np.copy(rr)

#print(mover_particulas_recipiente(rr , rr_r))

def evolucionar_recipiente(recipiente, k):
	
	for i in range(0,k):
		
		recipiente = mover_particulas_recipiente(recipiente , np.copy(recipiente))
	
	return recipiente

#rrr = agregar_particulas(crear_recipiente(9,9) , (5,5) , 80)
#print(evolucionar_recipiente(rrr , 10))

#######me quedan del 10 en adelante...

def inicializar_particulas(recipiente,cantidad):

	for fila in range(1,recipiente.shape[0]-1):
		
		recipiente = agregar_particulas(recipiente , (fila,1) , cantidad)

	return recipiente

#print(inicializar_particulas(crear_recipiente(9,9),50))

def simular_difusion_horizontal():
	
	'''
	devuelve el resultado final de simular 300 pasos temporales
	inicia con recipiente 35*35 primer columna llena de 50 particulas cada posicion
	'''
	
	simu = inicializar_particulas(crear_recipiente(35,35),50)
	
	simu = evolucionar_recipiente(simu,300)
	
	return simu

#r = (simular_difusion_horizontal())
#visualizar_recipiente(r)

def hay_particula_en_borde_derecho(recipiente):
	
	'''
	define si hay alguna particula en el borde derecho
	'''
	
	res = False
	
	for fila in range(1,recipiente.shape[0]-1):
		
		pos = (fila,recipiente.shape[1]-2)
		
		if(recipiente[pos]>=1):
			
			res = True
	
	return res

#print(agregar_particulas(crear_recipiente(3,3) , (2,3) , 3))#el 3 esta en (2,3)
#print(hay_particula_en_borde_derecho(agregar_particulas(crear_recipiente(3,3) , (2,3) , 3)) , 'deberia dar true')
#print(hay_particula_en_borde_derecho(agregar_particulas(crear_recipiente(3,3) , (1,3) , 1)) , 'deberia dar true')
#print(hay_particula_en_borde_derecho(agregar_particulas(crear_recipiente(3,3) , (3,3) , 1)) , 'deberia dar true')
#print(hay_particula_en_borde_derecho(agregar_particulas(crear_recipiente(3,3) , (1,2) , 1)) , 'deberia dar false')
#print(hay_particula_en_borde_derecho(crear_recipiente(3,3)) , 'deberia dar false')

######hasta aca todo anda joya!!!!!

###aprovechar esta ultima funcion para meter en un while, que temrine de simular
###anote el promedio desimulaciones hechas en una lista
####luego sacar el promedio de eso

def experimentar_particula_borde_derecho(n_filas,m_columnas,cantidad,ejecs):
	
	contador_arch = 1
	
	k = 1
	
	lista_lapsos = []
	
	for i in range(0 , ejecs):
	
		r = crear_recipiente(n_filas, m_columnas)
	
		r = inicializar_particulas(r,cantidad)
	
		lapsos_temporales = 0
	
		while(not(hay_particula_en_borde_derecho(r))):
			
			r = evolucionar_recipiente(r,k)
			
			lapsos_temporales += 1
			
			guardar_recipiente(r , '/home/mariano/Documents/Docencia/EP/difusion/imagenes/borde_derecho//imagen_borde_derecho_{}.png'.format(str(contador_arch)))
			
			contador_arch += 1
		
		lista_lapsos.append(lapsos_temporales)
	
	return(sum(lista_lapsos)/len(lista_lapsos))

#print(experimentar_particula_borde_derecho(5 , 5 , 5 , 100))



	
	


#####hacer funcion que genere pared en el medio, con aujerito en el medio

def hacer_pared(recipiente):
	
	pos_aujero = (recipiente.shape[0]//2 , recipiente.shape[1]//2)
	
	for fila in range(1 , recipiente.shape[0]-1):
	
		recipiente[fila,pos_aujero[1]] = -1
	
	recipiente[pos_aujero] = 0
	
	return recipiente

#print(hacer_pared(crear_recipiente(9,9)))

def pared_generalizada(recipiente , pos_aujero):
	
	for fila in range(1 , recipiente.shape[0]-1):
	
		recipiente[fila,pos_aujero[1]] = -1
	
	recipiente[pos_aujero] = 0
	
	return recipiente

#print(pared_generalizada(crear_recipiente(9,9) , (3,2)))


##################falopa mia, probar con pared, como cambia el prom, pared muy cerca inicio? pared cerca final??

def experimentar_particula_borde_derecho_con_pared_central(n_filas,m_columnas,cantidad,ejecs):
	
	contador_arch = 1
	
	k = 1
	
	lista_lapsos = []
	
	for i in range(0 , ejecs):
	
		r = crear_recipiente(n_filas, m_columnas)
	
		r = inicializar_particulas(r,cantidad)
		
		r = hacer_pared(r)
	
		lapsos_temporales = 0
	
		while(not(hay_particula_en_borde_derecho(r))):
			
			r = evolucionar_recipiente(r,k)
			
			lapsos_temporales += 1
			
			guardar_recipiente(r , '/imagenes/borde_derecho_pared_central/imagen_borde_derecho_pared_central_{}.png'.format(str(contador_arch)))
		
			contador_arch += 1
		
		lista_lapsos.append(lapsos_temporales)
	
	return(sum(lista_lapsos)/len(lista_lapsos))

#print(experimentar_particula_borde_derecho_con_pared_central(5 , 5 , 5 , 100))

def experimentar_particula_borde_derecho_con_pared_explicita(n_filas,m_columnas,cantidad,ejecs,pos_pared):
	
	contador_arch = 1
	
	k = 1
	
	lista_lapsos = []
	
	for i in range(0 , ejecs):
	
		r = crear_recipiente(n_filas, m_columnas)
	
		r = inicializar_particulas(r,cantidad)
		
		r = pared_generalizada(r , pos_pared)
	
		lapsos_temporales = 0
	
		while(not(hay_particula_en_borde_derecho(r))):
			
			r = evolucionar_recipiente(r,k)
			
			lapsos_temporales += 1
			
			guardar_recipiente(r , '/imagenes/borde_derecho_pared_i/imagen_borde_derecho_pared_i_{}.png'.format(str(contador_arch)))
			
			contador_arch +=1
		
		lista_lapsos.append(lapsos_temporales)
	
	return(sum(lista_lapsos)/len(lista_lapsos))

#print(experimentar_particula_borde_derecho_con_pared_explicita(5 , 5 , 5 , 100 , (2,2)))
#print(experimentar_particula_borde_derecho_con_pared_explicita(5 , 5 , 5 , 100 , (2,4)))

####solo queda simular algo tal que se guarde cada figura en cada iteracion, y asi guardar cada paso, y hacer
#####video, como pide consigna, usar guardar_recipiente(recipiente , nombre) dentro de un for, para ir guardando numeradas las
#####imagenes, asi hago las peliculas

def video(path , nombre_base_archivo):
	
	image_folder = path
	video_name = nombre_base_archivo + '_video.avi'

	images = [img for img in (os.listdir(image_folder)) if img.endswith(".png")]
	images_sorted = sorted(images , key=lambda x: int(x.split(nombre_base_archivo)[1].split(".")[0]))
	frame = cv2.imread(os.path.join(image_folder, images_sorted[0]))
	height, width, layers = frame.shape

	video = cv2.VideoWriter(video_name, 0, 1, (width,height))

	for image in images_sorted:
		video.write(cv2.imread(os.path.join(image_folder, image)))

	cv2.destroyAllWindows()
	video.release()

#experimentar_particula_borde_derecho(5 , 5 , 5 , 100)
video('/home/mariano/Documents/Docencia/EP/difusion/imagenes/borde_derecho/' , 'imagen_borde_derecho_')
