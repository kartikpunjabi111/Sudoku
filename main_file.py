import sys
from PyQt5 import QtCore, QtGui, QtWidgets
NO_OF_ROWS = 3
NO_OF_COLUMN = 3

class LoadTable(QtWidgets.QTableWidget):
    def __init__(self, parent=None):
        super(LoadTable, self).__init__(NO_OF_ROWS, NO_OF_COLUMN, parent)
        self.setFont(QtGui.QFont("Helvetica", 10, QtGui.QFont.Normal, italic=False))   

        self.verticalHeader().hide()
        self.horizontalHeader().setHighlightSections(False)
        self.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Fixed)

        self.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.setColumnWidth(0, 130)

        combox_lay = QtWidgets.QLabel(self)
        self.setCellWidget(0, NO_OF_COLUMN, combox_lay)
        # self.cellChanged.connect(self._row)

    def _row(self):
        row = self.rowCount()
        column = self.columnCount()
        read = [NO_OF_ROWS*NO_OF_COLUMN]
        for r in range(row):
            for c in range(column):
                it = self.item(r,c)
                if it:
                    text = it.text()
                    read[r*NO_OF_COLUMN+c] = text
                               

        #  Solve Sudoku (Main )


        answer  = ['1', '1', '1', '1', '1', '1', '1', '1', '1']

        # Set Values in table ()
        for r in range(row):
            for c in range(column):
                fill_this = answer[r*NO_OF_COLUMN+c]
                self.setItem(r,c,QtWidgets.QTableWidgetItem(fill_this))      


class ThirdTabLoads(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(ThirdTabLoads, self).__init__(parent)    

        table = LoadTable()

        submit_button = QtWidgets.QPushButton("Submit")
        submit_button.clicked.connect(table._row)


        button_layout = QtWidgets.QVBoxLayout()
        button_layout.addWidget(submit_button, alignment=QtCore.Qt.AlignTop)
        # button_layout.addWidget(delete_button, alignment=QtCore.Qt.AlignTop)
        # button_layout.addWidget(copy_button, alignment=QtCore.Qt.AlignTop)

        tablehbox = QtWidgets.QHBoxLayout()
        tablehbox.setContentsMargins(10, 10, 10, 10)
        tablehbox.addWidget(table)

        grid = QtWidgets.QGridLayout(self)
        grid.addLayout(button_layout, 0, 1)
        grid.addLayout(tablehbox, 0, 0)        


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = ThirdTabLoads()
    w.show()
    sys.exit(app.exec_())