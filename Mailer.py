#! python3
# Mailer.py - Sends and email with the big titles of the news from the day.

import openpyxl, smtplib, sys, datetime, time, os
import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders

destFolder = os.path.dirname(os.path.abspath(__file__))

class emailSender:

    def __init__(self):
        pd.options.display.max_colwidth = 200
        self.dfpais = pd.ExcelFile(destFolder + '\\ElPais.xlsx').parse("ElPais")
        self.dfconfi = pd.ExcelFile(destFolder + '\\ElConfidencial.xlsx').parse("ElConfidencial")
        self.dfmonde = pd.ExcelFile(destFolder + '\\LeMonde.xlsx').parse("LeMonde")
        self.dfother = pd.ExcelFile(destFolder + '\\Other.xlsx').parse("Other")
        self.today = datetime.datetime.now().strftime("%d/%m/%Y")
        data_monde = self.dfmonde[self.dfmonde.date == self.today]
        self.data_monde_int = data_monde[self.dfmonde.section == 'International'][['title', 'link']].to_string(index=False).split('link')[1]
        self.data_monde_eco = data_monde[self.dfmonde.section == 'Economics'][['title', 'link']].to_string(index=False).split('link')[1]
        self.data_monde_dec = data_monde[self.dfmonde.section == 'Décodeurs'][['title', 'link']].to_string(index=False).split('link')[1]
        data_elpais = self.dfpais[self.dfpais.date == self.today]
        self.data_elpais_int = data_elpais[self.dfpais.section == 'International'][['title', 'author', 'link']].to_string(index=False).split('link')[1]
        self.data_elpais_eco = data_elpais[self.dfpais.section == 'Economics'][['title', 'author', 'link']].to_string(index=False).split('link')[1]
        self.data_elpais_tec = data_elpais[self.dfpais.section == 'Technology'][['title', 'author', 'link']].to_string(index=False).split('link')[1]
        data_elconfi = self.dfconfi[self.dfconfi.date == self.today]
        self.data_elconfi_int = data_elconfi[self.dfconfi.section == 'International'][['title', 'author', 'link']].to_string(index=False).split('link')[1]
        self.data_elconfi_eco = data_elconfi[self.dfconfi.section == 'Economics'][['title', 'author', 'link']].to_string(index=False).split('link')[1]
        self.data_elconfi_tec = data_elconfi[self.dfconfi.section == 'Technology'][['title', 'author', 'link']].to_string(index=False).split('link')[1]
        data_other = self.dfother[self.dfother.date == self.today]
        self.data_others = data_other[['title', 'author', 'link']].to_string(index=False).split('link')[1]

    def send(self):

        gmail_user = input("FROM ? (type e-mail address): -->  ")
        TO = input("TO ? (type e-mail address): -->  ")
        SUBJECT = "Noticias del dia"
        gmail_pwd = input("Please, insert your password: -->  ")
    
        msg = MIMEMultipart()
        msg['From'] = gmail_user
        msg['To'] = TO
        msg['Subject'] = SUBJECT
        TEXT = '''NOTICIAS DE HOY\n\n\n
        INTERNACIONAL : \n\n
        LE MONDE\n {0} \n\n
        EL PAIS\n {1} \n\n
        EL CONFIDENCIAL\n {2} \n\n\n
        ECONOMIA : \n\n
        LE MONDE\n {3} \n\n
        EL PAIS\n {4} \n\n
        EL CONFIDENCIAL\n {5} \n\n\n
        TECNOLOGIA : \n\n
        EL PAIS\n {6} \n\n
        EL CONFIDENCIAL\n {7} \n\n\n
        DECODEURS\n {8} \n\n\n
        OTROS\n {9} \n\n\n   
        ¡Eso es todo por hoy!'''.format(self.data_monde_int, self.data_elpais_int, self.data_elconfi_int, self.data_monde_eco, self.data_elpais_eco, self.data_elconfi_eco, self.data_elpais_tec, self.data_elconfi_tec, self.data_monde_dec, self.data_others)

        msg.attach(MIMEText(TEXT, 'plain'))
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        text = msg.as_string()

        server.sendmail(gmail_user, TO, text)
        if server.sendmail(gmail_user, TO, text) == {}:
            print ('email sent')
        else:
            print('email not sent')
        server.quit()