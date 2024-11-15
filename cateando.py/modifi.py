# modificar atributos
class Email:
  def __init__(self) :
    self.enviado = False #se supone que 1paso esta falso 
  def enviar_correo(self):
    self.enviado= True # se supone que es falso 
  
mi_correo = Email ()
#print(mi_correo.enviado) # esto es por que he selecionado la primera declaracion
mi_correo.enviar_correo () #estoy declarado el TRUE  de formammas especifica
print (mi_correo.enviado)