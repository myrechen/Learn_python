from PyQt5 import QtCore, QtGui, QtWidgets

import matplotlib.pyplot as plt

import Ui_affinetranscontrol
import ifsdraw

class IFSControlWidget(QtWidgets.QWidget):

    def __init__(self, parent = None):
        super(IFSControlWidget, self).__init__(parent)
        # self.resize(800, 605)

        self.m_mainWindow = QtWidgets.QWidget(self)

        self.m_scrollArea = QtWidgets.QScrollArea(self)
        self.m_scrollArea.setWidgetResizable(True)
        self.m_scrollArea.setWidget(self.m_mainWindow)

        self.m_vLayout= QtWidgets.QVBoxLayout(self)
        self.m_vLayout.addWidget(self.m_scrollArea)

        # 网格布局
        self.m_gridLayout = QtWidgets.QGridLayout(self.m_mainWindow)

        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)

        # 添加仿射变换窗口的按钮
        self.m_btnAddTransWidget = QtWidgets.QToolButton(self)
        self.m_btnAddTransWidget.setText("添加仿射变换")
        self.m_btnAddTransWidget.setFont(font)
        self.m_btnAddTransWidget.setMinimumSize(250, 250)
        self.m_btnAddTransWidget.setMaximumSize(250, 250)
        self.m_btnAddTransWidget.setIcon(QtGui.QIcon("D:/eCode/IFS/image/addicon.png"))
        self.m_btnAddTransWidget.setIconSize(QtCore.QSize(200, 200))
        self.m_btnAddTransWidget.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextUnderIcon)


        # 将按钮添加到布局
        self.m_gridLayout.addWidget(self.m_btnAddTransWidget, 0, 0)
        self.m_btnAddTransWidget.clicked.connect(self.addTransControlWidget)

        # 管理控件的列表
        self.m_widgetList = []
        self.m_widgetList.append(self.m_btnAddTransWidget)

        self.m_btnStartDraw = QtWidgets.QPushButton("开始绘制",self)
        self.m_btnStartDraw.setFont(font)
        self.m_btnStartDraw.clicked.connect(self.drawFractal)
        self.m_vLayout.addWidget(self.m_btnStartDraw)


    def addTransControlWidget(self):
        widget = Ui_affinetranscontrol.AffineTransWidget(self)
        widget.setIndex(len(self.m_widgetList)-1)
        widget.sigDelete.connect(self.deleteTransWidget)
        self.m_widgetList.insert(-1, widget)
        self.updateWindow()

    def updateWindow(self):
        self.clearWidget()
        for i,w in enumerate(self.m_widgetList):
            if i < len(self.m_widgetList)-1:
                w.setIndex(i)
            self.m_gridLayout.addWidget(w, i//3, i%3)

    def deleteTransWidget(self, index):
        # print("del", index)
        self.m_widgetList.pop(index)
        item = self.m_gridLayout.itemAt(index)
        self.m_gridLayout.removeItem(item)
        if item.widget():
            item.widget().deleteLater()
        self.updateWindow()

    def clearWidget(self):
        item_list = list(range(self.m_gridLayout.count()))
        for i in item_list:
            item = self.m_gridLayout.itemAt(i)
            self.m_gridLayout.removeItem(item)

    def drawFractal(self):
        # IFSCode = []
        # for i,w in enumerate(self.m_widgetList):
        #     if i < len(self.m_widgetList)-1:
        #         IFSCode.append(w.getIFSCode())
        # print(IFSCode)

        # IFSCode = [(0.5,0,0,0.5,0,0, 0.333),
        #             (0.5,0,0,0.5,0.5,0, 0.333),
        #             (0.5,0,0,0.5,0.25,0.5, 0.334)]

        # IFSCode = [(0,0,0,0.5,0,0,0.05),
        #    (0.12,-0.82,0.42,0.42,0,0.2,0.4),
        #    (0.12,0.82,-0.42,0.42,0,0.2,0.4),
        #    (0.1,0,0,0.1,0,0.2,0.15)]

        IFSCode = [(0.05,0,0,0.6,0,0,0.1),
        (0.05,0,0,-0.5,0,1.0,0.1),
        (0.46,0.32,-0.386,0.383,0,0.6,0.2),
        (0.47,-0.154,0.171,0.423,0,1.0,0.2),
        (0.43,0.275,-0.26,0.476,0,1.0,0.2),
        (0.421,-0.357,0.354,0.307,0,0.7,0.2)]

        if len(IFSCode) != 0:
            ifsdraw.IFSDrawFractal(IFSCode, 50000)

