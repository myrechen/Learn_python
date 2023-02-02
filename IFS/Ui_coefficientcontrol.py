# 仿射变换系数控制


from PyQt5 import QtCore, QtGui, QtWidgets


class CoefficientControlWidget(QtWidgets.QWidget):
    def __init__(self, parent = None):
        super(CoefficientControlWidget, self).__init__(parent)

        self.resize(400, 60)
        self.setMinimumSize(QtCore.QSize(400, 60))
        self.setMaximumSize(QtCore.QSize(400, 60))

        self.label = QtWidgets.QLabel(self)
        self.label.setText("A:")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(25, 0))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label.setFont(font)


        self.coefficientSlider = QtWidgets.QSlider(self)
        self.coefficientSlider.setMaximumSize(QtCore.QSize(225, 25))
        self.coefficientSlider.setOrientation(QtCore.Qt.Horizontal)
        self.coefficientSlider.setMinimum(-999999)
        self.coefficientSlider.setMaximum(999999)

        self.coefficientSpinBox = QtWidgets.QDoubleSpinBox(self)
        sizePolicy.setHeightForWidth(self.coefficientSpinBox.sizePolicy().hasHeightForWidth())
        self.coefficientSpinBox.setSizePolicy(sizePolicy)
        self.coefficientSpinBox.setFont(font)
        self.coefficientSpinBox.setDecimals(6)
        self.coefficientSpinBox.setMinimum(-0.999999)
        self.coefficientSpinBox.setMaximum(0.999999)
        self.coefficientSpinBox.setSingleStep(1e-06)

        self.horizontalLayout = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)

        self.horizontalLayout.addWidget(self.label)
        self.horizontalLayout.addWidget(self.coefficientSlider)
        self.horizontalLayout.addWidget(self.coefficientSpinBox)

        # 绑定信号
        self.coefficientSlider.valueChanged.connect(self.changeSpinBox)
        self.coefficientSpinBox.valueChanged.connect(self.changeSlider)

    def setCoefficientName(self, name):
        self.label.setText(name)

    def changeSpinBox(self, val):
        self.coefficientSpinBox.setValue(val/1000000)

    def changeSlider(self, val):
        self.coefficientSlider.setValue(val*1000000)

    def setSliderRange(self, min, max):
        self.coefficientSlider.setMinimum(min*1000000)
        self.coefficientSlider.setMaximum(max*1000000)
        self.coefficientSpinBox.setMinimum(min)
        self.coefficientSpinBox.setMaximum(max)

    def setSliderAsProbability(self):
        self.coefficientSlider.setMinimum(0)
        self.coefficientSlider.setMaximum(1000000)
        self.coefficientSpinBox.setMinimum(0)
        self.coefficientSpinBox.setMaximum(1)

    def getValue(self):
        return self.coefficientSpinBox.value()
