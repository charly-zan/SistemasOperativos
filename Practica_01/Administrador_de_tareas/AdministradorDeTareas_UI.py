# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\AdministradorDeTareas.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(744, 593)
        MainWindow.setMinimumSize(QtCore.QSize(708, 495))
        MainWindow.setMaximumSize(QtCore.QSize(111111, 111111))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_01 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_01.setGeometry(QtCore.QRect(20, 520, 100, 50))
        self.btn_01.setObjectName("btn_01")
        self.btn_02 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_02.setGeometry(QtCore.QRect(130, 520, 100, 50))
        self.btn_02.setObjectName("btn_02")
        self.btn_03 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_03.setGeometry(QtCore.QRect(240, 520, 100, 50))
        self.btn_03.setObjectName("btn_03")
        self.btn_04 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_04.setGeometry(QtCore.QRect(350, 520, 100, 50))
        self.btn_04.setObjectName("btn_04")
        self.btn_KA = QtWidgets.QPushButton(self.centralwidget)
        self.btn_KA.setGeometry(QtCore.QRect(500, 510, 111, 71))
        self.btn_KA.setObjectName("btn_KA")
        self.gB_colaProcesos = QtWidgets.QGroupBox(self.centralwidget)
        self.gB_colaProcesos.setGeometry(QtCore.QRect(560, 10, 171, 491))
        self.gB_colaProcesos.setObjectName("gB_colaProcesos")
        self.colaProcesos = QtWidgets.QListWidget(self.gB_colaProcesos)
        self.colaProcesos.setGeometry(QtCore.QRect(10, 20, 151, 461))
        self.colaProcesos.setObjectName("colaProcesos")
        self.gB_procesosActuales = QtWidgets.QGroupBox(self.centralwidget)
        self.gB_procesosActuales.setGeometry(QtCore.QRect(10, 360, 541, 141))
        self.gB_procesosActuales.setObjectName("gB_procesosActuales")
        self.listaProcesos = QtWidgets.QTableWidget(self.gB_procesosActuales)
        self.listaProcesos.setGeometry(QtCore.QRect(10, 20, 521, 111))
        self.listaProcesos.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.listaProcesos.setObjectName("listaProcesos")
        self.listaProcesos.setColumnCount(0)
        self.listaProcesos.setRowCount(0)
        self.gB_recursos = QtWidgets.QGroupBox(self.centralwidget)
        self.gB_recursos.setGeometry(QtCore.QRect(10, 10, 141, 341))
        self.gB_recursos.setObjectName("gB_recursos")
        self.graphicsView = QtWidgets.QGraphicsView(self.gB_recursos)
        self.graphicsView.setGeometry(QtCore.QRect(10, 20, 121, 91))
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.gB_recursos)
        self.graphicsView_2.setGeometry(QtCore.QRect(10, 130, 121, 91))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.graphicsView_3 = QtWidgets.QGraphicsView(self.gB_recursos)
        self.graphicsView_3.setGeometry(QtCore.QRect(10, 240, 121, 91))
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.gB_procesosTiempo = QtWidgets.QGroupBox(self.centralwidget)
        self.gB_procesosTiempo.setGeometry(QtCore.QRect(160, 10, 391, 341))
        self.gB_procesosTiempo.setObjectName("gB_procesosTiempo")
        self.graphicsView_4 = QtWidgets.QGraphicsView(self.gB_procesosTiempo)
        self.graphicsView_4.setGeometry(QtCore.QRect(10, 20, 371, 311))
        self.graphicsView_4.setObjectName("graphicsView_4")
        self.btn_Limpiar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Limpiar.setGeometry(QtCore.QRect(620, 510, 111, 71))
        self.btn_Limpiar.setObjectName("btn_Limpiar")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Administrador de Tareas"))
        self.btn_01.setText(_translate("MainWindow", "Proceso A"))
        self.btn_02.setText(_translate("MainWindow", "Proceso B"))
        self.btn_03.setText(_translate("MainWindow", "Proceso D"))
        self.btn_04.setText(_translate("MainWindow", "Proceso C"))
        self.btn_KA.setText(_translate("MainWindow", "Matar procesos"))
        self.gB_colaProcesos.setTitle(_translate("MainWindow", "Cola de procesos"))
        self.gB_procesosActuales.setTitle(_translate("MainWindow", "Procesos Actuales"))
        self.gB_recursos.setTitle(_translate("MainWindow", "Recursos"))
        self.gB_procesosTiempo.setTitle(_translate("MainWindow", "Tiempo de ejecución"))
        self.btn_Limpiar.setText(_translate("MainWindow", "Limpiar cola"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

