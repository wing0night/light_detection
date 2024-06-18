from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
import page3


class DNA_Page(QWidget):
    def __init__(self):
        super().__init__()
        # 创建水平布局
        self.hLayout = QHBoxLayout(self)
        self.hLayout.setContentsMargins(0, 0, 0, 0)  # 设置水平布局在Widget内上下左右的间距
        self.hLayout.setSpacing(100)  # 设置间距
        self.hLayout.setDirection(0)  # 自左向右的布局
        self.hLayout.addSpacing(50)  # 左侧空隙

        self.font = QFont()
        self.font.setFamily("黑体")
        self.font.setBold(1)  # 设置为粗体
        self.font.setPixelSize(24)  # 字体大小



        # 创建a1图像按钮
        '''self.btn_a1 = QPushButton()  # 创建按钮
        self.btn_a1.setStyleSheet("QPushButton{color:white;background-color:rgb(51,204,255);font-family:黑体;}"
                                  "QPushButton:pressed{background-color:rgb(51,129,172)}")
        self.btn_a1.setFont(self.font)
        self.btn_a1.setText("a1")
        self.btn_a1.setFixedHeight(200)
        self.btn_a1.setFixedWidth(120)
        self.btn_a1.setParent(self)
        self.btn_a1.setCheckable(True)
        self.btn_a1.clicked.connect(self.slot_a1)
        self.hLayout.addWidget(self.btn_a1)'''

        self.recommend_button_1 = QToolButton()
        self.recommend_button_1.setText("测定标曲")  # 设置按钮文本
        self.recommend_button_1.setIcon(QtGui.QIcon('button_img/p1.png'))  # 设置按钮图标
        self.recommend_button_1.setIconSize(QtCore.QSize(100, 100))  # 设置图标大小
        self.recommend_button_1.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)  # 设置按钮形式为上图下文
        self.recommend_button_1.clicked.connect(self.slot_a1)
        #self.recommend_button_1.setFixedSize(50, 50)
        self.hLayout.addWidget(self.recommend_button_1)

        # 创建a2图标
        '''self.btn_a2 = QToolButton()
        self.btn_a2.setStyleSheet("QPushButton{color:white;background-color:rgb(51,204,255);}"
                                  "QPushButton:pressed{background-color:rgb(51,129,172)}")
        self.btn_a2.setFont(self.font)
        self.btn_a2.setText("测定标准曲线")
        self.btn_a2.setFixedHeight(300)
        self.btn_a2.setFixedWidth(200)
        # self.btn_a2.setCheckable(True)
        self.btn_a2.clicked.connect(self.slot_a2)
        self.hLayout.addWidget(self.btn_a2)
        self.btn_a2.setIcon(QtGui.QIcon('button_img/p2.png'))  # 设置按钮图标
        #self.btn_a2.setIconSize(QtCore.QSize(200, 200))  # 设置图标大小
        self.btn_a2.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)  # 设置按钮形式为上图下文'''

        self.recommend_button_2 = QToolButton()
        self.recommend_button_2.setText("测量样品")  # 设置按钮文本
        self.recommend_button_2.setIcon(QtGui.QIcon('button_img/p2.png'))  # 设置按钮图标
        self.recommend_button_2.setIconSize(QtCore.QSize(100, 100))  # 设置图标大小
        self.recommend_button_2.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)  # 设置按钮形式为上图下文
        self.recommend_button_2.clicked.connect(self.slot_a2)
        # self.recommend_button_1.setFixedSize(50, 50)
        self.hLayout.addWidget(self.recommend_button_2)

        '''self.recommend_button_2 = QToolButton()
        self.recommend_button_2.setText("可馨HANM")  # 设置按钮文本
        self.recommend_button_2.setIcon(QtGui.QIcon('button_img/p2.png'))  # 设置按钮图标
        self.recommend_button_2.setIconSize(QtCore.QSize(100, 100))  # 设置图标大小
        self.recommend_button_2.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)  # 设置按钮形式为上图下文
        self.recommend_button_2.clicked.connect(self.slot_a2)
        self.hLayout.addWidget(self.recommend_button_2)'''

        # 创建a3图标
        '''self.btn_a3 = QPushButton()
        self.btn_a3.setStyleSheet("QPushButton{color:white;background-color:rgb(51,204,255)}"
                                  "QPushButton:pressed{background-color:rgb(51,129,172)}")
        self.btn_a3.setFont(self.font)
        self.btn_a3.setText("a3")
        self.btn_a3.setFixedHeight(200)
        self.btn_a3.setFixedWidth(120)
        self.btn_a3.setParent(self)
        self.btn_a3.setCheckable(True)
        self.btn_a3.clicked.connect(self.slot_a3)
        self.hLayout.addWidget(self.btn_a3)'''
        self.recommend_button_3 = QToolButton()
        self.recommend_button_3.setText("测量样品")  # 设置按钮文本
        self.recommend_button_3.setIcon(QtGui.QIcon('button_img/p3.png'))  # 设置按钮图标
        self.recommend_button_3.setIconSize(QtCore.QSize(100, 100))  # 设置图标大小
        self.recommend_button_3.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)  # 设置按钮形式为上图下文
        self.recommend_button_3.clicked.connect(self.slot_a3)
        # self.recommend_button_1.setFixedSize(50, 50)
        self.hLayout.addWidget(self.recommend_button_3)

        '''self.recommend_button_3 = QToolButton()
        self.recommend_button_3.setText("可馨HANM")  # 设置按钮文本
        self.recommend_button_3.setIcon(QtGui.QIcon('button_img/p3.png'))  # 设置按钮图标
        self.recommend_button_3.setIconSize(QtCore.QSize(100, 100))  # 设置图标大小
        self.recommend_button_3.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)  # 设置按钮形式为上图下文
        self.recommend_button_3.clicked.connect(self.slot_a3)
        self.hLayout.addWidget(self.recommend_button_3)'''

        # 最后，在尾端添加弹簧，以至于布局呈现靠左而不是居中
        self.hLayout.addStretch()



    def slot_a1(self):
        print("slot_a1 ")

    def slot_a2(self):
        print("slot_a2 ")

    def slot_a3(self):
        print("slot_a3 ")

# 以下为按钮BBB定义一个类
class RNA_Page(QWidget):
    def __init__(self):
        super().__init__()
        # 创建水平布局
        self.hLayout = QHBoxLayout(self)
        self.hLayout.setContentsMargins(0, 0, 0, 0)  # 设置水平布局在Widget内上下左右的间距
        self.hLayout.setSpacing(10)  # 设置间距
        self.hLayout.setDirection(0)  # 自左向右的布局
        self.hLayout.addSpacing(10)  # 左侧空隙

        self.font = QFont()
        self.font.setFamily("黑体")
        self.font.setBold(1)  # 设置为粗体
        self.font.setPixelSize(24)  # 字体大小

        # 创建a1图像按钮
        self.btn_a1 = QPushButton()  # 创建按钮
        self.btn_a1.setStyleSheet("QPushButton{color:white;background-color:rgb(51,204,255);font-family:黑体;}"
                                  "QPushButton:pressed{background-color:rgb(51,129,172)}")
        self.btn_a1.setFont(self.font)
        self.btn_a1.setText("a1")
        self.btn_a1.setFixedHeight(50)
        self.btn_a1.setFixedWidth(120)
        self.btn_a1.setParent(self)
        self.btn_a1.setCheckable(True)
        self.btn_a1.clicked.connect(self.slot_a1)
        self.hLayout.addWidget(self.btn_a1)

        # 创建a2图标
        self.btn_a2 = QPushButton()
        self.btn_a2.setStyleSheet("QPushButton{color:white;background-color:rgb(51,204,255);}"
                                  "QPushButton:pressed{background-color:rgb(51,129,172)}")
        self.btn_a2.setFont(self.font)
        self.btn_a2.setText("a2")
        self.btn_a2.setFixedHeight(50)
        self.btn_a2.setFixedWidth(120)
        self.btn_a2.setParent(self)
        self.btn_a2.setCheckable(True)
        self.btn_a2.clicked.connect(self.slot_a2)
        self.hLayout.addWidget(self.btn_a2)

        # 创建a3图标
        self.btn_a3 = QPushButton()
        self.btn_a3.setStyleSheet("QPushButton{color:white;background-color:rgb(51,204,255)}"
                                  "QPushButton:pressed{background-color:rgb(51,129,172)}")
        self.btn_a3.setFont(self.font)
        self.btn_a3.setText("a3")
        self.btn_a3.setFixedHeight(50)
        self.btn_a3.setFixedWidth(120)
        self.btn_a3.setParent(self)
        self.btn_a3.setCheckable(True)
        self.btn_a3.clicked.connect(self.slot_a3)
        self.hLayout.addWidget(self.btn_a3)

        # 最后，在尾端添加弹簧，以至于布局呈现靠左而不是居中
        self.hLayout.addStretch()

    def slot_a1(self):
        print("slot_b1 ")

    def slot_a2(self):
        print("slot_b2 ")

    def slot_a3(self):
        print("slot_b3 ")

class Protein_Page(QWidget):
    def __init__(self):
        super().__init__()
        # 创建水平布局
        self.hLayout = QHBoxLayout(self)
        self.hLayout.setContentsMargins(0, 0, 0, 0)  # 设置水平布局在Widget内上下左右的间距
        self.hLayout.setSpacing(10)  # 设置间距
        self.hLayout.setDirection(0)  # 自左向右的布局
        self.hLayout.addSpacing(10)  # 左侧空隙

        self.font = QFont()
        self.font.setFamily("黑体")
        self.font.setBold(1)  # 设置为粗体
        self.font.setPixelSize(24)  # 字体大小

        # 创建a1图像按钮
        self.btn_a1 = QPushButton()  # 创建按钮
        self.btn_a1.setStyleSheet("QPushButton{color:white;background-color:rgb(51,204,255);font-family:黑体;}"
                                  "QPushButton:pressed{background-color:rgb(51,129,172)}")
        self.btn_a1.setFont(self.font)
        self.btn_a1.setText("a1")
        self.btn_a1.setFixedHeight(50)
        self.btn_a1.setFixedWidth(120)
        self.btn_a1.setParent(self)
        self.btn_a1.setCheckable(True)
        self.btn_a1.clicked.connect(self.slot_a1)
        self.hLayout.addWidget(self.btn_a1)

        # 创建a2图标
        self.btn_a2 = QPushButton()
        self.btn_a2.setStyleSheet("QPushButton{color:white;background-color:rgb(51,204,255);}"
                                  "QPushButton:pressed{background-color:rgb(51,129,172)}")
        self.btn_a2.setFont(self.font)
        self.btn_a2.setText("a2")
        self.btn_a2.setFixedHeight(50)
        self.btn_a2.setFixedWidth(120)
        self.btn_a2.setParent(self)
        self.btn_a2.setCheckable(True)
        self.btn_a2.clicked.connect(self.slot_a2)
        self.hLayout.addWidget(self.btn_a2)

        # 创建a3图标
        self.btn_a3 = QPushButton()
        self.btn_a3.setStyleSheet("QPushButton{color:white;background-color:rgb(51,204,255)}"
                                  "QPushButton:pressed{background-color:rgb(51,129,172)}")
        self.btn_a3.setFont(self.font)
        self.btn_a3.setText("a3")
        self.btn_a3.setFixedHeight(50)
        self.btn_a3.setFixedWidth(120)
        self.btn_a3.setParent(self)
        self.btn_a3.setCheckable(True)
        self.btn_a3.clicked.connect(self.slot_a3)
        self.hLayout.addWidget(self.btn_a3)

        # 最后，在尾端添加弹簧，以至于布局呈现靠左而不是居中
        self.hLayout.addStretch()

    def slot_a1(self):
        print("slot_c1 ")

    def slot_a2(self):
        print("slot_c2 ")

    def slot_a3(self):
        print("slot_c3 ")


class IonTolerance_Page(QWidget):
    def __init__(self):
        super().__init__()
        # 创建水平布局
        self.hLayout = QHBoxLayout(self)
        self.hLayout.setContentsMargins(0, 0, 0, 0)  # 设置水平布局在Widget内上下左右的间距
        self.hLayout.setSpacing(10)  # 设置间距
        self.hLayout.setDirection(0)  # 自左向右的布局
        self.hLayout.addSpacing(10)  # 左侧空隙

        self.font = QFont()
        self.font.setFamily("黑体")
        self.font.setBold(1)  # 设置为粗体
        self.font.setPixelSize(24)  # 字体大小

        # 创建a1图像按钮
        self.btn_a1 = QPushButton()  # 创建按钮
        self.btn_a1.setStyleSheet("QPushButton{color:white;background-color:rgb(51,204,255);font-family:黑体;}"
                                  "QPushButton:pressed{background-color:rgb(51,129,172)}")
        self.btn_a1.setFont(self.font)
        self.btn_a1.setText("a1")
        self.btn_a1.setFixedHeight(50)
        self.btn_a1.setFixedWidth(120)
        self.btn_a1.setParent(self)
        self.btn_a1.setCheckable(True)
        self.btn_a1.clicked.connect(self.slot_a1)
        self.hLayout.addWidget(self.btn_a1)

        # 创建a2图标
        self.btn_a2 = QPushButton()
        self.btn_a2.setStyleSheet("QPushButton{color:white;background-color:rgb(51,204,255);}"
                                  "QPushButton:pressed{background-color:rgb(51,129,172)}")
        self.btn_a2.setFont(self.font)
        self.btn_a2.setText("a2")
        self.btn_a2.setFixedHeight(50)
        self.btn_a2.setFixedWidth(120)
        self.btn_a2.setParent(self)
        self.btn_a2.setCheckable(True)
        self.btn_a2.clicked.connect(self.slot_a2)
        self.hLayout.addWidget(self.btn_a2)

        # 创建a3图标
        self.btn_a3 = QPushButton()
        self.btn_a3.setStyleSheet("QPushButton{color:white;background-color:rgb(51,204,255)}"
                                  "QPushButton:pressed{background-color:rgb(51,129,172)}")
        self.btn_a3.setFont(self.font)
        self.btn_a3.setText("a3")
        self.btn_a3.setFixedHeight(50)
        self.btn_a3.setFixedWidth(120)
        self.btn_a3.setParent(self)
        self.btn_a3.setCheckable(True)
        self.btn_a3.clicked.connect(self.slot_a3)
        self.hLayout.addWidget(self.btn_a3)

        # 最后，在尾端添加弹簧，以至于布局呈现靠左而不是居中
        self.hLayout.addStretch()

    def slot_a1(self):
        print("slot_c1 ")

    def slot_a2(self):
        print("slot_c2 ")

    def slot_a3(self):
        print("slot_c3 ")


class Development_Page(QWidget):
    def __init__(self):
        super().__init__()
        # 创建水平布局
        self.hLayout = QHBoxLayout(self)
        self.hLayout.setContentsMargins(0, 0, 0, 0)  # 设置水平布局在Widget内上下左右的间距
        self.hLayout.setSpacing(10)  # 设置间距
        self.hLayout.setDirection(0)  # 自左向右的布局
        self.hLayout.addSpacing(10)  # 左侧空隙

        self.font = QFont()
        self.font.setFamily("黑体")
        self.font.setBold(1)  # 设置为粗体
        self.font.setPixelSize(24)  # 字体大小

        # 创建a1图像按钮
        self.btn_a1 = QPushButton()  # 创建按钮
        self.btn_a1.setStyleSheet("QPushButton{color:white;background-color:rgb(51,204,255);font-family:黑体;}"
                                  "QPushButton:pressed{background-color:rgb(51,129,172)}")
        self.btn_a1.setFont(self.font)
        self.btn_a1.setText("a1")
        self.btn_a1.setFixedHeight(50)
        self.btn_a1.setFixedWidth(120)
        self.btn_a1.setParent(self)
        self.btn_a1.setCheckable(True)
        self.btn_a1.clicked.connect(self.slot_a1)
        self.hLayout.addWidget(self.btn_a1)

        # 创建a2图标
        self.btn_a2 = QPushButton()
        self.btn_a2.setStyleSheet("QPushButton{color:white;background-color:rgb(51,204,255);}"
                                  "QPushButton:pressed{background-color:rgb(51,129,172)}")
        self.btn_a2.setFont(self.font)
        self.btn_a2.setText("a2")
        self.btn_a2.setFixedHeight(50)
        self.btn_a2.setFixedWidth(120)
        self.btn_a2.setParent(self)
        self.btn_a2.setCheckable(True)
        self.btn_a2.clicked.connect(self.slot_a2)
        self.hLayout.addWidget(self.btn_a2)

        # 创建a3图标
        self.btn_a3 = QPushButton()
        self.btn_a3.setStyleSheet("QPushButton{color:white;background-color:rgb(51,204,255)}"
                                  "QPushButton:pressed{background-color:rgb(51,129,172)}")
        self.btn_a3.setFont(self.font)
        self.btn_a3.setText("a3")
        self.btn_a3.setFixedHeight(50)
        self.btn_a3.setFixedWidth(120)
        self.btn_a3.setParent(self)
        self.btn_a3.setCheckable(True)
        self.btn_a3.clicked.connect(self.slot_a3)
        self.hLayout.addWidget(self.btn_a3)

        # 最后，在尾端添加弹簧，以至于布局呈现靠左而不是居中
        self.hLayout.addStretch()

    def slot_a1(self):
        self.stackedWidget_func.setCurrentIndex(0)  # 将多页面窗口切换至页面序号0

    def slot_a2(self):
        print("slot_c2 ")

    def slot_a3(self):
        print("slot_c3 ")