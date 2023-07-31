import requests
from behave import *

from payload import *
from utilities.configurations import *
from utilities.resources import ApiResource


@given('the book details which needs to be added to Library')
def step_impl(context):
    context.headers = {'Content-type': 'application/json'}
    context.API = get_env_data()['API']['endpoint']
    context.addbookURL = context.API + ApiResource.addBook
    context.payload = addBookPayload('kffjhgggf', 345)


@given('the book details with {isbn} and {aisle} needs to be added to Library')
def step_impl(context, isbn, aisle):
    context.headers = {'Content-type': 'application/json'}
    context.API = get_env_data()['API']['endpoint']
    context.addbookURL = context.API + ApiResource.addBook
    context.payload = addBookPayload(isbn, aisle)


@when('we execute the AddBook PostAPI method')
def step_impl(context):
    context.addbookresp = requests.post(url=context.addbookURL, json=context.payload, headers=context.headers)


@then('book is successfully added')
def step_impl(context):
    jresp = context.addbookresp.json()
    print(jresp)
    context.book_id = jresp['ID']
    print(context.book_id)
    print('..........')
    print(jresp['Msg'])
    print('..........')
    assert jresp['Msg'] == 'successfully added'
