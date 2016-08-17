from PyQt5.QtWidgets import QApplication
import sys
from game import Game
from gui import GUI

def main():
    app = QApplication(sys.argv)
    game = Game()
    gui = GUI(game)
    gui.show()
    sys.exit(app.exec_())

main()