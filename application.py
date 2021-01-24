from tkinter import *
import string


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
        # self.label_2['background'] = "white"                       #背景颜色
        # self.label_2['width'] = 60                                 #宽度

        self.confrom_button_1 = Button(self)
        self.confrom_button_1['text'] = self.confrom_moji
        self.confrom_button_1['command'] = self.confrom_event

        self.input_button_1 = Button(self)
        self.input_button_1['text'] = "输入"
        self.input_button_1['command'] = self.input_text

        self.cancel_button_1 = Button(self)
        self.cancel_button_1['text'] = self.cancel_moji
        self.cancel_button_1['command'] = self.cancel_event

        self.clear_button = Button(self)
        self.clear_button['text'] = self.clear_moji
        self.clear_button['command'] = self.clear_event

        self.text_box_1 = Text(self)
        self.text_box_1['height'] = 10
        self.text_box_1['width'] = 80
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
        self.text_box_2['height'] = 20
        self.text_box_2['width'] = 80
        self.text_box_2['wrap'] = 'word'
        self.text_box_2['borderwidth'] = 1
        self.text_box_2['highlightcolor'] = 'yellow'
        self.text_box_2['yscrollcommand'] = Scrollbar(self, orient=VERTICAL)

        # 部件在窗口里布局
        self.label_1.grid(row=0, column=0)
        self.label_2.grid(row=0, column=1, sticky=W)

        self.confrom_button_1.grid(row=1, column=0)
        self.cancel_button_1.grid(row=1, column=1)
        self.clear_button.grid(row=1, column=2)
        self.input_button_1.grid(row=2, column=2, sticky=S)

        # sticky= 
        # 默认居中对齐
        # N 上对齐 S 下对齐 E 右对齐 W 左对齐
        # N+W

        self.text_box_1.grid(row=2, column=1)
        self.text_box_2.grid(row=3, column=1, columnspan=1)

        # self.bind("<Button-1>",self.callback())

    def content_of_Element_box(self, Element):
        return f"{Element['text']}\n"
        
    def confrom_event(self):
        # 根据text中有多少个\n判断有多少行
        row = self.text_box_2.get('0.0', 'end').count('\n')
        # 将光标移至最后一行
        self.text_box_2.mark_set('insert', "%d.0" % (row+1))
        if self.label_2['text'] == "you clicked it" or self.label_2['text'] == "you have clicked it":
            self.label_2['text'] = "you have clicked it"
            self.text_box_2.insert(
                'insert', self.content_of_Element_box(self.label_2))
        else:
            self.label_2['text'] = "you clicked it"
            self.text_box_2.insert(
                'insert', self.content_of_Element_box(self.label_2))

    def cancel_event(self):
        self.label_2['text'] = "you canceled"
        self.text_box_2.insert(
            'insert', self.content_of_Element_box(self.label_2))

    # 清除文本框里的内容
    def clear_event(self):
        self.text_box_2.delete('0.0', 'end')

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


if __name__ == "__main__":
    root = Tk()
    my_app = Window(root)
    menubar = Menu(root)
    menubar.add_command(label="文件", command=my_app.do_nothing)
    menubar.add_command(label="编辑", command=my_app.do_nothing)
    menubar.add_command(label="操作", command=my_app.do_nothing)
    menubar["background"] = "blue"
    root.wm_title("My App")
    root.geometry("720x540")
    root.config(menu=menubar)
    root.mainloop()