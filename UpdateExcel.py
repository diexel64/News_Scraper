import os
import pandas as pd
from pandas import ExcelWriter

output = "\\Global.xlsx"
destFolder = os.path.dirname(os.path.abspath(__file__))

class UpdateGlobalExcel:
    def __init__(self):
        dfpais = pd.ExcelFile(destFolder + '\\ElPais.xlsx').parse("ElPais")
        dfconfi = pd.ExcelFile(destFolder + '\\ElConfidencial.xlsx').parse("ElConfidencial")
        dfmonde = pd.ExcelFile(destFolder + '\\LeMonde.xlsx').parse("LeMonde")
        dfother = pd.ExcelFile(destFolder + '\\Other.xlsx').parse("Other")
        writer = ExcelWriter(destFolder + output)

        dfpais.to_excel(writer, sheet_name='ElPais', index = False)
        dfconfi.to_excel(writer, sheet_name='ElConfidencial', index = False)
        dfmonde.to_excel(writer, sheet_name='LeMonde', index = False)
        dfother.to_excel(writer, sheet_name='Other', index = False)

        writer.save() 