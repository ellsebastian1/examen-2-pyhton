from conexiones import conectividad,funciones
import os

SERVER = 'DESKTOP-HEMQVAQ'
DATABASE = 'Escuela'
TABLE = 'Asignaturas'

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def menu():
    conexion = conectividad.conectar(SERVER, DATABASE) 


    while True:
        print("_____MENU______")
        print("1- Registrar Asignatura")
        print("2- Leer Asignatura")
        print("3- Eliminar Asignatura")
        print("4- Actualizar Asignatura")
        print("5- Salir")
        respuesta = int(input("Ingrese la opcion: "))
        match respuesta:
            case 1:
                clear()
                id_clase=input("ingrese el codigo de la asignatura:")
                nombre=input("ingrese el nombre de la asignatura: ")
                credito=input("ingrese el credito de la asignatura: ")
                ID_curso=input("ingrese el codigo del curso: ")
                dicc = {
                    'AsignaturaID' : id_clase,
                    'Nombre' : nombre,
                    'Credito' : credito,
                    'CursoID' : ID_curso
                }
                respuesta = funciones.agrega(dicc,conexion)
                if respuesta:
                    print("Asignatura agregada correctamente")
            case 2:
                clear()
                resultado = funciones.leer_asignaturas(conexion)
                print("="*85)
                print("|"+"Asignatura".center(20)+"|"+"Nombre".center(20)+"|"+"Credito".center(20)+"|"+"Curso".center(20)+"|")
                for i in range(len(resultado)):
                    print("="*85)
                    print("|"+str(resultado[i][0]).center(20)+"|"+str(resultado[i][1]).center(20)+"|"+str(resultado[i][2]).center(20)+"|"+str(resultado[i][3]).center(20)+"|")
                print("="*85)

            case 3:
                clear()
                try:
                  id_clase = input("ingresa el id de la asignatura:  ")
                  resultado = funciones.eliminar(id_clase, conexion)

                  if(resultado):
                     print("asignatura eliminada con exito")
                except ValueError:
                    print("el id ingresado no existe")
                    input("")
                    return
            case 4:
                try: 
                    id_clase = input("Ingrese la id:")
                    clear()
                    funciones.actualizar(conexion,id_clase)
                except ValueError:
                    print("el id ingresado no existe pa intente de nuevo")
                    return
            case 5:
                print("Adios vuelva pronto")
                break



            
                

if __name__ == '__main__':
    menu()

                
                
            