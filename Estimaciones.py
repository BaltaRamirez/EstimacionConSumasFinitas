from fractions import Fraction  #Importacion de libreria de fracciones 
###################################################################################################################################
#Declaracion de variables 

a = 0
b = 1
n = 2

#En este ejercicio de calculo n puede ser 6,12,50,100,150

###################################################################################################################################
#Delta x se calcula de la forma deltaX = (b - a)/n  ;	la funcion es y = 1 - x^2 ;		El intervalo es [0,1] donde a = 0 y b = 1

deltaX = float(b-a)/n 
deltaX = Fraction(deltaX).limit_denominator(1000)	#Convierte el flotante a fraccion
deltaX = Fraction(b,n)		#Convertir a fraccion el deltaX, donde b es el numerador y n el denominador
limite = Fraction(n,n)
listaValores = [0,deltaX]	#Se agregan 0 y deltaX porque siempre se comienza de 0 y se realiza el incremento de deltaX en deltaX (valores de la izquierda)
listaValores2 = [deltaX]	#Se agrega desde deltaX porque se toman los valores de la derecha

###################################################################################################################################
#Funcion de Sobreestimacion
def sobreEstimacion():
	b = 1
	#A continuacion se agregan a la lista de Python, las subdivisiones de longitud en la recta de las X
	while b < n:
		listaValores.append(Fraction(b + 1, n))
		b = b + 1

	iterador = iter(listaValores)
	d = 0
	while True:
		try:
			y = (1 - iterador.next() ** 2) * deltaX
			d = d + y
		except StopIteration:
			break
	return d

####################################################################################################################################
#Funcion de Subestimacion
def subEstimacion():
	b = 1
	#A continuacion se agregan a la lista de Python, las subdivisiones de longitud en la recta de las X
	while b < n:
		listaValores2.append(Fraction(b + 1, n))
		b = b + 1

	listaValores2.append(limite)

	iterador = iter(listaValores2)
	p = 0
	while True:
		try:
			y = (1 -iterador.next() ** 2) * deltaX
			p = p + y
		except StopIteration:
			break
	return p

####################################################################################################################################