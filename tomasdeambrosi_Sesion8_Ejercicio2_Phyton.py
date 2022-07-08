'''En este segundo ejercicio, tendréis que crear un archivo py y dentro crearéis una clase Vehículo, haréis un objeto de ella, lo guardaréis 
en un archivo y luego lo cargamos.'''
import pickle

class Triangulo:
    name: None
    base: 0  
    altura: 0

    def __init__(self, nombre, base, altura):
        self.nombre = nombre
        self.base = base
        self.altura = altura
    
    def area(self):
        areaEs = int((self.base * self.altura)/2)
        return f'El área del triángulo {self.nombre} es {areaEs} cm3'

t1 = Triangulo('t1', 10,20)

f = open('ficheroTriangulo.bin', 'wb')
pickle.dump(t1, f)
f.close()

f = open('ficheroTriangulo.bin', 'rb')
triangulo1 = pickle.load(f)
f.close()

print(t1.area())


