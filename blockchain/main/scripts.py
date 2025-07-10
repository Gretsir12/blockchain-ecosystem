import sqlite3
# import re

# db = sqlite3.connect('users.db') #creating database

def Send_mail(FROM,TO,SUBJECT,TEXT,SERVER):
    import smtplib
    message = """\
    From: %s
    To: %s
    Subject: %s
    %s
    """ % (FROM, ",".join(TO), SUBJECT, TEXT)
    # Send the mail
    SERVER = smtplib.SMTP(SERVER)
    SERVER.sendmail(FROM, TO, message)
    SERVER.quit()

def DEBUG(username, email):
    print(f'DEBUG: Username:', {username})
    print(f'DEBUG: Email:', {email})
    #print(f'DEBUG: Password:', {password})

def registration(username, email, password):
    try:
        # Connect to SQLite Database and create a cursor
        sqliteConnection = sqlite3.connect('databases/users.db')
        cursor = sqliteConnection.cursor()
        print('DEBUG: Connect to users.db successfully')
        
        # Fetch and print the result
        cursor = sqlite3.createCursor()
        cursor.execute
        print('SQLite Version is {}'.format(result[0][0]))
        
        # Close the cursor after use
        cursor.close()

    except sqlite3.Error as error:
        print('DEBUG: Error occurred -', error)

    sqliteConnection.close() #closing database