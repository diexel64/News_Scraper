import requests, datetime, time, os
from bs4 import BeautifulSoup
import openpyxl, re, pprint
import pandas as pd
from pandas import ExcelWriter

#lst = []

destFolder = os.path.dirname(os.path.abspath(__file__))

headers = {
    'User-Agent': 'Mozilla/5.0',
    'From': 'monsieur@domain.com'
}

class OtherScraper:

    def __init__(self):
        self.url = ''

    def getInaki(self, url):
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        results = soup.find('div', class_="bloque__interior")
        articles = results.find_all('article')
        df0 = pd.ExcelFile(destFolder + '\\Other.xlsx').parse("Other")
        for post in articles:
            link = post.find('a', class_='enlace').get('href').split('//')
            title = post.find('h2', class_='articulo-titulo').text.strip()
            author = 'Iñaki Gabilondo'
            if None in (title, link):
                continue
            new_row = {'title': title, 'author': author, 'link': 'https://' + link[1], 'date': datetime.datetime.now().strftime("%d/%m/%Y")}
            #lst.append(new_row)
            df0 = df0.append(new_row, ignore_index=True)
        writer = ExcelWriter(destFolder + '\\Other.xlsx')
        df0 = df0.drop_duplicates(subset='title', keep='first')
        df0.to_excel(writer, sheet_name='Other', index = False)
        writer.save()

    def getPiketty(self, url):
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        results = soup.find('div', class_="content-area")
        articles = results.find_all('article')
        df0 = pd.ExcelFile(destFolder + '\\Other.xlsx').parse("Other")
        for post in articles:
            link = post.find('h3', class_='entry-title').find('a').get('href').split('//')
            title = post.find('h3', class_='entry-title').text.strip()
            author = 'Thomas Piketty'
            if None in (title, link):
                continue
            new_row = {'title': title, 'author': author, 'link': 'https://' + link[1], 'date': datetime.datetime.now().strftime("%d/%m/%Y")}
            #lst.append(new_row)
            df0 = df0.append(new_row, ignore_index=True)
        writer = ExcelWriter(destFolder + '\\Other.xlsx')
        df0 = df0.drop_duplicates(subset='title', keep='first')
        df0.to_excel(writer, sheet_name='Other', index = False)
        writer.save()

    def getLacalle(self, url):
        page = requests.get(url, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        results = soup.find('div', class_="content-area")
        articles = results.find_all('article')
        df0 = pd.ExcelFile(destFolder + '\\Other.xlsx').parse("Other")
        for post in articles:
            link = post.find('h1', class_='entry-title').find('a').get('href').split('//')
            title = post.find('h1', class_='entry-title').text.strip()
            author = 'Daniel Lacalle'
            if None in (title, link):
                continue
            new_row = {'title': title, 'author': author, 'link': 'https://' + link[1], 'date': datetime.datetime.now().strftime("%d/%m/%Y")}
            #lst.append(new_row)
            df0 = df0.append(new_row, ignore_index=True)
        writer = ExcelWriter(destFolder + '\\Other.xlsx')
        df0 = df0.drop_duplicates(subset='title', keep='first')
        df0.to_excel(writer, sheet_name='Other', index = False)
        writer.save()

    def getRallo(self, url):
        page = requests.get(url, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        results = soup.find('div', class_="content-area")
        articles = results.find_all('article')
        df0 = pd.ExcelFile(destFolder + '\\Other.xlsx').parse("Other")
        for post in articles:
            link = post.find('h1', class_='entry-title').find('a').get('href').split('//')
            title = post.find('h1', class_='entry-title').text.strip()
            author = 'Juan Ramón Rallo'
            if None in (title, link):
                continue
            new_row = {'title': title, 'author': author, 'link': 'https://' + link[1], 'date': datetime.datetime.now().strftime("%d/%m/%Y")}
            #lst.append(new_row)
            df0 = df0.append(new_row, ignore_index=True)
        writer = ExcelWriter(destFolder + '\\Other.xlsx')
        df0 = df0.drop_duplicates(subset='title', keep='first')
        df0.to_excel(writer, sheet_name='Other', index = False)
        writer.save()


    def CreateExcel(self):
        if os.path.isfile(destFolder + '\\Other.xlsx') == False:
            wb = openpyxl.Workbook()
            sheet = wb.get_sheet_by_name('Sheet')
            sheet.title = "Other"
            sheet = wb.get_sheet_by_name("Other")
            wb.save(destFolder + '\\Other.xlsx')

#OtherScraper().getInaki('https://elpais.com/agr/la_voz_de_inaki/a')
#OtherScraper().getPiketty('https://www.lemonde.fr/blog/piketty/')'''
#OtherScraper().getLacalle('https://www.dlacalle.com/')