import sqlite3
import re

import smtplib

# db = sqlite3.connect('users.db') #creating database

def registration(username, email, password. db):

    cursor = db.cursor() # creating cursor
    
    
    
    db.close()

    def send_mail(email):
        print(f"Sending confirmation email to {email}")
