from ingreso import Ingreso

class Menu():
    def opciones(self):
        ingreso=Ingreso()
        while True:
            print('''
                    1-Agregar
                    2-Listar
                    3-Consultar
                    4-Eliminar
                    0-Salir''')
            opcion=int(input('Elija: ')
            if opcion>=0 and opcion<=4:
                if opcion==1:
                    ingreso.agregar()
                elif opcion==2
                    ingreso.listar()
                elif opcion==3
                    ingreso.consulta()
                elif opcion==4
                    ingreso.eliminar()
                elif opcion==0
                    ingreso.salir()

principal=Menu()
principal.opciones()            

                