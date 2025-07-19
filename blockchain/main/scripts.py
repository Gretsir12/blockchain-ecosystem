import random
import sqlite3
from django.core.mail import send_mail
from .models import User

def generate_verification_code():
    return str(random.randint(100000, 999999))

def DEBUG(username, email, password):
    print(f'DEBUG: Username:', {username})
    print(f'DEBUG: Email:', {email})
    print(f'DEBUG: Password:', {password})

def send_verification_email(user):
    from random import randint
    import smtplib
    myemail = "cloudbox742@gmail.com"
    mypassword = "ugmp vczs gmnb ldlu "
    user_email = user.email
    secret_code = randint(100000, 999999)
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(myemail, mypassword)
            subject = 'Verification Code'
            body = f'Your verification code is: {secret_code}'
            message = f'Subject: {subject}\n\n{body}'
            server.sendmail(myemail, user_email, message)
        print(f'DEBUG: Verification email sent to {user_email}')
        return secret_code
    except Exception as e:
        print(f'DEBUG: Failed to send email - {e}')
        return None

# def registration(username, email, password):
#     try:
#         user = User.objects.create(username=username, email=email, password=password)
#         print(f'DEBUG: User {user.username} registered successfully')
#         return user
#     except Exception as error:
#         print('DEBUG: Error occurred -', error)
#         return None