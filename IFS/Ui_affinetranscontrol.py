# 仿射变换控制

from PyQt5 import QtCore, QtGui, QtWidgets

import Ui_coefficientcontrol


class AffineTransWidget(QtWidgets.QWidget):

    # 自定义删除变换widget信号
    sigDelete = QtCore.pyqtSignal(int)

    def __init__(self, parent = None):
        super(AffineTransWidget, self).__init__(parent)

        self.index = -1 #用于记录仿射变换的索引值

        self.setMinimumSize(QtCore.QSize(430, 450))
        self.setMaximumSize(QtCore.QSize(430, 450))

        self.m_coefA = Ui_coefficientcontrol.CoefficientControlWidget(self)
        self.m_coefA.setCoefficientName("A:")

        self.m_coefB = Ui_coefficientcontrol.CoefficientControlWidget(self)
        self.m_coefB.setCoefficientName("B:")

        self.m_coefC = Ui_coefficientcontrol.CoefficientControlWidget(self)
        self.m_coefC.setCoefficientName("C:")

        self.m_coefD = Ui_coefficientcontrol.CoefficientControlWidget(self)
        self.m_coefD.setCoefficientName("D:")

        self.m_coefE = Ui_coefficientcontrol.CoefficientControlWidget(self)
        self.m_coefE.setCoefficientName("E:")

        self.m_coefF = Ui_coefficientcontrol.CoefficientControlWidget(self)
        self.m_coefF.setCoefficientName("F:")

        self.m_coefP = Ui_coefficientcontrol.CoefficientControlWidget(self)
        self.m_coefP.setCoefficientName("p:")
        self.m_coefP.setSliderAsProbability()

        self.m_groupBox = QtWidgets.QGroupBox(self)
        self.m_groupBox.setTitle("仿射变换")
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.m_groupBox.setFont(font)

        self.m_verticalLayout2 = QtWidgets.QVBoxLayout(self.m_groupBox)
        self.m_verticalLayout2.addWidget(self.m_coefA)
        self.m_verticalLayout2.addWidget(self.m_coefB)
        self.m_verticalLayout2.addWidget(self.m_coefC)
        self.m_verticalLayout2.addWidget(self.m_coefD)
        self.m_verticalLayout2.addWidget(self.m_coefE)
        self.m_verticalLayout2.addWidget(self.m_coefF)
        self.m_verticalLayout2.addWidget(self.m_coefP)

        self.m_btnDelete = QtWidgets.QPushButton("删除变换", self)
        self.m_btnDelete.setMinimumSize(100, 30)
        self.m_btnDelete.setMaximumSize(100, 30)
        self.m_btnDelete.clicked.connect(self.sendDeleteSignal)

        self.m_verticalLayout = QtWidgets.QVBoxLayout(self)
        self.m_verticalLayout.addWidget(self.m_groupBox)
        self.m_verticalLayout.addWidget(self.m_btnDelete)

    def setIndex(self, i):
        self.index = i

    def sendDeleteSignal(self):
        # print(self.index)
        self.sigDelete.emit(self.index)

    def getIFSCode(self):
        code = []
        code.append(self.m_coefA.getValue())
        code.append(self.m_coefB.getValue())
        code.append(self.m_coefC.getValue())
        code.append(self.m_coefD.getValue())
        code.append(self.m_coefE.getValue())
        code.append(self.m_coefF.getValue())
        code.append(self.m_coefP.getValue())
        # print(code)
        return code

