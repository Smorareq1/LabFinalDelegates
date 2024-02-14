class Producto:
    def __init__(self, nombre, precio, categoria, descripcion, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        self.descripcion = descripcion
        self.cantidad = cantidad

    def __str__(self):
        return (f'Producto: {self.nombre}, Precio: {self.precio}, Categoria: {self.categoria}, '
                f'Descripcion: {self.descripcion}, Cantidad: {self.cantidad}')


class Main:
    listaProductos = []

    def agregarProductoALista(self):
        nombre = input('Nombre del producto: ')
        precio = input('Precio del producto: ')
        categoria = input('Categoria del producto: ')
        descripcion = input('Descripcion del producto: ')
        cantidad = input('Cantidad del producto: ')
        producto = Producto(nombre, precio, categoria, descripcion, cantidad)
        self.listaProductos.append(producto)

    def agregarProducto(self):
        self.agregarProductoALista()

    def imprimirProductos(self):
        for producto in self.listaProductos:
            print(producto)


if __name__ == "__main__":
    # Crear una instancia de Main
    main_instance = Main()
    # Llamar al método para agregar un producto
    main_instance.agregarProducto()
    # Llamar al método para imprimir los productos
    main_instance.imprimirProductos()
