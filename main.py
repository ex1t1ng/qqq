import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt
import random


class Circle:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color


class CirclesWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.circles = []

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.button = QPushButton("Create Circle")
        self.button.clicked.connect(self.create_circle)
        layout.addWidget(self.button)

    def create_circle(self):
        x = random.randint(10, 390)
        y = random.randint(10, 390)
        radius = random.randint(10, 50)
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        circle = Circle(x, y, radius, color)
        self.circles.append(circle)
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        for circle in self.circles:
            painter.setPen(Qt.NoPen)
            painter.setBrush(QColor(*circle.color))
            painter.drawEllipse(circle.x - circle.radius, circle.y - circle.radius, circle.radius * 2, circle.radius * 2)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Random Circles")
        self.setGeometry(100, 100, 400, 400)

        self.circles_widget = CirclesWidget()
        self.setCentralWidget(self.circles_widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
