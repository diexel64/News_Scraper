import requests, datetime, time, os
from bs4 import BeautifulSoup
import openpyxl, re, pprint
import pandas as pd
from pandas import ExcelWriter

#lst = []

destFolder = os.path.dirname(os.path.abspath(__file__))

class LeMondeScraper:

    def __init__(self, url, section):
        self.url = url
        self.section = section

    def getContent(self):
        page = requests.get(self.url)
        soup = BeautifulSoup(page.content, 'html.parser')
        results = soup.find('section', class_="page__float")
        articles = results.find_all('section', class_=re.compile('^teaser teaser*'))
        print(len(articles))
        return articles

    def getArticles(self):
        if os.path.isfile(destFolder + '\\LeMonde.xlsx') == False:
            self.CreateExcel()
        articles = self.getContent()
        df2 = pd.ExcelFile(destFolder + '\\LeMonde.xlsx').parse("LeMonde")
        for post in articles:
            link = post.find('a', class_='teaser__link').get('href').split('//')
            title = post.find('h3', class_='teaser__title').text.strip()

            if None in (title, link):
                continue
        
            new_row = {'title': title, 'link': 'https://' + link[1], 'section': self.section, 'date': datetime.datetime.now().strftime("%d/%m/%Y")}
            #lst.append(new_row)
            df2 = df2.append(new_row, ignore_index=True)
        return df2

    def UpdateExcel(self):
        df2 = self.getArticles()
        writer = ExcelWriter(destFolder + '\\LeMonde.xlsx')
        df2 = df2.drop_duplicates(subset='title', keep='first')
        df2.to_excel(writer, sheet_name='LeMonde', index = False)
        writer.save()

    def CreateExcel(self):
        wb = openpyxl.Workbook()
        sheet = wb.get_sheet_by_name('Sheet')
        sheet.title = "LeMonde"
        sheet = wb.get_sheet_by_name("LeMonde")
        wb.save(destFolder + '\\LeMonde.xlsx')
