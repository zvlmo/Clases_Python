import sqlite3
with sqlite3.connect("mi_base_datos.db") as conexion:
    try:
        #CREATE TABLE
        # sentencia = '''
        #             create table Empleados 
        #             (
        #                 id integer primary key autoincrement,
        #                 nombre text,
        #                 apellido text,
        #                 sueldo real
        #             )
        #             '''
        # sentencia = '''
        # alter table Empleados
        # add direccion text
        # '''
        # nombre = 'carlos'
        # apellido = 'balin'
        # sueldo = 23232
        # direccion = 'Peru 333'
        # sentencia = '''
        # insert into Empleados(nombre, apellido, sueldo, direccion) values(?,?,?,?)
        
        # '''
        # sentencia = '''
        # select nombre from Empleados order by sueldo desc limit 3
        # '''
        # cursor  = conexion.execute(sentencia)
        # for fila in cursor:
        #     print(fila)
        # id = 3
        # sueldo = 2
        # sentencia = '''
        # update Empleados set sueldo = ? where id = ?
        # '''
        sentence = '''
        delete from Empleados where sueldo < 500
        '''
        conexion.execute(sentence)
        print('Tabla creada con exito')
    except Exception as a:
        print("Error")
        print(a)        
        
#####################################################

'''
Insert into tabla([]) values(valores)
SELECT sum(sueldos)
FROM Empleados
[WHERE]
Order by asc/desc
limit 2
'''