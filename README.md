# Reto-Tecnico-Sofka

Este reto consiste en crear un juego tipo "¿Quién quiere ser millonario?" con el fin de evaluar las habilidades en POO (Programación orientada a objetos) y en un lenguaje de programación especifico, el cual para este proyecto es Python. El Reto es propuesto por la empresa Sofka Technologies.
Para correr este juego se debe tener en cuenta que en el Python se deben tener instalados los softwares python y git. Adicionalmente las librerías "csv" y "random" para el correcto funcionamiento.
Adicionalmente se debe configurar en las variables del sistema la ruta donde se encuentra el intérprete de Python, ya que esto nos permitirá correr el juego desde la consola de PowerShell de Windows.

Para correr el juego se debe: 
1. Abrir una ventana de PowerShell.
2. Cambiar de directorio en el PowerShell por uno en donde se quiera guardar el proyecto.
3. Una vez el la ventana de PowerShell se encuantre direccionado a dicha ruta se ejecuta el comando: git init
4. Ejecutar el comando: git romote add origin "https://github.com/ederperez95/Reto-Tecnico-Sofka.git"
5. Ejecutar el comando: git pull origin main
6. Ejecutar la instrucción: clear
7. Ejecutar la instrucción "py main.py" o "python main.py"
8. Disfrutar de un juego bastante retador.

Nota: Todos los archivos descargados del repositorio deben permanecer en la misma carpeta

Para la persistencia de datos del reto se usó archivos de texto plano.
Dentro de los archivos de texto plano adjuntos separados por ";" se tiene lo siguiente:
1. El archivo llamado jugadores.txt almacena los jugadores con la siguiente estructura de las columnas: nombre; premio; categoría; juegos ganados 
2. El archivo preguntas.txt contiene las preguntas del reto, las columnas de dicho archivo son como sigue: categoría de la pregunta; pregunta; opción 1; opción 2; opción 3; opción 4; respuesta
