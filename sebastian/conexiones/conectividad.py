import pyodbc

def cadena_conexion(SERVER, DATABASE):
    return f'DRIVER={{ODBC Driver 17 for SQL SERVER}}; SERVER={SERVER};DATABASE={DATABASE};Trusted_connection=yes'


def conectar(SERVER, DATABASE):
    cadena = cadena_conexion(SERVER, DATABASE)

    try:
        conexion = pyodbc.connect(cadena)
        print("LA CONEXION A LA BASE DE DATOS FUE REALIZADA EXITOSMENTE")
        return conexion
    except pyodbc.Error as error:
        print(f'error panita: {error}')
        return None
    
def cerrar_conexion(conexion):
    if conexion:
        conexion.close()
        print('conexion cerrada con exito')