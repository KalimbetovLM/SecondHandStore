from uuid import uuid4
import random
from django.template.loader import render_to_string
import threading
from django.core.mail import EmailMessage

        # Generating id for everything

def set_id():
    letters_list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P']
    number1 = random.randint(100,1000)
    number2 = random.randint(10,100)
    number3 = random.randint(10,100)
    letter1 = random.choice(letters_list)
    letter2 = random.choice(letters_list)
    id = letter1 + letter2 + str(number1) + str(number2) + str(number3)

    return id

#         # Working with email

# class EmailThread(threading.Thread):

#     def __init__(self,email):
#         self.email = email
#         threading.Thread.__init__(self)

#     def run(self):
#         self.email.send()

# class Email:

#     @staticmethod
#     def send_email(data):
#         email = EmailMessage(
#             subject = data['subject'],
#             body = data['body'],
#             to = [data['to_email']],
#         )
#         if data.get('content_type') == 'html':
#             email.content_subtype == 'html'
#         EmailThread(email).start()


# def send_email(email,code):
#     html_content = render_to_string(
#         'auth/activation_code.html',
#         {'code':code}
#     )   
#     Email.send_email(
#         {
#             "subject":"Confirmation",
#             "to_email":email,
#             "body": html_content,
#             "content_type":"html"
#         }
#     )

#         # generating confirmation passcode
    
# def gen_passcode():
#     first_number = random.randint(10,90)
#     second_number = random.randint(10,90)
#     passcode = str(first_number) + str(second_number)

#     return int(passcode)
