import pif, sys, os.path
from godaddypy import Client, Account


api_key = "ENTER_API_KEY_HERE"
secret_key = "ENTER_SECRET_KEY_HERE"

domain = 'edennimni.me'


acc = Account(api_key=api_key, api_secret=secret_key)
client = Client(acc)

public_ipv4 = pif.get_public_ip()

if client is None:
	print("[] Could not open the specified account.")
if client.get_domains() is None:
	print("[] Could not edit an account with no domains available.")
if public_ipv4 is None:
	print("[] Could not fetch public ip, please try again later.")

try:
	for records in client.get_records(domain, record_type='A'):
		if public_ipv4 == records["data"]:
			print("[] IPv4 is already updated.")
		else:
			if client.update_record_ip(public_ipv4, domain, records["name"], 'A'):
				print("[] IPv4 has been updated successfuly.")
			else:
				print("[] IPv4 has not been updated successfuly.")
except Exception as e:
	print(e)
	sys.exit()