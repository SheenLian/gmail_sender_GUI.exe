from tkinter import *
from tkinter import messagebox
import smtplib
from email.mime.text import MIMEText


GUI = Tk()
GUI.geometry('500x700')
GUI.title('Email Sender')

def send():
    username = E1.get()
    password = E2.get()
    receiver = E3.get()
    subject = E4.get()
    mail_content = msg.get('1.0', 'end-1c')

    message = MIMEText(mail_content,'html','utf-8')
    message['Subject'] = subject

    mail_server = 'smtp.gmail.com'
    mail_server_port = 587
    server = smtplib.SMTP(mail_server, mail_server_port)

    print('>connecting....')
    server.ehlo()
    server.starttls()
    print('>connected....')
    server.login(username, password)
    server.sendmail(username, receiver, message.as_string())
    server.quit()
    messagebox.showinfo('Result', 'Mail sent!')



B = Button(GUI, text='send', command=send, activebackground='green', bd=6)
B.place(x=400, y=660)
L1 = Label(GUI, text='Your email address')
L2 = Label(GUI, text='Password')
L3 = Label(GUI, text='Recipient Email address')
L4 = Label(GUI, text='Subject')
E1 = Entry(GUI, bd=4, width=60)
E2 = Entry(GUI, bd=4, width=60)
E3 = Entry(GUI, bd=4, width=60)
E4 = Entry(GUI, bd=4, width=60)

L1.place(x=10, y=10)
E1.place(x=10, y=30)
L2.place(x=10, y=50)
E2.place(x=10, y=70)
L3.place(x=10, y=90)
E3.place(x=10, y=110)
L4.place(x=10, y=130)
E4.place(x=10, y=150)

msg = Text(GUI, width=60, height=18)
msg.place(x=10, y=200)



GUI.mainloop()
