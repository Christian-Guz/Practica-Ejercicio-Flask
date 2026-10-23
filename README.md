## Práctica: Creación de un sitio web multipágina con Flask y Bootstrap

# Proceso de inicio de proyecto

- Crear la carpeta del proyecto
- Crar y activar el entorno virtual
- Instalar la librería Flask
- Crar el archivo requirements.txt con las dependencias del proyecto
- Crar el archivo .gitignore con el entorno virtual y el mismo .gitignore dentro

# Proceso de carpeta Templates
- Crear la carpeta templates con los archivos html que contendrá la página web
- Crear archivo index.html con la información inicial del sitio web
- Crear archivo catalogo.html con la información de los diferentes catálogos de los libros
- Crear archivo servicios.html con la información de los diferentes servicios que ofrece la página
- Crear archivo contacto.html con la información de contactos que se ofrecen
- Crear archivo layout.html con la estructura de la página web, en donde se incluye el diseño de Bootstrap extraído de la página web y el menu de navegación

# Proceso de archivo server
- Crear archivo server.py con la estructura de la página web
- Dentro de esto se asignan las rutas del url asignadas a cada página web
- Se asignaron los archivos .html a las rutas correspondientes
- Se asignó un título a cada página web para el menu de navegación

# Ejecurción y prueba
- Se cambió el puerto de ejecución y se ejecutó el archivo server.py
- Se abrieron los archivos index.html, catalogos.html, servicios.html y contacto.html en el navegador con la barra de navegación correspondientes

# Creación del repositorio
- Se inició el repositorio con el comando git init en la terminal
- Se revisaron que el entorno virtual y el archivo .gitignore no se incluyan en el repositorio con el comando git status
- Se agregaron los archivos al repositorio con el comando git add .
- Se realizó un commit con el comando git commit -m ""
- Se creó el repositorio en github
- Se realizó un push con el comando git push