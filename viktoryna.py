# Напиши програму, яка задає питання з можливістю вибрати відповідь.

# 1. При запуску програми з'являється вікно розміром 400х200. Заголовок вікна - «Конкурс від Crazy People».

# 2. У вікні програми повинні бути віджети:
# - напис з питанням «В якому році канал отримав" золоту кнопку "від YouTube?»,
# - 4 перемикача з варіантами відповіді: «2005», «2010», «2015», «2020».
# Віджети повинні бути розташовані як на картинці.

# 3. При натисканні мишею:
# - На перемикач з написом «2005» має з'являтися нове вікно з повідомленням: «Правильно! Ви виграли гіроскутер».
# - На будь-який інший перемикач - вікно з повідомленням: «Ні, в 2015 році. Ви виграли фірмовий плакат».

# Програма повинна працювати до тих пір, поки користувач не натисне на «хрестик» вікна з питанням.


from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, 
                             QMessageBox, QRadioButton)

import time
def show_win():
    victory_win = QMessageBox()
    victory_win.setText("Ви виграли електросамокат")
    victory_win.exec_()

def show_lose():
    victory_win = QMessageBox()
    victory_win.setText("Повезе наступного разу")
    victory_win.exec_()

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Конкурс від Crazy People')
main_win.resize(400, 200)

question = QLabel('Якого року канал отримав «золоту кнопку» від YouTube?')
btn_answer1 = QRadioButton('2005')
btn_answer2 = QRadioButton('2010')
btn_answer3 = QRadioButton('2015')
btn_answer4 = QRadioButton('2020')

layout_main = QVBoxLayout()
layoutH1 = QHBoxLayout()
layoutH2 = QHBoxLayout()
layoutH3 = QHBoxLayout()

layoutH1.addWidget(question, alignment=Qt.AlignCenter)
layoutH2.addWidget(btn_answer1, alignment=Qt.AlignCenter)
layoutH2.addWidget(btn_answer2, alignment=Qt.AlignCenter)
layoutH3.addWidget(btn_answer3, alignment=Qt.AlignCenter)
layoutH3.addWidget(btn_answer4, alignment=Qt.AlignCenter)

layout_main.addLayout(layoutH1)
layout_main.addLayout(layoutH2)
layout_main.addLayout(layoutH3)

main_win.setLayout(layout_main)

btn_answer1.clicked.connect(show_lose)
btn_answer2.clicked.connect(show_lose)
btn_answer3.clicked.connect(show_win)
btn_answer4.clicked.connect(show_lose)

main_win.show()
app.exec_()