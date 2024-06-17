class Diagnostico:
    def __init__(self,nro="",diagnostico=""):
        self.nro = nro
        self.diagnostico = diagnostico
    
    def __repr__(self):
        return f"Numero diagnostico {self.nro}, el diagnostico es {self.diagnostico}"
    
    def setDiagnostico(self,diagNew):
        self.diagnostico = diagNew

    def eliminarDiagnostico(self):
        self.nro = ""
        self.diagnostico = ""
    