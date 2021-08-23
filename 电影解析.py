import re   # 正则表达式
import tkinter as tk   # GUI桌面编程
from urllib import parse  # url地址解析
import tkinter.messagebox as msgbox # 消息盒子
import webbrowser   # 控制浏览器

class App:
    # 重写构造函数 创建类属性
    def __init__(self,width=500,height=300):     # 可以pass 防止代码出错  占位符
        self.w = width
        self.h = height  # 创建自定义类属性
        self.title = '视频解析助手'   # 软件名
        # tk对象
        self.root = tk.Tk(className=self.title)
        # 变量去接收用户输入的电影网址 并且对地址做处理
        self.url = tk.StringVar()
        # 控制单选框默认选中的属性
        self.v = tk.IntVar()
        self.v.set(1)

        # 软件空间划分
        frame_1 = tk.Frame(self.root)          # frame_1  不是类属性 所有不需要加self.
        frame_2 = tk.Frame(self.root)

        # 软件控件内容设置
        group = tk.Label(frame_1, text='播放通道:', padx=10,pady=10)
        tb = tk.Radiobutton(frame_1, text='唯一通道', variable=self.v, value=1, width=10, height=3)

        label = tk.Label(frame_2, text='请输入视频播放地址：')
        entry = tk.Entry(frame_2, textvariable=self.url, highlightcolor='Fuchsia', highlightthickness=1, width=30)
        play = tk.Button(frame_2, text='播放', font=('楷体', 12), fg='Purple', width=5, height=2, command=self.video_play)

        # 控件布局 激活空间
        frame_1.pack()
        frame_2.pack()

        # 位置确定
        group.grid(row=0, column=0)
        tb.grid(row=0, column=1)

        # 空间2的控件位置无需看空间1的位置
        # 空间与空间之间是独立的
        label.grid(row=0, column=0)
        entry.grid(row=0, column=1)
        play.grid(row=0, column=2, ipadx=10, ipady=10)

    #  定义播放按钮的事件函数,解析电影
    def video_play(self):
        # 第三方播放解析api
        port = 'http://www.wmxz.wang/video.php?url='
        # 判断用户输入的电影地址是否合法
        if re.match(r'https?:/{2}\w.+$', self.url.get()):
            ip = self.url.get()
            ip = parse.quote_plus(ip)
            # 自动打开浏览器
            webbrowser.open(port + ip)

        else:
            msgbox.showerror(title='错误', message='视频地址无效，请重新输入...')

    # 如何启动软件
    def loop(self):
        self.root.mainloop()


if __name__ == '__main__':
    app = App()
    app.loop()























