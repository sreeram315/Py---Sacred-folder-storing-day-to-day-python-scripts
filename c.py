import pandas as pd
from random import randint



if __name__ == '__main__':
	df = pd.read_csv('data.csv')
	df = df[['Name', 'DOB']]
	df['new_col'] = 1
	df['new_col2'] = df['new_col']+ randint(1, 100)
	for index, row in df.iterrows():
	    row['new_col'] = 999

	print(df) 