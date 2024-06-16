from Models.Consultas import Consultas
from Views.VistaConsultas import VistaConsultas
class ControllerConsultas:
    def __init__(self,controladorVeterinario,controladorDiagnosticos,controladorTratamientos,controladorVacunas,controladorMascotas):
        self.vista = VistaConsultas()
        self.model = Consultas()
        self.controladorVeterinario = controladorVeterinario
        self.controladorDiagnosticos = controladorDiagnosticos
        self.controladorTratamientos = controladorTratamientos
        self.controladorVacunas = controladorVacunas
        self.controladorMascotas = controladorMascotas
        self.listaConsultas = []
    def set_listas(self,mascotas,diagnosticos,tratamientos,vacunas,veterinarios):
        self.listaMascotas = mascotas
        self.listaDiagnosticos = diagnosticos
        self.listaTratamientos = tratamientos
        self.listaVacunas = vacunas
        self.listaVeterianarios = veterinarios   
    def getLista(self):
        return self.listaConsultas
    def buscarObj(self,codigo,arg):
        if arg == 1:
            a = 0
            for i in self.listaVeterianarios:
                if i.codigo == codigo:
                    a=1
                    return i #veterinario
            if a == 0:
                print("No se encontro Vet")
                codigo = self.controladorVeterinario.crearVeterinario()
                for i in self.listaVeterianarios:
                    if i.codigo == codigo:
                        return i
        elif arg == 2:
            b = 0
            for i in self.listaDiagnosticos:
                if i.nro == codigo:
                    b=1
                    return i #diagnostico
            if b==0:
                print("No se encontro DIAG")
                nro = self.controladorDiagnosticos.crearDiagnostico()
                for i in self.listaDiagnosticos:
                    if i.nro == nro:
                        return i
        elif arg == 3:
            c = 0
            for i in self.listaTratamientos:
                if i.codigo == codigo:
                    c=1
                    return i #tratamiento
            if c==0:
                print("No se encontro TRAT")
                codigo = self.controladorTratamientos.nuevoTratamiento()
                for i in self.listaTratamientos:
                    if i.codigo == codigo:
                        return i
        elif arg ==4:
            d =0
            for i in self.listaVacunas:
                if i.codigo == codigo:
                    d=1
                    return i #vacunas
            if d==0:
                print("No se encontro VAC")
                codigo = self.controladorVacunas.nuevaVacuna()
                for i in self.listaVacunas:
                    if i.codigo == codigo:
                        return i
        elif arg == 5:
            e=0
            for i in self.listaMascotas:
                if i.codigo == codigo:
                    e=1
                    return i #mascota
            if e==0:
                print("No se encontro MAS")
                codigo = self.controladorMascotas.nuevaMascota()
                for i in self.listaMascotas:
                    if i.codigo == codigo:
                        return i
    
    def cargarLista(self):
        with open("consultas.txt") as archivo:
            lineas = archivo.readlines()
        for i in lineas:
            codigo,fecha,veterinario,diagnostico,tratamiento,vacunas,mascota = i.strip().split(",")
            veterinarioObj = self.buscarObj(int(veterinario),1)
            diagnosticoObj = self.buscarObj(int(diagnostico),2)
            tratamientoObj= self.buscarObj(tratamiento,3)
            vacunasObj= self.buscarObj(int(vacunas),4)
            mascotaObj= self.buscarObj(int(mascota),5)
            self.listaConsultas.append(Consultas(codigo,fecha,veterinarioObj,diagnosticoObj,tratamientoObj,vacunasObj,mascotaObj))
    
    def crearConsulta(self):
        x=0
        o = 0
        codigo = self.vista.crearConsulta(1)
        fecha= self.vista.crearConsulta(2)
        veterinario= self.vista.crearConsulta(3)
        veterinarioObj = self.buscarObj(int(veterinario),1)
        if veterinarioObj != "":
            diagnostico= self.vista.crearConsulta(4)
            diagnosticoObj = self.buscarObj(int(diagnostico),2)
            if diagnosticoObj != "":
                tratamiento= self.vista.crearConsulta(5) 
                tratamientoObj= self.buscarObj(tratamiento,3)
                if tratamientoObj != "":
                    vacunas= self.vista.crearConsulta(6)
                    vacunasObj= self.buscarObj(int(vacunas),4)
                    if vacunasObj != "":
                        mascota = self.vista.crearConsulta(7)
                        mascotaObj= self.buscarObj(int(mascota),5)
                        o = 1
        if o ==1 :
            for i in self.listaConsultas:
                if i.codigo == codigo:
                    x = 1
                    self.aviso(5) #no se puede2
            if x == 0:
                self.listaConsultas.append(Consultas(codigo,fecha,veterinarioObj,diagnosticoObj,tratamientoObj,vacunasObj,mascotaObj))
   
    def verLista(self):
        self.vista.verLista(self.listaDiagnosticos)

    def cantConsultasXMascotas(self):
        listaCantConsultas = []
        for i in self.listaMascotas:
            sum = 0
            for j in self.listaConsultas:
                if i.codigo == j.mascota.codigo:
                    sum = sum + 1
            listaCantConsultas.append((i.nombre,sum))
        self.vista.verLista(listaCantConsultas)

    def cargarDatos(self):
        with open("consultas.txt","w") as archivo:
            for i in self.listaConsultas:
                linea = f"{i.codigo},{i.fecha},{i.veterinario},{i.diagnostico},{i.tratamiento},{i.vacunas},{i.mascota}\n"
                archivo.write(linea)
























