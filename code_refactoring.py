import os
import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from dotenv import load_dotenv

load_dotenv()


class WorkingWithMail:

    def __init__(self, mail_smtp, mail_imap, login, password):
        self.mail_smtp = mail_smtp
        self.mail_imap = mail_imap
        self.login = login
        self.password = password

    def send_message(self, recipients, subject, message):
        msg = MIMEMultipart()
        msg['From'] = self.login
        msg['To'] = ', '.join(recipients)
        msg['Subject'] = subject
        msg.attach(MIMEText(message))

        with smtplib.SMTP(self.mail_smtp, 587) as ms:
            ms.ehlo()
            ms.starttls()
            ms.ehlo()
            ms.login(self.login, self.password)
            ms.sendmail(self.login, recipients, msg.as_string())

    def receive_message(self, header=None):
        mail = imaplib.IMAP4_SSL(self.mail_imap)
        mail.login(self.login, self.password)
        mail.select("inbox")
        criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
        result, data = mail.uid('search', None, criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email)
        mail.logout()


if __name__ == '__main__':
    gmail_smtp = os.getenv('GMAIL_SMTP')
    gmail_imap = os.getenv('GMAIL_IMAP')
    gmail_login = os.getenv('LOGIN')
    gmail_password = os.getenv('PASSWORD')
    subject_ = 'Subject'
    recipients_ = ['vasya@email.com', 'petya@email.com']
    message_ = 'Message'

    email_client = WorkingWithMail(
        gmail_smtp, gmail_imap, gmail_login, gmail_password)
    email_client.send_message(subject_, recipients_, message_)
    email_client.receive_message()
