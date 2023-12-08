import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QGraphicsScene, QGraphicsView
from PyQt5.QtCore import Qt, QPointF
from PyQt5.QtGui import QPainter, QColor
import random

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle("Random Circles")
        
        self.pushButton = QPushButton(self)
        self.pushButton.setGeometry(150, 120, 100, 30)
        self.pushButton.setText("Draw Circle")
        self.pushButton.clicked.connect(self.draw_circle)
        
        self.graphicsView = QGraphicsView(self)
        self.graphicsView.setGeometry(50, 50, 300, 200)
        self.scene = QGraphicsScene(self.graphicsView)
        self.graphicsView.setScene(self.scene)
        
    def draw_circle(self):
        diameter = random.randint(10, 100)
        x = random.randint(0, self.graphicsView.width() - diameter)
        y = random.randint(0, self.graphicsView.height() - diameter)
        color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        
        painter = QPainter()
        painter.begin(self.graphicsView.viewport())
        painter.setBrush(color)
        painter.drawEllipse(QPointF(x, y), diameter, diameter)
        painter.end()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
