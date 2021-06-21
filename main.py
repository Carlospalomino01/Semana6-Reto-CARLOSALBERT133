"""
Reto Semana 6
Nombre: carlos palomino
Fecha: 19/06/2021
"""

from datetime import datetime
import pytz
import funciones as fe

def fecha_actual():
  tz = pytz.timezone('America/Bogota')
  x = datetime.now(tz) 
  x = x.strftime("%Y-%m-%d %H:%M:%S")
  return x


fecha = fecha_actual()
f = open("./SupermercadoDonPepe.txt", "w")
f.write (fecha +"\n")
f.write("Supermercado don Pepe \n")
f.write("Nit: 124545454\n")
f.write("--------------------------\n")

f.close()
lista_inventario=[{
  "ide":"000",
  "nombre":"leche",
  "marca":"Alpina",
  "categoria":"lactios",
  "presio":3000
 },
 {
  "ide":"0001",
  "nombre":"queso",
  "marca":"Alpina",
  "categoria":"lactios",
  "presio":6500
}]


ide=fe.ingreso_productos(lista_inventario,fecha)
