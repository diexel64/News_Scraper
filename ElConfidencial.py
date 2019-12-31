import requests, datetime, time, os
from bs4 import BeautifulSoup
import openpyxl, re, pprint
import pandas as pd
from pandas import ExcelWriter

#lst = []
output = "\\output.xlsx"
destFolder = os.path.dirname(os.path.abspath(__file__))

class ElConfidencialScraper:

    def __init__(self, url, section):
        self.url = url
        self.section = section

    def getContent(self):
        page = requests.get(self.url)
        soup = BeautifulSoup(page.content, 'html.parser')
        results = soup.find('div', class_="archive-body")
        articles = results.find_all('article', class_="archive-article")
        return articles

    def getArticles(self):
        if os.path.isfile(destFolder + '\\ElConfidencial.xlsx') == False:
            self.CreateExcel()
        articles = self.getContent()
        df1 = pd.ExcelFile(destFolder + '\\ElConfidencial.xlsx').parse("ElConfidencial")
        for post in articles:
            link = post.find('a', class_='archive-article-link').get('href').split('//')
            title = post.find('h1', class_='archive-article-tit').text.strip()
            try:
                author = post.find('span', class_='archive-article-author sig-color').text.strip()
            except:
                author = 'Unknown'
            if None in (title, link, author):
                continue
        
            new_row = {'title': title, 'author': author, 'link': 'https://' + link[1], 'section': self.section, 'date': datetime.datetime.now().strftime("%d/%m/%Y")}
            #lst.append(new_row)
            df1 = df1.append(new_row, ignore_index=True)
        return df1

    def UpdateExcel(self):
        df1 = self.getArticles()
        writer = ExcelWriter(destFolder + '\\ElConfidencial.xlsx')
        df1 = df1.drop_duplicates(subset='title', keep='first')
        df1.to_excel(writer, sheet_name='ElConfidencial', index = False)
        writer.save()

    def CreateExcel(self):
        wb = openpyxl.Workbook()
        sheet = wb.get_sheet_by_name('Sheet')
        sheet.title = "ElConfidencial"
        sheet = wb.get_sheet_by_name("ElConfidencial")
        wb.save(destFolder + '\\ElConfidencial.xlsx')   