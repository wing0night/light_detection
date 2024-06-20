from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QLineEdit


class EditableTableWidget(QTableWidget):
    def __init__(self, rows, columns):
        super().__init__(rows, columns)

        self.cellClicked.connect(self.edit_cell)

    def edit_cell(self, row, column):
        cell_widget = QLineEdit(self.item(row, column).text())
        self.setCellWidget(row, column, cell_widget)
        cell_widget.editingFinished.connect(lambda: self.update_cell(row, column, cell_widget.text()))

    def update_cell(self, row, column, value):
        self.setItem(row, column, QTableWidgetItem(value))
        self.cellWidget(row, column).deleteLater()


app = QApplication([])
main_window = QMainWindow()

table_widget = EditableTableWidget(3, 2)
table_widget.setHorizontalHeaderLabels(["列1", "列2"])

table_widget.setItem(0, 0, QTableWidgetItem("行1列1"))
table_widget.setItem(0, 1, QTableWidgetItem("行1列2"))

main_window.setCentralWidget(table_widget)
main_window.show()

app.exec_()