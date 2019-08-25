from AdministradorDeTareas_UI import *

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

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

def main():
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()