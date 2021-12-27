import mysql.connector
from mysql import Error 

class DAO():

    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host = 'localhost',
                port = 3306,
                user = 'root',
                password = '123456',
                db = 'jugadores'

            )
        except Error as ex:
            print("Error al intentar la conexion: {0}".format(ex))

    def listarUsusarios(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM jugadores by puntaje DSC")
                resultados = cursor.fetchall()
                return resultados
            except Error as ex:
                print("Error al intentar la conexion: {0}".format(ex))