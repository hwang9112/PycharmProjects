import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget,QPushButton, QMainWindow, QAction, qApp, QDesktopWidget
from PyQt5.QtCore import QCoreApplication

class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        btn = QPushButton('Quit', self)
        btn.setToolTip('Quit button <b> PUSH </b>')
        btn.move(150, 150)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(QCoreApplication.instance().quit)


        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)

        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        self.statusBar()

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)

        self.statusBar().showMessage('Ready')

        self.setWindowTitle('Practice')
        self.setWindowIcon(QIcon('Ico/web.png'))
        self.center()
        self.resize(500,500)
        self.show()

    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())