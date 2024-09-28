# Crear un diccionario con información personal ficticia
informacion_personal = {
    "nombre": "Ronaldo Grefa",
    "edad": 25,
    "ciudad": "Madrid",
    "profesion": "Ingeniero"
}

# Acceder al valor asociado con la clave "ciudad" y modificarlo
informacion_personal["ciudad"] = "Barcelona"

# Agregar una nueva clave-valor que represente la "profesion" de la persona
informacion_personal["profesion"] = "Desarrollador de Software"

# Verificar si la clave "telefono" existe en el diccionario
if "telefono" not in informacion_personal:
    # Si no existe, agregarla con un número de teléfono ficticio
    informacion_personal["telefono"] = "098-831-5372"

# Eliminar la clave "edad" del diccionario
if "edad" in informacion_personal:
    del informacion_personal["edad"]

# Imprimir el diccionario final
print(informacion_personal)