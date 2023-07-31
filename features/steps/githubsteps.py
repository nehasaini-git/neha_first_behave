import requests
from behave import *
from utilities.resources import *
from utilities.configurations import *


@given(u'I have github credentials')
def step_impl(context):
    context.se = requests.session()
    context.se.auth = auth = ('nsssaini@gmail.com', get_password())


@when(u'I hit getRepo API')
def step_impl(context):
    context.git_resp = context.se.get(url=ApiResource.githubrepo, auth=context.se.auth)


@then(u'status code of response should be {status_code:d}')
def step_impl(context, status_code):
    print(context.git_resp.status_code)
    assert context.git_resp.status_code == status_code



