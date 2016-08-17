from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel
from PyQt5.QtCore import Qt
from math import log


class GUI(QWidget):

    def __init__(self, game):
        super().__init__()
        self.game = game  # instance of Game class, main game object
        self.size = len(self.game.field)
        self.spacing = 10  # visual spacing between cells
        self.cells_width = 50
        self.initGUI()

    def update_labels(self):
        # we actually have a copy of field that contains QLabels
        for i in range(self.size):
            for j in range(self.size):
                if self.game.field[i][j] is None:
                    self.labels[i][j].setText('')
                    self.labels[i][j].setStyleSheet(
                        'background-color: rgb(0, 50, 50);'+
                        'color: white;'
                    )
                else:
                    self.labels[i][j].setText(str(self.game.field[i][j]))
                    self.labels[i][j].setStyleSheet(
                        'background-color: rgb(%d, 50, 50); color: white;'
                        % int(255 * (log(self.game.field[i][j], 2) / log(2048, 2)))
                    )

    def initGUI(self):
        self.setWindowTitle('2048 game')
        g_size = (self.size + self.spacing) * 10 + self.size * self.cells_width
        self.resize(g_size, g_size)

        self.grid = QGridLayout()
        self.grid.setSpacing(self.spacing)

        self.labels = [[None] * self.size for _ in range(self.size)]

        for i in range(self.size):
            for j in range(self.size):
                self.labels[i][j] = QLabel()
                self.labels[i][j].setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                self.grid.addWidget(self.labels[i][j], i, j)

        self.update_labels()

        self.setLayout(self.grid)

    def keyPressEvent(self, e):
        if self.game.over: return
        self.game.move(e.key())
        # self.game.print_field() debug
        self.update_labels()

        if self.game.over:
            self.setWindowTitle('2048 game - you won')

        # TODO
        #   i didnt find good way to check if game is over, so - you just cant move