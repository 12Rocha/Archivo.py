# Abrir el archivo en modo de escritura ('w')
archivo = open('mi_archivo.txt', 'w')

# Escribir en el archivo
archivo.write('Hola, mundo!')

# Cerrar el archivo
archivo.close()

# Abrir el archivo en modo de lectura ('r')
archivo = open('mi_archivo.txt', 'r')

# Leer el contenido del archivo
contenido = archivo.read()

# Cerrar el archivo
archivo.close()

# Imprimir el contenido del archivo
print(contenido)
