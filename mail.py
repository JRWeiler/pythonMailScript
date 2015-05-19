import smtplib
import getpass  
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

#Error message
def invalidEntry():
    print("E-mail address is invalid")

#Simple validation checking for an @ symbol
def checkEmail(address):
        if address.find('@') == -1:
            invalidEntry()
        else:
            return 1

#Login to mail server using user credentials
def login(server, username, password):
    server.ehlo()  
    server.starttls()
    server.ehlo()  
    server.login(username,password)

#Function to send email. Gather a from address, to address, subject, and mail body
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

    #Replace mail.domain.edu with mail server and port#
    server = smtplib.SMTP('mail.domain.edu:25')

    username =  fromaddr
    password =  getpass.getpass("Password: ")
    
    login(server, username, password)
            

    text = msg.as_string() 
    server.sendmail(fromaddr, toaddrs, text)  
    server.quit() 


sendMail() 