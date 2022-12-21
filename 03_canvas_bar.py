import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.pylab import mpl

mpl.rcParams['font.sans-serif'] = ['SimHei']  # 中文显示
mpl.rcParams['axes.unicode_minus'] = False  # 负号显示

class Form:
    def __init__(self):
        self.root = tk.Tk()                     # 创建窗体
        self.root.geometry('600x450')           # 设置窗体大小
        self.root.title("Basic_3_画布实现柱状图")  # 设置窗体名称

        self.canvas = tk.Canvas()               # 创建一个显示图形的画布
        self.figure = self.create_matplotlib()  # 返回matplotlib所画图形的figure对象

        self.create_form(self.figure)           # 组件布局函数
        self.root.mainloop()                    # 窗体展示

    def create_matplotlib(self):
        f = plt.figure() # 创建绘图对象
        fig1 = plt.subplot(1, 1, 1)  # 创建一副子图

        title = "柱状图示例--销售数据"
        x_label = "年度"
        y_label = "销售额"
        x_data = ["2017", "2018", "2019", "2020", "2021"]
        y_data = [2000, 3000, 4000, 5000, 6000]
        fig1.set_title(title)
        fig1.set_xlabel(x_label)  # 确定坐标轴标题
        fig1.set_ylabel(y_label)
        # fig1.set_ylim(0, 100) 设置纵坐标范围
        fig1.bar(x_data, y_data)  # 设置柱状图

        return f

    def create_form(self, figure):
        # 把绘制的图形显示到窗口中
        self.canvas = FigureCanvasTkAgg(figure, self.root)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack()

if __name__ == '__main__':
    Form()