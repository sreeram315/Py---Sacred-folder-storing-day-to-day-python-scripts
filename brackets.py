# proprietary to BEERA // DO NOT COPY
#python3
def brackets(line):
	dic = {'}':'{', ']':'[', ')':'('}
	k =[]
	arr ={}
	for i in range(len(line)):
		#print(line[i])
		if line[i] == '(' or line[i] == '{' or line[i] == '[':
			#print('appending',line[i])
			arr[line[i]] = i+1
			k.append(line[i])
		elif line[i] == ')' or line[i] == '}' or line[i] == ']':
			#print('arr[-1]==',arr[-1],'line[i]==',line[i])
			try:
				print(k[-1],'--------',dic[line[i]])
				if k[-1] == dic[line[i]]:
					#print('Removing',line[i])
					print(arr)
					k.pop()
				else:
					print('__________')
					return i+1
			except:
				print('***********')
				return i+1

	#print(arr)
	if len(k) == 0:
		return 'Success'
	else:
		#print('*************')
		#return line.index(arr[-1])+1
		return arr[k[-1]]


def brackets_stack(line):
	indexes = []
	dic = {'}':'{', ']':'[', ')':'('}
	arr=[]
	for i in range(len(line)):
		if line[i] == '(' or line[i] == '{' or line[i] == '[':
			arr.append(line[i])
			indexes.append(i)
		elif line[i] == ')' or line[i] == '}' or line[i] == ']':
			
			#print(arr[-1],'-----',dic[line[i]])
			if len(arr)>=1 and arr[-1] == dic[line[i]]:
				arr.pop()
				indexes.pop()
			else:
				#print('^^^^^^^^^^')
				return i+1
	if len(arr)==0:
		return 'Success'
	else:
		#print('**********')
		return indexes[-1] + 1




line = input()
print(brackets_stack(line))






















