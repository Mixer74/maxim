from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from random import shuffle

app = QApplication([])
window = QWidget()

window.setWindowTitle('Почти тест')
window.resize(400, 400)

'''Создание виджетов'''
# виджеты основного окна
question = QLabel('Тут должен быть вопрос')
group_ans = QGroupBox('Варианты ответа')
group_res = QGroupBox('Результат')
baton = QPushButton('Ответить')

# виджеты для групбокса "Варианты ответа"
ans1 = QRadioButton('Ответ №1')
ans2 = QRadioButton('Ответ №2')
ans3 = QRadioButton('Ответ №3')
ans4 = QRadioButton('Ответ №4')

# виджеты для крупбокса "Результат"
res = QLabel('Правильно/Нет')
right_answer = QLabel('Правильный ответ')

'''Создаем шампуры'''
# создаем для главного окна
h1 = QHBoxLayout()
h2 = QHBoxLayout()
h3 = QHBoxLayout()
v1 = QVBoxLayout()

# линии для групбокса "Варианты ответа"
h4 = QHBoxLayout()
h5 = QHBoxLayout()
v2 = QVBoxLayout()

# линии для групбокса "Результат"
v3 = QVBoxLayout()


'''Сборка макета'''
# "Варианты ответа"
h4.addWidget(ans1)
h4.addWidget(ans2)
h5.addWidget(ans3)
h5.addWidget(ans4)

v2.addLayout(h4)
v2.addLayout(h5)

group_ans.setLayout(v2)

# Результат
v3.addWidget(res)
v3.addWidget(right_answer)

group_res.setLayout(v3)

# Основное окно
h1.addWidget(question)
h2.addWidget(group_ans)
h2.addWidget(group_res)
h3.addWidget(baton)


v1.addLayout(h1)
v1.addLayout(h2)
v1.addLayout(h3)

window.setLayout(v1)

group_res.hide()

def show_res():
    group_ans.hide()
    group_res.show()
    baton.setText('Максим????')

def show_ans():
    group_ans.show()
    group_res.hide()
    baton.setText('Ответить')

def analysis_click():
    if baton.text() == 'Ответить':
        check_ans()
    else:
        ask_que()

baton.clicked.connect(analysis_click)

class QueInfo:
    def __init__(self, question, right, wrong1, wrong2, wrong3):
        self.question = question
        self.right = right
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
lst_quest = []

qu_qu = QueInfo('Чему равно 2 + 2', '4', '2', '22', '0')
lst_quest.append(qu_qu)

qu_qu = QueInfo('Чему равно 1 м', '100 см', 'онзи кг', '5 литвов', '1000км')
lst_quest.append(qu_qu)

lst_ans = [ans1, ans2, ans3, ans4]

def ask_que():
    shuffle(lst_quest)
    que = lst_quest[0]

    shuffle(lst_ans)
    lst_ans[0].setText(que.right)
    lst_ans[1].setText(que.wrong1)
    lst_ans[2].setText(que.wrong2)
    lst_ans[3].setText(que.wrong3)

    question.setText(que.question)
    right_answer.setText(que.right)
    show_ans()

def check_ans():
    if lst_ans[0].isChecked:
        res.setText("ты не онзи")
        show_res()

    if lst_ans[1].isChecked() or lst_ans[2].isChecked() or lst_ans[3].isChecked():
        res.setText("ты онзи")
        show_res()

ask_que()

window.show()
app.exec_()
