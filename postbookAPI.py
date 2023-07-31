import requests
from payload import *
from utilities.configurations import *
from utilities.resources import *

headers = {'Content-type': 'application/json'}
API = get_env_data()['API']['endpoint']
addbookURL = API + ApiResource.addBook
deleteBook = API + ApiResource.deleteBook
headers = {"Content-Type": "application/json"}
addbookresp = requests.post(url=addbookURL, json=addBookPayload('ydtre'), headers=headers)
jresp = addbookresp.json()
print(jresp)
book_id = jresp['ID']


# get data from table to add book details
# query = 'select * from Books'
# addbookresp = requests.post(addbookURL, json= buildPayloadfromDB(query), headers=headers )
# jresp = addbookresp.json()
# print(jresp)
# book_id = jresp['ID']


# delete a book
deleteresp = requests.post(url=deleteBook,json={
	'ID': book_id
}, headers=headers)

assert deleteresp.status_code == 200
print(deleteresp.json())




