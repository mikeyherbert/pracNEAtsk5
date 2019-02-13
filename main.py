###############
#
# Password validation program
# Mikey Herbert 08feb19 - 11feb19
# Includes visual UI
# (and object oriented programming because I can)
# Does not include validation because I'd rather write 183 lines not 6000
#
###############

import tkinter as tk
from tkinter import simpledialog
import time as t


def encode(non_cipher, key):
    cipher = ''
    for c in non_cipher:
        c = chr(ord(c) + (key + 3))  # key will be length of string + 3
        cipher += c

    return cipher

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
            if username == group[0] and password == decode(group[1]):
                success = True
            else:
                success = False

        if success:
            successw = tk.Tk()
            successtxt = tk.Label(successw)
            successtxt['text'] = 'Success!'
            successtxt.pack()
            successw.mainloop()
            t.sleep(2)
            quit()

        else:
            failw = tk.Tk()
            failtxt = tk.Label(failw)
            failtxt['text'] = 'Fail... '
            failtxt.pack()
            failw.mainloop()
            t.sleep(2)
            quit()

    def register(self):

        reg_w = tk.Tk()

        def sub_register():
            reg_w.withdraw()
            email = email_r.get()
            username = user_r.get()
            password = encode(password_r.get(), len(password_r.get()))
            confirm = encode(confirm_r.get(), len(confirm_r.get()))
            pin = pin_r.get()

            if not password == confirm:
                failw = tk.Tk()
                failtxt = tk.Label(failw)
                failtxt['text'] = 'Fail... '
                failtxt.pack()
                failw.mainloop()
                t.sleep(2)
                quit()

            else:
                with open('users.txt', 'a') as file:
                    to_add = '{}:{}:{}:{}\n'.format(username, password, pin, email)
                    file.write(to_add)

                successw = tk.Tk()
                successtxt = tk.Label(successw)
                successtxt['text'] = 'Success!'
                successtxt.pack()
                successw.mainloop()
                t.sleep(2)
                quit()

        email_t = tk.Label(reg_w, text='Email:')
        email_t.pack()

        email_r = tk.Entry(reg_w)
        email_r.pack()

        user_t = tk.Label(reg_w, text='Username:')
        user_t.pack()

        user_r = tk.Entry(reg_w)
        user_r.pack()

        password_t = tk.Label(reg_w, text='Password:')
        password_t.pack()

        password_r = tk.Entry(reg_w, show='•')
        password_r.pack()

        confirm_t = tk.Label(reg_w, text='Confirm password:')
        confirm_t.pack()

        confirm_r = tk.Entry(reg_w, show='•')
        confirm_r.pack()

        pin_t = tk.Label(reg_w, text='Emergency PIN:')
        pin_t.pack()

        pin_r = tk.Entry(reg_w, show='•')
        pin_r.pack()

        enter = tk.Button(reg_w, command=lambda: sub_register(), text='Enter')
        enter.pack()

        reg_w.mainloop()

    def recover(self):
        newroot = tk.Tk()

        username = tk.simpledialog.askstring('Username', 'Username:')
        pin = tk.simpledialog.askstring('PIN', 'PIN:', show='•')

        with open('users.txt', 'r') as file:
            found = False
            for l in file:
                gp = l.split(':')
                if pin in gp[3] and username in gp[0]:
                    pass_display = tk.Label(newroot, text='Password: {}'.format(decode(gp[1])))
                    pass_display.pack()
                    found = True
                else:
                    pass

            if not found:
                failw = tk.Tk()
                failtxt = tk.Label(failw)
                failtxt['text'] = 'Fail... '
                failtxt.pack()
                failw.mainloop()
                t.sleep(2)
                quit()

        newroot.mainloop()


root = tk.Tk()
root.geometry('160x150')
root.resizable(0, 0)
root.title('Login System v0.1')
run = App1(master=root)
run.mainloop()
