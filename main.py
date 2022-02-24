# Idea source:
# https://www.youtube.com/watch?v=pvimAM_SLic

import matplotlib.pyplot as plt
import numpy as np
from PyQt6 import QtCore, QtGui, QtWidgets


def main(start, end, n):
    res, dots = calculate_pi(start, end, n)
    plots(res, dots[0], dots[1], n, end)


def calculate_pi(start, end, n):
    points_in = 0
    points_total = 0
    # Creating array which contains numbers between 0 and 1
    # with shape 1 row and "n" columns
    x_arr = np.random.uniform(start, end, (1, n))
    y_arr = np.random.uniform(start, end, (1, n))
    x_in, y_in = [], []
    x_off, y_off = [], []
    for x, y in zip(x_arr[0], y_arr[0]):
        r = np.sqrt(x ** 2 + y ** 2)
        if r <= end:
            points_in += 1
            x_in.append(x)
            y_in.append(y)
        else:
            x_off.append(x)
            y_off.append(y)
        points_total += 1
    dots_in = np.array([[x_in], [y_in]])
    dots_off = np.array([[x_off], [y_off]])
    
    return (4 * (points_in / points_total), (dots_in, dots_off))


def plots(res, inside, outside, num, radius):
    plt.style.use('grayscale')
    plt.rcParams.update({'font.family': 'Arial'})
    fig, ax = plt.subplots(figsize=(10, 10), dpi=80, facecolor='#161616')
    circle = plt.Circle((0, 0), radius, color='c', fill=False, lw=2)
    
    ax.set_facecolor('#1F1F1F')
    ax.spines['bottom'].set_color('white')
    ax.spines['left'].set_color('white')
    ax.spines['right'].set_color('white')
    ax.spines['top'].set_color('white')
    ax.tick_params(axis='both', colors='white', labelsize=15)
    ax.set_aspect(1)
    ax.add_patch(circle)
    
    ax.set_title(f'Dots = {num}\nR = {radius}\nCalculated π = {res}',
                fontsize=20, 
                fontname='Cambria',
                fontstyle='italic',
                color='white', 
                pad=20
    )
   
    # Dots in the circle 
    ax.scatter(inside[0], inside[1], c='#ee9b00', s=2)
    
    # Dots off the circle 
    ax.scatter(outside[0], outside[1], c='#7209b7', s=2)
    
    plt.xlim([-radius, radius])
    plt.ylim([-radius, radius])
    plt.grid(color='#adb5bd')
    plt.show()
   

class Ui_MainWindow(object):
    length = 1.0
    number_of_dots = 10000
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(388, 519)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: #343a40;")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.topInnFrame = QtWidgets.QWidget(self.centralwidget)
        self.topInnFrame.setStyleSheet("* {\nbackground-color: #212529;\n}\n#topInnFrame {\nborder: 3px solid #000814;\n}")
        self.topInnFrame.setObjectName("topInnFrame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.topInnFrame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.topFrame = QtWidgets.QWidget(self.topInnFrame)
        self.topFrame.setObjectName("topFrame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.topFrame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.topFrame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setStyleSheet("color: #e9ecef;")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
		
        # Top input
        self.lineEdit = QtWidgets.QLineEdit(self.topFrame)
        font = QtGui.QFont()
        font.setFamily("Quant Antiqua")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("color: #fca311;\nbackground-color: #000814;")
        self.lineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
  
        self.verticalLayout_3.addWidget(self.lineEdit)
        self.verticalLayout_2.addWidget(self.topFrame)
        self.line = QtWidgets.QFrame(self.topInnFrame)
        self.line.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.line.setAutoFillBackground(False)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.botFrame = QtWidgets.QWidget(self.topInnFrame)
        self.botFrame.setObjectName("botFrame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.botFrame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.botFrame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: #e9ecef;")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.botFrame)
        font = QtGui.QFont()
        font.setFamily("Quant Antiqua")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
		
		# Bottom input
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("color: #fca311;\nbackground-color: #000814;")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        
        self.verticalLayout_4.addWidget(self.lineEdit_2)
        self.verticalLayout_2.addWidget(self.botFrame)
        self.verticalLayout.addWidget(self.topInnFrame)
        self.botInnFrame = QtWidgets.QWidget(self.centralwidget)
        self.botInnFrame.setStyleSheet("background-color: #212529;border: 3px solid #000814;")
        self.botInnFrame.setObjectName("botInnFrame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.botInnFrame)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.pushButton = QtWidgets.QPushButton(self.botInnFrame)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(20)
        
        # Button
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: #fca311;\nbackground-color: #000814;\nborder: 2px solid #e9ecef;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.getInputs)
        
        self.verticalLayout_5.addWidget(self.pushButton)
        self.verticalLayout.addWidget(self.botInnFrame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    def getInputs(self):
        self.length = float(self.lineEdit.text())
        self.number_of_dots = int(self.lineEdit_2.text())
        main(-self.length, self.length, self.number_of_dots)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculate the number π"))
        self.label.setText(_translate("MainWindow", "Length"))
        self.lineEdit.setText(_translate("MainWindow", str(self.length)))
        self.label_2.setText(_translate("MainWindow", "Number of dots"))
        self.lineEdit_2.setText(_translate("MainWindow", str(self.number_of_dots)))
        self.pushButton.setText(_translate("MainWindow", "Calculate"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
    