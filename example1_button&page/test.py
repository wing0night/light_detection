import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # 创建窗口
    window = QWidget()
    window.setWindowTitle('My First PyQt5 Window')
    window.setGeometry(100, 100, 300, 200)
    window.show()

    sys.exit(app.exec_())

'''在这个例子中，我首先导入了QApplication和QWidget类。
然后，我在if __name__ == '__main__':语句块中创建了一个QApplication对象，
并设置了窗口的标题、位置和大小。最后，通过调用show()方法显示窗口，
并通过调用app.exec_()启动应用程序的事件循环。
'''