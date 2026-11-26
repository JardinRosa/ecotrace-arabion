# Primero creamos nuestra Clase

class Vehiculo:
    def __init__(self, marca, modelo, anio, tipo_vehiculo,
                 cilindrada, cilindros, transmision, tipo_combustible,
                 consumo_ciudad, consumo_carretera,
                 consumo_combinado, emisiones_co2):

        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.tipo_vehiculo = tipo_vehiculo
        self.cilindrada = cilindrada
        self.cilindros = cilindros
        self.transmision = transmision
        self.tipo_combustible = tipo_combustible
        self.consumo_ciudad = consumo_ciudad
        self.consumo_carretera = consumo_carretera
        self.consumo_combinado = consumo_combinado
        self.emisiones_co2 = emisiones_co2

#Creación de nuestro primer Metodo
    def mostrar_información(self):
        print(f"Marca:{self.marca}")
        print(f"Modelo:{self.modelo}")
        print(f"año:{self.anio}")
        print(f"Combustible: {self.tipo_combustible}")
        print(f"Consumo combinado: {self.consumo_combinado} L/100 km")
        print(f"Emisiones de CO2: {self.emisiones_co2} g/km")
        print(f"Tipo de vehículo: {self.tipo_vehiculo}")
        print(f"Transmisión: {self.transmision}")
#Metodos para obtener el consumo y las emisiones de CO2
    def obtener_consumo(self):
        return self.consumo_combinado

    def obtener_emisiones(self):
        return self.emisiones_co2
# Metodo para crear nuestro metodo diccionario
    def a_diccionario(self):
        return {
        "marca": self.marca,
        "modelo": self.modelo,
        "anio": self.anio, 
        "cilindrada": self.cilindrada,
        "cilindros": self.cilindros,
        "tipo_combustible": self.tipo_combustible,
        "consumo_ciudad": self.consumo_ciudad,
        "consumo_carretera": self.consumo_carretera,
        "consumo_combinado": self.consumo_combinado,
        "emisiones_co2": self.emisiones_co2,
        "tipo_vehiculo": self.tipo_vehiculo,
        "transmision": self.transmision
    }