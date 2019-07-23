import sys
from PyQt5.QtWidgets import QApplication,QMainWindow ,QDesktopWidget #导入窗口模块
from PyQt5.QtGui import QIcon        #导入图标模块

class Example(QMainWindow):
    def __init__(self):
        super().__init__()     # 继承Example的父类（QWidget）的属性
        self.initUi()
        self.center()

    def initUi(self):
        self.setWindowTitle('爱心')
        self.setGeometry(100,200,600,400) # setGeometry(x轴位置，y轴位置，窗口的宽度，窗口的高度)
        self.setWindowIcon(QIcon('Love.png'))   # 设置图标



    def center(self):
        screen=QDesktopWidget().screenGeometry()
        size=self.geometry()
        newTop=(screen.height()-size.height())/2
        newLeft=(screen.width()-size.width())/2
        self.move(newLeft,newTop)



if __name__=='__main__':        # 防止在被其他文件导入时显示多余的程序主体部分。
                                # 该语句之前的被导入到其他模块会被执行，语句之后的不会被执行
    app=QApplication(sys.argv)
    example=Example()
    example.show()  # 显示窗口
    sys.exit(app.exec_())    #在循环中断后，退出进程