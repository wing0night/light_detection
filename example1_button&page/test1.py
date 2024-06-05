import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QInputDialog, QFileDialog, QLabel, QVBoxLayout, QPushButton


def show_message_box():
    QMessageBox.information(window, 'Message', 'Hello World!')


def show_input_dialog():
    text, ok = QInputDialog.getText(window, 'Input', 'Enter your name:')
    if ok and text:
        label.setText(f'Hello, {text}!')


def show_file_dialog():
    filename, _ = QFileDialog.getOpenFileName(window, 'Open File', '', 'Text files (*.txt)')
    if filename:
        with open(filename, 'r') as file:
            content = file.read()
            label.setText(content)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # 创建窗口
    window = QWidget()
    window.setWindowTitle('PyQt5 Dialog Example')
    window.setGeometry(100, 100, 300, 200)

    # 创建布局管理器
    layout = QVBoxLayout(window)

    # 添加标签
    label = QLabel('Hello World!')
    layout.addWidget(label)

    # 添加按钮
    message_button = QPushButton('Show Message Box')
    message_button.clicked.connect(show_message_box)
    layout.addWidget(message_button)

    input_button = QPushButton('Show Input Dialog')
    input_button.clicked.connect(show_input_dialog)
    layout.addWidget(input_button)

    file_button = QPushButton('Show File Dialog')
    file_button.clicked.connect(show_file_dialog)
    layout.addWidget(file_button)

    window.show()

    sys.exit(app.exec_())