from Controllers.ControllerRazas import ControllerRazas
from Controllers.ControllerPropietarios import ControllerPropietarios
from Controllers.ControllerVeterinarios import ControllerVeterinarios
from Controllers.ControllerMascotas import ControllerMascotas
from Controllers.ControllerDiagnostico import ControllerDiagnostico
from Controllers.ControllerTratamientos import ControllerTratamiento
from Controllers.ControllerVacunas import ControllerVacunas
from Controllers.ControllerConsultas import ControllerConsultas
from Controllers.ControllerFichasMedicas import ControllerFichasMedicas
from Controllers.ControllerMenu import ControllerMenu

def menu():
    controladorMenu = ControllerMenu(controladorRazas,controladorVacunas,controladorVeterinarios,controladorDiagnostico,controladorPropietarios,controladorMascotas,controladorTratamientos,controladorConsultas,controladorFichasMedicas)
    try:
        controladorMenu.opciones()
    except ValueError:
        print("Valor incorrecto")


if __name__== "__main__":
    controladorPropietarios = ControllerPropietarios()
    controladorPropietarios.cargarLista()
    controladorVeterinarios = ControllerVeterinarios()
    controladorVeterinarios.cargarLista()
    controladorRazas = ControllerRazas()
    controladorRazas.cargarLista()
    controladorMascotas = ControllerMascotas()
    controladorMascotas.setListas(controladorPropietarios,controladorRazas,controladorPropietarios.getListaProp(),controladorRazas.getListaRaza())
    controladorMascotas.cargarLista()
    controladorDiagnostico = ControllerDiagnostico()
    controladorDiagnostico.cargarLista()
    controladorTratamientos = ControllerTratamiento()
    controladorTratamientos.cargarTratamientos()
    controladorVacunas = ControllerVacunas()
    controladorVacunas.cargarVacunas()
    controladorConsultas = ControllerConsultas(controladorVeterinarios,controladorDiagnostico,controladorTratamientos,controladorVacunas,controladorMascotas)
    controladorConsultas.set_listas(controladorMascotas.getListaMascotas(),controladorDiagnostico.get_listaDiagnosticos(),controladorTratamientos.getListaTratamientos(),controladorVacunas.getListaVacunas(),controladorVeterinarios.getListaVeterinarios())
    controladorConsultas.cargarLista()
    controladorFichasMedicas = ControllerFichasMedicas()
    controladorFichasMedicas.cargarListas(controladorMascotas.getListaMascotas(),controladorConsultas.getLista())
    menu()





