from AdministradorDeTareas_UI import *

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow_):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        
        self.setupUi(self)
        self.procesos = []

        # Acciones de botones
        self.btn_01.clicked.connect(self.agregarProcesoA)
        self.btn_02.clicked.connect(self.agregarProcesoB)
        self.btn_03.clicked.connect(self.agregarProcesoC)
        self.btn_04.clicked.connect(self.agregarProcesoD)
        self.btn_Limpiar.clicked.connect(self.limpiarCola)

    def agregarProcesoA(self):
        self.colaProcesos.addItem("Proceso A")

    def agregarProcesoB(self):
        self.colaProcesos.addItem("Proceso B")

    def agregarProcesoC(self):
        self.colaProcesos.addItem("Proceso C")

    def agregarProcesoD(self):
        self.colaProcesos.addItem("Proceso D")

    def limpiarCola(self):
        self.colaProcesos.clear()

    def leerArchivo(self):
        mensaje = QtWidgets.QMessageBox()
        mensaje.setIcon(QtWidgets.QMessageBox.Warning)
        mensaje.setText("Por favor selecciona un archivo")
        mensaje.setInformativeText("Es necesario que selecciones un archivo *.proc para continuar con la ejecución")
        mensaje.setWindowTitle("Fallo la selección de archivo")
        mensaje.setStandardButtons(QtWidgets.QMessageBox.Retry | QtWidgets.QMessageBox.Cancel)
        mensaje.setDefaultButton(QtWidgets.QMessageBox.Retry)

        orden = True

        while orden:
            nombreArchivo = QtWidgets.QFileDialog.getOpenFileName(self, "Abrir archivo", ".", "Procesos (*.proc)")
            
            if nombreArchivo:
                print(nombreArchivo)
                orden = False
                archivo = open(nombreArchivo[0], "r")
                for linea in archivo:
                    self.procesos.append(linea.strip().split(","))

                print(self.procesos)
                return True
            else:
                print(nombreArchivo)
                orden = mensaje.exec_()
                # 4194304 código de retorno para boton cancelar
                if orden == 4194304:
                    orden = False
        return False

    def tomarProceso(self):
        if(len(self.colaProcesos)):
            #Tomar procesos
        
def main():
    app = QtWidgets.QApplication([])
    window = MainWindow()
    if window.leerArchivo():
        window.show()
        app.exec_()
    else:
        return -1


if __name__ == "__main__":
    main()