import json
from datetime import datetime

months = {
	"1": "Jan",
	"2":"Feb",
	"3": "Mar",
	"4": "Apr",
	"5": "May",
	"6": "Jun",
	"7": "Jul",
	"8": "Aug",
	"9": "Sep",
	"10": "Oct",
	"11": "Nov",
	"12": "Dec",
}

import requests
data = requests.get(url = 'https://api.covid19india.org/states_daily.json').json()
# print(data)
# exit()
# data = json.loads(data)
today = datetime.today()
today = f'24-{months[str(today.month)]}-{str(today.year)[2:]}'
today_data = {}
for obj in data['states_daily']:
	if today == obj["date"]:
		today_data[obj['status']] = obj


TOTAL_CONFIRMED = int(today_data['Confirmed']['tt'])
TOTAL_CONFIRMED_TS = int(today_data['Confirmed']['tg'])
today_data['Confirmed'].pop('status', None)
today_data['Confirmed'].pop('date', None)
today_data['Confirmed'].pop('tt', None)
today_data['Confirmed'] = {k: v for k, v in sorted(today_data['Confirmed'].items(), key=lambda item: int(item[1]), reverse = True)}
today_confirmed = [ [k,v] for k,v in today_data['Confirmed'].items() ][:3]
# print(today_confirmed)

# CONFIRMED 
TOTAL_RECOVERED = int(today_data['Recovered']['tt'])
TOTAL_RECOVERED_TS = int(today_data['Recovered']['tg'])
today_data['Recovered'].pop('status', None)
today_data['Recovered'].pop('date', None)
today_data['Recovered'].pop('tt', None)
today_data['Recovered'] = {k: v for k, v in sorted(today_data['Recovered'].items(), key=lambda item: int(item[1]), reverse = True)}
today_recovered = [ [k,v] for k,v in today_data['Recovered'].items() ][:3]
print(today_recovered)

# CONFIRMED 
TOTAL_DECEASED = int(today_data['Deceased']['tt'])
TOTAL_DECEASED_TS = int(today_data['Deceased']['tg'])
today_data['Deceased'].pop('status', None)
today_data['Deceased'].pop('date', None)
today_data['Deceased'].pop('tt', None)
today_data['Deceased'] = {k: v for k, v in sorted(today_data['Deceased'].items(), key=lambda item: int(item[1]), reverse = True)}
today_deceased = [ [k,v] for k,v in today_data['Deceased'].items() ][:3]


Message = f'''
				{today_confirmed}, {today_recovered}, {today_deceased}
		
		'''


import requests 
import json

import boto3







AWS_ACCESS_KEY_ID   =   "AKIAU6GF7N5GBJWZ4Z5P"
AWS_ACCESS_KEY      =   "LDszgzMxJeeMW+1heh3sgNZGRab9hwMLYOwpiD6H"
AWS_REGION          =   'ap-south-1'

sns = boto3.client(
						'sns',
						aws_access_key_id 		= 	AWS_ACCESS_KEY_ID,
                        aws_secret_access_key	=	AWS_ACCESS_KEY,
                        region_name 			=	AWS_REGION
                 )
contact_number = '8919937557'
number 			= 		"+91" + str(contact_number)
response 		= 		sns.publish(
										PhoneNumber = number, 
										Message = Message,  
										MessageAttributes = {
											                   'AWS.SNS.SMS.SMSType': {
											                       'DataType': 'String',
											                       'StringValue': 'Transactional'  # or 'Transactional'
											                   }
											               }
								)




