import sys
import time
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
class LoginDlg(QDialog):

    def __init__(self):
        super(LoginDlg, self).__init__()

##        self.password = QLineEdit()
##        self.password.setEchoMode(QLineEdit.Password)
##        self.button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
##        self.button_box.accepted.connect(self.accept)
##        self.button_box.rejected.connect(self.reject)
##
##        layout = QFormLayout()
##        layout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
##        layout.addRow('Password', self.password)
##        layout.addWidget(self.button_box)
##
##        self.setLayout(layout)
##        self.setWindowTitle("Login")
##        self.setMinimumWidth(350)
        self.title = 'Anamed Systems'
        self.left = 100
        self.top = 100
        self.width = 1300
        self.height = 650
        self.initUI()
    def getTime(self):
        time = QTime.currentTime().toString()
        return time

    def updateTime(self):
        time = QTime.currentTime().toString()
        print("Time: " + time)
        self.time_label.setText(time)
        return time
    def createGridLayout(self):
        time = self.getTime()
        self.time_label = QLabel(time, self)
        self.time_label.move(800, 400)
        self.horizontalGroupBox = QGroupBox()
        layout = QGridLayout()
        layout.addWidget(QPushButton('1'), 0, 0)
        layout.addWidget(QPushButton(time), 0, 1)
        layout.addWidget(self.time_label, 0, 2)
        self.horizontalGroupBox.setLayout(layout)
    def paintEvent(self,e):
        painter=QPainter(self)
        painter.setPen(QPen(Qt.black,1,Qt.SolidLine))
        painter.setBrush(QBrush(Qt.white,Qt.SolidPattern))
        painter.drawRect(0,0,1300,95)

        
    def initUI(self):
            time1 = self.getTime()
            self.label=QLabel(self)
            self.label.setPixmap(QPixmap('image1.png'))
            self.label.setGeometry(0,0,200,90)
            self.label.setStyleSheet('background-color:white;')
            self.label.move(0,5)
            
            labelB = QLabel(self)
            labelB.setText("Current Time:")
            labelB.move(1000, 30)
            labelB.setStyleSheet('background-color:white;font-family:Times New Roman Bold;font-size:19px;')
            self.createGridLayout()
            self.time_label = QLabel(self)
            self.time_label.setText(time1)
            self.time_label.move(1120, 30)
            self.time_label.setStyleSheet('background-color:white;font-family:Times New Roman Bold;font-size:19px;')
            self.setWindowTitle(self.title)
            self.setStyleSheet("background-color:#f7faff;")
            self.setGeometry(self.left, self.top, self.width, self.height)
            self.show()

        
class App(QWidget):

    def __init__(self):
        super(App,self).__init__()
        self.title = 'Anamed Systems'
        self.left = 100
        self.top = 100
        self.width = 1300
        self.height = 650

        self.initUI()
    def getTime(self):
        time = QTime.currentTime().toString()
        return time

    def updateTime(self):
        time = QTime.currentTime().toString()
        print("Time: " + time)
        self.time_label.setText(time)
        return time
    def createGridLayout(self):
        time = self.getTime()
        self.time_label = QLabel(time, self)
        self.time_label.move(800, 400)
        self.horizontalGroupBox = QGroupBox()
        layout = QGridLayout()
        layout.addWidget(QPushButton('1'), 0, 0)
        layout.addWidget(QPushButton(time), 0, 1)
        layout.addWidget(self.time_label, 0, 2)
        self.horizontalGroupBox.setLayout(layout)
    def paintEvent(self,e):
        painter=QPainter(self)
        painter.setPen(QPen(Qt.black,1,Qt.SolidLine))
        painter.setBrush(QBrush(Qt.white,Qt.SolidPattern))
        painter.drawRect(0,0,1300,95)



            
        
    def initUI(self):
            


            time = self.getTime()
            
            
  

            self.label=QLabel(self)
            self.label.setPixmap(QPixmap('image1.png'))
            self.label.setGeometry(0,0,200,90)
            self.label.setStyleSheet('background-color:white;')
            self.label.move(0,5)
            
            #self.setToolTip('This is a <b>QWidget</b> widget')
            labelA = QLabel(self)
            labelA.setText('Current Temperature:')
            labelA.move(500, 30)
            labelA.setStyleSheet('background-color:white;font-family:Times New Roman Bold;font-size:19px;')

            
            btn = QPushButton('Start Test', self)
            btn.setStyleSheet("background-color:white;color:black;font-family:Times New Roman Bold;font-size:19px;border-style: outset;border-width: 2px;border-color: black;padding: 4px;")
            btn.resize(200,90)
            btn.move(200, 200)
            btn.clicked.connect(self.btn_clicked)
            #self.dialog=Second(self)
            
            btn1 = QPushButton('Settings', self)
            btn1.setStyleSheet("background-color:white;color:black;font-family:Times New Roman Bold;font-size:19px;border-style: outset;border-width: 2px;border-color: black;padding: 4px;")
            btn1.resize(200,90)
            btn1.move(200, 310)

            btn2 = QPushButton('User', self)
            btn2.setStyleSheet("background-color:white;color:black;font-family:Times New Roman Bold;font-size:19px;border-style: outset;border-width: 2px;border-color: black;padding: 4px;")
            btn2.resize(200,90)
            btn2.move(200, 420)

            btn3 = QPushButton('Results', self)
            btn3.setStyleSheet("background-color:white;color:black;font-family:Times New Roman Bold;font-size:19px;border-style: outset;border-width: 2px;border-color: black;padding: 4px;")
            btn3.resize(200,90)
            btn3.move(430, 200)

            btn4 = QPushButton('About', self)
            btn4.setStyleSheet("background-color:white;color:black;font-family:Times New Roman Bold;font-size:19px;border-style: outset;border-width: 2px;border-color: black;padding: 4px;")
            btn4.resize(200,90)
            btn4.move(430, 310)

            btn5 = QPushButton('Damper', self)
            btn5.setStyleSheet("background-color:white;color:black;font-family:Times New Roman Bold;font-size:19px;border-style: outset;border-width: 2px;border-color: black;padding: 4px;")
            btn5.resize(200,90)
            btn5.move(430, 420)

            
            self.setWindowTitle(self.title)
            self.setStyleSheet("background-color:#f7faff;")
            self.setGeometry(self.left, self.top, self.width, self.height)
            
           

            labelB = QLabel(self)
            labelB.setText("Current Time:")
            labelB.move(1000, 30)
            labelB.setStyleSheet('background-color:white;font-family:Times New Roman Bold;font-size:19px;')
            self.createGridLayout()
            self.time_label = QLabel(self)
            self.time_label.setText(time)
            self.time_label.move(1120, 30)
            self.time_label.setStyleSheet('background-color:white;font-family:Times New Roman Bold;font-size:19px;')
 
            self.show()
    def btn_clicked(self):
        login = LoginDlg()
        if login.exec_():
            self.edit.setText(login.password.text())
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    timer = QTimer()
    timer.timeout.connect(ex.updateTime)
    timer.start(1000)
    ex.show()
    sys.exit(app.exec_())
