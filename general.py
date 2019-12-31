from pandas import ExcelWriter
from ElPais import ElpaisScraper
from ElConfidencial import ElConfidencialScraper
from LeMonde import LeMondeScraper
from Other import OtherScraper
from UpdateExcel import UpdateGlobalExcel
from Mailer import emailSender

urlint = ['https://elpais.com/internacional/', 'https://www.elconfidencial.com/mundo/', 'https://www.lemonde.fr/international/']
urleco = ['https://elpais.com/economia/', 'https://www.elconfidencial.com/economia/', 'https://www.lemonde.fr/economie/']
urltec = ['https://elpais.com/tecnologia/', 'https://www.elconfidencial.com/tecnologia/', '']

ElpaisScraper(urlint[0], 'International').UpdateExcel()
ElpaisScraper(urleco[0], 'Economics').UpdateExcel()
ElpaisScraper(urltec[0], 'Technology').UpdateExcel()

ElConfidencialScraper(urlint[1], 'International').UpdateExcel()
ElConfidencialScraper(urleco[1], 'Economics').UpdateExcel()
ElConfidencialScraper(urltec[1], 'Technology').UpdateExcel()

LeMondeScraper(urlint[2], 'International').UpdateExcel()
LeMondeScraper(urleco[2], 'Economics').UpdateExcel()
LeMondeScraper('https://www.lemonde.fr/les-decodeurs/', 'Décodeurs').UpdateExcel()

OtherScraper().CreateExcel()
OtherScraper().getInaki('https://elpais.com/agr/la_voz_de_inaki/a')
OtherScraper().getPiketty('https://www.lemonde.fr/blog/piketty/')
OtherScraper().getLacalle('https://www.dlacalle.com/')

UpdateGlobalExcel()
emailSender().send()