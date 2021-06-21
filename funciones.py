def ingreso_productos(lista_inventario,fecha):
  venta = 0
  
  ingreso_productos
  accion = "r"
  while accion == "r":
    if accion == "r":
      print("====================================")
      ide = input("Dijite es codigo del Producto:\n ")
      for i in lista_inventario:
        if i["ide"] == ide:
          print("***producto agregado con exito***")
          print("=================")
          posicion_lista = lista_inventario.index(i)
          
          price = lista_inventario[posicion_lista]["presio"]
          name = lista_inventario[posicion_lista]["nombre"]
                          
          f = open("./SupermercadoDonPepe.txt", "a")
          f.write(name+"---------------- $")
          f.write (str(price)+"\n")
          venta += price
          
          print("valor de la compra:---",venta)
    accion = input("Ingrese r para registrar s para salir :\n")
    #accion = accion.upper()
  f.write ("Sub Total:------------$"+str(venta)+"\n")
  iva = (19*venta)/100
  f.write ("IVA:------------------$"+str(iva)+"\n")
  total=venta+iva
  f.write ("Total a pagar:--------$"+str(total)+"\n")
  
  f.close()
  f = open("./SupermercadoDonPepe.txt", "r")
  r=f.read()
  print("____________________________")
  print("****************************")
  print(r)
  f.close()
  
  f2 = open("./SupermercadoDonPepe" + fecha + ".txt", "a")
  f2.write(r)
  f2.close()
  print("____________________________")
  print("****************************")
  
  

  
