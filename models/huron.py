from models.animal_exotico import Animal_Exotico

"""
Punto 3 | Hurones y Boas Constrictor
A partir del enunciado construya las clases Huron y Boa_Constrictor. Recuerde que 
estas dos clases deben heredar a partir de la clase Animal_Exotico definida en el 
punto anterior. No olvide redefinir el método de hacer_sonido según el sonido hecho 
por cada animal, y recuerde que la Boa Constrictor tiene atributos y métodos 
adicionales a los definidos por ser animal exótico.
"""
#Clase Huron que implementa de Animal_Exotico con los metodos abstractos implementados
class Huron(Animal_Exotico):
    def __init__(self, nombre: str, peso: float, edad: int, pais_origen: str, impuestos: float) -> None:
        super().__init__(nombre, peso, edad, pais_origen, impuestos)
    
    # Metodos implementados
    def hacer_sonido(self) -> str:
        return "¡Eek Eek!"