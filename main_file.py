import sys
from PyQt5 import QtCore, QtGui, QtWidgets
SIZE = 9
sizeby3 = int(SIZE/3)
class LoadTable(QtWidgets.QTableWidget):
    def __init__(self, parent=None):
        super(LoadTable, self).__init__(SIZE, SIZE, parent)
        
        self.setFont(QtGui.QFont("Helvetica", 10, QtGui.QFont.Bold, italic=False))   

        self.verticalHeader().hide()
        self.horizontalHeader().setHighlightSections(False)
        self.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Fixed)

        self.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        for r in range(SIZE):
            self.setColumnWidth(r, 40)

        combox_lay = QtWidgets.QLabel(self)
        self.setCellWidget(0, SIZE, combox_lay)
        # self.cellChanged.connect(self._row)


    def _row(self):
        read      = [[0 for i in range(SIZE)] for i in range(SIZE)]
        row_check = [[False for i in range(SIZE)] for i in range(SIZE) ]
        col_check = [[False for i in range(SIZE)] for i in range(SIZE) ]
        box_check = [[[False for i in range(SIZE)] for i in range(sizeby3)] for i in range(sizeby3)]
        

        # cpp file (data)

        for r in range(SIZE):
            for c in range(SIZE):
                it = self.item(r,c)
                if it:
                    text = it.text()
                    if text=='':
                        read[r][c] = 0
                    else :
                        read[r][c] = int(text)

        def solver(i,j):
            i,j = int(i),int(j)
            if i==SIZE:
                return True
            nextRow,nextCol = int((SIZE*i+j+1)/SIZE),int((SIZE*i+j+1)%SIZE)
            
            if read[i][j]!=0:
                return solver(nextRow,nextCol)
            
            for val in range(1,SIZE+1):
                if (row_check[i][val-1] or col_check[j][val-1] or box_check[int(i/sizeby3)][int(j/sizeby3)][val-1]):
                    continue
                row_check[i][val-1] = True
                col_check[j][val-1] = True
                box_check[int(i/sizeby3)][int(j/sizeby3)][val-1] = True
                read[i][j] = val
                if solver(nextRow , nextCol)==True:
                    return True
                row_check[i][val-1] = False
                col_check[j][val-1] = False
                box_check[int(i/sizeby3)][int(j/sizeby3)][val-1] = False
                read[i][j] = 0
            
            return False
        
        def solveSudoku(read):
            for r in range(SIZE):
                for c in range(SIZE):
                    if read[r][c] != 0:
                        col_check[c][read[r][c]-1] = True
                        row_check[r][read[r][c]-1] = True
                        box_check[int(r/sizeby3)][int(c/sizeby3)][read[r][c]-1] = True

            return solver(0,0)

        check = solveSudoku(read)

        if check==True:
            for r in range(SIZE):
                for c in range(SIZE):
                    self.setItem(r,c,QtWidgets.QTableWidgetItem(str(read[r][c])))      
        else:
            for r in range(SIZE):
                for c in range(SIZE):
                    self.setItem(r,c,QtWidgets.QTableWidgetItem(str(0)))      

    def _reset(self):
        for r in range(SIZE):
                for c in range(SIZE):   
                    self.setItem(r,c,QtWidgets.QTableWidgetItem(''))              



class ThirdTabLoads(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(ThirdTabLoads, self).__init__(parent)    
        # combo = QtWidgets.QComboBox()
        # combo.addItems(["9","16"])
        # role = combo.currentData()
        # print(role)        
        table = LoadTable()
        submit_button = QtWidgets.QPushButton("Submit")
        submit_button.clicked.connect(table._row)

        reset_button = QtWidgets.QPushButton("RESET")
        reset_button.clicked.connect(table._reset)

        button_layout = QtWidgets.QVBoxLayout()
        button_layout.addWidget(submit_button, alignment=QtCore.Qt.AlignTop)
        button_layout.addWidget(reset_button, alignment=QtCore.Qt.AlignTop)
        # button_layout.addWidget(combo, alignment=QtCore.Qt.AlignTop)
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