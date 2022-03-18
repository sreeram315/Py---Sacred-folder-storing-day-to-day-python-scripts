

from clockwork import clockwork
api = clockwork.API('1234290cc958a6c43312fec7dcfbb15c76403457') #Be careful not to post your API Keys to public repositories.
message = clockwork.SMS(to = '441234123456', message = 'This is a test message.')
response = api.send(message)

if response.success:
    print (response.id)
else:
    print (response.error_code)
    print (response.error_message)



'https://api.clockworksms.com/http/send.aspx?key=1234290cc958a6c43312fec7dcfbb15c76403457&to=918847373493&content=Hello+World'