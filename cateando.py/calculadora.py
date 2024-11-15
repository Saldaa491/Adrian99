#calculadora
class Calculadora:
  def __init__(self, num1,num2):
    self.suma= num1+num2
    self.resta= num1 - num2
    self.multipli= num1 * num2
    self.division = num1 / num2
operador = Calculadora (5,5)
print(operador.suma)