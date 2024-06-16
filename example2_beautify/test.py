from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QDoubleSpinBox, QPushButton

app = QApplication([])
window = QWidget()

grid_layout = QGridLayout(window)

# 定义一个数组来存储输入的浮点数
float_numbers = []

# 添加浮点数输入框和测定按钮到表格布局中
for row in range(6):
    spin_box = QDoubleSpinBox()
    button = QPushButton("测定")

    # 将测定按钮与对应的浮点数输入框关联
    button.clicked.connect(lambda checked, row=row: measure_value(row))

    grid_layout.addWidget(spin_box, row, 0)
    grid_layout.addWidget(button, row, 1)

    # 将浮点数输入框添加到数组中
    float_numbers.append(spin_box)

# 测定按钮的槽函数，将输入的浮点数添加到数组中
def measure_value(row):
    value = float_numbers[row].value()
    float_numbers[row].setEnabled(False)  # 禁用输入框，防止重复测定
    print("测定结果：", value)
    for row in range(6):
        print(float_numbers[row].value())


window.setLayout(grid_layout)
window.show()
app.exec_()