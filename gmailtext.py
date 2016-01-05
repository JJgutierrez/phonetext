import smtplib


class Gmailtext():
    def __init__(self):
        self.content = ""
        self.number = ""
    def textGmail(self):
        self.number = input('  Enter Phone number: ')
        self.content = input ('  Enter txt: ')
     
        self.number0 = self.number + "@mms.att.net"
        self.number1 = self.number + "@messaging.sprintpcs.com"
        self.number2 = self.number + "@tmomail.net"
        self.number3 = self.number + "@vtext.com"
        self.number4 = self.number + "@mms.uscc.net"
        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail.ehlo()
        mail.starttls()
        mail.login('gutierrez014642@gmail.com', 'juan40685194')
        mail.sendmail('gutierrez014642@gmail.com', self.number0, self.content)
        mail.sendmail('gutierrez014642@gmail.com', self.number1, self.content)
        mail.sendmail('gutierrez014642@gmail.com', self.number2, self.content)
        mail.sendmail('gutierrez014642@gmail.com', self.number3, self.content)
        mail.sendmail('gutierrez014642@gmail.com', self.number4, self.content)
        mail.close()
        print ('    Message is sent!!')
        
tx = Gmailtext()
textGmail = tx.textGmail()