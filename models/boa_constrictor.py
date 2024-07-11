from models.animal_exotico import Animal_Exotico

"""
Punto 3 | Hurones y Boas Constrictor
A partir del enunciado construya las clases Huron y Boa_Constrictor. Recuerde que 
estas dos clases deben heredar a partir de la clase Animal_Exotico definida en el 
punto anterior. No olvide redefinir el método de hacer_sonido según el sonido hecho 
por cada animal, y recuerde que la Boa Constrictor tiene atributos y métodos 
adicionales a los definidos por ser animal exótico.
"""
#Clase Boa_Constrictor que implementa de Animal_Exotico con los metodos abstractos implementados
class Boa_Constrictor(Animal_Exotico):
    def __init__(self, nombre: str, peso: float, edad: int, pais_origen: str, impuestos: float) -> None:
        super().__init__(nombre, peso, edad, pais_origen, impuestos)
        self.__ratones_comidos = 0
    
    # Metodos implementados
    def hacer_sonido(self) -> str:
        return "Tsss!"
    
    # Otros metodos
    def obtener_ratones_comidos(self) -> int:
        return self.__ratones_comidos
    
    def sumar_ratones_comidos(self, ratones: int) -> None:
        if self.__ratones_comidos == 10:
            return ValueError("La boa está llena")
        self.__ratones_comidos += ratones
        return "Éxito"