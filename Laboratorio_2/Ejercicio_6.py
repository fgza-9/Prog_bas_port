class Vehiculo:
    def __init__(self, marca, modelo, ano, precio):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.precio = precio
    
    def mostrar_informacion(self):
        return f"Marca: {self.marca}\nModelo: {self.modelo}\nAño: {self.ano}\nPrecio: ${self.precio:.2f}"
    
class Automovil(Vehiculo):
    def __init__(self, marca, modelo, ano, precio, num_puertas):
        super().__init__(marca, modelo, ano, precio)
        self.num_puertas = num_puertas
    
    def mostrar_informacion(self):
        info_vehiculo = super().mostrar_informacion()
        return f"{info_vehiculo}\nNúmero de puertas: {self.num_puertas}"

class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, ano, precio, cilindrada):
        super().__init__(marca, modelo, ano, precio)
        self.cilindrada = cilindrada
    
    def mostrar_informacion(self):
        info_vehiculo = super().mostrar_informacion()
        return f"{info_vehiculo}\nCilindrada: {self.cilindrada}cc"



auto1 = Automovil("Toyota", "Corolla", 2022, 25000, 4)

moto1 = Motocicleta("Yamaha", "MT-07", 2021, 7500, 689)


print("Información del Automóvil:")
print(auto1.mostrar_informacion())

print("\nInformación de la Motocicleta:")
print(moto1.mostrar_informacion())
