from Controllers.ControllerRazas import ControllerRazas
from Controllers.ControllerPropietarios import ControllerPropietarios
from Controllers.ControllerVeterianarios import ControllerVeterinarios
from Controllers.ControllerMascotas import ControllerMascotas
from Controllers.ControllerDiagnostico import ControllerDiagnostico
from Controllers.ControllerTratamientos import ControllerTratamiento
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
    controladorMascotas.setListaRazas(controladorRazas.getListaRaza())
    controladorMascotas.setListaPropietarios(controladorPropietarios.getListaProp())
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
    #######################################################################################



    