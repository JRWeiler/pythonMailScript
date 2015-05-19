import smtplib
import getpass  
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText


def invalidEntry():
    print("E-mail address is invalid")

def checkEmail(address):
        if address.find('@') == -1:
            invalidEntry()
        else:
            return 1

def login(server, username, password):
    server.ehlo()  
    server.starttls()
    server.ehlo()  
    server.login(username,password)


def sendMail():
    while True:
        fromaddr = raw_input("From address: ")
        if checkEmail(fromaddr) == 1:
            break

    while True:    
        toaddrs  = raw_input("To address: ")
        if checkEmail(toaddrs) == 1:
            break

    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddrs
    msg['Subject'] = raw_input("Subject: ")
    body = raw_input("Message Body: ")
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('webmail.cn.edu:25')

    username =  fromaddr
    password =  getpass.getpass("Password: ")
    
    login(server, username, password)
            

    text = msg.as_string() 
    server.sendmail(fromaddr, toaddrs, text)  
    server.quit() 


sendMail() 