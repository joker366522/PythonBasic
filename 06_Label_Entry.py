import tkinter as tk
from tkinter import *
from tkinter import messagebox # 必须要引用子模块，否则无法识别messagebox

class Form:
    def __init__(self):
        self.root = tk.Tk()                      # 创建窗体
        # self.root.geometry('400x300')          # 设置窗体大小
        self.root.title("Basic_6_文本输入及展示实现")     # 设置窗体名称
        self.answerStr = tk.StringVar()

        self.create_button()  # 按钮创建函数
        self.create_entry()                     # 输入框创建函数
        self.create_form()                      # 组件布局函数
        self.root.mainloop()                    # 窗体展示

    def create_button(self):
        self.btn_info = tk.Button(text="数据更新", height=2, command=self.fun_btnInfo)  # 消息提示按钮
    def fun_btnInfo(self):
        self.answerStr.set(self.E1.get())
        messagebox.showinfo("提示信息", "这是一条自主设置的提示信息")

    def create_entry(self):
        self.answerStr.set(str(1.00))
        self.L1 = Label(self.root, text="网站名")
        self.E1 = Entry(self.root, bd=5)
        self.L2 = Label(self.root, textvariable=self.answerStr)

    def create_form(self):
        self.L1.pack(side='left')
        self.btn_info.pack(side='right')
        self.L2.pack(side='right')
        self.E1.pack(side='right')


if __name__ == '__main__':
    Form()