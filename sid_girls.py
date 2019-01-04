import pandas as pd 

# result_df	=	df = pd.DataFrame( columns = ['RegNo','Name','DOB','CGPA','Address','Section','Contact','Batch','Department'])

df 	=	pd.read_csv('all_girls_in_lpu_copy.csv')


def is_east(row):
	east_states		=	['manipur','sikkim','arunachal','nepal','assam','meghalaya','mizoram','nagaland'
						]
	if any([True for i in row['Address'].split() if i.lower() in east_states]): return True
	return False

def what_state(row):
	try: return row['Address'].split()[-2]
	except: return row['Address']

df['East']	=	df.apply(is_east, axis = 1)
df['State']	=	df.apply(what_state, axis = 1)

df 	=	df[df['East'] == True]

print(df)


