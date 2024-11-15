## HERENCIA
#class pokemon:
  #def __init__(self, nombre, tipo):
    #self.nombre = nombre
    #self.tipo = tipo
  #def descripcion (self):
    #return "{}es un pokemon de tipo : {}" .format (self.nombre,self.tipo)
#class pikachu (pokemon):
  #def ataque (self,tipoataque):
    #return "{}es tipo de ataque : {}".format (self.nombre, tipoataque)
#class charmader (pokemon):
  #def ataque (self, tipoataque):
    #return "{} tipo de ataque: {}".format(self.nombre, tipoataque)
#nuevo_pokemon = pikachu("boby","piedra")
#print (nuevo_pokemon.descripcion())
class  celular:
  def __init__(self, nombre, marca, color, pulgada):
    self.nombre = nombre
    self.marca = marca
    self.color = color
    self.pulgada = pulgada
  def descripcion (self):
    return "su nombre es : {}  pertence a la marca: {}  de color : {} y con una pantalla de : {}".format(self.nombre, self.marca, self.color, self.pulgada)
class iphone (celular):
  def pais (self,pais):
    return "{}proviene del pais : {}".format(self.nombre, self.pais)
class mayor (celular):
  def mayor (self,vender):
    return "{} la ciudad que mas lo compra  es : {}".format(self.nombre, self,mayor)
nuevo_tele = celular ("huawei", "galaxi", "rojo vivo", "32 pulgadas")
print (nuevo_tele.descripcion())

    
    
    
    
  