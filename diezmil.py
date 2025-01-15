import random

def tirar_cubilete():

	tirada = []

	for i in range(0,5):
		
		tirada.append(random.randint(1,6))
	
	return(tirada)

#print(tirar_cubilete())
#print(tirar_cubilete())
#print(tirar_cubilete())
#print(tirar_cubilete())
#print(tirar_cubilete())

def cuantos_hay(elemento , lista):

	contador = 0	
	
	for i in lista:
	
		if i == elemento:
		
			contador += 1
	return contador

#print(cuantos_hay(5,[5,5]),'deberia dar: 2')

def puntos_por_unos(tirada):
	
	puntaje = 0

	if(cuantos_hay(1 , tirada) == 5):
	
		puntaje = 10000
		
	elif(cuantos_hay(1 , tirada) == 4):
	
		puntaje = 1100
		
	elif(cuantos_hay(1 , tirada) == 3):
	
		puntaje = 1000
		
	elif(cuantos_hay(1 , tirada) <= 2 and cuantos_hay(1 , tirada)>= 1):
	
		puntaje = cuantos_hay(1 , tirada)*100
		
	return puntaje

#print(puntos_por_unos([1,1,1,1,1]), 'deberia dar: 10000')
#print(puntos_por_unos([1,1,2,1,1]), 'deberia dar: 1100')
#print(puntos_por_unos([1,1,3,1,2]), 'deberia dar: 1000')
#print(puntos_por_unos([6,1,2,1,3]), 'deberia dar: 200')
#print(puntos_por_unos([6,6,6,1,6]), 'deberia dar: 100')
#print(puntos_por_unos([6,6,6,4,6]), 'deberia dar: 0')

def puntos_por_cinco(tirada):

	puntaje = 0

	if(cuantos_hay(5 , tirada) == 5):
	
		puntaje = ((cuantos_hay(5 , tirada)+1)*100)
	
	elif(cuantos_hay(5 , tirada) == 4):
	
		puntaje = 550
		
	elif(cuantos_hay(5 , tirada) == 3):
	
		puntaje = 500
		
	elif(cuantos_hay(5 , tirada) <= 2 and cuantos_hay(5 , tirada) >= 1):
	
		puntaje = cuantos_hay(5 , tirada)*50
	
	return puntaje

#print(puntos_por_cinco([5,5,5,5,5]), 'deberia dar: 600')
#print(puntos_por_cinco([5,5,2,5,5]), 'deberia dar: 550')
#print(puntos_por_cinco([5,5,3,5,2]), 'deberia dar: 500')
#print(puntos_por_cinco([6,5,2,5,3]), 'deberia dar: 100')
#print(puntos_por_cinco([6,6,6,5,6]), 'deberia dar: 50')
#print(puntos_por_cinco([6,6,6,4,6]), 'deberia dar: 0')

def total_puntos(tirada):

	return(puntos_por_unos(tirada) + puntos_por_cinco(tirada))

#print(total_puntos([1,1,1,1,1]),'deberia dar: 10000')
#print(total_puntos([5,5,5,5,5]),'deberia dar: 600')
#print(total_puntos([1,5,1,1,5]),'deberia dar: 1100')

def jugar_ronda(k):
	
	lista_puntos = []

	for i in range(0 , k):
	
		jugada_jugador = tirar_cubilete()
	
		lista_puntos.append(total_puntos(jugada_jugador))
		
	return(lista_puntos)

#print(jugar_ronda(10))

def acumular_puntos(puntajes_acumulados , puntajes_ronda):

	#puntajes_acumulados = [0]*len(puntajes_ronda)
	
	for i in range(0 , len(puntajes_ronda)):
	
		#if(len(puntajes_acumulados) == 0):
		
			#puntajes_acumulados.append(puntajes_ronda[i])
		
		#else:
		
		puntajes_acumulados[i] += puntajes_ronda[i]
			
	return puntajes_acumulados

def hay10mil(puntajes_acumulados):

	res = False

	for i in puntajes_acumulados:
		
		if i >= 10000:
		
			res = True
		
	return res

def partida_completa(k):

	rondas_jugadas = 0
	
	puntajes_ronda = [0]*k

	puntajes_acumulados = [0]*len(puntajes_ronda)

	while((not (hay10mil(puntajes_acumulados)))):
	
		lista_puntos = jugar_ronda(k)
		
		puntajes_acumulados = acumular_puntos(puntajes_acumulados , lista_puntos)
	
		rondas_jugadas += 1
	
	return rondas_jugadas
	
#print(partida_completa(10))

'''
queda ver en promedio cuentas rondas necesita una ronde de  10 jugadores?

chances de llegar a 10mil para 10 jugadores con 18 rondas maximo??

y con 20 jugadores??


'''

def rondas_por_jugadores(rondas , k):

	lista_rondas_por_jugadores = []
	
	for i in range(0,rondas):
	
		lista_rondas_por_jugadores.append(partida_completa(k))
		
	return lista_rondas_por_jugadores , sum(lista_rondas_por_jugadores)/len(lista_rondas_por_jugadores)
	
#print(rondas_por_jugadores(1000,10))

def con_cota(rondas , k , cota):

	lista = rondas_por_jugadores(rondas , k)[0]
	
	contador = 0
	
	for i in lista:
	
		if(i<=cota):
		
			contador += 1
	return ((contador/len(lista))*100)

#print(con_cota(1000,10,18))

def N_con_cota(rondas, k , cota , N):

	lista_proporciones = []
	
	for i in range(0,N):
	
		lista_proporciones.append(con_cota(rondas , k , cota))
		
	return(sum(lista_proporciones)/len(lista_proporciones))

#print(N_con_cota(100,10,18,100))

#para 20 jugadores
#print(con_cota(1000,20,18))

#para 20 jugadores la probabilidad de hasta 18 jugadas
#print(N_con_cota(100,20,18,100))
