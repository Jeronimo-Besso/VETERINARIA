from Controllers.ControllerRazas import ControllerRazas
from Controllers.ControllerPropietarios import ControllerPropietarios
from Controllers.ControllerVeterianarios import ControllerVeterinarios
from Controllers.ControllerMascotas import ControllerMascotas
from Controllers.ControllerDiagnostico import ControllerDiagnostico
from Controllers.ControllerTratamientos import ControllerTratamiento
from Controllers.ControllerVacunas import ControllerVacunas
from Controllers.ControllerFichaMedica import ControllerFichaMedica
if __name__== "__main__":
    #######################################################################################
    controladorRazas = ControllerRazas()
    controladorRazas.cargarLista()
    #controladorRazas.crearRaza()
    #controladorRazas.modificarRaza()
    #controladorRazas.eliminarRaza()
    #######################################################################################
    controladorPropietarios = ControllerPropietarios()
    controladorPropietarios.cargarLista()
    #controladorPropietarios.crearPropietario()
    #controladorPropietarios.modificarPropietario()
    #controladorPropietarios.eliminarPropietario()
    #######################################################################################
    controladorVeterinarios = ControllerVeterinarios()
    controladorVeterinarios.cargarLista()
    #controladorVeterinarios.crearVeterinario()
    #controladorVeterinarios.modificarVeterinario()
    #controladorVeterinarios.eliminarVeterinario()
    #######################################################################################
    controladorMascotas = ControllerMascotas()
    controladorMascotas.setListas(controladorPropietarios.getListaProp(),controladorRazas.getListaRaza())
    controladorMascotas.cargarLista()
    #controladorMascotas.nuevaMascota()
    #controladorMascotas.modificarMascota()
    #controladorMascotas.eliminarMascota()
    #######################################################################################
    controladorDiagnostico = ControllerDiagnostico()
    controladorDiagnostico.setListaMascotas(controladorMascotas.getListaMascotas())
    controladorDiagnostico.cargarLista()
    #controladorDiagnostico.eliminarDiagnostico()
    #controladorDiagnostico.crearDiagnostico()
    #controladorDiagnostico.modificarDiagnostico()
    #######################################################################################
    controladorTratamientos = ControllerTratamiento()
    controladorTratamientos.setListaMascotas(controladorMascotas.getListaMascotas())
    controladorTratamientos.cargarTratamientos()
    #controladorTratamientos.nuevoTratamiento()
    #controladorTratamientos.modificarTratamientos()
    #controladorTratamientos.eliminarTramiento()
    #######################################################################################
    controladorVacunas = ControllerVacunas()
    controladorVacunas.cargarVacunas()
    #controladorVacunas.nuevaVacuna()
    #controladorVacunas.modificarVacuna()
    #controladorVacunas.eliminarVacunas()
    #######################################################################################
    controladorFichasMedicas = ControllerFichaMedica()
    controladorFichasMedicas.set_listas(controladorMascotas.getListaMascotas(),controladorDiagnostico.get_listaDiagnosticos(),controladorTratamientos.getListaTratamientos(),controladorVacunas.getListaVacunas(),controladorVeterinarios.getListaVeterinarios())
    controladorFichasMedicas.cargarLista()

    