import tkinter as tk
from tkinter import messagebox # 必须要引用子模块，否则无法识别messagebox
from tkinter import filedialog

class Form:
    def __init__(self):
        self.root = tk.Tk()                     # 创建窗体
        # self.root.geometry('400x300')           # 设置窗体大小
        self.root.title("Basic_5_滚动条实现")     # 设置窗体名称

        self.create_scale()                     # 滚动条创建函数
        self.create_form()                      # 组件布局函数
        self.root.mainloop()                    # 窗体展示

    def create_scale(self):
        self.scale1 = tk.Scale(self.root, from_=0, to=30, tickinterval=1, length=600, orient="horizontal") # orient是滚动条横向

    def create_form(self):
        self.scale1.pack()


if __name__ == '__main__':
    Form()