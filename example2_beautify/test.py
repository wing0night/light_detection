# coding:utf-8

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import qtawesome
from PyQt5.QtWidgets import QApplication, QDesktopWidget
import page2


class MainUi(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

        # 设置主界面背景色
        #self.setStyleSheet("background-color:#006989")

    def init_ui(self):
        # 布局和组件设置
        self.setFixedSize(960, 700)
        self.main_widget = QtWidgets.QWidget()  # 创建窗口主部件
        self.main_layout = QtWidgets.QGridLayout()  # 创建主部件的网格布局
        self.main_widget.setLayout(self.main_layout)  # 设置窗口主部件布局为网格布局

        self.left_widget = QtWidgets.QWidget()  # 创建左侧部件
        self.left_widget.setObjectName('left_widget')
        self.left_layout = QtWidgets.QGridLayout()  # 创建左侧部件的网格布局层
        self.left_widget.setLayout(self.left_layout)  # 设置左侧部件布局为网格

        self.right_widget = QtWidgets.QWidget()  # 创建右侧部件
        self.right_widget.setObjectName('right_widget')
        self.right_layout = QtWidgets.QGridLayout()
        self.right_widget.setLayout(self.right_layout)  # 设置右侧部件布局为网格

        self.main_layout.addWidget(self.left_widget, 0, 0, 12, 2)  # 左侧部件在第0行第0列，占8行3列
        self.main_layout.addWidget(self.right_widget, 0, 2, 12, 10)  # 右侧部件在第0行第3列，占8行9列
        self.setCentralWidget(self.main_widget)  # 设置窗口主部件

        # 实例化创建按钮
        self.left_close = QtWidgets.QPushButton("")  # 关闭按钮
        self.left_visit = QtWidgets.QPushButton("")  # 空白按钮
        self.left_mini = QtWidgets.QPushButton("")  # 最小化按钮

        self.left_label_1 = QtWidgets.QPushButton("测试项目")
        self.left_label_1.setObjectName('left_label')
        self.left_label_2 = QtWidgets.QPushButton("开发信息")
        self.left_label_2.setObjectName('left_label')
        '''self.left_label_3 = QtWidgets.QPushButton("联系与帮助")
        self.left_label_3.setObjectName('left_label')'''

        self.left_button_1 = QtWidgets.QPushButton(qtawesome.icon('fa.paper-plane', color='white'), "测DNA")
        self.left_button_1.setObjectName('left_button')
        self.left_button_2 = QtWidgets.QPushButton(qtawesome.icon('fa.hand-pointer-o', color='white'), "测RNA")
        self.left_button_2.setObjectName('left_button')
        self.left_button_3 = QtWidgets.QPushButton(qtawesome.icon('fa.heartbeat', color='white'), "测蛋白")
        self.left_button_3.setObjectName('left_button')
        self.left_button_4 = QtWidgets.QPushButton(qtawesome.icon('fa.star-half-full', color='white'), "Ion Tolerance")
        self.left_button_4.setObjectName('left_button')
        self.left_button_5 = QtWidgets.QPushButton(qtawesome.icon('fa.child', color='white'), "开发人员")
        self.left_button_5.setObjectName('left_button')
        self.left_xxx = QtWidgets.QPushButton(" ")
        # 图标修改https://fontawesome.com/v4/icons/

        # 使用qtawesome这个第三方库来实现按钮中的Font Awesome字体图标的显示。然后将创建的按钮添加到左侧部件的网格布局层中
        self.left_layout.addWidget(self.left_mini, 0, 0, 1, 1)
        self.left_layout.addWidget(self.left_close, 0, 2, 1, 1)
        self.left_layout.addWidget(self.left_visit, 0, 1, 1, 1)
        self.left_layout.addWidget(self.left_label_1, 1, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_1, 2, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_2, 3, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_3, 4, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_4, 5, 0, 1, 3)
        self.left_layout.addWidget(self.left_label_2, 6, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_5, 7, 0, 1, 3)
        '''self.left_layout.addWidget(self.left_button_6, 8, 0, 1, 3)
        self.left_layout.addWidget(self.left_label_3, 9, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_7, 10, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_8, 11, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_9, 12, 0, 1, 3)'''

        # 添加图标
        self.right_recommend_label = QtWidgets.QLabel("今日推荐")
        self.right_recommend_label.setObjectName('right_lable')

        self.right_recommend_widget = QtWidgets.QWidget()  # 推荐封面部件
        self.right_recommend_layout = QtWidgets.QGridLayout()  # 推荐封面网格布局
        self.right_recommend_widget.setLayout(self.right_recommend_layout)

        self.recommend_button_1 = QtWidgets.QToolButton()
        self.recommend_button_1.setText("可馨HANM")  # 设置按钮文本
        self.recommend_button_1.setIcon(QtGui.QIcon('button_img/p1.png'))  # 设置按钮图标
        self.recommend_button_1.setIconSize(QtCore.QSize(100, 100))  # 设置图标大小
        self.recommend_button_1.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)  # 设置按钮形式为上图下文

        self.recommend_button_2 = QtWidgets.QToolButton()
        self.recommend_button_2.setText("那首歌")
        self.recommend_button_2.setIcon(QtGui.QIcon('button_img/p2.png'))
        self.recommend_button_2.setIconSize(QtCore.QSize(100, 100))
        self.recommend_button_2.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        self.recommend_button_3 = QtWidgets.QToolButton()
        self.recommend_button_3.setText("伟大的渺小")
        self.recommend_button_3.setIcon(QtGui.QIcon('button_img/p3.png'))
        self.recommend_button_3.setIconSize(QtCore.QSize(100, 100))
        self.recommend_button_3.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        self.recommend_button_4 = QtWidgets.QToolButton()
        self.recommend_button_4.setText("荣耀征战")
        self.recommend_button_4.setIcon(QtGui.QIcon('button_img/p4.png'))
        self.recommend_button_4.setIconSize(QtCore.QSize(100, 100))
        self.recommend_button_4.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        self.recommend_button_5 = QtWidgets.QToolButton()
        self.recommend_button_5.setText("猎场合辑")
        self.recommend_button_5.setIcon(QtGui.QIcon('button_img/p5.png'))
        self.recommend_button_5.setIconSize(QtCore.QSize(100, 100))
        self.recommend_button_5.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        self.right_recommend_layout.addWidget(self.recommend_button_1, 0, 0)
        self.right_recommend_layout.addWidget(self.recommend_button_2, 0, 1)
        self.right_recommend_layout.addWidget(self.recommend_button_3, 0, 2)
        self.right_recommend_layout.addWidget(self.recommend_button_4, 0, 3)
        self.right_recommend_layout.addWidget(self.recommend_button_5, 0, 4)

        self.right_layout.addWidget(self.right_recommend_label, 1, 0, 1, 9)
        self.right_layout.addWidget(self.right_recommend_widget, 2, 0, 2, 9)


        # 美化窗口部件
        self.left_close.setFixedSize(15, 15)  # 设置关闭按钮的大小
        self.left_visit.setFixedSize(15, 15)  # 设置按钮大小
        self.left_mini.setFixedSize(15, 15)  # 设置最小化按钮大小

        self.left_close.setStyleSheet('''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
        self.left_visit.setStyleSheet('''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
        self.left_mini.setStyleSheet('''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')

        self.left_close.clicked.connect(self.close_window)  # 为按钮设置槽函数
        self.left_visit.clicked.connect(self.enlarge_window)  # 为按钮设置槽函数

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框

        # 设置左侧按钮的样式
        self.left_widget.setStyleSheet('''
          QPushButton{border:none;color:white;}
          QPushButton#left_label{
            border:none;
            border-bottom:1px solid white;
            font-size:18px;
            font-weight:700;
            font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
          }
          QPushButton#left_button:hover{border-left:4px solid red;font-weight:700;}
        ''')

        # 右侧的部件的右上角和右下角需要先行处理为圆角的，同时背景设置为白色。对推荐模块、音乐列表模块和音乐歌单模块的标题我们也需要对其字体进行放大处理
        self.right_widget.setStyleSheet('''
          QWidget#right_widget{
            color:#232C51;
            background:white;
            border-top:1px solid darkGray;
            border-bottom:1px solid darkGray;
            border-right:1px solid darkGray;
            border-top-right-radius:10px;
            border-bottom-right-radius:10px;
          }
          QLabel#right_lable{
            border:none;
            font-size:16px;
            font-weight:700;
            font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
          }
        ''')

        # 对其他的几个按钮进行样式修改



        # 设置窗口透明
        self.setWindowOpacity(0.9)  # 设置窗口透明度
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明

        self.right_recommend_widget.setStyleSheet(
            '''
              QToolButton{border:none;}
              QToolButton:hover{border-bottom:2px solid #FFFFFF;}
            ''')

        # 左侧部件的样式
        self.main_widget.setStyleSheet('''
        QWidget#left_widget{
        background:gray;
        border-top:1px solid white;
        border-bottom:1px solid white;
        border-left:1px solid white;
        border-top-left-radius:10px;
        border-bottom-left-radius:10px;
        }
        ''')

        self.main_layout.setSpacing(0)

        # 1.8 为按钮组内的按钮添加信号槽
        self.left_button_1.clicked.connect(self.slot_DNA)  # 为按钮组中序号为0的按钮建立信号槽，点击就会触发slot_AAA()函数
        self.left_button_2.clicked.connect(self.slot_RNA)  # 为按钮组中序号为1的按钮建立信号槽，点击就会触发slot_BBB()函数
        self.left_button_3.clicked.connect(self.slot_Protein)  # 为按钮组中序号为2的按钮建立信号槽，点击就会触发slot_CCC()函数
        self.left_button_4.clicked.connect(self.slot_IT)  # 为按钮组中序号为1的按钮建立信号槽，点击就会触发slot_BBB()函数
        self.left_button_5.clicked.connect(self.slot_Product)  # 为按钮组中序号为2的按钮建立信号槽，点击就会触发slot_CCC()函数
        # 2.创建二级菜单栏
        # 2.1 创建多分页窗口
        self.stackedWidget_func = QtWidgets.QStackedWidget(self)  # QStackedWidget表示多分页的窗口
        self.stackedWidget_func.setObjectName("stackedWidget_func")
        self.stackedWidget_func.setGeometry(QtCore.QRect(220, 80, 700, 600))
        self.stackedWidget_func.setStyleSheet("QWidget{background-color:rgb(255, 255, 255);border:none}")

        # 2.2 创建分页对象，并载入分页
        self.page_1 = page2.DNA_Page()
        self.stackedWidget_func.addWidget(self.page_1)
        self.page_2 = page2.RNA_Page()
        self.stackedWidget_func.addWidget(self.page_2)
        self.page_3 = page2.Protein_Page()
        self.stackedWidget_func.addWidget(self.page_3)
        self.page_4 = page2.IonTolerance_Page()
        self.stackedWidget_func.addWidget(self.page_4)
        self.page_5 = page2.Development_Page()
        self.stackedWidget_func.addWidget(self.page_5)

    # 关闭窗口按钮的槽函数
    def close_window(self):
        self.close()

    def enlarge_window(self):
        # 获取当前窗口的大小
        '''current_width = self.width()
        current_height = self.height()

        # 增加窗口的大小
        new_width = current_width + 50
        new_height = current_height + 50

        # 更新窗口的大小
        self.resize(new_width, new_height)'''
        '''screen = QDesktopWidget().screenGeometry()
        width = screen.width()
        height = screen.height()
        self.setFixedSize(width, height)'''

    # 以下两个是鼠标拖动窗口移动的函数
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self._drag_position = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(event.globalPos() - self._drag_position)
            event.accept()

    # 以下定义一级菜单按钮响应函数
    def slot_DNA(self):
        self.stackedWidget_func.setCurrentIndex(0)  # 将多页面窗口切换至页面序号0
    def slot_RNA(self):
        self.stackedWidget_func.setCurrentIndex(1)  # 将多页面窗口切换至页面序号0
    def slot_Protein(self):
        self.stackedWidget_func.setCurrentIndex(2)  # 将多页面窗口切换至页面序号0
    def slot_IT(self):
        self.stackedWidget_func.setCurrentIndex(3)  # 将多页面窗口切换至页面序号0
    def slot_Product(self):
        self.stackedWidget_func.setCurrentIndex(4)  # 将多页面窗口切换至页面序号0

def main():
    app = QtWidgets.QApplication(sys.argv)
    gui = MainUi()
    gui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()