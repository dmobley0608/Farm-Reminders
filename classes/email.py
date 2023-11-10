import os
from email.message import EmailMessage
import ssl
import smtplib

class Email:    
    def __init__(self, subject):
        self.sent_from = 'DD Cattle Company'
        self.send_to = []
        self.body = ''
        self.subject = subject
        self.sender = os.getenv('GOOGLE_USERNAME')
        self.google_key = os.getenv("GOOGLE_KEY")
        
    def add_recipient(self, recipient):
        self.send_to.append(recipient)
        
    def send_email(self):
        try:
            print('Sending Email')
            em = EmailMessage()
            em['From'] = self.sent_from
            em['To'] = ', '.join(self.send_to)
            em.add_header('Content-Type','text/html')
            em['Subject'] = self.subject
            em.set_payload(self.body)
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                smtp.login(os.getenv('GOOGLE_USERNAME'), self.google_key)
                smtp.sendmail(self.sent_from, self.send_to, em.as_string()) 
            print('Successfully Sent Email')
            return True
        except smtplib.SMTPAuthenticationError:
            print('Invalid Username or Password')
            return False
        except:
            print('Error Sending Message')
            return False
        
    def set_body_for_vaccines(self, coggins, rabies, vaccines, worming, trimmed):
        self.body = f"""
            <img src='https://ddcattle.company/static/media/ddc.b51fd10ab57a812f22d9.png' width='200px'/>
            <h1>Vaccination Status and Worming Updates</h1>
            """
        if len(worming) > 0:
            self.body += f"""<h2>The following horses need to be wormed:</h2>
            <ol>
            <li>
                {'<li>'.join(worming)}
            </ol>
            """
        if len(coggins) > 0:
            self.body += f"""<hr>
            <h2>The following horses need Coggins pulled:</h2>
            <ol>
            <li>
                {'<li>'.join(coggins)}
            </ol>
            """
        if len(rabies) > 0:
            self.body +=f"""
            <hr>
            <h2>The following horses need rabies shots:</h2>
            <ol>
            <li>
                {'<li>'.join(rabies)}
            </ol>
            """
        if len(vaccines) > 0:
            self.body += f"""
            <hr>
            <h2>The following horses need yearly vaccines:</h2>
            <ol>
            <li>
                {'<li>'.join(vaccines)}
            </ol>
            <hr>
            """
        if len(trimmed) > 0:
            self.body += f"""
            <h2>The following horses need to be trimmed:</h2>
            <ol>
            <li>
                {'<li>'.join(trimmed)}
            </ol>
            """
