import web
from ..models.modelo_productos import ModeloProductos

PRODUCTO = ModeloProductos()
render = web.template.render('mvc/views/', base='layout')
class ActualizarProductos:

    def GET(self, idProducto):
        """
            Función que se encarga de renderizar la vista de actualizar_productos recibiendo como parámetro
            el identificador del producto
        """
        try:
            producto = PRODUCTO.detalleProductos(idProducto)
            return render.actualizar_productos(producto)
        except Exception as error:
            print(f'Ocurrió un error {error} - 105 | Controlador')
            return "Ocurrió un error"

    def POST(self, idProducto):
        try:
            entrada = web.input()
            if entrada and idProducto == entrada.producto:
                producto =  {
                    "producto": entrada.producto,
                    "nombre":entrada.nombre_producto,
                    "descripcion":entrada.descripcion,
                    "precio":entrada.precio,
                    "existencia":entrada.existencia
                }
                resultado = PRODUCTO.actualizarProductos(producto)
            if resultado:
                web.seeother("/")
            else:
                return render.actualizar_productos(entrada.producto)
        except Exception as error:
            print(f'Ocurrió un error {error} - 105_2 | Controlador')
            return "Oucrrió un error"