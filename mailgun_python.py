
def key():
	import os
	t = os.environ['MAILGUN_KEY']
	return t

def mailgun(t):
	import requests
	request=requests.post(
    	'https://api.mailgun.net/v3/sandbox5b66d0c868564de588449ed8b765c59c.mailgun.org/messages',
    	auth=("api", t),
    	files=[("attachment", open("test.txt"))],
    	data={"from":"Mailgun Sandbox <postmaster@sandbox5b66d0c868564de588449ed8b765c59c.mailgun.org>",
          	"to": "shafi0907@gmail.com",
          	"subject": "Rejul Mail gun Testing",
          	"text": "Testing some Mailgun awesomness!",
          	"html": '<!DOCTYPE html><html><body><h1>Mailgun mail</h1><p>Sample Mail sent with attachment and html</p></body></html>'})

	print (request.status_code)
	print (request.text)

k = key()
mailgun(k)
