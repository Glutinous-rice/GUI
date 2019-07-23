#第一次用Qt desiger 创建文件，并且转化成文件，在加入补充代码，然后运行


import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
import first   #导入生成的模块（文件）

if __name__ == '__main__':   #确保if一下的语句只在当前窗口下运行
    app=QApplication(sys.argv)    #创建一个应用（创建一个QAPPlication类实列）
    mainWindow=QMainWindow()      #创建一个主窗口
    ui = first.Ui_MainWindow()    #创建一个类实例， 文件名+类名
    ui.setupUi(mainWindow)        #向主窗口上添加控件，入口参数是mainWindow
    mainWindow.show()             #显示主窗口
    sys.exit(app.exec_())         #进入程序主循环，并通过exit()函数确保主循环安全退出

