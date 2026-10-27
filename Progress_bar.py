from PyQt6.QtWidgets import (QApplication, QWidget)
from PyQt6.QtGui import QPainter, QPen, QBrush, QFont, QColor
from PyQt6.QtCore import Qt, QRect

class Progress_bar(QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedHeight(80) 
        self.setMinimumWidth(800)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing, True)

        font = QFont("Arial", 16, 700)
        font2 = QFont("Arial", 11)
        painter.setPen(QPen(QColor("#6491bf"), 2, Qt.PenStyle.SolidLine))
        #painter.setBrush(QBrush(QColor("#6491bf"), Qt.BrushStyle.SolidPattern))
        painter.setBrush(QBrush(QColor("#6491bf"), Qt.BrushStyle.SolidPattern))

        rect = QRect(120,5,50,50)
        painter.drawEllipse(rect)
        painter.setFont(font)
        painter.setPen(Qt.GlobalColor.white)
        painter.drawText(rect, Qt.AlignmentFlag.AlignCenter, "1")

        text = QRect(70,40,150,50)
        painter.setPen(Qt.GlobalColor.black)
        painter.setFont(font2)
        painter.drawText(text, Qt.AlignmentFlag.AlignCenter, "Booking Details")

        painter.setPen(QPen(QColor("#6491bf"), 2, Qt.PenStyle.SolidLine))
        painter.drawLine(180, 30, 350, 30)

        painter.setPen(QPen(QColor("#6491bf"), 2, Qt.PenStyle.SolidLine))
        #painter.setBrush(QBrush(QColor("#6491bf"), Qt.BrushStyle.SolidPattern))
        painter.setBrush(QBrush(QColor("#6491bf"), Qt.BrushStyle.SolidPattern))
        
        rect = QRect(360,5,50,50)
        painter.drawEllipse(rect)
        painter.setFont(font)
        painter.setPen(Qt.GlobalColor.white)
        painter.drawText(rect, Qt.AlignmentFlag.AlignCenter, "2")

        text = QRect(310,40,150,50)
        painter.setPen(Qt.GlobalColor.black)
        painter.setFont(font2)
        painter.drawText(text, Qt.AlignmentFlag.AlignCenter, "Confirmation")

        painter.setPen(QPen(QColor("#6491bf"), 2, Qt.PenStyle.SolidLine))
        painter.drawLine(420, 30, 590, 30)

        painter.setPen(QPen(QColor("#6491bf"), 2, Qt.PenStyle.SolidLine))
        #painter.setBrush(QBrush(QColor("#6491bf"), Qt.BrushStyle.SolidPattern))
        painter.setBrush(QBrush(QColor("#6491bf"), Qt.BrushStyle.SolidPattern))

        rect = QRect(600,5,50,50)
        painter.drawEllipse(rect)
        painter.setFont(font)
        painter.setPen(Qt.GlobalColor.white)
        painter.drawText(rect, Qt.AlignmentFlag.AlignCenter, "3")

        text = QRect(550,40,150,50)
        painter.setPen(Qt.GlobalColor.black)
        painter.setFont(font2)
        painter.drawText(text, Qt.AlignmentFlag.AlignCenter, "Success")

        painter.end()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = Progress_bar()
    window.show()
    sys.exit(app.exec())


        