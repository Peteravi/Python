class PuntoDeVenta:
    def __init__(self):
        self.datos_equipo = "Datos del equipo"
        self.materia = "Materia"
        self.nombre_escuela = "Nombre de la Escuela"
        self.docente = "Docente"
        self.nombre_sistema = "Nombre del Sistema"
        self.inventario = {
            "Dama": {"Blusa": {"Código": 101, "Descripción": "Blusa elegante para mujeres", "Precio": 30.0},
                    "Pantalón": {"Código": 102, "Descripción": "Pantalón moderno para mujeres", "Precio": 40.0},
                    "Vestido": {"Código": 103, "Descripción": "Vestido de ocasión para mujeres", "Precio": 50.0}},
            "Caballero": {"Camisa": {"Código": 201, "Descripción": "Camisa formal para hombres", "Precio": 35.0},
                          "Pantalón": {"Código": 202, "Descripción": "Pantalón clásico para hombres", "Precio": 45.0},
                          "Corbata": {"Código": 203, "Descripción": "Corbata elegante para hombres", "Precio": 15.0}},
            "Niño": {"Camiseta": {"Código": 301, "Descripción": "Camiseta cómoda para niños", "Precio": 20.0},
                     "Short": {"Código": 302, "Descripción": "Short deportivo para niños", "Precio": 25.0},
                     "Sudadera": {"Código": 303, "Descripción": "Sudadera abrigada para niños", "Precio": 35.0}},
            "Niña": {"Vestido": {"Código": 401, "Descripción": "Vestido encantador para niñas", "Precio": 40.0},
                      "Pantalón": {"Código": 402, "Descripción": "Pantalón moderno para niñas", "Precio": 30.0},
                      "Blusa": {"Código": 403, "Descripción": "Blusa bonita para niñas", "Precio": 25.0}},
            "Bebé": {"Body": {"Código": 501, "Descripción": "Body cómodo para bebés", "Precio": 15.0},
                     "Pijama": {"Código": 502, "Descripción": "Pijama suave para bebés", "Precio": 20.0},
                     "Gorro": {"Código": 503, "Descripción": "Gorro lindo para bebés", "Precio": 10.0}}
        }

    def mostrar_presentacion(self):
        print(self.datos_equipo)
        print(self.materia)
        print(self.nombre_escuela)
        print(self.docente)
        print(self.nombre_sistema)
        print("\nBienvenido al Sistema de Programación. A continuación, elija una opción del menú.")

    def mostrar_opciones_ropa(self, departamento):
        print(f"\nOpciones disponibles en {departamento}:")
        for ropa, info in self.inventario[departamento].items():
            print(f"{ropa} - Código: {info['Código']} - Descripción: {info['Descripción']} - Precio: ${info['Precio']:.2f}")

    def procesar_compra(self, departamento):
        total = 0
        descuento = 0

        while True:
            try:
                codigo = input("Ingrese el código del producto a comprar (0 para salir): ")
                if codigo == "0":
                    break

                if codigo.isdigit():  # Verificar si el código es un número
                    codigo = int(codigo)

                    for ropa, info in self.inventario[departamento].items():
                        if info["Código"] == codigo:
                            cantidad = int(input("Ingrese la cantidad de productos a comprar: "))
                            precio_unitario = info["Precio"]
                            subtotal = cantidad * precio_unitario

                            total += subtotal

                            print(f"\nProducto: {ropa} - Código: {info['Código']} - Descripción: {info['Descripción']} - Precio: ${info['Precio']:.2f}")
                            print(f"Cantidad: {cantidad}")
                            print(f"Subtotal: ${subtotal:.2f}")
                            print(f"Total acumulado: ${total:.2f}")
                            break
                    else:
                        print("Código no válido. Inténtelo de nuevo.")
                else:
                    print("Ingrese un código válido (números).")

            except ValueError:
                print("Ingrese un valor válido.")

        if total > 3000:
            descuento = total * 0.25
            total_con_descuento = total - descuento
            print(f"\nDescuento aplicado: ${descuento:.2f}")
            print(f"Total a pagar con descuento: ${total_con_descuento:.2f}")
        else:
            print(f"\nTotal a pagar: ${total:.2f}")

        if total > 0:
            print(f"\nTipo de producto adquirido: {departamento}")

    def menu(self):
        while True:
            print("\nMenú:")
            print("1. Dama")
            print("2. Caballero")
            print("3. Niño")
            print("4. Niña")
            print("5. Bebé")
            print("S. Salir")

            opcion_departamento = input("Seleccione un departamento (1-5) o S para salir: ")

            if opcion_departamento.upper() == "S":
                break

            if opcion_departamento in ["1", "2", "3", "4", "5"]:
                departamento = list(self.inventario.keys())[int(opcion_departamento) - 1]
                self.mostrar_opciones_ropa(departamento)
                self.procesar_compra(departamento)
            else:
            
                print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    punto_de_venta = PuntoDeVenta()
    punto_de_venta.mostrar_presentacion()
    punto_de_venta.menu()