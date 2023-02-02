# 仿射变换系数控制bak

from PyQt5 import QtCore, QtGui, QtWidgets


class CoefficientControlWidget(QtWidgets.QWidget):
    def __init__(self, parent = None):
        super(CoefficientControlWidget, self).__init__(parent)

        self.resize(415,95)
        self.horizontalLayout = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.groupBox = QtWidgets.QGroupBox(self)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.horizontalSlider = QtWidgets.QSlider(self.groupBox)
        self.horizontalSlider.setMinimum(-999999)
        self.horizontalSlider.setMaximum(999999)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalLayout_2.addWidget(self.horizontalSlider)

        self.coefficientSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.coefficientSpinBox.sizePolicy().hasHeightForWidth())
        self.coefficientSpinBox.setSizePolicy(sizePolicy)
        self.coefficientSpinBox.setMinimumSize(QtCore.QSize(80, 0))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.coefficientSpinBox.setFont(font)
        self.coefficientSpinBox.setDecimals(6)
        self.coefficientSpinBox.setMinimum(-0.999999)
        self.coefficientSpinBox.setMaximum(0.999999)
        self.coefficientSpinBox.setSingleStep(1e-06)
        self.coefficientSpinBox.setObjectName("coefficientSpinBox")
        self.horizontalLayout_2.addWidget(self.coefficientSpinBox)
        self.horizontalLayout.addWidget(self.groupBox)

        self.horizontalSlider.valueChanged.connect(self.changeSpinBox)
        self.coefficientSpinBox.valueChanged.connect(self.changeSlider)

        
        self.groupBox.setTitle("coename")

    # def setupUi(self, coefficientControlWidget):
    #     coefficientControlWidget.setObjectName("coefficientControlWidget")
    #     coefficientControlWidget.resize(413, 95)
    #     self.horizontalLayout = QtWidgets.QHBoxLayout(coefficientControlWidget)
    #     self.horizontalLayout.setObjectName("horizontalLayout")

    #     self.groupBox = QtWidgets.QGroupBox(coefficientControlWidget)
    #     font = QtGui.QFont()
    #     font.setFamily("微软雅黑")
    #     font.setPointSize(9)
    #     self.groupBox.setFont(font)
    #     self.groupBox.setObjectName("groupBox")
    #     self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox)
    #     self.horizontalLayout_2.setObjectName("horizontalLayout_2")

    #     self.horizontalSlider = QtWidgets.QSlider(self.groupBox)
    #     self.horizontalSlider.setMinimum(-999999)
    #     self.horizontalSlider.setMaximum(999999)
    #     self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
    #     self.horizontalSlider.setObjectName("horizontalSlider")
    #     self.horizontalLayout_2.addWidget(self.horizontalSlider)

    #     self.coefficientSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
    #     sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
    #     sizePolicy.setHorizontalStretch(0)
    #     sizePolicy.setVerticalStretch(0)
    #     sizePolicy.setHeightForWidth(self.coefficientSpinBox.sizePolicy().hasHeightForWidth())
    #     self.coefficientSpinBox.setSizePolicy(sizePolicy)
    #     self.coefficientSpinBox.setMinimumSize(QtCore.QSize(80, 0))
    #     font = QtGui.QFont()
    #     font.setFamily("微软雅黑")
    #     font.setPointSize(10)
    #     self.coefficientSpinBox.setFont(font)
    #     self.coefficientSpinBox.setDecimals(6)
    #     self.coefficientSpinBox.setMinimum(-0.999999)
    #     self.coefficientSpinBox.setMaximum(0.999999)
    #     self.coefficientSpinBox.setSingleStep(1e-06)
    #     self.coefficientSpinBox.setObjectName("coefficientSpinBox")
    #     self.horizontalLayout_2.addWidget(self.coefficientSpinBox)
    #     self.horizontalLayout.addWidget(self.groupBox)

    #     self.retranslateUi(coefficientControlWidget)
    #     QtCore.QMetaObject.connectSlotsByName(coefficientControlWidget)

    #     self.horizontalSlider.valueChanged.connect(self.changeSpinBox)
    #     self.coefficientSpinBox.valueChanged.connect(self.changeSlider)

    # def retranslateUi(self, coefficientControlWidget):
    #     _translate = QtCore.QCoreApplication.translate
    #     coefficientControlWidget.setWindowTitle(_translate("coefficientControlWidget", "Form"))
    #     self.groupBox.setTitle(_translate("coefficientControlWidget", "coename"))

    def setCoefficientName(self, name):
        self.groupBox.setTitle(name)

    def changeSpinBox(self, val):
        self.coefficientSpinBox.setValue(val/1000000)

    def changeSlider(self, val):
        self.horizontalSlider.setValue(val*1000000)

