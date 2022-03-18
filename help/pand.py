import pandas as pd

df = pd.DataFrame(columns = ['Institute', 'Programme', 'GATE Registration Id', 'Candidate Category', 'GATE Score', 'Group Id', 'Allotted Seat Type'])


data = open('output.txt', 'r').readlines()

# print(data)

for d in data:
	d = d.split('   ')
	# print(d[0], d[1], d[2], d[3], d[4], d[5], d[6][:-1])
	df = df.append(
					{
						'Institute': d[6][:-1],
						'Programme':d[0],
						'GATE Registration Id':d[1],
						'Candidate Category':d[2], 
						'GATE Score':d[3],
						'Group Id':d[4],
						'Allotted Seat Type':d[5]
					}, 
				ignore_index=True)  

print(df)
df.to_csv('cs_allotment_top_3_nits.csv')