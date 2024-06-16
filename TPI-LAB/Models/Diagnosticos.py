class Diagnostico:
    def __init__(self,nro="",diagnostico=""):
        self.nro = nro
        self.diagnostico = diagnostico
    
    def __repr__(self):
        return f"{self.nro}"
    
    def setDiagnostico(self,diagNew):
        self.diagnostico = diagNew

    def eliminarDiagnostico(self):
        self.nro = ""
        self.diagnostico = ""