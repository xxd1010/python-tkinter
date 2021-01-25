from tkinter import *
import string
import pretty_errors




class Function():

    def geometry(self, width, height):
        return f"{width}x{height}"


class MsgWindow(Frame):
    win_label = "通知"

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.create_widgets()
        self.pack()

    def create_widgets(self):

        pass


class Window(Frame):

    new_fun = Function()

    confrom_moji = "确认"
    cancel_moji = '取消'
    clear_moji = '清除'
    input_moji = '输入'

    Str = ''

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.create_widgets()
        self.pack(side='top')

    def create_widgets(self):



        self.label_1 = Label(self)
        self.label_1['text'] = '提示：'

        self.label_2 = Label(self)
        self.label_2['text'] = "hello"
        # 背景颜色
        # self.label_2['background'] = "white"
        # 宽度
        # self.label_2['width'] = 60



        self.output_text_box = Text(self)
        # 字体 (family:字体名, size:大小, weight:字重(normal/bold), slant:倾斜(roman/italic), underline:下划线(True/False), overstrike:删除线(True/False))
        self.output_text_box['font'] = ('Microsoft YaHei UI', 10)
        # 文本框高度 单位 行
        self.output_text_box['height'] = 5
        # 文本框宽度 单位 字符数
        self.output_text_box['width'] = 40
        self.output_text_box['wrap'] = 'word'
        self.output_text_box['borderwidth'] = 1
        # self.output_text_box['highlighthickness'] = 1
        self.output_text_box['highlightcolor'] = 'gray'
        self.output_text_box['highlightbackground'] = 'yellow'
        self.output_text_box['exportselection'] = 'no'
        self.output_text_box['selectbackground'] = 'blue'
        self.output_text_box['tabs'] = 2
        self.output_text_box['yscrollcommand'] = Scrollbar(
            self, orient=VERTICAL)

        self.input_text_box = Text(self)
        self.input_text_box['font'] = ('Microsoft YaHei UI', 10)
        self.input_text_box['height'] = 5
        self.input_text_box['width'] = 40
        self.input_text_box['wrap'] = 'word'
        self.input_text_box['borderwidth'] = 1
        self.input_text_box['highlightcolor'] = 'yellow'
        self.input_text_box['yscrollcommand'] = Scrollbar(
            self, orient=VERTICAL)


        self.confrom_button_1 = Button(self)
        self.confrom_button_1['text'] = self.confrom_moji
        # 要执行的命令
        self.confrom_button_1['command'] = self.confrom_event(self.output_text_box, self.label_2)

        self.input_button_1 = Button(self)
        self.input_button_1['text'] = "输入"
        self.input_button_1['command'] = self.input_text(
            self.input_text_box, self.output_text_box)


        self.cancel_button_1 = Button(self)
        self.cancel_button_1['text'] = self.cancel_moji
        self.cancel_button_1['command'] = self.cancel_event(self.label_2, self.output_text_box)


        self.clear_button_output = Button(self)
        self.clear_button_output['text'] = self.clear_moji
        self.clear_button_output['command'] = self.clear_event(self.output_text_box)


        self.clear_button_input = Button(self)
        self.clear_button_input['text'] = self.clear_moji
        self.clear_button_input['command'] = self.clear_event(self.input_text_box)



        # 部件在窗口里布局
        self.label_1.grid(row=0, column=0)
        self.label_2.grid(row=0, column=1)


        self.confrom_button_1.grid(row=2, column=0)
        self.cancel_button_1.grid(row=2, column=1)
        self.clear_button_output.grid(row=2, column=2)
        self.input_button_1.grid(row=4, column=0)
        self.clear_button_input.grid(row=4, column=1)


        # sticky=
        # 默认居中对齐
        # N 上对齐 S 下对齐 E 右对齐 W 左对齐
        # N+W
        self.output_text_box.grid(row=3, column=1)
        self.input_text_box.grid(row=3, column=2)

        # self.bind("<Button-1>",self.callback())


    def text_of_Element(self, Element):
        return f"{Element['text']}\n"



    def confrom_event(self, Text_Box, Label):
        # 根据text中有多少个\n判断有多少行
        row = (self.get_text(Text_Box)).count('\n')
        # 将光标移至最后一行
        Text_Box.mark_set('insert', "%d.0" % (row+1))
        if Label['text'] == "you clicked it" or Label['text'] == "you have clicked it":
            Label['text'] = "you have clicked it"
            Text_Box.insert('insert', self.text_of_Element(Label))
        else:
            Label['text'] = "you clicked it"
            Text_Box.insert('insert', self.text_of_Element(Label))



    # 取消事件
    def cancel_event(self, Label, Text_Box):
        Label['text'] = "you canceled"
        Text_Box.insert(
            'insert', self.text_of_Element(Label))



    # 清除文本框里的内容
    def clear_event(self, Text_Box):
        Text_Box.delete('0.0', 'end')



    # 传递文本框中输入的内容
    def input_text(self, Text_Box_1, Text_Box_2):
        self.Str = self.get_text(Text_Box_1)
        if self.Str != '':
            # 将输入的内容在文本框2里显示
            Text_Box_2.insert('insert', self.Str)
        else:
            Text_Box_2.insert('insert', '')
        self.Str = ''



    # 获取文本框的内容
    def get_text(self, Text_Box):
        return Text_Box.get('0.0', 'end')



    def focus_in(self, Element_1, Element_2):
        # self.bind("<Button-1>", )
        if Element_1.get('0.0', 'end') != '':
            Element_2['text'] = "正在输入..."


    # 空操作
    def do_nothing(self):
        pass


    def callback(self, event):
        return [event.x, event.y]


    def show_msg_win(self):

        width = 360
        height = 120

        root_msg = Tk()

        root_msg.wm_title("Msg")
        root_msg.geometry(self.new_fun.geometry(width, height))

        msg_win = MsgWindow(root_msg)
    


    def show_login_win(self):

        width = 300
        height = 350

        root_login = Tk()

        root_login.wm_title('login')
        root_login.geometry(self.new_fun.geometry(width, height))


if __name__ == "__main__":
    
    width_mainwin = 720
    height_mainwin = 540


    root = Tk()
    my_app = Window(root)

    menubar = Menu(root)
    menubar.add_command(label="登录", command=my_app.show_login_win)
    menubar.add_command(label="好友", command=my_app.show_msg_win)
    menubar.add_command(label="操作", command=my_app.show_msg_win)
    menubar.add_command(label="新窗口", command=my_app.show_msg_win)
    menubar["background"] = "blue"

    root.wm_title("My App")
    root.geometry(f"{width_mainwin}x{height_mainwin}")
    root.config(menu=menubar)

    root.mainloop()
