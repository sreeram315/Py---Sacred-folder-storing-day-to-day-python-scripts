# proprietary to BEERA // DO NOT COPY
import pandas as pd

df = pd.read_csv('invitis.csv')

count = 0

print(df)


df.columns = ['S.No:', 'Name', 'Village', 'Contact Number', 'Remarks']

print(df)



