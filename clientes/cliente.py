class Cliente:
    def __init__(self, nombre, correo, direccion, telefono):
        self.nombre = nombre
        self.correo = correo
        self.direccion = direccion
        self.telefono = telefono

    def __str__(self):
        return f"Cliente: {self.nombre}"

    def realizar_compra(self, producto, cantidad):
        # Aca podemos hacer una compra
        print(f"{self.nombre} compro {cantidad} unidades de {producto}.")

    def actualizar_informacion(self, nuevo_correo, nueva_direccion, nuevo_telefono):
        # Aca actualizamos la informacion del cliente
        self.correo = nuevo_correo
        self.direccion = nueva_direccion
        self.telefono = nuevo_telefono
        print(f"Información actualizada para {self.nombre}: Correo: {nuevo_correo}, Dirección: {nueva_direccion}, Teléfono: {nuevo_telefono}")

# Este bloque se ejecutará si ejecutas el script directamente
cliente1 = Cliente("Javier Pires", "javierpires@gmail.com", "Bogota 1230, CABA", "11-8324-9485")
print(cliente1)
cliente1.realizar_compra("Remera", 3)
cliente1.actualizar_informacion("javierpires30@gmail.com", "Arenales 10, Ramos Mejia", "11-3521-9077")