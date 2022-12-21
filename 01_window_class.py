import tkinter as tk

class Form:
    def __init__(self):
        self.root = tk.Tk()                     # 创建窗体
        self.root.geometry('400x300')           # 设置窗体大小
        self.root.title("Basic_2_窗体类实现")     # 设置窗体名称
        self.root.mainloop()                    # 窗体展示

if __name__ == '__main__':
    Form()
