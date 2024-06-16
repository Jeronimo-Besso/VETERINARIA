from Views.VistaMenu import VistaMenu





class ControllerMenu:    
    def __init__(self,cont1,cont2,cont3,cont4,cont5,cont6,cont7,cont8,cont9):
        self.cont1 = cont1 
        self.cont2 = cont2 
        self.cont3 = cont3 
        self.cont4 = cont4 
        self.cont5 = cont5 
        self.cont6 = cont6 
        self.cont7 = cont7 
        self.cont8 = cont8 
        self.cont9 = cont9 
        self.vista = VistaMenu()   
    def opciones(self):
        pregunta = self.vista.accion()
        while pregunta != 0:
            if pregunta ==1:
                valor = self.vista.pregunta(1)
                if valor ==1:
                    self.cont1.crearRaza()
                elif valor ==2:
                    self.cont1.modificarRaza()
                elif valor ==3:
                    self.cont1.eliminarRaza()
                elif valor ==4:
                    self.cont1.verLista()
                else:
                    self.vista.aviso(1)
            
            
            elif pregunta ==2:
                valor = self.vista.pregunta(2)
                if valor ==1:
                    self.cont2.nuevaVacuna()
                elif valor ==2:
                    self.cont2.modificarVacuna()
                elif valor ==3:
                    self.cont2.eliminarVacuna()
                elif valor ==4:
                    self.cont2.verLista()
                else:
                    self.vista.aviso(1)

        
        
            elif pregunta ==3:
                valor = self.vista.pregunta(3)
                if valor ==1:
                    self.cont3.crearVeterinario()
                elif valor ==2:
                    self.cont3.modificarVeterinario()
                elif valor ==3:
                    self.cont3.eliminarVeterinario()
                elif valor ==4:
                    self.cont3.verLista()
                else:
                    self.vista.aviso(1)
            
            elif pregunta ==4:
                valor = self.vista.pregunta(4)
                if valor ==1:
                    self.cont4.crearDiagnostico()
                elif valor ==2:
                    self.cont4.modificarDiagnostico()
                elif valor ==3:
                    self.cont4.eliminarDiagnostico()
                elif valor ==4:
                    self.cont4.verLista()
                else:
                    self.vista.aviso(1)
        
            elif pregunta ==5:
                valor = self.vista.pregunta(5)
                if valor ==1:
                    self.cont5.crearPropietario()
                elif valor ==2:
                    self.cont5.modificarPropietario()
                elif valor ==3:
                    self.cont5.eliminarPropietario()
                elif valor ==4:
                    self.cont5.verLista()
                else:
                    self.vista.aviso(1)
            
            
            elif pregunta ==6:
                valor = self.vista.pregunta(6)
                if valor ==1:
                    self.cont6.nuevaMascota()
                elif valor ==2:
                    self.cont6.modificarMascota()
                elif valor ==3:
                    self.cont6.eliminarMascota()
                elif valor ==4:
                    self.cont6.verLista()
                else:
                    self.vista.aviso(1)
            
            elif pregunta ==7:
                valor = self.vista.pregunta(7)
                if valor ==1:
                    self.cont7.nuevoTratamiento()
                elif valor ==2:
                    self.cont7.modificarTratamientos()
                elif valor ==3:
                    self.cont7.eliminarTramiento()
                elif valor ==4:
                    self.cont7.verLista()
                else:
                    self.vista.aviso(1)
            
            
            elif pregunta ==8:
                valor = self.vista.pregunta(8)
                if valor ==1:
                    self.cont8.crearConsulta()
                elif valor ==4:
                    self.cont8.verLista()
                else:
                    self.vista.aviso(1)
            
            elif pregunta ==9:
                valor = self.vista.pregunta(9)
                if valor ==1:
                    self.cont9.crearFichas()
                elif valor ==4:
                    self.cont9.verLista()
            elif pregunta==10:
                valor = self.vista.pregunta(10)
                if valor == 10:
                    self.cont6.contarCant()
            elif pregunta == 11:
                valor = self.vista.pregunta(11)
                if valor ==11:
                    self.cont8.cantConsultasXMascotas()
            elif pregunta == 12:
                    valor = self.vista.pregunta(12)
                    if valor ==12:
                        self.cont7.cantidadTratamientos()
            pregunta = self.vista.accion()
            self.cargarTodo()
    def cargarTodo(self):   
        self.cont1.cargarDatos()
        self.cont2.cargarDatos()
        self.cont3.cargarDatos()
        self.cont4.cargarDatos()
        self.cont5.cargarDatos()
        self.cont6.cargarDatos()
        self.cont7.cargarDatos()
        self.cont8.cargarDatos()
        self.cont9.cargarDatos()