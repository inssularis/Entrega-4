class productosmain:

    # Se crea la lista de productos
    def __init__(self):
        self.productos = []

    # Función para crear un nuevo producto
    def CrearNuevoProducto(self, id_producto, nombre, descripcion, precio, cantidad):
        if any(prod["Id"] == id_producto for prod in self.productos):  # Para evitar repetir el ID
            return "Error: El ID ya existe."

        producto = {
            "Id": id_producto,
            "Nombre": nombre,
            "Descripcion": descripcion,
            "Precio": precio,
            "Cantidad": cantidad
        }
        self.productos.append(producto)
        return "Producto creado con éxito."

    # Función para traer los productos creados
    def GetProductos(self):
        if not self.productos:
            return "Producto no encontrado."
        return self.productos

    # Función para modificar un producto
    def ModificarProducto(self, id_producto, nombre=None, descripcion=None, precio=None, cantidad=None):
        for producto in self.productos:
            if producto["Id"] == id_producto:  # Cambié "id" por "Id"
                if nombre:
                    producto["Nombre"] = nombre
                if descripcion:
                    producto["Descripcion"] = descripcion
                if precio is not None:
                    producto["Precio"] = precio
                if cantidad is not None:
                    producto["Cantidad"] = cantidad
                return "Producto modificado con éxito."
        return "Error: Producto no encontrado."  # Ajusté el mensaje para que coincida.

    # Función para eliminar un producto
    def EliminarProducto(self, id_producto):
        for producto in self.productos:
            if producto["Id"] == id_producto:
                self.productos.remove(producto)
                return "Producto eliminado con éxito."
        return "Error: Producto no encontrado."
