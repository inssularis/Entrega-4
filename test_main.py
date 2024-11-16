import unittest
from main import productosmain

class testProductos(unittest.TestCase):

    def setUp(self):
        self.pm = productosmain()

    def test_crear_producto_exitoso(self):
        resultado = self.pm.CrearNuevoProducto(1, "Producto A", "Descripción A", 100.0, 10)
        self.assertEqual(resultado, "Producto creado con éxito.")
        self.assertEqual(len(self.pm.productos), 1)  # Cambié a self.pm.productos
        self.assertEqual(self.pm.productos[0]["Nombre"], "Producto A")

    def test_crear_producto_id_duplicado(self):
        self.pm.CrearNuevoProducto(1, "Producto A", "Descripción A", 100.0, 10)
        resultado = self.pm.CrearNuevoProducto(1, "Producto B", "Descripción B", 200.0, 5)
        self.assertEqual(resultado, "Error: El ID ya existe.")

    def test_consultar_productos(self):
        self.pm.CrearNuevoProducto(1, "Producto A", "Descripción A", 100.0, 10)
        productos = self.pm.GetProductos()
        self.assertEqual(len(productos), 1)
        self.assertEqual(productos[0]["Nombre"], "Producto A")
    
    def test_modificar_producto_exitoso(self):
        self.pm.CrearNuevoProducto(1, "Producto A", "Descripción A", 100.0, 10)
        resultado = self.pm.ModificarProducto(1, nombre="Producto A Modificado", precio=150.0)
        self.assertEqual(resultado, "Producto modificado con éxito.")
        producto = self.pm.GetProductos()[0]
        self.assertEqual(producto["Nombre"], "Producto A Modificado")
        self.assertEqual(producto["Precio"], 150.0)

    def test_modificar_producto_no_encontrado(self):
        resultado =  self.pm.ModificarProducto(99, nombre="Inexistente")
        self.assertEqual(resultado, "Error: Producto no encontrado.")

    def test_eliminar_producto_exitoso(self):
        self.pm.CrearNuevoProducto(1, "Producto A", "Descripción A", 100.0, 10)
        resultado = self.pm.EliminarProducto(1)
        self.assertEqual(resultado, "Producto eliminado con éxito.")
        self.assertEqual(len(self.pm.productos), 0)

    def test_eliminar_producto_no_encontrado(self):
        resultado = self.pm.EliminarProducto(99)
        self.assertEqual(resultado, "Error: Producto no encontrado.")

if __name__ == "__main__":
    unittest.main()
