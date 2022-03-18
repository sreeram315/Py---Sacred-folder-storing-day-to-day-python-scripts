

AWS_ACCESS_KEY = 'Nr1CvAG/7GJQM0ercf0OzhkIXf2DjUpbUtShCjNJ'
AWS_ACCESS_ID = 'AKIATBXC5EP657ORVH4J'

import requests 
import json

import boto3

sns = boto3.client(
						'sns',
						aws_access_key_id 		= 	AWS_ACCESS_ID,
                        aws_secret_access_key	=	AWS_ACCESS_KEY,
                        region_name 			=	'us-east-1'
                 )

# sns.set_sms_attributes(
# 							attributes = {
# 											'DefaultSMSType':'Transactional'
# 										}
# 									)

number 			= 		"+91" + str(9115514084)
response 		= 		sns.publish(PhoneNumber=number, Message = "HELLO BROTHERMAN")

print(response)