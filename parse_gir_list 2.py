# proprietary to BEERA // DO NOT COPY
import pandas as pd
from time import sleep

somttt = 0
foreign_cgpa = 0
state_avg = {}
doubt = []
ignored = 0
df = pd.DataFrame( columns = ['RegNo','Name','DOB','CGPA','Address','Section','Contact','Batch','Department'])

#df = df.append({'RegNo': '11610529', 'Name': 'Sreeram Maram', 'DOB': '31 may 1999', 'CGPA': '8.47', 'Address': 'Hyderabad', 'Section': 'E1601', 'Contact':'8919937557', 'Department': 'ECE'}, ignore_index = True)

foreign_list = ['-', 'Sri', 'United', 'Salaam', 'Congo', 'Nicobar', 'Hav', 'Nigeria', 'Bhutan','Ivory', 'Thimphu', 'Puducherry', 'Mara', 'KATHMANDU', 'Diu',  'The', 'P/gatshel', 'Nyamagana', 'Mwanza' ]
file_list = ['0kto2K_girls_data.txt', '2kto3K_girls_data.txt', '3kto4K_girls_data.txt', '4kto5K_girls_data.txt', '5kto6K_girls_data.txt', '6kto9K_girls_data.txt', '9kto12K_girls_data.txt', '12kto15K_girls_data.txt', '15kto16K_girls_data.txt', '16ktoend_girls_data.txt']

for file in file_list:
	print('Parsing file',file)
	handle = open(file)
	lines = handle.readlines()
	for line in lines:
		data = line.split('   ')
		#print(data[0])
		df = df.append({'RegNo': data[0], 'Name': data[1], 'DOB': data[2], 'CGPA': data[3], 'Address': data[4], 'Section': data[5], 'Contact':data[6][:-4], 'Batch': data[6][-4:], 'Department': data[7]}, ignore_index = True)
	
df.set_index(['RegNo'], inplace = True)
dic = {}
state_cgpa = {}
for index, row in df.iterrows():
	try:
		if row['Address'].split()[-2] in foreign_list:
			ignored += 1
			foreign_cgpa += float(row['CGPA'])
			continue
		if row['Address'].split()[-2] == 'Pradesh': state = row['Address'].split()[-3] + ' ' +row['Address'].split()[-2]
		elif row['Address'].split()[-2] == 'Kashmir': state = 'Jammu & kashmir'
		elif row['Address'].split()[-2] == 'Nadu': state = 'Tamil Nadu'
		elif row['Address'].split()[-2] == 'Bengal': state = 'West Bengal'
		else: state = row['Address'].split()[-2]
		if state in dic.keys():
			dic[state] += 1
			state_cgpa[state] += float(row['CGPA'])
			print('passed for',row['CGPA'])
		else:
	 		dic[state] = 1
	 		state_cgpa[state] = float(row['CGPA'])
	 		print('passed for',row['CGPA'])
	except:
	 	print('failed for',row['CGPA'])
	 	

for st in dic:
	state_avg[st] = state_cgpa[st]/dic[st]

#print(state_avg)
sorted_by_value = sorted(state_avg.items(), key=lambda kv: kv[1])

df = pd.DataFrame(columns = ['State', 'Num_of_students', 'Average_cgpa'])
for state in sorted_by_value:
	df = df.append({'State':list(state)[0], 'Num_of_students':str(dic[list(state)[0]]), 'Average_cgpa':list(state)[1]}, ignore_index = True)
	
df = df.append({'State':'Foreign students','Num_of_students':str(ignored),'Average_cgpa':str(foreign_cgpa/ignored)}, ignore_index = True)
df.set_index(['State'], inplace = True)
df.to_csv('girls_cgps_analysis.csv')

print(df)

#print('ignored forig students == ', ignored)

	
