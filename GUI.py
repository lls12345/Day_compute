import tkinter
import tkinter.messagebox


class ComputeDay(object):
    def __init__(self):
        self.root = tkinter.Tk()
        # 创建主窗口，用于容纳其他组件
        self.root.title('天数计算器')
        # 窗口名称
        self.label_1 = tkinter.Label(self.root, text='请输入年份:')
        self.year_input = tkinter.Entry(self.root, width=25)
        # 输入并设置尺寸
        self.label_2 = tkinter.Label(self.root, text='请输入月份:')
        self.month_input = tkinter.Entry(self.root, width=25)
        self.label_3 = tkinter.Label(self.root, text='请输入日期:')
        self.day_input = tkinter.Entry(self.root, width=25)
        self.button = tkinter.Button(self.root, command=self.check_date, text='计算', width=10)
        self.display_result = tkinter.Listbox(self.root, width=30, height=4)

    def hit_me(self, count):
        L = ['', '年份', '月份', '日期']
        self.hit = tkinter.messagebox.showinfo(title='输入错误', message='请重新输入{}'.format(L[count]))

    def hit_me2(self):
        self.hit = tkinter.messagebox.showinfo(title='输入错误', message='该月没有{}号\n请重新输入'.format(self.day))

    def gui_arrange(self):
        self.label_1.grid(row=0, column=0, padx=10, )
        self.year_input.grid(row=0, column=1, padx=10, )
        self.label_2.grid(row=1, column=0, padx=10, )
        self.month_input.grid(row=1, column=1, padx=10, pady=5)
        self.label_3.grid(row=2, column=0, padx=10, pady=5)
        self.day_input.grid(row=2, column=1, padx=10, pady=5)
        self.button.grid(row=3, columnspan=2)
        self.display_result.grid(row=4, columnspan=2)

    def check_date(self):
        self.year = self.year_input.get()
        if not self.year.isdigit():  # 判断年数字是否正确
            self.hit_me(1)
        self.month = self.month_input.get()  # 判断月数字是否正确
        if not self.month.isdigit() or 1 < int(self.month) > 12:
            self.hit_me(2)
        self.day = self.day_input.get()
        if not self.day.isdigit():  # 判断日数字是否正确
            self.hit_me(3)
        s = 0
        if int(self.year) % 4 == 0 or int(self.year) % 400 == 0:  # 闰年
            self.days = ['', 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        else:  # 不是闰年
            self.days = ['', 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if int(self.day) > self.days[int(self.month)] or 1 < int(self.day) > 31:  # 日数字不正确
            self.hit_me2()
        else:
            s = sum(self.days[1:int(self.month)]) + int(self.day)
            for item in range(10):
                self.display_result.insert(0, "")
            self.display_result.insert(0, s)  # 为回显列表赋值


def main():
    cd = ComputeDay()
    cd.gui_arrange()
    cd.year_input.get()
    tkinter.mainloop()


if __name__ == '__main__':
    main()
