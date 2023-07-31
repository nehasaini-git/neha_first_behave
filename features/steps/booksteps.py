from behave import *
import requests
from utilities.configurations import *
from utilities.resources import *


@given('the book details are available')
def step_impl(context):
    context.API = get_env_data()['API']['endpoint']
    context.getBookURL = context.API + ApiResource.getBookAuthor
    context.headers = {'Content-Type': 'application/json'}
    context.params = {'AuthorName': 'Rahul Shetty2'}



@when('I execute GetBook API')
def step_impl(context):
    context.getbookresp = requests.get(context.getBookURL, context.params, headers=context.headers)


@then('book details are successfully received')
def step_impl(context):
    print(context.getbookresp.json())
    json_bookresp = context.getbookresp.json()
    book_id = json_bookresp[0]
    print(book_id)




