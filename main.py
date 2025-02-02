##################################################
# Idea source:                                   #
# https://www.youtube.com/watch?v=pvimAM_SLic    #
##################################################

import matplotlib.pyplot as plt
import numpy as np
from PyQt6 import QtCore, QtGui, QtWidgets
from matplotlib.font_manager import FontProperties


def main(start, end, n):
    res, dots = calculate_pi(start, end, n)
    plots(res, dots[0], dots[1], n, start, end)


def calculate_pi(start, end, n):
    points_in = 0
    points_total = 0
    # Creating array which contains numbers between "start" and "end"
    # both for "x" and "y"
    # with shape 1 row and "n" columns
    x_arr = np.random.uniform(start, end, (1, n))
    y_arr = np.random.uniform(start, end, (1, n))
    x_in, y_in = [], []
    x_off, y_off = [], []
    for x, y in zip(x_arr[0], y_arr[0]):
        offset = (start + end) / 2
        segment = np.sqrt((x - offset) ** 2 + (y - offset) ** 2)
        radius = np.abs((end - start) / 2)
        if segment <= radius:
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


def plots(res, inside, outside, num, start, end):
    plt.style.use('grayscale')
    plt.rcParams.update({'font.family': 'Arial'})
    fig, ax = plt.subplots(figsize=(10, 10), dpi=80, facecolor='#161616')
    O = (start + end) / 2           # Center coords
    R = np.abs((end - start) / 2)   # Circle radius
    circle = plt.Circle((O, O), R, color='c', fill=False, lw=2)
    
    # Plot theme properties 
    ax.set_facecolor('#1F1F1F')
    ax.spines['bottom'].set_color('white')
    ax.spines['left'].set_color('white')
    ax.spines['right'].set_color('white')
    ax.spines['top'].set_color('white')
    ax.tick_params(axis='both', colors='white', labelsize=15)
    ax.set_aspect(1)
    ax.add_patch(circle)
   
    # Plot title properties 
    prop = FontProperties() 
    prop.set_file('materials/STIXGeneral-Regular.ttf')
    ax.set_title(f'Dots = {num}\nx \u2208 [{start}, {end}]\nCalculated π = {res}',
                fontproperties=prop,
                fontsize=20, 
                fontname='Cambria',
                fontstyle='italic',
                color='white', 
                pad=20
    )
   
    # Dots in the circle 
    ax.scatter(inside[0], inside[1], c='#ee9b00', s=2, label='Inside dots')
    
    # Dots off the circle 
    ax.scatter(outside[0], outside[1], c='#7209b7', s=2, label='Outside dots')
    ax.legend(loc='center left', bbox_to_anchor=(0.775, 1.080), fontsize='xx-large', frameon=False, markerscale=6.0, labelcolor='white', handletextpad=0.6, handlelength=0.9, handleheight=1.2)
    
    plt.xlim([start, end])
    plt.ylim([start, end])
    plt.grid(color='#adb5bd')
    plt.show()
   

# GUI
# Form implementation generated from reading ui file 'Calculate the number pi.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

class Ui_MainWindow(object):
    xStart = -1.0
    xEnd = 1.0
    number_of_dots = 10000
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(388, 519)
        MainWindow.setWindowIcon(QtGui.QIcon('materials/python.ico'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: #343a40;")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.topInnFrame = QtWidgets.QWidget(self.centralwidget)
        self.topInnFrame.setStyleSheet(
            """
            * {
                background-color: #212529;
            }
            #topInnFrame {
                border: 3px solid #000814;
            }
            """
        )
        self.topInnFrame.setObjectName("topInnFrame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.topInnFrame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.topFrame = QtWidgets.QWidget(self.topInnFrame)
        self.topFrame.setObjectName("topFrame")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.topFrame)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.right_part = QtWidgets.QWidget(self.topFrame)
        self.right_part.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.right_part.setObjectName("right_part")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.right_part)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelLengthStart = QtWidgets.QLabel(self.right_part)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(28)
        font.setItalic(True)
        self.labelLengthStart.setFont(font)
        self.labelLengthStart.setStyleSheet("color: #e9ecef;")
        self.labelLengthStart.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.labelLengthStart.setObjectName("labelLengthStart")
        self.horizontalLayout_2.addWidget(self.labelLengthStart)
        self.inputStart = QtWidgets.QLineEdit(self.right_part)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputStart.sizePolicy().hasHeightForWidth())
        self.inputStart.setSizePolicy(sizePolicy)
        self.inputStart.setMaximumSize(QtCore.QSize(350, 16777215))
        font = QtGui.QFont()
        font.setFamily("Quant Antiqua")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        self.inputStart.setFont(font)
        self.inputStart.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.inputStart.setStyleSheet("color: #fca311;\nbackground-color: #000814;")
        self.inputStart.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.inputStart.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.inputStart)
        self.verticalLayout_7.addWidget(self.right_part)
        self.left_part = QtWidgets.QWidget(self.topFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.left_part.sizePolicy().hasHeightForWidth())
        self.left_part.setSizePolicy(sizePolicy)
        self.left_part.setObjectName("left_part")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.left_part)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelLengthEnd = QtWidgets.QLabel(self.left_part)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(28)
        font.setItalic(True)
        self.labelLengthEnd.setFont(font)
        self.labelLengthEnd.setStyleSheet("color: #e9ecef;")
        self.labelLengthEnd.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.labelLengthEnd.setObjectName("labelLengthEnd")
        self.horizontalLayout.addWidget(self.labelLengthEnd)
        self.inputEnd = QtWidgets.QLineEdit(self.left_part)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputEnd.sizePolicy().hasHeightForWidth())
        self.inputEnd.setSizePolicy(sizePolicy)
        self.inputEnd.setMaximumSize(QtCore.QSize(350, 16777215))
        font = QtGui.QFont()
        font.setFamily("Quant Antiqua")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        self.inputEnd.setFont(font)
        self.inputEnd.setStyleSheet("color: #fca311;\nbackground-color: #000814;")
        self.inputEnd.setFrame(True)
        self.inputEnd.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.inputEnd.setObjectName("inputEnd")
        self.horizontalLayout.addWidget(self.inputEnd)
        self.verticalLayout_7.addWidget(self.left_part)
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
        self.labelDotsNumber = QtWidgets.QLabel(self.botFrame)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.labelDotsNumber.setFont(font)
        self.labelDotsNumber.setStyleSheet("color: #e9ecef;")
        self.labelDotsNumber.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelDotsNumber.setObjectName("labelDotsNumber")
        self.verticalLayout_4.addWidget(self.labelDotsNumber)
        self.inputDots = QtWidgets.QLineEdit(self.botFrame)
        font = QtGui.QFont()
        font.setFamily("Quant Antiqua")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        self.inputDots.setFont(font)
        self.inputDots.setStyleSheet("color: #fca311;\nbackground-color: #000814;")
        self.inputDots.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.inputDots.setObjectName("inputDots")
        self.verticalLayout_4.addWidget(self.inputDots)
        self.verticalLayout_2.addWidget(self.botFrame)
        self.verticalLayout.addWidget(self.topInnFrame)
        self.botInnFrame = QtWidgets.QWidget(self.centralwidget)
        self.botInnFrame.setStyleSheet("background-color: #212529;border: 3px solid #000814;")
        self.botInnFrame.setObjectName("botInnFrame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.botInnFrame)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.pushButton = QtWidgets.QPushButton(self.botInnFrame)
        self.pushButton.clicked.connect(self.getInputs)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(
            """
            QPushButton {
                color: #fca311;
                background-color: #000814;
                border: 2px solid #e9ecef;
            }
            QPushButton::Pressed {
                color: green;
            }
            """
        )
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_5.addWidget(self.pushButton)
        self.verticalLayout.addWidget(self.botInnFrame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculate the number π"))
        self.labelLengthStart.setText(_translate("MainWindow", "x<sub>start</sub>"))
        self.inputStart.setText(_translate("MainWindow", str(self.xStart)))
        self.labelLengthEnd.setText(_translate("MainWindow", "x<sub>end</sub>"))
        self.inputEnd.setText(_translate("MainWindow", str(self.xEnd)))
        self.labelDotsNumber.setText(_translate("MainWindow", "Number of dots"))
        self.inputDots.setText(_translate("MainWindow", str(self.number_of_dots)))
        self.pushButton.setText(_translate("MainWindow", "Calculate"))
    
    def getInputs(self):
        self.xStart = float(self.inputStart.text())
        self.xEnd = float(self.inputEnd.text())
        self.number_of_dots = int(self.inputDots.text())
        main(self.xStart, self.xEnd, self.number_of_dots)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
    