import requests
import threading

requestUrl = '' #Enter the URL to which the request is being made

"""
You need to find out what type of data the request requires.
You can do so by opening the network tab after inspecting the page element. Then enter the data accordingly. Below is an example of a valid VISA credit card.
Note: Do not share your original credit card details.

"""

data = {
	'cc_number': '4007000000027'
	'cc_expmonth': '05'
	'cc_expyear': '24'
	'cc_cvv': '472'
}
 
def sendRequest():
	while True:
		response = request(requestUrl, data = data).text  
		print(response)

threads = []

for i in range(50):
	t = threading.Thread(target=sendRequest)
	t.daemon = True
	threads.append(t)

for i in range(50):
	threads[i].start()

for i in range(50):
	threads[i].join()



