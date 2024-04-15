from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class Window(QMainWindow):
	def __init__(self):
		super(Window, self).__init__()
		self.setGeometry(100, 100, 350, 600)
		self.setWindowTitle("QT Milo Label Editor Test")
		self.initUI()

	def initUI(self):
		self.label = QtWidgets.QLabel(self)
		self.label.setText("Object")
		self.label.move(10,10)

		self.testbutton = QtWidgets.QPushButton(self)
		self.testbutton.setText("Test")
		self.testbutton.move(10,40)
		self.testbutton.clicked.connect(self.clicked)

	def clicked(self):
		self.label.setText("changed")
		self.update()

	def update(self):
		self.label.adjustSize()









def AppRun():
	app = QApplication(sys.argv)
	win = Window()




	win.show()
	sys.exit(app.exec_())

AppRun()