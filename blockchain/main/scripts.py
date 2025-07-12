import random
import sqlite3
from django.core.mail import send_mail
from .models import User

def Send_mail(user_email):
    import smtplib
    code = generate_verification_code()
    subject = "Ваш код подтверждения CloudBox"
    text = f"Ваш код подтверждения: {code}"
    FROM = "cloudbox742@gmail.com"
    PASSWORD = "Kena_bridge"

    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    EMAIL_HOST_USER = FROM
    EMAIL_HOST_PASSWORD = PASSWORD

    from django.core.mail import send_mail

    server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
    server.starttls()
    server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
    print(f'DEBUG: Sending email to {user_email} with code {code}')
    send_mail( subject, text, FROM, [user_email], fail_silently=False)


def generate_verification_code():
    return str(random.randint(100000, 999999))


def DEBUG(username, email, password):
    print(f'DEBUG: Username:', {username})
    print(f'DEBUG: Email:', {email})
    print(f'DEBUG: Password:', {password})


def registration(username, email, password):
    try:
        user = User.objects.create(username=username, email=email, password=password)
        print(f'DEBUG: User {user.username} registered successfully')
        return user
    except Exception as error:
        print('DEBUG: Error occurred -', error)
        return None