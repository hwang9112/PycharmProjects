import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QMainWindow, QLCDNumber, QLineEdit, QLabel, QTextEdit
from PyQt5.QtCore import QCoreApplication
from random import randrange





class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.resulttext = ""
        self.i = 1
        self.okButton = QPushButton('굴리기',self)
        self.cancelButton = QPushButton('취소')
        self.Start_range = QLineEdit()
        self.End_range = QLineEdit()
        # Range_label = QLabel("범위입력",self)
        self.lcd = QLCDNumber(self)
        self.Result_List = QTextEdit()

        self.Result_List.setAcceptRichText(False)
        self.Result_List.setText("11111111111111")

        self.Start_range.setText("0")
        self.End_range.setText("1")

        self.okButton.clicked.connect(self.okbtn_click)
        self.cancelButton.clicked.connect(QCoreApplication.instance().quit)


        range_box = QHBoxLayout()
        range_box.addStretch(1)
        range_box.addWidget(self.Start_range)
        range_box.addWidget(self.End_range)
        range_box.addStretch(1)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.okButton)
        hbox.addWidget(self.cancelButton)
        hbox.addWidget(self.Result_List)
        hbox.addStretch(1)

        lcd_box = QHBoxLayout()
        lcd_box.addStretch(1)
        lcd_box.addWidget(self.lcd)
        lcd_box.addStretch(1)

        result_box = QHBoxLayout()
        result_box.addStretch(3)
        result_box.addLayout(lcd_box)
        result_box.addWidget(self.Result_List)
        result_box.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        vbox.addLayout(range_box)
        vbox.addLayout(result_box)
        vbox.addStretch(1)

        self.setLayout(vbox)

        self.setWindowTitle('랜덤 숫자 뽑기')
        self.setGeometry(300, 300, 300, 200)
        self.show()


    def okbtn_click(self):
        randnum = randrange(int(self.Start_range.text()), int(self.End_range.text()) + 1)
        self.lcd.display(int(randnum))
        self.resulttext += str(self.i) + "번째 결과값 : " + str(randnum) + "\n"
        self.Result_List.setText(self.resulttext)
        self.i += 1



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())