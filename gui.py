# Coded By MachineGun 
# Date : 26/June/2024
# Time : 6:17 PM 
#SOON WE WILL HAVE A HUGE UPDATE ON THE TOOL 
#######################################
from tkinter import *
import pygame
import os
from PIL import ImageTk, Image
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import tkinter.messagebox as messagebox

###########################
root = Tk()
pwd = os.getcwd()
icon_path = pwd+"\icon.ico"
root.geometry("650x550")
root.resizable(0, 0)
root.title("Smtp Sender Pro")
root.iconbitmap(icon_path)
#######################################
# Create Functions


def startAttack():
    smtpinput.config(state=DISABLED)
    dataLines = []
    text = smtpinput.get('1.0', END)
    lines = text.splitlines()
    dataLines = [line.strip() for line in lines]
    # print(dataLines)
    smtpinput.config(state=NORMAL)
    if len(dataLines) >= 1 and dataLines[0] != "" or dataLines[0] != " ":
        number_of_spam = int(etyconfig.get('1.0', END))
        number_of_sent = 0

        for j in dataLines:
            if j != "":
                # kanta-kirjaudu.kitchen4mam.com,587,server799@kanta-kirjaudu.kitchen4mam.com,Leet@007'
                credentials = j.split("|")
                smtp_server = credentials[0]
                smtp_port = credentials[1]
                sender_email = credentials[2]
                email_password = credentials[3]
                recipient_email = smtpconfig.get('1.0', END)
                subject = subjectconfig.get('1.0', END)
                message = emailmsg.get('1.0', END)
                msg = MIMEMultipart()
                msg['From'] = sender_email
                msg['To'] = recipient_email
                msg['Subject'] = subject
                msg.attach(MIMEText(message, 'plain'))

                try:
                    # Create a SMTP session
                    server = smtplib.SMTP(smtp_server, smtp_port)
                    server.starttls()  # Enable TLS
                    # Login with sender's credentials
                    server.login(sender_email, email_password)

                    # Send email
                    for i in range(number_of_spam):
                        server.sendmail(sender_email, recipient_email, msg.as_string())
                        number_of_sent = number_of_sent + 1

                    messagebox.showinfo(title="Email Sent",
                                        message="Email sent successfully!")
                    number_of_sent = number_of_sent + 1
                    # ncriptech.com|25|info@ncriptech.com|sl33per_bTkfjU5KYVv#x
                except Exception as e:
                    messagebox.showerror(
                        title="Email Error",
                        message=f"Failed to send email. Error: {str(e)}"
                    )
                finally:
                    # Close the SMTP session
                    server.quit()
        number_of_sent = number_of_sent - 1
        number_of_sent = str(number_of_sent)
        messagebox.showinfo(title="Sent Emails", message=number_of_sent)


# Create Frames
#################
# ABOUT FRAME
# LOGO PART
aboutframe = LabelFrame(root, text="About Us X_o", font=(
    "Arial", 8, "bold"), bg="#000", fg="white", bd=2, relief=GROOVE, padx=5, pady=5)
aboutframe.place(x=0, y=0, width=650, height=80)
pwd_logo = os.getcwd()
pwd_logo = pwd_logo+r"\111.ico"
img = Image.open(pwd_logo)
img = img.resize((50, 50))
img = ImageTk.PhotoImage(img)
logo = Label(aboutframe, image=img)
logo.grid(row=0, column=0, pady=(0,0))
#################

# SOCIALS PART
socialsframe = Label(aboutframe, width=50, text="|# website:zerodey.ir X_x Telegram: @undergroundcy #| \n Coded By MachineGun- Version:1.0",
                     font=("Tahoma", 10, "italic"), justify=LEFT, background="#000", foreground="#00ff00")
socialsframe.grid(row=0, column=1, padx=(0, 30), pady=5)
button_help = Button(aboutframe, justify=RIGHT, text="Help",
                     width=6, height=1, font=("Tahoma", 10), fg="white", bg="#000")
button_help.grid(row=0, column=2, pady=5, padx=5)
button_help = Button(aboutframe, command=startAttack, justify=RIGHT, text="Send",
                     width=6, height=1, font=("Tahoma", 10), fg="white", bg="#000")
button_help.grid(row=0, column=3, pady=5, padx=5)
button_help = Button(aboutframe, justify=RIGHT, text="Stop",
                     width=6, height=1, font=("Tahoma", 10), fg="white", bg="#000")
button_help.grid(row=0, column=4, pady=5, padx=5)
###################################

# INPUT DATA
smtpframe = LabelFrame(root, text="SMTPS #_X ", font=(
    "Arial", 8, "bold"), bg="#000", fg="white", bd=2, relief=GROOVE, padx=5, pady=15)
smtpframe.place(x=0, y=80, width=650, height=250)
scroll_y = Scrollbar(smtpframe, orient=VERTICAL)
smtpinput = Text(smtpframe, font=(
    "Arial", 8), yscrollcommand=scroll_y.set, bg="#1d1d1d", fg="white", state=NORMAL)
scroll_y.config(command=smtpinput.yview)
scroll_y.pack(side=RIGHT, fill=Y)
smtpinput.pack(fill=BOTH)

# INPUT Credentials
configframe = LabelFrame(root, text="CONFIG X_X ", font=(
    "Arial", 8, "bold"), bg="#000", fg="white", bd=2, relief=GROOVE, padx=5, pady=15)
configframe.place(x=0, y=330, width=650, height=230)

reciveremail = Label(configframe, text="Reciver Email",
                     font=("Sans-serif", 8), bg="#000", fg="#fefefe")
reciveremail.grid(row=0, column=0, padx=5)

smtpconfig = Text(configframe, width=48, height=1, font=(
    "Arial", 8), bg="#1d1d1d", fg="white", state=NORMAL)
smtpconfig.grid(row=1, column=0, padx=(10, 15))


subject_email = Label(configframe, text="Subject", font=(
    "Sans-serif", 8), bg="#000", fg="#fefefe")
subject_email.grid(row=0, column=1, padx=5)

subjectconfig = Text(configframe, width=22, height=1, font=(
    "Arial", 8), bg="#1d1d1d", fg="white", state=NORMAL)
subjectconfig.grid(row=1, column=1, padx=(15, 5))

eqty = Label(configframe, text="NUMBER OF SPAM", font=(
    "Sans-serif", 8), bg="#000", fg="#fefefe")
eqty.grid(row=0, column=2, padx=5)

etyconfig = Text(configframe, width=22, height=1, font=(
    "Arial", 8), bg="#1d1d1d", fg="white", state=NORMAL)
default_value_ety = "10"
etyconfig.insert(INSERT, default_value_ety)
etyconfig.grid(row=1, column=2, padx=(15, 5))

message_label = Label(configframe, text="MESSAGE", font=(
    "Sans-serif", 8), bg="#000", fg="#fefefe")
message_label.grid(row=2, column=0, columnspan=3, padx=5, pady=(5, 0))

emailmsg = Text(configframe, wrap=WORD, width=80, height=8, font=(
    "Arial", 8), bg="#1d1d1d", fg="white", state=NORMAL)
emailmsg.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

scrollbar_emailmsg = Scrollbar(
    configframe, orient=VERTICAL, command=emailmsg.yview)
scrollbar_emailmsg.grid(row=3, column=3, sticky="nsew")

emailmsg.config(yscrollcommand=scrollbar_emailmsg.set)


#################
root.mainloop()


#SOON WE WILL HAVE A HUGE UPDATE ON THE TOOL 