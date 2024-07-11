from models.animal import Animal
from abc import ABC, abstractmethod

"""
Punto 2 | Animal Exótico
A partir del enunciado construya la clase Animal_Exotico. Recuerde que esta debe 
heredar a partir de la clase ya definida de Animal. No olvide incluir todas las funciones 
y atributos nuevos que no tiene ni la clase padre ni la interfaz.
"""
#Clase Animal_Exotico que implementa de Animal con sus metodos abstractos
class Animal_Exotico(Animal, ABC):
    def __init__(self, nombre: str, peso: float, edad: int, pais_origen: str, impuestos: float) -> None:
        super().__init__(nombre, peso, edad)
        self._pais_origen = pais_origen
        self._impuestos = impuestos

    # Metodos abstactos
    @abstractmethod
    def hacer_sonido(self) -> str:
        pass
    
    # Otros metodos
    def calcular_flete(self) -> float:
        return round(self._peso * self._impuestos, 2)