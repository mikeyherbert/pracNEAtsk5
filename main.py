###############
#
# Password validation program
# Mikey Herbert 08feb19 - 11feb19
# Includes visual UI
#
###############

import tkinter as tk
from tkinter import simpledialog


class App1(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.intro = tk.Label(self)
        self.op1 = tk.Button(self, command=lambda: self.register())
        self.op2 = tk.Button(self, command=lambda: self.login())
        self.op3 = tk.Button(self, command=lambda: self.recover())
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.intro['text'] = 'Choose appropriate option: \n' \
                             'To quit click the quit button\n'
        self.intro.grid(column=0, row=0)

        self.op1['text'] = 'Register new user'
        self.op1.grid(column=0, row=2)

        self.op2['text'] = 'Log in'
        self.op2.grid(column=0, row=3)

        self.op3['text'] = 'Recovery'
        self.op3.grid(column=0, row=4)

    def login(self):
        login_w = tk.Tk()
        login_w.withdraw()
        username = ''
        password = ''
        success = False

        while username == '':
            username = tk.simpledialog.askstring('Username', 'Enter your username:')

        while password == '':
            password = tk.simpledialog.askstring('Password', 'Enter your password:', show='•')

        userlist = open('users.txt', 'r')

        for l in userlist:
            group = l.split(':')
            if username == group[0] and password == group[1]:
                success = True
            else:
                success = Fase

        if success:
            successw = tk.Tk()
            successtxt = tk.Label(successw)
            successtxt['text'] = 'Success!'
            successtxt.pack()
            successw.mainloop()

        else:
            failw = tk.Tk()
            failtxt = tk.Label(failw)
            failtxt['text'] = 'Fail... '
            failtxt.pack()
            failw.mainloop()


    def register(self):
        user = ''

    def recover(self):
        user = ''


root = tk.Tk()
root.geometry('160x150')
root.resizable(0, 0)
root.title('Login System v0.1')
run = App1(master=root)
run.mainloop()
