import tkinter as tk
from tkinter import messagebox # 必须要引用子模块，否则无法识别messagebox
from tkinter import filedialog

class Form:
    def __init__(self):
        self.root = tk.Tk()                     # 创建窗体
        self.root.geometry('400x300')           # 设置窗体大小
        self.root.title("Basic_2_窗体类实现")     # 设置窗体名称

        self.create_button()                    # 按钮创建函数
        self.create_form()                      # 组件布局函数
        self.root.mainloop()                    # 窗体展示

    def create_button(self):
        self.btn_info = tk.Button(text="提示信息", height=2, command=self.fun_btnInfo)  # 消息提示按钮
        self.btn_warning = tk.Button(text="警告信息", height=2, command=self.fun_btnWarning)  # 消息提示按钮
        self.btn_error = tk.Button(text="错误信息", height=2, command=self.fun_btnError)  # 消息提示按钮
        self.btn_openFile = tk.Button(text="打开文件管理器", height=2, command=self.fun_btnOpenFile)
        self.btn_close = tk.Button(text="关闭窗口", height=2, command=self.fun_btnClose)  # 关闭窗体

    def fun_btnInfo(self):
        messagebox.showinfo("提示信息", "这是一条自主设置的提示信息")

    def fun_btnWarning(self):
        messagebox.showwarning("警告信息", "这是一条自主设置的警告信息")

    def fun_btnError(self):
        messagebox.showerror("错误信息", "这是一条自主设置的错误信息")

    def fun_btnOpenFile(self):
        file_path = filedialog.askopenfilename() # 获取文件地址
        file_type = file_path.split(".")[1] # 获取文件后缀名
        if file_type in ["xlsx", "xls"]: # 通过文件后缀判断是否为希望选择的文件
            messagebox.showinfo("提示", '选择完成')
        else:
            messagebox.showerror('错误', '选择的文件不是excel文件')

    def fun_btnClose(self):
        self.root.destroy()

    def create_form(self):
        self.btn_info.pack()
        self.btn_warning.pack()
        self.btn_error.pack()
        self.btn_openFile.pack()
        self.btn_close.pack()

if __name__ == '__main__':
    Form()