import csv
import pandas as pd 
import openpyxl

'''

def from_xl_sheet():
    wb = openpyxl.load_workbook('') # specify the path to xlsx sheet
    sheet = wb.active

'''

def from_csv():
    df = pd.read_csv('./wie-2020-registration-2020-05-15.csv') # specify the path to csv file
    emails = df['Email'] # check the headers once
    return emails




