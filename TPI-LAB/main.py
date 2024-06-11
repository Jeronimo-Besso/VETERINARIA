from Controllers.ControllerRazas import ControllerRazas
from Controllers.ControllerPropietarios import ControllerPropietarios
from Controllers.ControllerVeterianarios import ControllerVeterinarios
from Controllers.ControllerMascotas import ControllerMascotas

if __name__== "__main__":
    controladorRazas = ControllerRazas()
    controladorRazas.cargarLista()
    controladorPropietarios = ControllerPropietarios()
    controladorPropietarios.cargarLista()
    controladorVeterinarios = ControllerVeterinarios()
    controladorVeterinarios.cargarLista()
    controladorMascotas = ControllerMascotas()
    controladorMascotas.setListaRazas(controladorRazas.getListaRaza())
    controladorMascotas.setListaPropietarios(controladorPropietarios.getListaProp())
    controladorMascotas.cargarLista()
    #controladorRazas.crearRaza()
    #controladorRazas.modificarRaza()
    #controladorRazas.eliminarRaza()
    #controladorVeterinarios.cargarLista()
    #controladorPropietarios.crearPropietario()
    #controladorPropietarios.modificarPropietario()
    #controladorPropietarios.eliminarPropietario()
    #controladorVeterinarios.crearVeterinario()
    #controladorVeterinarios.modificarVeterinario()
    #controladorVeterinarios.eliminarVeterinario()
    #controladorMascotas.nuevaMascota()
    #controladorMascotas.modificarMascota()
    #controladorMascotas.eliminarMascota()