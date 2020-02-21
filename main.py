import logging
import threading
from api import PixabayAPI

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

carpeta_imagenes = './imagenes'
query = 'gatos'
api = PixabayAPI('15310794-fd5276e7c177406541a95fec7', carpeta_imagenes)

logging.info(f'Buscando imagenes de {query}')

urls = api.buscar_imagenes(query, 12)

for u in urls:
  thread = threading.Thread(target = api.descargar_imagen, args = [u])
  thread.start()
  logging.info(f'Descargando imagen... {u}')
