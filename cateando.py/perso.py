class persona:
  def __init__(self,nombre,año) :
    self.nombre=nombre
    self.año= año
    
  def descripcion (self):
    return "{} tiene: {}años".format(self.nombre,self.año)
  
  def cometario (self,frase):
    return "{} dice: {}".format(self.nombre,frase)

doctor = persona ("adrian",27)
print(doctor.descripcion())
print(doctor.cometario("hola mundo"))
  