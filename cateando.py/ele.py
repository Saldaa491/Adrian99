num1=float(input("ingresa el primer número :  "))
num2=float(input("ingresa el segundo número :  "))
print("1 = suma")
print("2 = resta")
print("3 = multiplicar")
print("4 = dividir")

ope=int(input("ingresa la operacion a realizar : "))
if ope ==1:
  resultado=num1 + num2
  print(f"la suma de {num1} + {num2} es : {resultado}")
elif ope==2:
  resultado= num1-num2
  print(f"la suma de {num1}-{num2}es : {resultado}")
elif ope==3:
  resultado= num1*num2
  print(f"la suma de {num1}*{num2}es : {resultado}")
elif ope==4:
  if num2 !=0:
    resultado= num1/num2
    print(f"la suma de {num1}/{num2}es : {resultado}")
  else :
    print("numero se puede dividir por cero ")
else :
  print("numero de operacion no existe")

  
  