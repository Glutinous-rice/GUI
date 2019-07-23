import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QWidget,QToolTip,QPushButton,QHBoxLayout
from PyQt5.Qt import QFont


class toolTip(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        QToolTip.setFont(QFont('SansSerif',12))
        self.setToolTip('今天是星期五')
        self.setGeometry(200,300,400,400)
        self.setWindowTitle('提示信息')

        self.button1=QPushButton('退出应用')
        self.button1.setToolTip('退出程序')
        layout=QHBoxLayout()
        layout.addWidget(self.button1)

        mainFrame=QWidget()
        mainFrame.setLayout(layout)
        self.setCentralWidget(mainFrame)



if __name__ == '__main__':
    app=QApplication(sys.argv)
    main=toolTip()
    main.show()
    sys.exit(app.exec_())

"""
ssssssssssssssssssssssssssssssssssssssssssss
111111111111111111111111111111111111111
"""