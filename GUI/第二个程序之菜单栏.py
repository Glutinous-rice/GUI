import sys
from PyQt5.QtWidgets import QApplication , QMainWindow , QAction
from PyQt5.QtGui import QIcon

class Gui(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUi()      #初始化initUi

    def initUi(self):
        self.setWindowTitle('菜单栏')
        self.setGeometry(200,300,400,500)
        self.setWindowIcon(QIcon('Love.png'))
        self.statusBar().showMessage('文本状态栏')

        menu = self.menuBar()     #设置菜单栏
        file_menu = menu.addMenu('文件')
        file_menu.addSeparator()            #设置分割线
        edit_menu = menu.addMenu('修改')

         # 设置一个行为
        new_action = QAction('新的文件',self)    # 需要加入self参数，不然会出错
        new_action.setStatusTip('打开新的文件')
        # 把行为添加到file_menu中
        file_menu.addAction(new_action)

        exit_action = QAction('退出',self)       # exit_action = QAction('退出',self)

        exit_action.setStatusTip('点击退出程序')
        exit_action.triggered.connect(self.close)
        exit_action.setShortcut('ctrl+Q')
        file_menu.addAction(exit_action)


if __name__ == '__main__':
    app=QApplication(sys.argv)
    gui=Gui()
    gui.show()
    sys.exit(app.exec_())

