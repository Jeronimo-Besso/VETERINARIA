class VistaMenu:
    def accion(self):
        pregunta = int(input("Que desea editar:\n1)Razas\n2)Vacunas\n3)Veterinarios\n4)Diagnosticos\n5)Propietarios\n6)Mascotas\n7)Tratamientos\n8)Consultas\n9)Fichas Medicas\n10)Ver cantidad de mascotas por propietarios\n11)Ver consultas por mascota\n12)Ver cantidad de tratamientos\n0)Cerrar APP\nINSERTE AQUI:"))
        return pregunta 
    def pregunta(self,arg):
        if arg ==1:
            valor = int(input("1)CREAR RAZA\n2)MODIFICAR RAZA\n3)ELIMINAR RAZA\n4)VER LISTA\nINSERTE AQUI:"))
        elif arg ==2:
            valor = int(input("1)CREAR VACUNA\n2)MODIFICAR VACUNA\n3)ELIMINAR VACUNA\n4)VER LISTA\nINSERTE AQUI:"))
        elif arg ==3:
            valor = int(input("1)CREAR VETERINARIO\n2)MODIFICAR VETERINARIO\n3)ELIMINAR VETERINARIO\n4)VER LISTA\nINSERTE AQUI:"))
        elif arg ==4:
            valor = int(input("1)CREAR DIAGNOSTICO\n2)MODIFICAR DIAGNOSTICO\n3)ELIMINAR DIAGNOSTICO\n4)VER LISTA\nINSERTE AQUI:"))
        elif arg ==5:
            valor = int(input("1)CREAR PROPIETARIO\n2)MODIFICAR PROPIETARIO\n3)ELIMINAR PROPIETARIO\n4)VER LISTA\nINSERTE AQUI:"))
        elif arg ==6:
            valor = int(input("1)CREAR MASCOTA\n2)MODIFICAR MASCOTA\n3)ELIMINAR MASCOTA\n4)VER LISTA\nINSERTE AQUI:"))
        elif arg ==7:
            valor = int(input("1)CREAR TRATAMIENTOS\n2)MODIFICAR TRATAMIENTOS\n3)ELIMINAR TRATAMIENTOS\n4)VER LISTA\nINSERTE AQUI:"))
        elif arg ==8:
            valor = int(input("1)CREAR CONSULTAS\n4)VER LISTA\nINSERTE AQUI:"))
        elif arg ==9:
            valor = int(input("1)GENERAR FICHAS MEDICAS\n4)VER LISTA\nINSERTE AQUI:"))
        else:
            print("Numero desconocido!")


        return valor
    def aviso(self,codigo):
        if codigo == 1:
            print("Numero inexistente")
    def verLista(self,lista):
        for i in lista:
            print(i)