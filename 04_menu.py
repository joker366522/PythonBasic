import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.pylab import mpl

mpl.rcParams['font.sans-serif'] = ['SimHei']  # 中文显示
mpl.rcParams['axes.unicode_minus'] = False    # 负号显示

class Form:
    def __init__(self):
        self.root = tk.Tk()                         # 创建窗体
        self.root.geometry('600x450')               # 设置窗体大小
        self.root.title("Basic_4_菜单实现")          # 设置窗体名称
        self.root.iconbitmap("source\snoopy.ico")   # 设置窗体logo

        self.menu = tk.Menu(self.root)              # 创建一个菜单
        self.create_menu(self.menu)                 # 设置菜单

        self.root.mainloop()                    # 窗体展示

    def create_menu(self, menu):
        labelList = ['参数设置', '数据导入', '系统辨识', '调参模拟', '退出']
        acceleratorList = ['Ctrl+N', 'Ctrl+O', 'Ctrl+O', 'Ctrl+O', 'Ctrl+O']

        for i in range(5):
            menu.add_command(label=labelList[i], accelerator=acceleratorList[i])

        self.root.config(menu = menu)

if __name__ == '__main__':
    Form()
