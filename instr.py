# write a code for saving text instructions for the app
from PyQt5.QtCore import Qt
from PyQt5 import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel
app = QApplication([])
txt_hello = 'Selamat datang di program deteksi status kesehatan!'
txt_title = 'health'
txt_next = 'start'
txt_instruction = 'This application allows you to use the Rufier test to make an initial diagnosis of your health. The Rufier test is a set of physical exercises designed to assess your cardiac performance during physical exertion. The subject lies in the supine position for 5 minutes and has their pulse rate measured for 15 seconds; then, within 45 seconds, the subject performs 30 squats. When the exercise ends, the subject lies down and their pulse is measured again for the first 15 seconds and then for the last 15 seconds of the first minute of the recovery period. Important! If you feel unwell during the test (dizziness, tinnitus, shortness of breath, etc.), stop the test and consult a physician.'
win_width, win_height= 1000, 600
win_x, win_y= 200, 100