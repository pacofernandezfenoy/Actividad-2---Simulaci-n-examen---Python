import pandas as pd
import matplotlib.pyplot as plt
import pymongo

# Conexión a MongoDB
conexion = pymongo.MongoClient('mongodb+srv://franciscofernandezfenoy:45871200@cluster0.zctgzx7.mongodb.net/')
base_de_datos = conexion['Practica1']
tabla = base_de_datos['clientes']

# Obtener los datos y cargarlos en un DataFrame
datos = pd.DataFrame(list(tabla.find()))

# Procesar los datos para el gráfico
total_facturacion = datos['facturacion'].sum()
datos['porcentaje'] = datos['facturacion'] / total_facturacion * 100

# Crear el gráfico circular
plt.figure(figsize=(8, 8))
plt.pie(datos['porcentaje'], labels=datos['nombre'], autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Para asegurar que el gráfico es un círculo
plt.title('Distribución de Facturación de Clientes')
plt.show()
