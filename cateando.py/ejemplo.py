## crear un programa que con un capital de 20.000.000 millones
##permita perstar a muvhar personal y lo que le preste a dicha persona
## se le preste con un interes del 15% "si es de un mes"
# 20% "si son 2 meses " y 30% "si es superior a 3 meses"
# y cada vez que la persona abone se va a disminuir
# la cantidad prestada junto con los interese
capital=20000000
nombre=input("Nombre de la persona : ")
prestamo=int(input("Cantidad a presatar : "))
print(" 1 mes 15%")
print(" 2 mes 20%")
print(" 3 mes 30%")
meses=input("Cuantos meses desea pagar el credito")
if meses <= 1 :
  interes =  15
elif meses >= 2:
  interes = 20
elif meses >= 3:
  interes = 30
else:
  interes = 0
  print("selecciona alguna  de las 3 opciones ")
if interes > 0:
  print(f"El interés para {meses} mes(es) es del {interes}%.")
    
  

while capital > prestamo:
  print (f"{nombre} a solicitado un monto de {prestamo }. prestamo aprobado ")        
  capital-= prestamo
  print(f"capital despues del prestamo {capital}")
  prestamo = int(input("Cantidad a prestar (o 5 para finalizar): "))
  
  
  if prestamo == 0:
        
        print("Proceso de préstamo finalizado.")
        break
if capital < prestamo:
    print(f"No hay suficiente capital para aprobar el préstamo de {prestamo}.")
  
  
  
