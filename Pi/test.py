import pandas as pd 

df = pd.read_csv('all_boys_in_lpu.csv')

df = df[df['Name'].str.contains('Manideep') | df['Name'].str.contains('manideep')]

df = df[df['Department'].str.contains('Comp') | df['Department'].str.contains('cse') | df['Department'].str.contains('comp') | df['Department'].str.contains('CSE')]

df = df[df['RegNo'] >= 11700000]
df = df[df['RegNo'] <= 11800000]

print(df[1:2])



 