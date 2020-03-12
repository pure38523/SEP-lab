import sys
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

class Simple_drawing_window3(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)
        self.setWindowTitle("T's Drawing")
        self.jojo = QPixmap("image/jojo.png")

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)
        p.drawPixmap(QRect(120,100,200,200), self.jojo)
        p.end()

def main():
    app = QApplication(sys.argv)
    t = Simple_drawing_window3()
    t.show()

    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())