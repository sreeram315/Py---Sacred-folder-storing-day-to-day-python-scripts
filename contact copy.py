import pandas
import sys

sys.stdout = open('contact_py.txt', 'w+')



df = pandas.read_excel('7wmt7-z3749.xlsx', error_bad_lines=False)

keep_cols = []

# for col in df.columns:
# 	if any(df[col]):
# 		keep_cols.append(col)

# print(keep_cols)

df = df[['Display Name', 'Organization', 'Mobile Phone', 'Home Phone']]

ans = ''
ign_names = ['adc', 'imessage', 'i message', 'Schl', 'games', 'Roopa', 'dominos', 'Scjc', 'Akka', 'mom', 'Aurora']
ignored = []

def to_ignore(s):
	for name in ign_names:
		if name.lower() in s.lower():
			ignored.append(s)
			return True
	return False

no_c, yes_c = 0, 0
for index, row in df.iterrows():
	try:
		s = ''
		s += str(row['Display Name'])

		if to_ignore(s):
			no_c += 1
			continue
		
		if not str(row['Organization']) == 'nan':
			s+=' - '
			s += str(row['Organization'])
		
		if not str(row['Mobile Phone']) == 'nan':
			s+= ' - '
			s += str(row['Mobile Phone'])
		
		if not str(row['Home Phone']) == 'nan':
			s += ' - '
			s += str(row['Home Phone'])

		# print(s)
		ans += f'{s}\n'
		yes_c += 1
	except:
		print(f'''

				FAILED FOR {row}

			''')

print(ans)
# print(ignored)

# print('\n\n')
# print(f'yes = {yes_c}')
# print(f'no = {no_c}')
# import csv

# f = csv.reader(open('7wmt7-z3749.csv', 'r'))

# for line in f:
# 	print(line)