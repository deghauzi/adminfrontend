from django.core.mail import EmailMessage
from djoser import email
import threading


class EmailThread(threading.Thread):

    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send()


class EmailUtils:
    @staticmethod
    def send_email(data):
        email = EmailMessage(subject=data['email_subject'], body=data['email_body'], to=[
                             data['to_email']])
        EmailThread(email).start()

class ActivationEmail(email.ActivationEmail):
    template_name= "email/activationemail.html"

class ConfirmationEmail(email.ConfirmationEmail):
    template_name= "email/confirmation.html"

class PasswordResetEmail(email.PasswordResetEmail):
    template_name= "email/password_reset.html"

class PasswordChangedConfirmationEmail(email.PasswordChangedConfirmationEmail):
    template_name= "email/password_changed_confirm.html"
