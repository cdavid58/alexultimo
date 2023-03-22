import sqlite3
list_category = [
	'Accesorios para Vehículos','Agro','Alimentos y Bebidas','Licores','Regalos','Animales y Mascotas','Antigüedades y Colecciones','Arte, Papelería y Mercería','Bebés',
'Belleza y Cuidado Personal','Celulares y Teléfonos','Computación','Consolas y Videojuegos','Construcción','Deportes y Fitness','Electrodomésticos','Electrónica, Audio y Video',
'Herramientas','Hogar y Muebles','Industrias y Oficinas','Inmuebles','Instrumentos Musicales','Juegos y Juguetes','Recuerdos, Piñatería y Fiestas','Ropa y Accesorios','Salud y Equipamiento Médico',
'Servicios','Otras categorías'
]

conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()
for i in list_category:
	sql = ("INSERT INTO inventory_categories(name)values(?)")
	args = (i)
	cursor.execute(sql,[args])
conn.commit()

