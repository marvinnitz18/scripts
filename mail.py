#!/bin/env python
import subprocess
import smtplib
import socket
import sys
from email.mime.text import MIMEText
import argparse
import mailauth

# Accountinformationen zum Login (definiert in auth.py)

Absender = str(mailauth.username)
Passwort = str(mailauth.password)


smtpserver = smtplib.SMTP("smtp.strato.de", 587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo

#Argparser
parser = argparse.ArgumentParser(description='mail programm')
parser.add_argument('reciever', help='mail adresss you want to send to')
parser.add_argument('subject', help='subject line')
parser.add_argument('message', help='message you want to send' )

args=parser.parse_args()

# In Account einloggen
smtpserver.login(Absender, Passwort)

# Alle Argumente einlesen und in einem String speichern

msg = MIMEText(args.message)

# Betreff + Datum
msg["Subject"] = args.subject
# Absender
msg["From"] = Absender
#Empfaenger
msg["To"] = args.reciever

# E-Mail abschicken

smtpserver.sendmail(Absender, args.reciever, str(msg))
smtpserver.quit()

