import requests

URL = 'http://216.10.245.166/Library/GetBook.php'
params = {'AuthorName': 'Rahul Shetty2'}
resp = requests.get(url=URL,params=params)

assert resp.status_code == 200
assert resp.headers['Content-Type'] ==  'application/json;charset=UTF-8'
jresp = resp.json()
# get book details with ISBN= RGHCC
expected_book = {'book_name': 'Appium Automation with Java2', 'isbn': 'A1bryy78', 'aisle': '200277'}
for book in jresp:
    if book['isbn'] == 'A1bryy78':
        actual_book = book
        break
assert expected_book == actual_book , 'dont match'
