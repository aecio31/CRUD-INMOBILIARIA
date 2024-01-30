#!/usr/bin/env python
# coding: utf-8

# # CRUD 
# se trato de crear una base de clientes para un agente mobiliario, en el cual se incluia nombre, telefono, correo electronico, fecha de primer contacto

# In[6]:


import sqlite3
from tabulate import tabulate

# Conectar a la base de datos (o crearla si no existe)
conexion = sqlite3.connect('inmobiliaria1.db')
cursor = conexion.cursor()

# Crear una tabla si no existe
cursor.execute('''
    CREATE TABLE IF NOT EXISTS agentes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        telefono TEXT,
        correo TEXT,
        fecha_primer_contacto TEXT
    )
''')
conexion.commit()

# Operación de Crear (Create)
def crear_agente(nombre, telefono, correo, fecha_primer_contacto):
    cursor.execute('INSERT INTO agentes (nombre, telefono, correo, fecha_primer_contacto) VALUES (?, ?, ?, ?)',
                   (nombre, telefono, correo, fecha_primer_contacto))
    conexion.commit()

# Operación de Leer (Read)
def obtener_agentes():
    cursor.execute('SELECT * FROM agentes')
    return cursor.fetchall()

# Operación de Actualizar (Update)
def actualizar_agente(id, nombre, telefono, correo, fecha_primer_contacto):
    cursor.execute('''
        UPDATE agentes SET nombre=?, telefono=?, correo=?, fecha_primer_contacto=?
        WHERE id=?
    ''', (nombre, telefono, correo, fecha_primer_contacto, id))
    conexion.commit()

# Operación de Eliminar (Delete)
def eliminar_agente(id):
    cursor.execute('DELETE FROM agentes WHERE id=?', (id,))
    conexion.commit()

# Ejemplo de uso
crear_agente('John Doe', '123456789', 'john@example.com', '2020-01-30')
crear_agente('Jane Smith', '987654321', 'jane@example.com', '2020-01-25')

print("Agentes antes de la actualización:")
print(tabulate(obtener_agentes(), headers=['ID', 'Nombre', 'Teléfono', 'Correo', 'Fecha de Primer Contacto'], tablefmt='pretty'))

actualizar_agente(1, 'John Doe', '999999999', 'john@example.com', '2020-01-30')

print("\nAgentes después de la actualización:")
print(tabulate(obtener_agentes(), headers=['ID', 'Nombre', 'Teléfono', 'Correo', 'Fecha de Primer Contacto'], tablefmt='pretty'))

eliminar_agente(2)

print("\nAgentes después de la eliminación:")
print(tabulate(obtener_agentes(), headers=['ID', 'Nombre', 'Teléfono', 'Correo', 'Fecha de Primer Contacto'], tablefmt='pretty'))

# Cerrar la conexión a la base de datos al finalizar
conexion.close()


# In[ ]:




