from tkinter import *
from ID2 import *
class IDCheckGUI:
    def __init__(self):
        self.frame = Tk()
        self.frame.title("身份证校验")
        self.frame.geometry("700x450+200+200")
        self.frame["bg"] = "lightblue"

        # 图片
        self.image = PhotoImage(file="E://pycharm/python/venv/身份证验证/jingcha.png")
        self.Label_image = Label(self.frame, image=self.image)
        self.Label_image.place(x=10, y=20)

    # 校验表单
        self.Label_is_input = Label(self.frame, text="请输入身份证号码：", font=("微软雅黑", 14, "bold"), bg="navy", fg="lightblue")
        self.Label_is_input.place(x=321, y=20)

        self.Entry_is_input = Entry(self.frame , width=21, font=("微软雅黑", 16, "bold"))
        self.Entry_is_input.place(x=320, y=58)

        self.Button_is_input = Button(self.frame, width=10,command= self.get_info, text="校验", font=("微软雅黑", 10, "bold"), bg="#eee")
        self.Button_is_input.place(x=600, y=58)

    # 显示表单
        #1
        self.Label_id_exits = Label(self.frame, text="是否有效：", font=("微软雅黑", 14, "bold"), fg="navy", bg="lightblue")
        self.Label_id_exits.place(x=320, y=150)

        self.e = Variable()
        self.e.set('')
        self.Entry_id_exits = Entry(self.frame,textvariable = self.e, width=8, state=DISABLED, font=("微软雅黑", 14, "bold"))
        self.Entry_id_exits.place(x=420, y=150)

        #2
        self.Label_id_gender = Label(self.frame, text="性别：", font=("微软雅黑", 14, "bold"), fg="navy", bg="lightblue")
        self.Label_id_gender.place(x=358, y=210)

        self.e1 = Variable()
        self.e1.set('')
        self.Entry_id_gender = Entry(self.frame, textvariable = self.e1,width=8, state=DISABLED, font=("微软雅黑", 14, "bold"))
        self.Entry_id_gender.place(x=420, y=210)

        #3
        self.Label_id_birthday = Label(self.frame, text="出生日期：", font=("微软雅黑", 14, "bold"), fg="navy", bg="lightblue")
        self.Label_id_birthday.place(x=320, y=270)

        self.e2 = Variable()
        self.e2.set('')
        self.Entry_id_birthday = Entry(self.frame, textvariable = self.e2,width=20, state=DISABLED, font=("微软雅黑", 14, "bold"))
        self.Entry_id_birthday.place(x=420, y=270)

        #4
        self.Label_id_area = Label(self.frame, text="所在地：", font=("微软雅黑", 14, "bold"), fg="navy", bg="lightblue")
        self.Label_id_area.place(x=338, y=330)

        self.e3 = Variable()
        self.e3.set('')
        self.Entry_id_area = Entry(self.frame, textvariable = self.e3,width=20, state=DISABLED, font=("微软雅黑", 14, "bold"))
        self.Entry_id_area.place(x=420, y=330)

        self.Button_close = Button(self.frame, width=10, text="关闭",command = self.quit,font=("微软雅黑", 10, "bold"), bg="#eee")
        self.Button_close.place(x=550, y=390)
        self.show()
    def quit(self):
        self.frame.destroy()
    def show(self):
        self.frame.mainloop()
    def get_info(self):
        a = self.Entry_is_input.get()
        if len(a) == 18:

            b = ID(a)
            if b.lists[0] == '无效':
                self.e.set(b.lists[0])
                self.e1.set('')
                self.e2.set('')
                self.e3.set('')
            else:
                self.e.set(b.lists[0])
                self.e1.set(b.lists[1])
                self.e2.set(b.lists[2])
                self.e3.set(b.lists[3])
        else:
            self.e.set('无效')
            self.e1.set('')
            self.e2.set('')
            self.e3.set('')
idc = IDCheckGUI()
