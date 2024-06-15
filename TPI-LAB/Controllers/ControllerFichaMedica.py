from Models.FichasMedicas import FichaMedica
from Views.VistaFichaMedica import VistaFichaMedica
class ControllerFichaMedica:
    def __init__(self):
        self.vista = VistaFichaMedica()
        self.model = FichaMedica()
        self.listaFichasMedicas = []
    def set_listas(self,mascotas,diagnosticos,tratamientos,vacunas,veterinarios):
        self.listaMascotas = mascotas
        self.listaDiagnosticos = diagnosticos
        self.listaTratamientos = tratamientos
        self.listaVacunas = vacunas
        self.listaVeterianarios = veterinarios
    
    def buscarObj(self,codigo,arg):
        if arg == 1:
            for i in self.listaVeterianarios:
                if i.codigo == codigo:
                    return i #veterinario
        elif arg == 2:
            for i in self.listaDiagnosticos:
                if i.nro == codigo:
                    return i #diagnostico
        elif arg == 3:
            for i in self.listaTratamientos:
                if i.codigo == codigo:
                    return i #tratamiento
        elif arg ==4:
            for i in self.listaVacunas:
                if i.codigo == codigo:
                    return i #vacunas
        elif arg == 5:
            for i in self.listaMascotas:
                if i.codigo == codigo:
                    return i #mascota

    def cargarLista(self):
        with open("fichasMedicas.txt") as archivo:
            lineas = archivo.readlines()
        for i in lineas:
            codigo,fecha,veterinario,diagnostico,tratamiento,vacunas,mascota = i.strip().split(",")
            veterinarioObj = self.buscarObj(int(veterinario),1)
            diagnosticoObj = self.buscarObj(int(diagnostico),2)
            tratamientoObj= self.buscarObj(tratamiento,3)
            vacunasObj= self.buscarObj(int(vacunas),4)
            mascotaObj= self.buscarObj(int(mascota),5)
            self.listaFichasMedicas.append(FichaMedica(codigo,fecha,veterinarioObj,diagnosticoObj,tratamientoObj,vacunasObj,mascotaObj))