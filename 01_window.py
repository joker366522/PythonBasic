import tkinter as tk

root = tk.Tk() # 创建窗体

def start_win():
    root.geometry('400x300')         # 设置窗体大小
    root.title("Basic_1_简单窗体")     # 设置窗体名称
    root.mainloop()                  # 窗体展示

if __name__ == '__main__':
    start_win()


