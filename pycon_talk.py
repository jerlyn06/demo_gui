from PyQt4 import QtGui
import sys

class MainWindow(QtGui.QMainWindow):
  def __init__(self):
    super(MainWindow,self).__init__()
    self.setWindowTitle("CGPA Calculator")
    wid = QtGui.QWidget()
    self.setCentralWidget(wid)
    layout = QtGui.QFormLayout()
    self.label = QtGui.QLabel()
    self.label.setText("Enter Subject")
    self.sub_box = QtGui.QLineEdit()
    self.sub_box.setPlaceholderText("Enter your subject")
    self.label1 = QtGui.QLabel()
    self.label1.setText("Enter marks")
    self.mbox = QtGui.QLineEdit()
    self.mbox.setPlaceholderText("Enter your marks")
    self.btn = QtGui.QPushButton()
    self.btn.setText("Get Results")
    self.btn.clicked.connect(lambda:self.get_results(str(self.sub_box.text()),int(self.mbox.text())))
    self.res = QtGui.QTextEdit()
    self.res.setReadOnly(True)
    layout.addWidget(self.label)
    layout.addWidget(self.sub_box)
    layout.addWidget(self.label1)
    layout.addWidget(self.mbox)
    layout.addWidget(self.btn)
    layout.addWidget(self.res)
    wid.setLayout(layout)
    self.setStyleSheet('''QMainWindow{background-color:black;color:white}QLabel{color:white}''')

  def get_results(self,subject,mark):
  	print(subject,mark)

if __name__=='__main__':
  app = QtGui.QApplication(sys.argv)
  win = MainWindow()
  win.show()
  try:
    sys.exit(app.exec_())
  except:
    pass