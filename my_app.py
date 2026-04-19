# write the code for main app and first screen
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import(
    QApplication,QWidget,QHBoxLayout,QVBoxLayout, QGroupBox, QRadioButton,QPushButton,QLabel
    ,QListWidget,QLineEdit)
from instr import*
from second_win import*

txt_hello = 'Selamat datang di program deteksi status kesehatan'
txt_title = 'health'
txt_next = 'start'
txt_instruction = 'This application allows you to use the Rufier test to make an initial diagnosis of your health. The Rufier test is a set of physical exercises designed to assess your cardiac performance during physical exertion. The subject lies in the supine position for 5 minutes and has their pulse rate measured for 15 seconds; then, within 45 seconds, the subject performs 30 squats. When the exercise ends, the subject lies down and their pulse is measured again for the first 15 seconds and then for the last 15 seconds of the first minute of the recovery period. Important! If you feel unwell during the test (dizziness, tinnitus, shortness of breath, etc.), stop the test and consult a physician.'
win_width, win_height= 1000, 600
win_x, win_y= 200, 100
class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.connects()
        self.set_appear()
        self.show()
    def initUI(self):
        self.btn_next = QPushButton(txt_next, self)
        self.hello_text = Qlabel(txt_hello)
        self.instruction = QLabel(txt_instruction)
        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.hello_text, alignment = Qt.AlignLeft)
        self.layout_line.addWidget(self.instruction, alignment = Qt.AlignLeft)
        self.layout_line.addWidget(self.btn_next, alignment = Qt.AlignCenter)
        self.setLayout(self.layout_line)
    def next_click(self):
        self.tw = TestWin()
        self.hide()
    def connects(self):
        self.btn_next.clicked.connect(self.next_click)
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

app = QApplication([])
mw = MainWin()
app.exec_()