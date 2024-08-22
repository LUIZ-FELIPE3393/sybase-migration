from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from sample.widgets_example import WidgetGallery

app = QApplication([])
window = WidgetGallery()
layout = QVBoxLayout()
layout.addWidget(QPushButton('Top'))
layout.addWidget(QPushButton('Bottom'))
window.setLayout(layout)
window.show()
app.exec()