import pyodbc

def agrega(asignaturas, conexion ):
   try:
      cursor= conexion.cursor()
      query = 'INSERT INTO Asignaturas VALUES(?,?,?,?)'
      cursor.execute(query, asignaturas['AsignaturaID'], asignaturas['Nombre'], asignaturas['Credito'], asignaturas['CursoID'])
      cursor.commit()
      cursor.close()
      return True
   except pyodbc.Error as error:
        print(f'Error al agregar la asignatura . Error: {error}')
        cursor.close()
        input('Presione Enter para continuar...')
        return None

def leer_asignaturas(conexion):
   try:
      cursor = conexion.cursor()
      query = 'SELECT * FROM Asignaturas'
      cursor.execute(query)
      imprimi = cursor.fetchall()
      return imprimi
   except pyodbc.Error as error:
        print(f'Error al leer la asignatura . Error: {error}')
        cursor.close()
        input('Presione Enter para continuar...')
        return None
    
def eliminar(id_clase,conexion):
   try:
       cursor = conexion.cursor()
       query = 'DELETE FROM Asignaturas WHERE AsignaturaID = ?'
       cursor.execute(query, id_clase)
       cursor.commit()
       cursor.close()
   except pyodbc.Error as error:
        print(f'Error al eliminar la asignatura. Error: {error}')
        cursor.close()
        input('Presione Enter para continuar...')
        return None

def actualizar(conexion, id_clase):
    try:
       print("seleccione el campo de la asignatura que desea actualizar")
       print("1- Actualizar Nombre de la Asignatura: ")
       print("2- Actualizar Creditos de la Asignatura: ")
       print("3- Actualizar ID del curso: ")
       print("4- No actualizar: ")
       r = int(input("ingrese una opcion: "))
       cursor = conexion.cursor()
       match r:
         case 1:
            nombre = input("ingresa el nuevo Nombre de la clase: ")
            query = 'UPDATE Asignaturas SET Nombre=? WHERE AsignaturaID=?'
            cursor.execute(query,nombre,id_clase)
         case 2:
            credito = input("ingresa el nuevo credito de la asignatura: ")
            query = 'UPDATE Asignaturas SET Creditos=? WHERE AsignaturaID=?'
            cursor.execute(query,credito,id_clase)
         case 3: 
            id_curso = input("ingresa el nuevo id del curso: ")
            query = 'UPDATE Asignaturas SET CursoID=? WHERE AsignaturaID=?'
            cursor.execute(query,id_curso,id_clase)
         case 4:
            print("decidiste no actualizar nada de asignatura presione enter para continuar")
            input("")
            return
    except ValueError:
       print("el id que ingreso no existe")
       return
    cursor.commit()
    cursor.close()
    return True
        
        
        

    



    





