import random
def bosque_vacio(n):
	
	return [0]*n
#print(bosque_vacio(5))

def brotar(bosque , probabilidad):

	for i in range(0 , len(bosque)):
	
		if (bosque[i] == 0):
		
			p = random.randint(0,100)
		
			if p>=100-probabilidad:
		
				bosque[i] = 1
	
	return (bosque)

#print(brotar(bosque_vacio(100) , 50))

def iniciar_fuego(bosque , probabilidad):
	
	for i in range(0 , len(bosque)):
	
		if (bosque[i] == 1):
		
			p = random.randint(0,100)
		
			if p>=100-probabilidad:
		
				bosque[i] = -1
	
	return (bosque)

#print(iniciar_fuego(brotar(bosque_vacio(100) , 50) , 50))

#def extender_incendio(bosque):

#	for i in range(0 , len(bosque)):
	
#		if (i>0 and i<len(bosque)-1 and bosque[i]==-1 and (bosque[i-1]==1 or bosque[i+1]==1)):
			
#			if bosque[i-1]==1:
			
#				bosque[i-1] = -1

#			if bosque[i+1]==1:
			
#				bosque[i+1]= -1
				
#		if (i==0 and bosque[i]==-1 and bosque[i+1]==1):
		
#			bosque[i+1] = -1
			
#		if (i==len(bosque)-1 and bosque[i]==-1 and bosque[i-1]==1):
		
#			bosque[i-1] = -1
			
#	return bosque

#print(extender_incendio([0,1,-1,1,0,0,-1,0,1,1]),'\n','deberia dar: ' , [0,-1,-1,-1,0,0,-1,0,1,1])
#print(extender_incendio([1,1,-1,1,0,0,-1,0,1,1]),'\n','deberia dar: ' , [-1,-1,-1,-1,0,0,-1,0,1,1])
#print(extender_incendio([1,-1,0,1,1,1,1,-1,1,0,0,-1,0,1,1]),'\n','deberia dar: ' , [-1,-1,0,-1,-1,-1,-1,-1,-1,0,0,-1,0,1,1])

def extender_incendio_2(bosque):

	for i in range(0,len(bosque)):
	
		if (i>0 and i<len(bosque)-1 and bosque[i]==-1 and (bosque[i-1]==1 or bosque[i+1]==1)):
			
			if bosque[i-1]==1:
			
				bosque[i-1] = -1
			
			if bosque[i+1]==1:
			
				bosque[i+1] = -1
			
				for j in range(1,len(bosque)-1):
				
					if(bosque[j-1]==-1 and bosque[j]==1):
					
						bosque[j]=-1
		
		if (i==0 and bosque[i]==-1 and bosque[i+1]==1):
		
			bosque[i+1] = -1
			
		if (i==len(bosque)-1 and bosque[i]==-1 and bosque[i-1]==1):
		
			bosque[i-1] = -1
	
	#volver a recorrer pero de atraz para adelante
	
	for i in range(len(bosque)-1,0,-1):
	
		if (i>0 and i<len(bosque)-1 and bosque[i]==-1 and (bosque[i-1]==1 or bosque[i+1]==1)):
			
			if bosque[i-1]==1:
			
				bosque[i-1] = -1
			
			if bosque[i+1]==1:
			
				bosque[i+1] = -1
			
				for j in range(len(bosque)-1,1,-1):
				
					if(bosque[j+1]==-1 and bosque[j]==1):
					
						bosque[j]=-1
		
		if (i==0 and bosque[i]==-1 and bosque[i-1]==1):
		
			bosque[i-1] = -1
			
		if (i==len(bosque)-1 and bosque[i]==-1 and bosque[i-1]==1):
		
			bosque[i+1] = -1
	
	
	return bosque

#print(extender_incendio_2([0,1,-1,1,0,0,-1,0,1,1]),'\n','deberia dar: ' , [0,-1,-1,-1,0,0,-1,0,1,1])
#print(extender_incendio_2([1,1,-1,1,0,0,-1,0,1,1]),'\n','deberia dar: ' , [-1,-1,-1,-1,0,0,-1,0,1,1])
#print(extender_incendio_2([1,-1,0,1,1,1,1,-1,1,0,0,-1,0,1,1]),'\n','deberia dar: ' , [-1,-1,0,-1,-1,-1,-1,-1,-1,0,0,-1,0,1,1])


def limpiar_incendio(bosque):

	for i in range(0 , len(bosque)):
	
		if(bosque[i] == -1):
		
			bosque[i] = 0
	
	return bosque

#print(limpiar_incendio([-1,-1,0,-1,-1]),'deberia dar: ' , [0,0,0,0,0])

def cuantos(elemento , bosque):
	
	contador = 0
	
	for i in bosque:
		
		if i == elemento:
		
			contador += 1
			
	return contador
	
#print(cuantos(0 , [0,0,1]),'da: 2')
#print(cuantos(1 , [0,0,1]),'da: 1')
#print(cuantos(-1 , [0,0,1]),'da: 0')
#print(cuantos(-1 , [-1,-1,-1]),'da: 3')

def dinamica(n,a,p,f):

	'''n = num posiciones
	a = cantidad anios
	p = probabilidad brotes
	f = probabilidad rayo que prende fuego

	se concidera un anio a temporada de brote,rayo,expancionfuego,limpieza'''

	bosque = bosque_vacio(n)
	
	lista_sobrevida = []
	
	for anio in range(0,a):
	
		brotado = brotar(bosque , p)
		
		rayo = iniciar_fuego(brotado , f)
		
		incendio = extender_incendio_2(rayo)
		
		bosque = limpiar_incendio(incendio)
		
		lista_sobrevida.append(cuantos(1 , bosque))
	
	return (lista_sobrevida , sum(lista_sobrevida)/len(lista_sobrevida))

#print(dinamica(1000,500,50,4))

def N_din(n,a,f,desde,hasta):

	lista_din = []
	
	lista_p = []
	
	for i in range(desde, hasta+1):
	
		lista_p.append(i)
	
		lista_din.append(dinamica(n,a,i,f)[1])
	
	return (lista_p , lista_din)

from matplotlib import pyplot as plt

dinas = N_din(1000,500,4,0,100)
#print(dinas[0][:5])
#print(dinas[1][:5])
plt.plot(dinas[0] , dinas[1])

plt.show()
