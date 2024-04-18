import requests

API_KEY = 'YOUR_API_KEY'
DOMAIN_NAME = 'YOUR_DOMAIN_NAME'
FROM = 'Excited User <mailgun@YOUR_DOMAIN_NAME>''

def send_simple_message(receiver_email, subject, text):
	return requests.post(
		f"https://api.mailgun.net/v3/{DOMAIN_NAME}/messages",
		auth=("api", API_KEY),
		data={"from": FROM,
			"to": receiver_email,
			"subject": subject,
			"text": text})

receiver_email = ["a@abc.com", "b@abc.com", "c@abc.com"]
subject = "Hello World!"
text = '''
Congratulations! You have successfully sent an email with Mailgun.
'''
send_simple_message(receiver_email=receiver_email, subject=subject, text=text)