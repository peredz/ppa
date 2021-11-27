from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow
from PyQt5 import uic
from sys import argv, exit
from PyQt5.QtGui import QPainter, QColor, QBrush
from random import randint
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self):
        self.resize(674, 547)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(260, 190, 171, 161))
        self.pushButton.setObjectName("pushButton")
        self.setCentralWidget(self.centralwidget)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.pushButton.setText(_translate("MainWindow", "КРУГИ ТУТ!"))


class CyrcleVashka(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.a = False
        self.setupUi()
        self.setup()

    def setup(self):
        self.setGeometry(450, 300, 800, 600)

        self.pushButton.setStyleSheet("""border-radius : 50; 
                              border : 2px solid black""")
        self.pushButton.clicked.connect(self.cyrclllls)

    def cyrclllls(self):
        self.pushButton.hide()
        self.a = True
        self.repaint()

    def paintEvent(self, event):
        if self.a:
            qp = QPainter(self)
            qp.begin(self)
            self.drawCyrcled(qp)
            qp.end()

    def drawCyrcled(self, qp):
        col = QColor(0, 0, 0)
        col.setNamedColor('#yellow')
        qp.setPen(col)
        qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        a = randint(70, 250)
        qp.drawEllipse(randint(0, 500), randint(0, 500), a, a)
        qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        a = randint(70, 250)
        qp.drawEllipse(randint(0, 500), randint(0, 500), a, a)
        qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        a = randint(70, 250)
        qp.drawEllipse(randint(0, 500), randint(0, 500), a, a)


if __name__ == '__main__':
    app = QApplication(argv)
    ex = CyrcleVashka()
    ex.show()
    exit(app.exec())