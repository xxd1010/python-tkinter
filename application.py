from tkinter import *
import string
import pretty_errors

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

        self.text_box_1 = Text(self)
        # 字体 (family:字体名, size:大小, weight:字重(normal/bold), slant:倾斜(roman/italic), underline:下划线(True/False), overstrike:删除线(True/False))
        self.text_box_1['font'] = ('Microsoft YaHei UI', 10)
        # 文本框高度 单位 行
        self.text_box_1['height'] = 5
        # 文本框宽度 单位 字符数
        self.text_box_1['width'] = 20
        self.text_box_1['wrap'] = 'word'
        self.text_box_1['borderwidth'] = 1
        # self.text_box_1['highlighthickness'] = 1
        self.text_box_1['highlightcolor'] = 'gray'
        self.text_box_1['highlightbackground'] = 'yellow'
        self.text_box_1['exportselection'] = 'no'
        self.text_box_1['selectbackground'] = 'blue'
        self.text_box_1['tabs'] = 2
        self.text_box_1['yscrollcommand'] = Scrollbar(self, orient=VERTICAL)

        self.text_box_2 = Text(self)
        self.text_box_2['font'] = ('Microsoft YaHei UI', 10)
        self.text_box_2['height'] = 10
        self.text_box_2['width'] = 20
        self.text_box_2['wrap'] = 'word'
        self.text_box_2['borderwidth'] = 1
        self.text_box_2['highlightcolor'] = 'yellow'
        self.text_box_2['yscrollcommand'] = Scrollbar(self, orient=VERTICAL)



        self.confrom_button_1 = Button(self)
        self.confrom_button_1['text'] = self.confrom_moji
        # 要执行的命令
        self.confrom_button_1['command'] = self.confrom_event

        self.input_button_1 = Button(self)
        self.input_button_1['text'] = "输入"
        self.input_button_1['command'] = self.input_text

        self.cancel_button_1 = Button(self)
        self.cancel_button_1['text'] = self.cancel_moji
        self.cancel_button_1['command'] = self.cancel_event

        self.clear_button = Button(self)
        self.clear_button['text'] = self.clear_moji
        self.clear_button['command'] = self.clear_event(self.text_box_2)

        
        # 部件在窗口里布局
        self.label_1.grid(row=0, column=0)
        self.label_2.grid(row=0, column=1, sticky=W)

        self.confrom_button_1.grid(row=2, column=0)
        self.cancel_button_1.grid(row=2, column=1)
        self.clear_button_1.grid(row=2, column=2)
        self.input_button_1.grid(row=4, column=0, sticky=S)

        self.clear_button_2 = self.clear_button
        self.clear_button_2['command'] = self.clear_event(self.text_box_1)
        self.clear_button_2.grid(row=4, column=1)

        # sticky=
        # 默认居中对齐
        # N 上对齐 S 下对齐 E 右对齐 W 左对齐
        # N+W

        self.text_box_1.grid(row=3, column=0)
        self.text_box_2.grid(row=3, column=1)

        # self.bind("<Button-1>",self.callback())

    def content_of_Element(self, Element):
        return f"{Element['text']}\n"

    def confrom_event(self):
        # 根据text中有多少个\n判断有多少行
        row = self.text_box_2.get('0.0', 'end').count('\n')
        # 将光标移至最后一行
        self.text_box_2.mark_set('insert', "%d.0" % (row+1))
        if self.label_2['text'] == "you clicked it" or self.label_2['text'] == "you have clicked it":
            self.label_2['text'] = "you have clicked it"
            self.text_box_2.insert(
                'insert', self.content_of_Element(self.label_2))
        else:
            self.label_2['text'] = "you clicked it"
            self.text_box_2.insert(
                'insert', self.content_of_Element(self.label_2))

    # 取消事件
    def cancel_event(self):
        self.label_2['text'] = "you canceled"
        self.text_box_2.insert(
            'insert', self.content_of_Element(self.label_2))

    # 清除文本框里的内容
    def clear_event(self, Text_Box):
        Text_Box.delete('0.0', 'end')

    # 传递文本框中输入的内容
    def input_text(self):
        self.Str = self.text_box_1.get('0.0', 'end')
        if self.Str != '':
            # 将输入的内容在文本框2里显示
            self.text_box_2.insert('insert', self.Str)
        else:
            self.text_box_2.insert('insert', '')
        self.Str = ''

    def get_text(self, Element):
        return Element.get('0.0', 'end')

    def focus_in_text_box_2(self):
        # self.bind("<Button-1>", )
        if self.text_box_2.get('0.0', 'end') != '':
            self.confrom_button_1['text'] = "正在输入..."

    # 空操作
    def do_nothing(self):
        pass

    def callback(self, event):
        return [event.x, event.y]

    def show_msg_win(self):
        root_msg = Tk()
        
        root_msg.wm_title("Msg")
        root_msg.geometry("360x120")

        msg_win = MsgWindow(root_msg)


class Function():



    pass

if __name__ == "__main__":
    root = Tk()
    my_app = Window(root)

    menubar = Menu(root)
    menubar.add_command(label="登录", command=my_app.show_msg_win)
    menubar.add_command(label="好友", command=my_app.show_msg_win)
    menubar.add_command(label="操作", command=my_app.show_msg_win)
    menubar.add_command(label="新窗口", command=my_app.show_msg_win)
    menubar["background"] = "blue"

    root.wm_title("My App")
    root.geometry("720x540")
    root.config(menu=menubar)
    
    root.mainloop()