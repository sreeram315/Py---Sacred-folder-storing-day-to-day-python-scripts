
import requests


if __name__ == '__main__':
	# response  = requests.get('http://127.0.0.1:8000/api/students/aadhya-choudhary/')
	# print(response.json())

	
	

	
	session = requests.Session()
	session.auth = ('srm', 'srm')

	# response = session.get('http://frish.herokuapp.com/api/students/all/').json()



	# print(len(response['results']))


	# while response['next']:
	# 	response = requests.get(response['next']).json()
	# 	for i in range(len(response['results'])):
	# 		print((response['results'][i]['name']))

	data = {
		'name': 'someone new here',
		'reg_no': 982001004,
		'section': 'E1232',
		'cgpa'	:	4,
		'gender': 'F',
		"description" : "Very Intelligent fellow"
		}


	url = "http://frish.herokuapp.com/api/students/create/"

	for _ in range(2):
		response = session.post(url , data = data)

	print(response.json())