import Estimaciones		#Importacion del archivo donde estan las funciones
from fractions import Fraction  #Importacion de libreria de fracciones 

aSobre = Estimaciones.sobreEstimacion()
aSub = Estimaciones.subEstimacion()
print("SobreEstimacion\n")
print(aSobre)
print("SubEstimacion\n")
print(aSub)

###################################################################################################################################

errorAbsoluto = abs(aSobre - aSub) 	#Formula para calcular el arror absoluto
print("El error absoluto es:\n")
print(errorAbsoluto)
