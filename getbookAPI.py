import requests
from payload import *
from utilities.configurations import *
from utilities.resources import *

getBookURL = get_env_data()['API']['endpoint'] + ApiResource.getBookAuthor
headers = {'Content-Type': 'application/json'}
params = {'AuthorName': 'Rahul Shetty2'}
getbookresp = requests.get(getBookURL, params, headers=headers)
jgetbookresp = getbookresp.json()
print(type(jgetbookresp['book_name']))


