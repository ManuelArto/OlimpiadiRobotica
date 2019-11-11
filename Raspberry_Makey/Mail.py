""" Author: Arto Manuel, Gabriele Genovese, Federico Crescentini
    MAKEY MAKEY CHALLENGE
    ############################################################
    Class of support for the email sending action
    Create a connection to the SMTP server and send a personalized message for every email in the list
"""
import smtplib

from string import Template

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# List of emails
emails = [["manu", "manuelartociao@gmail.com"], ["geno", "gabrigeno@gmail.com"], ["fede", "federicocrescentini59@gmail.com"]]

message_template = Template("""
Hi ${PERSON_NAME},

Mario press the Email button, maybe he needs help.
""")


class Mail:

    def __init__(self):
        # set up the SMTP server
        self.s = smtplib.SMTP(host='smtp.gmail.com', port=25)
        self.s.starttls()
        self.s.login(YOUR_ADDRESS, YOUR_PASSWORD)

    def send(self):
        # For each contact, send the email:
        for name, email in emails:
            msg = MIMEMultipart()       # create a message

            # add in the actual person name to the message template
            message = message_template.substitute(PERSON_NAME=name)

            # setup the parameters of the message
            msg['From'] = YOUR_ADDRESS
            msg['To'] = email
            msg['Subject'] = "TEST"

            # add in the message body
            msg.attach(MIMEText(message, 'plain'))

            # send the message via the server set up earlier.
            self.s.send_message(msg)
            del msg