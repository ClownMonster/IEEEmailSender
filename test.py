import pandas as pd 

df = pd.read_csv('./reg1.csv')
mails = df['Username']

for i in mails:
    print(i)