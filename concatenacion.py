import numpy as np
import os
import threading
import logging
from PIL import Image
from archivos import leer_imagen, escribir_imagen
from contador import Contador

def concatenar_horizontal(imagenes):
  min_img_shape = sorted([(np.sum(i.size), i.size) for i in imagenes])[0][1]
  return np.hstack(list((np.asarray(i.resize(min_img_shape, Image.ANTIALIAS)) for i in imagenes)))

def concatenar_vertical(imagenes):
  min_img_shape = sorted([(np.sum(i.size), i.size) for i in imagenes])[0][1]
  return np.vstack(list((np.asarray(i.resize(min_img_shape, Image.ANTIALIAS)) for i in imagenes)))

rutas = os.listdir('./imagenes')
imagenes = []

print(rutas)

for img in rutas:
  imagenes.append(leer_imagen(img))


contador = Contador()
contador.iniciar()

# def procesar(lista, pos):
#   print(len(lista))
#   if len(lista) == 0 or len(lista) == 2:
#     escribir_imagen(f'vertical{pos}.jpg', concatenar_vertical([lista[0], lista[1]]))
#     return
#   else:
#       procesar(lista[2:], pos + 1)  

# procesar(imagenes, 1)


# for i in range(len(imagenes)):
#   escribir_imagen(f'vertical{i}.jpg', concatenar_vertical([imagenes[i], imagenes[i+1]]))

# contador.finalizar()
# contador.imprimir()

# for i in range(len(imagenes)):
#   thread = threading.Thread(target=escribir_imagen(str(i) + '.jpg', concatenar_vertical([imagenes[i], imagenes[i+1]])))
#   thread.start()
#   logging.info('Concatenando imagen...') 

# imagen1 = leer_imagen('1.jpg')
# imagen2 = leer_imagen('2.jpg')

# escribir_imagen('concatenada-vertical.jpg', concatenar_vertical([imagen1, imagen2]))    
# escribir_imagen('concatenada-horizontal.jpg', concatenar_horizontal([imagen1, imagen2]))    
