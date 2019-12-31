import requests, datetime, time, os
from bs4 import BeautifulSoup
import openpyxl, re, pprint
import pandas as pd
from pandas import ExcelWriter

#lst = []
output = "\\output.xlsx"
destFolder = os.path.dirname(os.path.abspath(__file__))

class ElpaisScraper:

    def __init__(self, url, section):
        self.url = url
        self.section = section

    def getContent(self):
        page = requests.get(self.url)
        soup = BeautifulSoup(page.content, 'html.parser')
        results = soup.find('div', class_="contenedor")
        articles = results.find_all('div', class_="articulo__interior")
        return articles

    def getArticles(self):
        if os.path.isfile(destFolder + '\\ElPais.xlsx') == False:
            self.CreateExcel()
        articles = self.getContent()
        df0 = pd.ExcelFile(destFolder + '\\ElPais.xlsx').parse("ElPais")
        for post in articles:
            link = post.find('h2', class_='articulo-titulo').find('a').get('href').split('//')
            title = post.find('h2', class_='articulo-titulo').text.strip()
            try:
                author = post.find('span', class_='autor-nombre').text.strip()
            except:
                author = 'Unknown'
            if None in (title, link, author):
                continue
        
            new_row = {'title': title, 'author': author, 'link': 'https://' + link[1], 'section': self.section, 'date': datetime.datetime.now().strftime("%d/%m/%Y")}
            #lst.append(new_row)
            df0 = df0.append(new_row, ignore_index=True)
        return df0

    def UpdateExcel(self):
        df0 = self.getArticles()
        writer = ExcelWriter(destFolder + '\\ElPais.xlsx')
        df0 = df0.drop_duplicates(subset='title', keep='first')
        df0.to_excel(writer, sheet_name='ElPais', index = False)
        writer.save()

    def CreateExcel(self):
        wb = openpyxl.Workbook()
        sheet = wb.get_sheet_by_name('Sheet')
        sheet.title = "ElPais"
        sheet = wb.get_sheet_by_name("ElPais")
        wb.save(destFolder + '\\ElPais.xlsx')