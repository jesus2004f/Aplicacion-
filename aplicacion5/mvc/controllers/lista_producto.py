import web
from ..models.producto_model import ModeloProducto

PRODUCTO = ModeloProducto()
render = web.template.render('mvc/views', base='layout')

class ListaProducto:
    def GET(self):
        try:
            productos = PRODUCTO.listaProductos()
            return render.lista(productos)
        except Exception as error:
            print(f"Ocurrion un error {error} - 101 | Controlador")
            return "Ocurrio un error"
    
    def POST(self):
        try:
            entrada = web.input()
            producto_buscado = entrada.nombre
            if entrada and producto_buscado:
                respuesta = PRODUCTO.buscarProductos(producto_buscado)
            if respuesta:
                return render.lista_productos(respuesta)
            else:
                web.seeother("/")
        except Exception as error:
            print(f"Ocurrió un error {error} - 101_2 | Controlador")
            return "Ocurrió un error"