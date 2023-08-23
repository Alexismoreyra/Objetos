from Usuario import Usuario

listaUsuario = []

class Ingreso():
    def agregar (self):
        prit('registro de usuario')
        dni=input('dni: ')
        nombre=input('nombre: ')
        apellido=input('apellido: ')
        deposito=int(input('deposito: '))
        retiro=int(input('retiro: '))
        objeto=Usuario(dni,nombre,apellido,deposito,retiro)
        listaUsuario.append(objeto)

    def listar(self):
        print('lista de usuario')
        for objeto in listaUsuario:
            objeto.imprimir()

    def consulta(self):
        dni=input('dni: ')
        for lista in listaUsuario:
            if dni==lista.dni:
                lista.imprimir()

    def eliminar (self)
        dni=input('dni: ')
        for lista in listaUsuario:
            if dni==lista.dni:
                listaUsuario.remove(object)