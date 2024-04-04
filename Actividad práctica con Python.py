import matplotlib.pyplot as plt
import pymongo

# Conexión a MongoDB
conexion = pymongo.MongoClient('mongodb+srv://franciscofernandezfenoy:45871200@cluster0.zctgzx7.mongodb.net/')
base_de_datos = conexion['Practica1']
tabla = base_de_datos['clientes']

# Obtener los datos
datos = list(tabla.find())

print(datos)

# Procesar los datos para el gráfico
nombres = [dato['nombre'] for dato in datos]
facturaciones = [dato['facturacion'] for dato in datos]

# Calcular el total de facturación
total_facturacion = sum(facturaciones)

# Calcular los porcentajes de facturación
porcentajes = [facturacion / total_facturacion * 100 for facturacion in facturaciones]

# Crear el gráfico circular
plt.figure(figsize=(8, 8))
plt.pie(porcentajes, labels=nombres, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Para asegurar que el gráfico es un círculo
plt.title('Distribución de Facturación de Clientes')
plt.show()