import boto.ses

AWS_SECRET_ACCESS_KEY = 'Nr1CvAG/7GJQM0ercf0OzhkIXf2DjUpbUtShCjNJ'
AWS_ACCESS_KEY_ID = 'AKIATBXC5EP657ORVH4J'
AWS_SES_REGION_NAME = 'us-east-1'
FROM_EMAIL = 'no-reply@sns.amazonaws.com'

to_email = 'sreerammaram2@gmail.com'

conn = boto.ses.connect_to_region(AWS_SES_REGION_NAME, aws_access_key_id= AWS_ACCESS_KEY_ID,
                                          aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
conn.send_email( FROM_EMAIL, "HELLO SUBJECT", "BODY", [to_email], format='text')


# conn = boto.ses.connect_to_region( AWS_SES_REGION_NAME, aws_access_key_id= AWS_ACCESS_KEY_ID,
#                                           aws_secret_access_key= AWS_SECRET_ACCESS_KEY)

# conn.send_email( FROM_EMAIL, subject, html_body, [to_email], format='html')


# send_email('sreerammaram2@gmail.com', 'Hello Ram', "Hello message")
